# TODO — Landing pública LoptorCRE

## Base visual y técnica

- [ ] La landing se ejecuta como proyecto independiente y no accede, modifica ni depende técnicamente de `app.loptorcre.com`; los únicos enlaces hacia la aplicación son CTAs externos a `https://app.loptorcre.com`.
- [ ] La página usa el lenguaje visual aprobado: fondo claro frío, azul marino/negro suave, azul medio para acciones, verde para verificación, tipografía editorial serif para titulares, sans-serif para cuerpo y monospace para metadatos.
- [ ] Existe una composición responsive de escritorio, tablet y móvil con navegación accesible, foco visible, HTML semántico y soporte de `prefers-reduced-motion`.
- [ ] Existe `public/manus-routes.json` con la ruta pública `/` y el servidor responde con HTTP 200 a ese recurso sin devolver el shell HTML.

## Landing narrativa

- [ ] El hero presenta exactamente el posicionamiento «Presenta con rigor. Conecta con criterio.» y explica la transformación de información dispersa de activos en teasers institucionales A4 auditables y cruces anónimos con mandatos de compra.
- [ ] La página contiene secciones narrativas para flujo de trabajo, quien vende, quien compra, Dark Pool y doble ciego, visión de cartera, transparencia radical, pricing, beta, FAQ y CTAs.
- [ ] La sección de transparencia explica qué es y qué no es LoptorCRE, incluyendo que no es VDR, no gestiona NDAs o firmas electrónicas, no es catálogo público y no inventa datos.
- [ ] La razón social Ginete Inversiones S.L. no aparece en la narrativa comercial ni en el contenido público de la landing; queda reservada a documentación legal obligatoria.
- [ ] Los precios implementan los niveles Solo, Boutique & Deal Desk, Family Office & Funds, y el lado comprador con radar gratuito y pases de desbloqueo según la especificación aprobada.

## Walkthrough incrustado

- [ ] La landing contiene un walkthrough interactivo integrado, autónomo y responsive; no usa iframe, login, backend, base de datos ni datos reales.
- [ ] El walkthrough recorre carga de documentos, extracción de datos, procedencia por documento/página/celda, conflicto entre fuentes, estado «En verificación», control de visibilidad, teaser A4 y matching anónimo.
- [ ] El walkthrough utiliza exclusivamente un caso ficticio de Commercial Real Estate y muestra estados coherentes de «Sin documentar», «En verificación», «Bajo solicitud» y «Verificado».
- [ ] Los controles del walkthrough son operables con teclado, tienen etiquetas accesibles, muestran progreso y respetan `prefers-reduced-motion`.
- [ ] El CTA del walkthrough enlaza a `https://app.loptorcre.com` sin pretender abrir una sesión ni compartir datos con la aplicación.

## Idiomas

- [ ] La landing está disponible en English, Español y Français mediante selector visible.
- [ ] La traducción cubre navegación, hero, CTAs, walkthrough, estados, pricing, FAQ, beta, roadmap, transparencia y footer.
- [ ] Las etiquetas canónicas se mantienen semánticamente equivalentes: Not documented / Sin documentar / Non documenté; Under verification / En verificación / En vérification; Available upon request / Bajo solicitud / Sur demande.

## SEO y revisión

- [ ] La carga inicial contiene contenido significativo sin depender de ejecutar JavaScript para que un crawler vea el mensaje principal.
- [ ] La página incluye title, meta description, Open Graph, Twitter Card y canonical preparados para `https://loptorcre.com/`, sin inventar URLs internas.
- [ ] Se preparan `robots.txt` y `sitemap.xml` coherentes con la ruta pública.
- [ ] No se realiza publicación en `loptorcre.com` ni conexión con el repositorio de la aplicación hasta que el usuario revise y apruebe el resultado.
