#!/bin/bash
# Construye dist/: copia el sitio, minifica CSS/JS e inserta el CSS inline en cada HTML.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/.nvm/versions/node/v22.13.1/bin:$PATH"

rm -rf dist
mkdir dist
cp -R ./*.html robots.txt sitemap.xml _headers img dist/

mkdir -p dist/css dist/js
npx -y esbuild css/styles.css --minify --outfile=dist/css/styles.css --log-level=error
npx -y esbuild js/main.js --minify --outfile=dist/js/main.js --log-level=error

# CSS crítico inline: elimina la petición que bloquea el renderizado
python3 - <<'EOF'
import glob
css = open('dist/css/styles.css', encoding='utf-8').read()
tag = '<link rel="stylesheet" href="/css/styles.css">'
for path in sorted(glob.glob('dist/*.html')):
    html = open(path, encoding='utf-8').read()
    assert tag in html, f'{path}: no se encontró la etiqueta link'
    open(path, 'w', encoding='utf-8').write(html.replace(tag, f'<style>{css}</style>'))
    print(f'{path}: CSS inline OK')
EOF

echo "dist/ listo"
