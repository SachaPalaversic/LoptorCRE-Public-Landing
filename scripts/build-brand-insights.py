#!/usr/bin/env python3
"""Logo interno de Actium Insights: icono + "Actium Insights" en una sola línea,
misma fuente (Newsreader 400), tamaño (19 px) y tracking que "Actium" del logo oficial.
Sin subtítulo. Texto en trazados. Uso: python3 scripts/build-brand-insights.py"""
import importlib.util, pathlib
p = pathlib.Path(__file__).with_name("build-brand-logos.py")
s = importlib.util.spec_from_file_location("b", p); b = importlib.util.module_from_spec(s); s.loader.exec_module(b)
import cairosvg
u, a, d = b.metrics("newsreader-latin-wght-normal.woff2")
base = (b.ICON - (a - d) * b.NAME_SIZE / u) / 2 + a * b.NAME_SIZE / u
x0 = b.ICON + b.GAP
dpath, right = b.text_path("newsreader-latin-wght-normal.woff2", "Actium Insights", b.NAME_SIZE, b.NAME_LS, x0, base)
w = round(right, 2); mark = b.mark_group()
for v, c in b.COLORS.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {b.ICON}" width="{w:g}" height="{b.ICON}" role="img" aria-labelledby="t">
  <title id="t">Actium Insights</title>
  <g transform="scale({b.ICON/64:g})">{mark}</g>
  <path fill="{c['name']}" d="{dpath}"/>
</svg>
'''
    f = b.BRAND / f"actium-insights-{v}.svg"; f.write_text(svg)
    cairosvg.svg2png(url=str(f), write_to=str(f.with_suffix(".png")), output_height=b.ICON*8)
    print(f.name, w)
