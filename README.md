# Aqua Perruquers — Web estática optimizada para SEO

Réplica de [aquapeluqueriasantfeliu.com](https://aquapeluqueriasantfeliu.com/) reconstruida como **HTML estático** con mejoras de SEO técnico, contenido y rendimiento.

## Estructura

```
index.html               Página principal (one-page con todas las secciones)
aviso-legal.html         Aviso legal
politica-privacidad.html Política de privacidad
politica-cookies.html    Política de cookies
css/styles.css           Estilos (sin frameworks)
js/main.js               Menú móvil + formulario → WhatsApp
img/                     Imágenes optimizadas en WebP con nombres descriptivos
robots.txt               Directivas para rastreadores + sitemap
sitemap.xml              Mapa del sitio con imágenes
```

## Mejoras SEO respecto a la web original

### 1. Contenido indexable (lo más importante)
La web original era una SPA de React (Bolt.new): Google recibía un `<div id="root"></div>` vacío y dependía del renderizado JS. Ahora **todo el contenido está en el HTML**, indexable al instante por cualquier buscador.

### 2. SEO técnico
- `<html lang="es">` correcto (la original declaraba `lang="ca"` con contenido mayoritariamente en castellano).
- `<link rel="canonical">` apuntando al dominio real (el JSON-LD original apuntaba a un dominio distinto, `aqua-perruquers.com`).
- Etiquetas **Open Graph** y **Twitter Card** para compartir en redes.
- Metas de geolocalización (`geo.region`, `geo.position`) para SEO local.
- `robots.txt` + `sitemap.xml` con extensión de imágenes.
- Páginas legales con `noindex, follow` (evita contenido duplicado/diluido).

### 3. Datos estructurados (Schema.org)
- `HairSalon` + `BeautySalon` con: dirección, geo, **horarios corregidos** (la original declaraba L-V 9:00-20:00 en el schema pero el horario real es M-V 10:00-19:00 y S 10:00-14:00), teléfono, email, `aggregateRating` 4.8, las 3 reseñas, y catálogo con los 10 servicios.
- `FAQPage` con 5 preguntas frecuentes (sección visible nueva en la página) — apta para resultados enriquecidos.

### 4. Rendimiento (Core Web Vitals)
- Sin framework JS: ~3 KB de JS frente a 254 KB de bundle React.
- Imágenes convertidas a **WebP** con nombres descriptivos: de ~6 MB a ~1,2 MB en total (p. ej. interior del salón: 2,3 MB → 172 KB).
- `width`/`height` en todas las imágenes (evita CLS), `loading="lazy"` fuera del viewport, `fetchpriority="high"` + `preload` en la imagen hero.

### 5. Semántica y accesibilidad
- Jerarquía correcta de encabezados (un solo `h1` con la keyword principal, `h2` por sección).
- HTML5 semántico: `header`, `nav`, `main`, `section`, `article`, `address`, `footer`, `blockquote`/`time` en reseñas.
- Alt descriptivos en todas las imágenes, skip-link, `aria-label`/`aria-expanded`, `prefers-reduced-motion`.
- Enlaces clicables `tel:` y `mailto:`.

### 6. Contenido
- Idioma unificado en castellano (la original mezclaba catalán y castellano de forma aleatoria).
- Nueva sección de **preguntas frecuentes** orientada a búsquedas long-tail ("depilación láser Sant Feliu", "HifemSculpt qué es"...).
- Botón flotante de WhatsApp en toda la página.

## Cómo publicar

Es una web 100 % estática: súbela a cualquier hosting (Cloudflare Pages, Netlify, Vercel, o el hosting actual). No requiere build ni Node.

## Pendiente / recomendado

- Verificar la propiedad en **Google Search Console** y enviar `sitemap.xml`.
- Mantener actualizada la ficha de **Google Business Profile** (mismo NAP: nombre, dirección, teléfono).
- Valorar una versión en catalán (`/ca/`) con `hreflang` para captar búsquedas en ambos idiomas.
