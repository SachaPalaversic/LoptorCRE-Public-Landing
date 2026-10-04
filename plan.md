# Plan — Landing pública LoptorCRE

## Alcance

Construir una landing pública independiente para `loptorcre.com`. La aplicación SaaS real permanece en `app.loptorcre.com` y no se toca: no habrá integración técnica, iframe, autenticación compartida, backend, base de datos ni acceso a datos de producción.

La landing será una experiencia comercial institucional para Commercial Real Estate, con el posicionamiento **«Presenta con rigor. Conecta con criterio.»**, una narrativa centrada en evidencia y una demo interactiva autónoma.

## Decisiones de diseño aprobadas

### Movimiento visual

**Editorial institucional / data room de confianza**: una mezcla de publicación financiera sobria, documentación de inversión y producto SaaS de alta precisión. La interfaz debe comunicar criterio y trazabilidad, no espectáculo tecnológico.

### Principios

1. **La evidencia antes que el hype**: cada afirmación visual debe sugerir fuente, estado o decisión.
2. **Confidencialidad visible**: anonimato, doble ciego y control de visibilidad aparecen como comportamientos de producto.
3. **Jerarquía editorial**: titulares serif con presencia, cuerpo sans-serif muy legible y metadatos monospace.
4. **Rigor sereno**: animación contenida, espacios generosos, bordes finos y estados cromáticos discretos.

### Filosofía de color

El fondo marfil frío y el azul casi negro toman la base de la aplicación existente y transmiten calma, control y contexto documental. El azul medio se reserva para acciones y enlaces; el verde identifica evidencia verificada; el ámbar marca revisión o conflicto sin convertirlo en una alerta agresiva. La paleta propia de Loptor será un **azul petróleo institucional** usado en botones, líneas de procedencia y estados de interacción.

### Paradigma de layout

Composición editorial asimétrica: texto y prueba visual se alternan en una retícula amplia, evitando una sucesión de tarjetas centradas. El walkthrough actúa como eje narrativo y la página se desplaza desde el expediente individual hacia el mercado anónimo y la visión de cartera.

### Motivos de marca

- **Líneas de procedencia**: conexiones finas entre dato, fuente y salida.
- **Estados documentales**: chips de estado sobrios para verificación, solicitud y ausencia de documentación.
- **Hoja A4 / teaser**: documento vertical como objeto recurrente que ancla el producto en un artefacto real.

### Interacción y animación

La interacción debe explicar, no distraer. El walkthrough se presenta como un product showcase embebido: tabs horizontales para cambiar de módulo y un único workspace ficticio de gran formato, con marco de navegador, barra de progreso temporal de 20 segundos, autoplay pausado al interactuar, estado activo, descripción y CTA de prueba de 7 días. El recorrido usa cuatro fases: ingesta multifuente, procedencia sin fabricación, arbitraje de conflictos/anonimización y teaser institucional con matching ciego. Las líneas de procedencia pueden dibujarse suavemente al entrar en viewport. No habrá parallax intenso, contadores falsos ni animaciones que sugieran una garantía financiera.

### Tipografía

- Titulares: serif editorial cercana a `Iowan Old Style`, `Palatino` o `Georgia`.
- Interfaz y cuerpo: `Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, sans-serif.
- Metadatos y etiquetas: `Geist Mono`, `IBM Plex Mono`, `ui-monospace`.

### Esencia de marca

**LoptorCRE es la capa de rigor documental y conexión anónima para profesionales que presentan y buscan activos CRE off-market.**

Personalidad: **rigurosa, sobria, discreta**.

### Voz

Titulares: directos, precisos y sin grandilocuencia.

Ejemplos:

- «Presenta con rigor. Conecta con criterio.»
- «Primero el encaje. Después la identidad.»

### Wordmark

Usar el wordmark tipográfico `loptor` con tratamiento editorial sobrio, acompañado de `CRE INTELLIGENCE` en monospace pequeño donde corresponda. No crear un símbolo ornamental independiente en esta primera versión.

## Arquitectura del producto

- `src/data/content.ts`: contenido por idioma (`en`, `es`, `fr`), incluyendo navegación, copy, precios, FAQ, estados y walkthrough.
- `src/components/Header.tsx`: navegación, selector de idioma y CTA de acceso.
- `src/components/Hero.tsx`: promesa central, CTAs y panel visual de producto.
- `src/components/Walkthrough.tsx`: demo autónoma de seis/ocho estados con datos ficticios y localización completa.
- `src/components/Workflow.tsx`: flujo en cuatro pasos.
- `src/components/MarketSections.tsx`: sell-side, buy-side, Dark Pool y cartera.
- `src/components/TrustBoundaries.tsx`: qué es y qué no es LoptorCRE, beta y límites.
- `src/components/Pricing.tsx`: planes y toggle mensual/anual donde aplique.
- `src/components/Footer.tsx`: enlaces institucionales y legal placeholders; la razón social no forma parte de la narrativa comercial.
- `src/App.tsx`: composición, estado de idioma y navegación por anclas.
- `public/manus-routes.json`: declaración de la ruta pública `/`.
- `public/robots.txt`, `public/sitemap.xml`: documentos para el dominio canónico cuando se configure.

## Experiencia trilingüe

El selector de idioma estará disponible en el header. El estado del idioma se reflejará en la experiencia completa, incluidos los textos del walkthrough. La versión inicial puede conservar una sola ruta con estado local para prototipo; la arquitectura de contenido debe permitir rutas localizadas (`/en`, `/es`, `/fr`) en la siguiente iteración sin duplicar componentes.

## Walkthrough

Demo visual e interactiva sin iframe y sin red. El caso ficticio será un activo hotelero urbano. Sus estados mostrarán:

1. Carga de IM, Excel y nota del broker.
2. Extracción de una métrica.
3. Referencia de documento, página y celda.
4. Conflicto 128 vs. 132 habitaciones.
5. Estado «En verificación».
6. Elección de visibilidad del teaser.
7. Preview del A4 institucional.
8. Match anónimo con un mandato.

El CTA final enlaza externamente a `https://app.loptorcre.com` y la demo nunca pretende ser una sesión real.

## Infraestructura

Landing estática sin servidor ni base de datos. Se utilizará el runtime de Preview en el puerto configurado por WebDev. La publicación queda separada de la aplicación SaaS y no se realizará hasta revisión y aprobación explícita del usuario.

## SEO y accesibilidad

La ruta pública contendrá HTML significativo, un `<title>`, descripción, Open Graph, Twitter Card, canonical preparado para `https://loptorcre.com/`, sitemap, robots y navegación semántica. El contenido visible deberá existir en la carga inicial; la interactividad del walkthrough se añadirá sobre esa base. Se respetarán contraste, foco visible, teclado, `aria-label`, `prefers-reduced-motion` y tamaños táctiles.
