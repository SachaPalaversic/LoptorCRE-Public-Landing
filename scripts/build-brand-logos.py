#!/usr/bin/env python3
"""Genera los archivos oficiales del logo de Actium CRE Intelligence.

Fuente de la especificación: la cabecera de la landing (index.html + styles.css).
  - Icono: public/brand/actium-mark.svg (32 px, hueco de 10 px hasta el texto)
  - "Actium": Newsreader 400, 19 px, interlineado 1, tracking -0.02em
  - "CRE INTELLIGENCE": IBM Plex Mono 600 (500 + negrita sintética, como en el
    navegador), 8 px, tracking 0.16em, apilado 2 px bajo el nombre
  - Texto centrado en vertical respecto al icono

El texto se convierte a trazados: el SVG resultante no depende de ninguna fuente.
Requiere: fonttools, brotli, uharfbuzz y (para los PNG) cairosvg.
Uso: python3 scripts/build-brand-logos.py
"""
import io, re, pathlib
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "public" / "fonts"
BRAND = ROOT / "public" / "brand"

# Medidas de la cabecera tal como se ve en un portátil (ventana de 1121 a 1280 px,
# regla "@media (min-width:1121px) and (max-width:1280px)" de styles.css).
# En pantallas más anchas la landing usa 40/22 px; ver docs/BRAND.md.
ICON = 32
GAP = 10
NAME_SIZE, NAME_LS = 19, -0.02 * 19
SUB_SIZE, SUB_LS = 8, 0.16 * 8
STACK_GAP = 2
SUB_FAKE_BOLD = SUB_SIZE / 24  # negrita sintética del navegador (Skia)

COLORS = {
    "on-light": {"name": "#111A28", "sub": "#55657B"},  # --ink / --muted
    "on-dark": {"name": "#F1F4F8", "sub": "#A6B0BF"},   # --on-dark / --on-dark-2
}


def load(fname):
    f = TTFont(FONTS / fname)
    f.flavor = None
    buf = io.BytesIO()
    f.save(buf)
    return f, hb.Font(hb.Face(buf.getvalue()))


def text_path(fname, text, size, ls, x0, baseline):
    """Trazado SVG del texto, con kerning de HarfBuzz y tracking en px."""
    tt, hbfont = load(fname)
    upm = tt["head"].unitsPerEm
    s = size / upm
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": False})
    pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
    x = x0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        name = order[info.codepoint]
        tp = TransformPen(pen, (s, 0, 0, -s, x + pos.x_offset * s, baseline))
        gs[name].draw(tp)
        x += pos.x_advance * s + ls
    return pen.getCommands(), x - ls  # borde derecho sin el tracking final


def metrics(fname):
    t = TTFont(FONTS / fname)
    return t["head"].unitsPerEm, t["hhea"].ascent, t["hhea"].descent


def mark_group():
    svg = (BRAND / "actium-mark.svg").read_text()
    return re.search(r'(<g transform="skewX\(-10\)">.*?</g>)', svg, re.S).group(1)


def build():
    block_h = NAME_SIZE + STACK_GAP + SUB_SIZE
    top = (ICON - block_h) / 2
    # línea del nombre: interlineado 1 (22 px)
    u, a, d = metrics("newsreader-latin-wght-normal.woff2")
    name_base = top + (NAME_SIZE - (a - d) * NAME_SIZE / u) / 2 + a * NAME_SIZE / u
    # línea del subtítulo: interlineado 1 (8 px)
    u, a, d = metrics("ibm-plex-mono-latin-500-normal.woff2")
    sub_top = top + NAME_SIZE + STACK_GAP
    sub_base = sub_top + (SUB_SIZE - (a - d) * SUB_SIZE / u) / 2 + a * SUB_SIZE / u
    x0 = ICON + GAP

    name_d, name_r = text_path("newsreader-latin-wght-normal.woff2", "Actium", NAME_SIZE, NAME_LS, x0, name_base)
    sub_d, sub_r = text_path("ibm-plex-mono-latin-500-normal.woff2", "CRE INTELLIGENCE", SUB_SIZE, SUB_LS, x0, sub_base)
    width = round(max(name_r, sub_r) + SUB_FAKE_BOLD, 2)
    scale = ICON / 64
    mark = mark_group()

    for variant, c in COLORS.items():
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:g} {ICON}" width="{width:g}" height="{ICON}" role="img" aria-labelledby="t">
  <title id="t">Actium CRE Intelligence</title>
  <g transform="scale({scale:g})">{mark}</g>
  <path fill="{c['name']}" d="{name_d}"/>
  <path fill="{c['sub']}" stroke="{c['sub']}" stroke-width="{SUB_FAKE_BOLD:.2f}" d="{sub_d}"/>
</svg>
'''
        (BRAND / f"actium-logo-{variant}.svg").write_text(svg)
        print("escrito", f"actium-logo-{variant}.svg", f"{width:g}x{ICON}")
    return width


def pngs(width):
    import cairosvg
    for variant in COLORS:
        cairosvg.svg2png(url=str(BRAND / f"actium-logo-{variant}.svg"),
                         write_to=str(BRAND / f"actium-logo-{variant}.png"),
                         output_height=ICON * 8)
    cairosvg.svg2png(url=str(BRAND / "actium-mark.svg"),
                     write_to=str(BRAND / "actium-mark.png"), output_width=512, output_height=512)
    print("PNG escritos")


if __name__ == "__main__":
    w = build()
    pngs(w)
