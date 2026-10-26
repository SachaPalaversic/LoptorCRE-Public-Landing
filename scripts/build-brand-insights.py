#!/usr/bin/env python3
"""Logo interno de Actium Insights: igual que el logo oficial, pero con "Actium Insights"
en la línea del nombre (misma fuente Newsreader 400, tamaño 19 px y tracking que "Actium")
y "CRE INTELLIGENCE" debajo, exactamente como en el logo oficial.
Texto en trazados. Uso: python3 scripts/build-brand-insights.py"""
import importlib.util, pathlib
p = pathlib.Path(__file__).with_name("build-brand-logos.py")
s = importlib.util.spec_from_file_location("b", p); b = importlib.util.module_from_spec(s); s.loader.exec_module(b)
import cairosvg
block_h = b.NAME_SIZE + b.STACK_GAP + b.SUB_SIZE
top = (b.ICON - block_h) / 2
u, a, d = b.metrics("newsreader-latin-wght-normal.woff2")
name_base = top + (b.NAME_SIZE - (a - d) * b.NAME_SIZE / u) / 2 + a * b.NAME_SIZE / u
u, a, d = b.metrics("ibm-plex-mono-latin-500-normal.woff2")
sub_top = top + b.NAME_SIZE + b.STACK_GAP
sub_base = sub_top + (b.SUB_SIZE - (a - d) * b.SUB_SIZE / u) / 2 + a * b.SUB_SIZE / u
x0 = b.ICON + b.GAP
name_d, name_r = b.text_path("newsreader-latin-wght-normal.woff2", "Actium Insights", b.NAME_SIZE, b.NAME_LS, x0, name_base)
sub_d, sub_r = b.text_path("ibm-plex-mono-latin-500-normal.woff2", "CRE INTELLIGENCE", b.SUB_SIZE, b.SUB_LS, x0, sub_base)
w = round(max(name_r, sub_r) + b.SUB_FAKE_BOLD, 2); mark = b.mark_group()
for v, c in b.COLORS.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {b.ICON}" width="{w:g}" height="{b.ICON}" role="img" aria-labelledby="t">
  <title id="t">Actium Insights · CRE Intelligence</title>
  <g transform="scale({b.ICON/64:g})">{mark}</g>
  <path fill="{c['name']}" d="{name_d}"/>
  <path fill="{c['sub']}" stroke="{c['sub']}" stroke-width="{b.SUB_FAKE_BOLD:.2f}" d="{sub_d}"/>
</svg>
'''
    f = b.BRAND / f"actium-insights-{v}.svg"; f.write_text(svg)
    cairosvg.svg2png(url=str(f), write_to=str(f.with_suffix(".png")), output_height=b.ICON*8)
    print(f.name, w)
