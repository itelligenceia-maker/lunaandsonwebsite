#!/usr/bin/env python3
"""Generates work/index.html (Our Work gallery). Run from the site root."""
import os
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import *  # noqa: F401,F403
from work_data import WORK, CATEGORIES


def tile(item):
    f, w, h, cat, aen, aes = item
    src = "../" + quote(f)
    return f"""        <button type="button" class="gallery-item" data-cat="{cat}" data-full="{src}" aria-label="{attr('View photo: ' + aen)}">
          <img src="{src}" width="{w}" height="{h}" alt="{attr(aen)}" data-alt-en="{attr(aen)}" data-alt-es="{attr(aes)}" loading="lazy" decoding="async">
        </button>"""


def page():
    chips = [f'<button type="button" class="filter-chip" data-filter="all" aria-pressed="true" {bi(("All Projects", "Todos los Proyectos"))}</button>']
    chips += [f'<button type="button" class="filter-chip" data-filter="{k}" aria-pressed="false" {bi((en, es))}</button>' for k, en, es in CATEGORIES]
    tiles = "\n".join(tile(i) for i in WORK)
    title = "Our Work | Patios, Walls &amp; Landscapes | Luna &amp; Sons Landscaping"
    desc = "See recent patios, pavers, retaining walls and landscape transformations by Luna &amp; Sons Landscaping, serving Santa Maria and California's Central Coast."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(title, desc, depth="../")}
</head>
<body>
{render_header("work", depth="../")}
<main>
  <section class="page-banner" style="background-image:url('../images/hero-slide-5.jpg')">
    <div class="page-banner-scrim"></div>
    <div class="container page-banner-inner">
      <p class="eyebrow eyebrow-light" {bi(("Our Work", "Nuestro Trabajo"))}</p>
      <h1 {bi(("Spaces we've built.", "Espacios que hemos construido."))}</h1>
      <p {bi(("Patios, walls and landscapes completed by the Luna & Sons crew.", "Patios, muros y paisajes terminados por el equipo de Luna & Sons."))}</p>
    </div>
  </section>

  <section class="gallery-section">
    <div class="container">
      <div class="filter-bar" role="group" aria-label="Filter projects">
        {chr(10).join(chips)}
      </div>
      <div class="gallery-grid">
{tiles}
      </div>
    </div>
  </section>

{render_closing_cta(depth="../")}
</main>

<dialog id="lightbox" class="lightbox" aria-label="Project photo viewer">
  <button type="button" class="lb-close" aria-label="Close"><i data-lucide="x" aria-hidden="true"></i></button>
  <button type="button" class="lb-prev" aria-label="Previous photo"><i data-lucide="chevron-left" aria-hidden="true"></i></button>
  <img class="lb-img" src="" alt="">
  <button type="button" class="lb-next" aria-label="Next photo"><i data-lucide="chevron-right" aria-hidden="true"></i></button>
  <p class="lb-count"></p>
</dialog>
{render_footer(depth="../")}
{render_scripts("../")}
</body>
</html>
"""


if __name__ == "__main__":
    write_page("work/index.html", page())
