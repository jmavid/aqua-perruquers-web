#!/usr/bin/env python3
"""Genera y comprueba dominios .com de 4 letras con patrón CVCV (consonante-vocal-consonante-vocal).

Genera las 11.025 combinaciones posibles (21 consonantes x 5 vocales x 21
consonantes x 5 vocales) y consulta RDAP (rdap.verisign.com), el protocolo
que sustituye a whois para el TLD .com, para saber si cada dominio está
libre (404 = sin registrar) u ocupado (200 = registrado).

Requiere acceso completo a Internet hacia rdap.verisign.com: no funciona en
entornos con la salida de red restringida a dominios de desarrollo.

Uso:
    python3 tools/check_four_letter_domains.py --output libres.csv
    python3 tools/check_four_letter_domains.py --limit 50  # prueba rápida
    python3 tools/check_four_letter_domains.py --start 500 --end 1000
"""
import argparse
import csv
import sys
import time
import urllib.error
import urllib.request

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
RDAP_URL = "https://rdap.verisign.com/com/v1/domain/{domain}"


def generate_words():
    words = []
    for c1 in CONSONANTS:
        for v1 in VOWELS:
            for c2 in CONSONANTS:
                for v2 in VOWELS:
                    words.append(c1 + v1 + c2 + v2)
    return words


def check_domain(domain, timeout=10, retries=3):
    """Devuelve 'libre', 'ocupado' o 'error' para <domain>."""
    url = RDAP_URL.format(domain=domain)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/rdap+json"})
            urllib.request.urlopen(req, timeout=timeout)
            return "ocupado"
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "libre"
            if e.code == 429:
                time.sleep(2 ** attempt)
                continue
            return "error"
        except urllib.error.URLError:
            time.sleep(2 ** attempt)
    return "error"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="four_letter_domains.csv", help="CSV de salida")
    parser.add_argument("--start", type=int, default=0, help="índice inicial (para reanudar)")
    parser.add_argument("--end", type=int, default=None, help="índice final (exclusivo)")
    parser.add_argument("--limit", type=int, default=None, help="número máximo de dominios a comprobar")
    parser.add_argument("--delay", type=float, default=0.3, help="segundos de espera entre consultas")
    parser.add_argument("--list-only", action="store_true", help="solo genera la lista, no comprueba disponibilidad")
    args = parser.parse_args()

    words = generate_words()
    end = args.end if args.end is not None else len(words)
    subset = words[args.start:end]
    if args.limit:
        subset = subset[: args.limit]

    if args.list_only:
        with open(args.output, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["dominio"])
            for word in subset:
                writer.writerow([f"{word}.com"])
        print(f"{len(subset)} dominios escritos en {args.output}")
        return

    print(f"Comprobando {len(subset)} de {len(words)} dominios totales...", file=sys.stderr)
    with open(args.output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["dominio", "estado"])
        for i, word in enumerate(subset):
            domain = f"{word}.com"
            estado = check_domain(domain)
            writer.writerow([domain, estado])
            f.flush()
            print(f"[{i + 1}/{len(subset)}] {domain}: {estado}", file=sys.stderr)
            time.sleep(args.delay)


if __name__ == "__main__":
    main()
