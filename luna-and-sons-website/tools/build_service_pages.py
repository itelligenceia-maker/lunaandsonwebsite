#!/usr/bin/env python3
"""
Generates the three /services/* pages from ONE shared template.

Why this exists: the site is plain static HTML with no framework/build step,
so there's no <Component prop={...}> to reach for. This script is the
equivalent — a single template (HEAD/HEADER/HERO/INTRO/BLOCK/CTA/FOOTER
functions below) fed by a plain data dict per page — so the layout is
defined once and only the data below differs per page. Edit the data at the
bottom of this file (or the render_* functions for structural changes), then
re-run:

    python3 tools/build_service_pages.py

from the luna-and-sons-website/ directory. It overwrites the three
services/<slug>/index.html files. Output is committed plain HTML (not
client-rendered) so the pages stay crawlable and work with JS disabled,
matching the rest of the site.
"""
import os

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ITEMS = [
    ("landscape-design", "Landscape Design", "Diseño de Paisaje"),
    ("landscape-construction", "Landscape Construction", "Construcción de Paisaje"),
    ("landscape-management", "Landscape Management", "Manejo de Paisaje"),
]


def render_head(title, description):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">

<!-- Fonts: Fraunces (confident serif for headlines) + Inter (clean sans for body/nav) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<!-- AOS (Animate On Scroll) - restrained fade-up reveals only -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">

<link rel="stylesheet" href="../../style.css">"""


def render_header(active_slug):
    dropdown_items = []
    for slug, label_en, label_es in NAV_ITEMS:
        active_attrs = ' class="active" aria-current="page"' if slug == active_slug else ""
        dropdown_items.append(
            f'            <li><a href="../../services/{slug}/"{active_attrs} data-en="{label_en}" data-es="{label_es}">{label_en}</a></li>'
        )
    dropdown_html = "\n".join(dropdown_items)

    return f"""<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="../../index.html" class="logo" aria-label="Luna &amp; Sons Landscaping home">
      <img class="logo-mark" src="../../images/logo-moon.png" alt="Luna &amp; Sons moon logo">
      <span class="logo-text">
        <span class="logo-name">Luna &amp; Sons</span>
        <span class="logo-sub" data-en="Landscaping" data-es="Paisajismo">Landscaping</span>
      </span>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Primary">
      <ul>
        <li><a href="../../index.html" data-en="Home" data-es="Inicio">Home</a></li>
        <li class="has-dropdown">
          <div class="nav-link-wrap">
            <a href="../../index.html#services" data-en="Services" data-es="Servicios">Services</a>
            <button class="dropdown-toggle" type="button" aria-expanded="false" aria-controls="services-dropdown" aria-label="Toggle services menu">
              <i data-lucide="chevron-down" aria-hidden="true"></i>
            </button>
          </div>
          <ul class="dropdown-menu" id="services-dropdown">
{dropdown_html}
          </ul>
        </li>
        <li><a href="../../index.html#projects" data-en="Projects" data-es="Proyectos">Projects</a></li>
        <li><a href="../../index.html#contact" data-en="Contact" data-es="Contacto">Contact</a></li>
      </ul>
    </nav>

    <div class="header-actions">
      <a class="header-phone" href="tel:+18052682808">
        <i data-lucide="phone" aria-hidden="true"></i>
        <span>(805) 268-2808</span>
      </a>
      <button class="lang-toggle" id="lang-toggle" type="button" aria-label="Switch language / Cambiar idioma">
        <span class="lang-en-flag" data-active="true">EN</span>/<span class="lang-es-flag">ES</span>
      </button>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="main-nav">
        <i data-lucide="menu" aria-hidden="true"></i>
      </button>
    </div>
  </div>
</header>"""


def render_media(css_class, image, placeholder_note, extra_attrs="", loading="lazy"):
    """Renders either a real <img> (when `image` dict is given) or the dashed
    placeholder box. `image`: {src, width, height, alt} — src is relative to
    the images/ directory (e.g. "luna-sons-paver-patio-01.jpg")."""
    if image:
        fetchpriority = ' fetchpriority="high"' if loading == "eager" else ""
        return (
            f'<div class="{css_class}"{extra_attrs}>'
            f'<img src="../../images/{image["src"]}" width="{image["width"]}" height="{image["height"]}" '
            f'alt="{image["alt"]}" loading="{loading}"{fetchpriority}>'
            f"</div>"
        )
    return (
        f'<div class="{css_class} placeholder-img"{extra_attrs} role="img" aria-label="Placeholder: {placeholder_note} — image coming soon">'
        f'<i data-lucide="image" aria-hidden="true"></i>'
        f"<span>Image coming soon</span>"
        f"</div>"
    )


def render_hero(title, subheading, image_note, image=None):
    media_html = render_media(
        "service-hero-media placeholder-img--bleed" if not image else "service-hero-media",
        image, image_note, loading="eager",
    )
    return f"""  <!-- =========================================================
       SERVICE HERO
  ========================================================= -->
  <div class="service-accent-bar"></div>
  <section class="service-hero">
    <!-- PLACEHOLDER PHOTO: {image_note} -->
    {media_html}
    <div class="service-hero-scrim"></div>
    <div class="container service-hero-content" data-aos="fade-up" data-aos-duration="600" data-aos-easing="ease-out">
      <span class="eyebrow eyebrow-light">Services</span>
      <h1>{title}</h1>
      <p>{subheading}</p>
    </div>
  </section>"""


def render_intro(paragraphs, image_note, image=None):
    paras_html = "\n        ".join(f"<p>{p}</p>" for p in paragraphs)
    media_html = render_media(
        "service-intro-media", image, image_note,
        extra_attrs=' data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out" data-aos-delay="100"',
    )
    return f"""  <!-- =========================================================
       INTRO
  ========================================================= -->
  <section class="service-intro">
    <div class="container service-intro-grid">
      <div class="service-intro-copy" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
        {paras_html}
      </div>
      <!-- PLACEHOLDER PHOTO: {image_note} -->
      {media_html}
    </div>
  </section>"""


def render_block(block, index):
    """block: {heading, body: [..paragraphs..], image_side: 'left' | 'right' | None, image_note, image}"""
    paras_html = "\n          ".join(f"<p>{p}</p>" for p in block["body"])
    heading_html = f'<h3>{block["heading"]}</h3>' if block.get("heading") else ""

    if block.get("image_side") is None:
        return f"""      <div class="service-block service-block--text-only" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
        <div class="service-block-copy">
          {heading_html}
          {paras_html}
        </div>
      </div>"""

    reverse_class = " reverse" if block["image_side"] == "left" else ""
    media_html = render_media("service-block-media", block.get("image"), block.get("image_note", ""))
    return f"""      <div class="service-block{reverse_class}" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
        <div class="service-block-copy">
          {heading_html}
          {paras_html}
        </div>
        <!-- PLACEHOLDER PHOTO: {block.get("image_note", "")} -->
        {media_html}
      </div>"""


def render_blocks(blocks):
    blocks_html = "\n".join(render_block(b, i) for i, b in enumerate(blocks))
    return f"""  <!-- =========================================================
       REPEATING CONTENT BLOCKS
  ========================================================= -->
  <section class="service-blocks-section">
    <div class="container service-blocks">
{blocks_html}
    </div>
  </section>"""


def render_cta(heading, button_text):
    return f"""  <!-- =========================================================
       CTA
  ========================================================= -->
  <section class="service-cta">
    <div class="container" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
      <h2>{heading}</h2>
      <a href="../../index.html#contact" class="btn btn-primary">
        <span>{button_text}</span>
        <i data-lucide="arrow-right" aria-hidden="true"></i>
      </a>
    </div>
  </section>"""


# Sitewide constants — identical on every service page, so they live here once
# rather than being repeated (or omitted) in each page's data dict.
SITE_TAGLINE = "Landscapes built to last."
SITE_PHONE_DISPLAY = "(805) 268-2808"
SITE_PHONE_HREF = "tel:+18052682808"
SITE_LICENSE = "45178"
# TODO: swap in the real Google Business review link once available
SITE_REVIEW_HREF = "https://search.google.com/local/writereview?placeid=REPLACE_WITH_GOOGLE_PLACE_ID"


def render_footer():
    """The single consolidated footer: brand block (logo, wordmark, tagline,
    contact, review button, social) + Quick Links / Services / Contact columns
    + copyright bar. Used unconditionally by every service page via render_page,
    so it's shared sitewide by construction."""
    return f"""<footer class="service-footer">
  <div class="container">
    <div class="service-footer-brand" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
      <img class="service-footer-logo" src="../../images/logo/luna-sons-moon.jpg" width="900" height="900" alt="Luna & Sons Landscaping moon logo" loading="lazy">
      <div class="service-footer-wordmark">
        <span class="service-footer-name">Luna &amp; Sons</span>
        <span class="service-footer-sub"><span class="closing-line"></span>Landscaping<span class="closing-line"></span></span>
      </div>
      <p class="service-footer-tagline" data-en="{SITE_TAGLINE}" data-es="Paisajes construidos para durar.">{SITE_TAGLINE}</p>
      <p class="service-footer-contact-line">
        <a href="{SITE_PHONE_HREF}">{SITE_PHONE_DISPLAY}</a> &middot; License #{SITE_LICENSE}
      </p>
      <a class="btn btn-primary service-footer-review" href="{SITE_REVIEW_HREF}" target="_blank" rel="noopener">
        <span data-en="Leave a Review" data-es="Dejar una Reseña">Leave a Review</span>
        <i data-lucide="star" aria-hidden="true"></i>
      </a>
      <div class="service-footer-social">
        <a href="#" aria-label="Luna & Sons on Facebook"><i data-lucide="facebook" aria-hidden="true"></i></a>
        <a href="#" aria-label="Luna & Sons on Instagram"><i data-lucide="instagram" aria-hidden="true"></i></a>
        <a href="#" aria-label="Luna & Sons on YouTube"><i data-lucide="youtube" aria-hidden="true"></i></a>
      </div>
    </div>

    <div class="service-footer-links">
      <div class="service-footer-col">
        <h4 data-en="Quick Links" data-es="Enlaces Rápidos">Quick Links</h4>
        <ul>
          <li><a href="../../index.html" data-en="Home" data-es="Inicio">Home</a></li>
          <li><a href="../../index.html#about" data-en="About" data-es="Sobre Nosotros">About</a></li>
          <li><a href="../../index.html#services" data-en="Services" data-es="Servicios">Services</a></li>
          <li><a href="../../index.html#projects" data-en="Projects" data-es="Proyectos">Projects</a></li>
          <li><a href="../../index.html#contact" data-en="Contact" data-es="Contacto">Contact</a></li>
        </ul>
      </div>

      <div class="service-footer-col">
        <h4 data-en="Services" data-es="Servicios">Services</h4>
        <ul>
          <li><a href="../../index.html#services" data-en="Landscape Design" data-es="Diseño de Paisaje">Landscape Design</a></li>
          <li><a href="../../index.html#services" data-en="Hardscaping" data-es="Hardscape">Hardscaping</a></li>
          <li><a href="../../index.html#services" data-en="Irrigation Systems" data-es="Sistemas de Riego">Irrigation Systems</a></li>
          <li><a href="../../index.html#services" data-en="Planting" data-es="Plantación">Planting</a></li>
          <li><a href="../../index.html#services" data-en="Sod Installation" data-es="Instalación de Césped">Sod Installation</a></li>
          <li><a href="../../index.html#services" data-en="Tree Services" data-es="Servicios de Árboles">Tree Services</a></li>
        </ul>
      </div>

      <div class="service-footer-col">
        <h4 data-en="Contact" data-es="Contacto">Contact</h4>
        <ul class="service-footer-contact-list">
          <li><i data-lucide="map-pin" aria-hidden="true"></i><span data-en="Santa Maria, CA" data-es="Santa Maria, CA">Santa Maria, CA</span></li>
          <li><i data-lucide="phone" aria-hidden="true"></i><a href="{SITE_PHONE_HREF}">{SITE_PHONE_DISPLAY}</a></li>
          <li><i data-lucide="mail" aria-hidden="true"></i><a href="mailto:info@lunaandsonslandscaping.com">info@lunaandsonslandscaping.com</a></li>
        </ul>
      </div>
    </div>
  </div>

  <div class="service-footer-bottom">
    <div class="container service-footer-bottom-inner">
      <p>&copy; <span id="year"></span> <span data-en="Luna &amp; Sons Landscaping. All rights reserved." data-es="Luna &amp; Sons Landscaping. Todos los derechos reservados.">Luna &amp; Sons Landscaping. All rights reserved.</span></p>
      <button class="lang-toggle" type="button" aria-label="Switch language / Cambiar idioma">
        <span class="lang-en-flag" data-active="true">EN</span>/<span class="lang-es-flag">ES</span>
      </button>
    </div>
  </div>
</footer>"""


def render_page(data):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(data["meta_title"], data["meta_description"])}
</head>
<body>

<!-- =========================================================
     HEADER / NAV
========================================================= -->
{render_header(data["slug"])}

<main>

{render_hero(data["title"], data["subheading"], data["hero_image_note"], data.get("hero_image"))}

{render_intro(data["intro_paragraphs"], data["intro_image_note"], data.get("intro_image"))}

{render_blocks(data["blocks"])}

{render_cta(data["cta_heading"], data["cta_button_text"])}

</main>

<!-- =========================================================
     FOOTER
========================================================= -->
{render_footer()}

<script src="https://unpkg.com/lucide@0.462.0/dist/umd/lucide.js"></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script src="../../script.js"></script>
</body>
</html>
"""


PAGES = [
    {
        "slug": "landscape-design",
        "meta_title": "Landscape Design | Luna &amp; Sons Landscaping",
        "meta_description": "Custom landscape design in Santa Maria, CA — drought-tolerant planting layouts, hardscape placement, irrigation zones, and lighting design from Luna &amp; Sons Landscaping.",
        "title": "Landscape Design",
        "subheading": "Outdoor spaces designed to work as hard as the Central Coast does.",
        "hero_image_note": "full-width hero photo of a completed design project",
        "intro_paragraphs": [
            "Every great landscape starts with a plan. Our design process takes into account your property's layout, climate, and how you actually want to use the space — whether that's a low-maintenance front yard, an entertaining area built for warm Santa Maria evenings, or a full property transformation. We walk the site with you first, so the plan we hand you is built around how your yard actually sits, not a generic template.",
        ],
        "intro_image_note": "design process / rendering example",
        "intro_image": {
            "src": "luna-sons-planting-bed-03.jpg", "width": 1600, "height": 1120,
            "alt": "Luna & Sons landscape design featuring a front-entry bed with hostas, coral bells, and ornamental grasses",
        },
        "blocks": [
            {
                "heading": "From Concept to Detailed Plans",
                "body": [
                    "We handle everything from initial concept to detailed design plans, including drought-tolerant planting layouts, hardscape placement, irrigation zones, and lighting. Each plan lays out exactly which materials we're using and where every feature goes, so you can see the finished space before any of it is built.",
                ],
                "image_side": "right",
                "image_note": "design plan sketch or rendering",
                "image": {
                    "src": "luna-sons-flagstone-patio-02.jpg", "width": 1600, "height": 1120,
                    "alt": "Irregular flagstone patio with a yellow bistro set beside a moss-covered boulder accent",
                },
            },
            {
                "heading": "Know Before We Break Ground",
                "body": [
                    "You'll know exactly what you're getting before we break ground. That means a clear plan and a real quote in hand — not a verbal estimate — so there are no surprises once construction starts.",
                ],
                "image_side": "left",
                "image_note": "finished outdoor living space built from a Luna & Sons design plan",
                "image": {
                    "src": "luna-sons-pergola-01.jpg", "width": 1600, "height": 1120,
                    "alt": "Hardtop pergola over a paver patio with a stone-clad seating area and gravel bed",
                },
            },
            {
                "heading": "Water-Wise, Low-Maintenance Choices",
                "body": [
                    "Central Coast summers are long and dry, so every design leans on drought-tolerant plants grouped by water need, with irrigation zoned to match. The result is a landscape that holds its color through the dry months without running up your water bill or demanding a weekend of upkeep every week.",
                ],
                "image_side": "right",
                "image_note": "drought-tolerant rock garden bed",
                "image": {
                    "src": "luna-sons-planting-bed-01.jpg", "width": 1600, "height": 1292,
                    "alt": "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
                },
            },
        ],
        "cta_heading": "Ready to plan your space?",
        "cta_button_text": "Get a Free Estimate",
    },
    {
        "slug": "landscape-construction",
        "meta_title": "Landscape Construction | Luna &amp; Sons Landscaping",
        "meta_description": "Full-service landscape construction in Santa Maria, CA — hardscaping, irrigation, planting, drainage, and grading, built to last by a licensed &amp; insured crew.",
        "title": "Landscape Construction",
        "subheading": "Built right the first time — hardscape, irrigation, and planting that lasts.",
        "hero_image_note": "full-width hero photo of a completed construction project",
        "intro_paragraphs": [
            "A good design only matters if it's built well. Our construction crews handle the full installation: hardscaping (patios, walkways, retaining walls), irrigation systems, planting, drainage, and grading — all done to hold up against Central Coast conditions for years to come.",
        ],
        "intro_image_note": "hardscape/patio installation",
        "intro_image": {
            "src": "luna-sons-paver-patio-02.jpg", "width": 1123, "height": 1600,
            "alt": "Paver patio with a lounge sofa and dining set beneath a brick chimney backdrop",
        },
        "blocks": [
            {
                "heading": "Licensed, Insured &amp; Fully Managed",
                "body": [
                    "We're licensed and insured, and we manage every phase of the build so you're not coordinating multiple contractors.",
                ],
                "image_side": "left",
                "image_note": "crew managing a job site",
                "image": {
                    "src": "luna-sons-retaining-wall-01.jpg", "width": 1600, "height": 1292,
                    "alt": "A Luna & Sons retaining wall build — curved segmental block planters framing a brick-home entry",
                },
            },
            {
                "heading": "Ground-Breaking to Final Walkthrough",
                "body": [
                    "From ground-breaking to final walkthrough, we keep the process straightforward and the communication clear.",
                ],
                "image_side": "right",
                "image_note": "irrigation or planting work in progress",
                "image": {
                    "src": "luna-sons-paver-walkway-01.jpg", "width": 971, "height": 1600,
                    "alt": "Square concrete paver walkway set in pea gravel along a side-yard privacy fence",
                },
            },
        ],
        "cta_heading": "Ready to build?",
        "cta_button_text": "Get a Free Estimate",
    },
    {
        "slug": "landscape-management",
        "meta_title": "Landscape Management | Luna &amp; Sons Landscaping",
        "meta_description": "Ongoing landscape management and maintenance in Santa Maria, CA — mowing, seasonal planting refreshes, irrigation checks, fertilization, and year-round upkeep.",
        "title": "Landscape Management",
        "subheading": "Ongoing care to keep your landscape looking its best, year-round.",
        "hero_image_note": "full-width hero photo of a well-maintained landscape",
        "intro_paragraphs": [
            "A landscape is an investment — regular maintenance is what protects it.",
        ],
        "intro_image_note": "maintenance crew at work",
        "intro_image": {
            "src": "luna-sons-planting-bed-01.jpg", "width": 1600, "height": 1292,
            "alt": "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
        },
        "blocks": [
            {
                "heading": "Management",
                "body": [
                    "Our management services include routine mowing and trimming, seasonal planting refreshes, irrigation checks and repairs, fertilization, and general upkeep tailored to your property's needs.",
                ],
                "image_side": "right",
                "image_note": "maintenance crew at work",
                "image": {
                    "src": "luna-sons-retaining-wall-03.jpg", "width": 1123, "height": 1600,
                    "alt": "Curved stone retaining wall planter with purple-flowering shrubs above an artificial turf lawn",
                },
            },
            {
                "heading": "Maintenance",
                "body": [
                    "Whether you need a one-time cleanup or a standing maintenance schedule, our team treats every property like it's our own — because in a lot of ways, it is. Family-owned since 2019, we've built our reputation on doing the small things right, consistently.",
                ],
                "image_side": None,
            },
        ],
        "cta_heading": "Ready for ongoing care?",
        "cta_button_text": "Get a Free Estimate",
    },
]


def main():
    for data in PAGES:
        out_dir = os.path.join(SITE_ROOT, "services", data["slug"])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
        with open(out_path, "w") as f:
            f.write(render_page(data))
        print(f"wrote {os.path.relpath(out_path, SITE_ROOT)}")


if __name__ == "__main__":
    main()
