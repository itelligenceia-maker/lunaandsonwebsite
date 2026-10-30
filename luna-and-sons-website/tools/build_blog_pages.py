#!/usr/bin/env python3
"""
Generates the /blog/ index page and one static page per blog post.

Same reasoning as build_service_pages.py: no framework, so a "dynamic route"
on this site means a real folder + index.html per slug, generated from one
template + a plain data list — not literally client-side routing. Reuses the
shared render_head/render_header/render_footer from build_service_pages.py so
the nav/footer stay byte-for-byte identical to every other page on the site.

Run from the luna-and-sons-website/ directory:

    python3 tools/build_blog_pages.py

Overwrites blog/index.html and blog/<slug>/index.html for every entry in POSTS.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_service_pages import SITE_ROOT, render_head, render_header, render_footer, bi  # noqa: E402

PLACEHOLDER_NOTE = "featured image — replace with a real photo"
PLACEHOLDER_TAG = ("Placeholder post", "Publicación de muestra")

POSTS = [
    {
        "slug": "seasonal-lawn-care-tips",
        "title": (
            "Seasonal Lawn Care Tips for the Central Coast",
            "Consejos de Cuidado del Césped por Temporada para la Costa Central",
        ),
        "excerpt": (
            "Placeholder post — replace with real content. A short preview of this article will appear here once the real post is written, giving visitors a two-to-three-line summary before they click through to read more.",
            "Publicación de muestra — reemplazar con contenido real. Aquí aparecerá una breve vista previa de este artículo una vez que se escriba la publicación real, con un resumen de dos o tres líneas antes de que los visitantes hagan clic para leer más.",
        ),
    },
    {
        "slug": "choosing-drought-tolerant-plants",
        "title": (
            "Choosing Drought-Tolerant Plants for Your Yard",
            "Cómo Elegir Plantas Resistentes a la Sequía para su Jardín",
        ),
        "excerpt": (
            "Placeholder post — replace with real content. A short preview of this article will appear here once the real post is written, giving visitors a two-to-three-line summary before they click through to read more.",
            "Publicación de muestra — reemplazar con contenido real. Aquí aparecerá una breve vista previa de este artículo una vez que se escriba la publicación real, con un resumen de dos o tres líneas antes de que los visitantes hagan clic para leer más.",
        ),
    },
    {
        "slug": "planning-a-backyard-renovation",
        "title": (
            "Planning a Backyard Renovation: Where to Start",
            "Cómo Planificar una Renovación del Patio Trasero: Por Dónde Empezar",
        ),
        "excerpt": (
            "Placeholder post — replace with real content. A short preview of this article will appear here once the real post is written, giving visitors a two-to-three-line summary before they click through to read more.",
            "Publicación de muestra — reemplazar con contenido real. Aquí aparecerá una breve vista previa de este artículo una vez que se escriba la publicación real, con un resumen de dos o tres líneas antes de que los visitantes hagan clic para leer más.",
        ),
    },
]


def render_placeholder_media(css_class, note, extra_attrs=""):
    return (
        f'<div class="{css_class} placeholder-img"{extra_attrs} role="img" aria-label="Placeholder: {note} — image coming soon">'
        f'<i data-lucide="image" aria-hidden="true"></i>'
        f'<span data-en="Image coming soon" data-es="Imagen próximamente">Image coming soon</span>'
        f"</div>"
    )


def render_blog_index():
    cards = []
    for post in POSTS:
        media = render_placeholder_media("blog-card-media", PLACEHOLDER_NOTE)
        cards.append(f"""        <a class="blog-card" href="../blog/{post["slug"]}/" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
          {media}
          <span class="blog-card-placeholder-tag" {bi(PLACEHOLDER_TAG)}</span>
          <h3 class="blog-card-title" {bi(post["title"])}</h3>
          <p class="blog-card-excerpt" {bi(post["excerpt"])}</p>
        </a>""")
    cards_html = "\n".join(cards)

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head("Blog | Luna &amp; Sons Landscaping", "Landscaping tips, project stories, and seasonal advice from Luna &amp; Sons Landscaping in Santa Maria, CA.", depth="../")}
<meta name="robots" content="noindex">
</head>
<body>

<!-- =========================================================
     HEADER / NAV
========================================================= -->
{render_header("blog", depth="../")}

<main>

  <!-- =========================================================
       BLOG BANNER
  ========================================================= -->
  <section class="blog-hero">
    <h1 data-en="Blog" data-es="Blog">Blog</h1>
  </section>

  <!-- =========================================================
       POST GRID
  ========================================================= -->
  <section class="blog-section">
    <div class="container blog-grid">
{cards_html}
    </div>
  </section>

</main>

<!-- =========================================================
     FOOTER
========================================================= -->
{render_footer(depth="../")}

<script src="https://unpkg.com/lucide@0.462.0/dist/umd/lucide.js"></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script src="../script.js"></script>
</body>
</html>
"""
    return body


def render_blog_post(post):
    media = render_placeholder_media("blog-post-media", PLACEHOLDER_NOTE)
    title_en = post["title"][0]

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(f"{title_en} | Luna &amp; Sons Landscaping Blog", "Placeholder blog post on the Luna &amp; Sons Landscaping site — replace with real content.", depth="../../")}
</head>
<body>

<!-- =========================================================
     HEADER / NAV
========================================================= -->
{render_header("blog", depth="../../")}

<main>

  <section class="blog-hero">
    <h1 {bi(post["title"])}</h1>
  </section>

  <section class="blog-post-section">
    <div class="container blog-post-body">
      <a class="blog-post-back" href="../../blog/index.html">
        <i data-lucide="arrow-left" aria-hidden="true"></i>
        <span data-en="Back to Blog" data-es="Volver al Blog">Back to Blog</span>
      </a>
      <span class="blog-card-placeholder-tag" {bi(PLACEHOLDER_TAG)}</span>
      {media}
      <p {bi(post["excerpt"])}</p>
      <p data-en="This is a placeholder post used to establish the blog's page structure. Replace this paragraph — and everything else on this page — with the real article once it's written." data-es="Esta es una publicación de muestra utilizada para establecer la estructura de la página del blog. Reemplace este párrafo — y todo lo demás en esta página — con el artículo real una vez que esté escrito.">This is a placeholder post used to establish the blog's page structure. Replace this paragraph — and everything else on this page — with the real article once it's written.</p>
    </div>
  </section>

</main>

<!-- =========================================================
     FOOTER
========================================================= -->
{render_footer(depth="../../")}

<script src="https://unpkg.com/lucide@0.462.0/dist/umd/lucide.js"></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script src="../../script.js"></script>
</body>
</html>
"""
    return body


def main():
    blog_dir = os.path.join(SITE_ROOT, "blog")
    os.makedirs(blog_dir, exist_ok=True)
    with open(os.path.join(blog_dir, "index.html"), "w") as f:
        f.write(render_blog_index())
    print("wrote blog/index.html")

    for post in POSTS:
        post_dir = os.path.join(blog_dir, post["slug"])
        os.makedirs(post_dir, exist_ok=True)
        with open(os.path.join(post_dir, "index.html"), "w") as f:
            f.write(render_blog_post(post))
        print(f"wrote blog/{post['slug']}/index.html")


if __name__ == "__main__":
    main()
