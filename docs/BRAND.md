# Manual de marca — Actium CRE

Fuente única de verdad del logo. Todos los repos (landing, app, Founding, Insights) deben COPIAR estos archivos, nunca recrearlos.

## Archivos oficiales (`public/brand/`)
| Archivo | Uso |
|---|---|
| `actium-logo-on-light.svg` / `.png` | Logo completo sobre fondo claro |
| `actium-logo-on-dark.svg` / `.png` | Logo completo sobre fondo oscuro |
| `actium-mark.svg` / `.png` | Solo el icono (barras + puntos ámbar) |
| `favicon.svg`, `favicon-32.png`, `/favicon.ico` | Favicons |
| `apple-touch-icon.png` | 180×180, fondo #090A0F |
| `icon-192.png`, `icon-512.png` | App instalable (PWA) |

Los SVG llevan el texto convertido a trazados: no dependen de fuentes.

## Composición
Icono a la izquierda; a su derecha, apilado: **Actium** (A mayúscula, Newsreader serif 400, tracking -0.02em) y debajo **CRE INTELLIGENCE** (IBM Plex Mono 600, mayúsculas, tracking 0.16em). Sin barra "/", sin minúsculas, sin sans bold.

## Colores
Cobalto #3B82F6 · Ámbar #F5A524 · Tinta #111A28 · Gris #55657B · Sobre oscuro #F1F4F8 / #A6B0BF · Fondo oscuro #090A0F · Papel #F4F7FB.

## Tamaños (icono / nombre / subtítulo, px)
- Compacto (cabecera portátil): 32 / 19 / 8 — es el de los archivos.
- Pantalla ancha: 40 / 22 / 8.
- Pie y legales: 30 / 18 / 7.

## Reglas
- Nunca recrear ni describir el logo: usar los archivos.
- Prohibido Arial/Helvetica, "ACTIUM" en mayúsculas, "actium" en minúsculas, el "NEXT-GEN DIGITAL".
- Regenerar: `python3 scripts/build-brand-logos.py`.

## Variante interna: Actium Insights
Solo para insights.actiumcre.com (privado). Icono + "Actium Insights" en una línea, misma fuente, tamaño y tracking que "Actium"; sin subtítulo.
`public/brand/actium-insights-on-dark.svg` / `.png` y `actium-insights-on-light.svg` / `.png`. Regenerar: `python3 scripts/build-brand-insights.py`.
