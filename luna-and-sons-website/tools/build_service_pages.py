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


def render_head(title, description, depth="../../"):
    """depth: relative path prefix back to the site root — see render_header()."""
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

<link rel="stylesheet" href="{depth}style.css">"""


def render_header(active, depth="../../"):
    """active: 'home' | 'blog' | 'contact' | 'services:<slug>' | None.
    depth: relative path prefix back to the site root — '../../' for pages one
    directory deep in a category (services/<slug>/, blog/<slug>/), '../' for
    pages one level deep overall (contact/, blog/)."""
    is_service_page = bool(active) and active.startswith("services:")
    active_service_slug = active.split(":", 1)[1] if is_service_page else None

    def nav_class(key):
        return ' class="active" aria-current="page"' if active == key else ""

    services_class = ' class="active" aria-current="page"' if is_service_page else ""

    dropdown_items = []
    for slug, label_en, label_es in NAV_ITEMS:
        active_attrs = ' class="active" aria-current="page"' if slug == active_service_slug else ""
        dropdown_items.append(
            f'            <li><a href="{depth}services/{slug}/"{active_attrs} data-en="{label_en}" data-es="{label_es}">{label_en}</a></li>'
        )
    dropdown_html = "\n".join(dropdown_items)

    return f"""<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="{depth}index.html" class="logo" aria-label="Luna &amp; Sons Landscaping home">
      <img class="logo-mark" src="{depth}images/logo-moon.png" alt="Luna &amp; Sons moon logo">
      <span class="logo-text">
        <span class="logo-name">Luna &amp; Sons</span>
        <span class="logo-sub" data-en="Landscaping" data-es="Paisajismo">Landscaping</span>
      </span>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Primary">
      <ul>
        <li><a href="{depth}index.html"{nav_class("home")} data-en="Home" data-es="Inicio">Home</a></li>
        <li class="has-dropdown">
          <div class="nav-link-wrap">
            <a href="{depth}index.html#services"{services_class} data-en="Services" data-es="Servicios">Services</a>
            <button class="dropdown-toggle" type="button" aria-expanded="false" aria-controls="services-dropdown" aria-label="Toggle services menu">
              <i data-lucide="chevron-down" aria-hidden="true"></i>
            </button>
          </div>
          <ul class="dropdown-menu" id="services-dropdown">
{dropdown_html}
          </ul>
        </li>
        <li><a href="{depth}blog/index.html"{nav_class("blog")} data-en="Blog" data-es="Blog">Blog</a></li>
        <li><a href="{depth}contact/index.html"{nav_class("contact")} data-en="Contact" data-es="Contacto">Contact</a></li>
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
  <div class="header-stripe" aria-hidden="true">
    <span class="header-stripe-half header-stripe-purple"></span>
    <span class="header-stripe-half header-stripe-black"></span>
  </div>
</header>"""


def bi(pair):
    """pair: (en, es) -> data-en/data-es attribute string, English as the initial content."""
    en, es = pair
    return f'data-en="{en}" data-es="{es}">{en}'


def render_media(css_class, image, placeholder_note, extra_attrs="", loading="lazy"):
    """Renders either a real <img> (when `image` dict is given) or the dashed
    placeholder box. `image`: {src, width, height, alt: (en, es)} — src is
    relative to the images/ directory (e.g. "luna-sons-paver-patio-01.jpg")."""
    if image:
        fetchpriority = ' fetchpriority="high"' if loading == "eager" else ""
        alt_en, alt_es = image["alt"]
        return (
            f'<div class="{css_class}"{extra_attrs}>'
            f'<img src="../../images/{image["src"]}" width="{image["width"]}" height="{image["height"]}" '
            f'alt="{alt_en}" data-alt-en="{alt_en}" data-alt-es="{alt_es}" loading="{loading}"{fetchpriority}>'
            f"</div>"
        )
    return (
        f'<div class="{css_class} placeholder-img"{extra_attrs} role="img" aria-label="Placeholder: {placeholder_note} — image coming soon">'
        f'<i data-lucide="image" aria-hidden="true"></i>'
        f'<span data-en="Image coming soon" data-es="Imagen próximamente">Image coming soon</span>'
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
      <span class="eyebrow eyebrow-light" data-en="Services" data-es="Servicios">Services</span>
      <h1 {bi(title)}</h1>
      <p {bi(subheading)}</p>
    </div>
  </section>"""


def render_intro(paragraphs, image_note, image=None):
    paras_html = "\n        ".join(f"<p {bi(p)}</p>" for p in paragraphs)
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
    """block: {heading: (en, es) | None, body: [(en, es), ...], image_side, image_note, image}"""
    paras_html = "\n          ".join(f"<p {bi(p)}</p>" for p in block["body"])
    heading_html = f'<h3 {bi(block["heading"])}</h3>' if block.get("heading") else ""

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
      <h2 {bi(heading)}</h2>
      <a href="../../contact/index.html" class="btn btn-primary">
        <span {bi(button_text)}</span>
        <i data-lucide="arrow-right" aria-hidden="true"></i>
      </a>
    </div>
  </section>"""


# Sitewide constants — identical on every service page, so they live here once
# rather than being repeated (or omitted) in each page's data dict.
SITE_TAGLINE = "Landscapes built to last."
SITE_PHONE_DISPLAY = "(805) 268-2808"
SITE_PHONE_HREF = "tel:+18052682808"
SITE_LICENSE = "1160930"
# TODO: swap in the real Google Business review link once available
SITE_REVIEW_HREF = "https://search.google.com/local/writereview?placeid=REPLACE_WITH_GOOGLE_PLACE_ID"


def render_footer(depth="../../"):
    """The single consolidated footer: brand block (logo, wordmark, tagline,
    contact, review button, social) + Quick Links / Services / Contact columns
    + copyright bar. Used unconditionally by every service page via render_page,
    so it's shared sitewide by construction."""
    return f"""<footer class="service-footer">
  <div class="container">
    <div class="service-footer-brand" data-aos="fade-up" data-aos-duration="550" data-aos-easing="ease-out">
      <img class="service-footer-logo" src="{depth}images/logo/luna-sons-moon.jpg" width="900" height="900" alt="Luna & Sons Landscaping moon logo" loading="lazy">
      <div class="service-footer-wordmark">
        <span class="service-footer-name">Luna &amp; Sons</span>
        <span class="service-footer-sub"><span class="closing-line"></span><span data-en="Landscaping" data-es="Paisajismo">Landscaping</span><span class="closing-line"></span></span>
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
          <li><a href="{depth}index.html" data-en="Home" data-es="Inicio">Home</a></li>
          <li><a href="{depth}index.html#about" data-en="About" data-es="Sobre Nosotros">About</a></li>
          <li><a href="{depth}index.html#services" data-en="Services" data-es="Servicios">Services</a></li>
          <li><a href="{depth}blog/index.html" data-en="Blog" data-es="Blog">Blog</a></li>
          <li><a href="{depth}contact/index.html" data-en="Contact" data-es="Contacto">Contact</a></li>
        </ul>
      </div>

      <div class="service-footer-col">
        <h4 data-en="Services" data-es="Servicios">Services</h4>
        <ul>
          <li><a href="{depth}index.html#services" data-en="Landscape Design" data-es="Diseño de Paisaje">Landscape Design</a></li>
          <li><a href="{depth}index.html#services" data-en="Landscape Construction" data-es="Construcción de Paisaje">Landscape Construction</a></li>
          <li><a href="{depth}index.html#services" data-en="Landscape Management" data-es="Manejo de Paisaje">Landscape Management</a></li>
        </ul>
      </div>

      <div class="service-footer-col">
        <h4 data-en="Contact" data-es="Contacto">Contact</h4>
        <ul class="service-footer-contact-list">
          <li><i data-lucide="map-pin" aria-hidden="true"></i><span data-en="Santa Maria, CA" data-es="Santa Maria, CA">Santa Maria, CA</span></li>
          <li><i data-lucide="phone" aria-hidden="true"></i><a href="{SITE_PHONE_HREF}">{SITE_PHONE_DISPLAY}</a></li>
          <li><i data-lucide="mail" aria-hidden="true"></i><a href="mailto:lunaandsonslandscape@gmail.com">lunaandsonslandscape@gmail.com</a></li>
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
{render_header(f'services:{data["slug"]}')}

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
        "title": ("Landscape Design", "Diseño de Paisaje"),
        "subheading": (
            "Outdoor spaces designed to work as hard as the Central Coast does.",
            "Espacios exteriores diseñados para trabajar tan duro como la Costa Central.",
        ),
        "hero_image_note": "full-width hero photo of a completed design project",
        "intro_paragraphs": [
            (
                "Every great landscape starts with a plan. Our design process takes into account your property's layout, climate, and how you actually want to use the space — whether that's a low-maintenance front yard, an entertaining area built for warm Santa Maria evenings, or a full property transformation. We walk the site with you first, so the plan we hand you is built around how your yard actually sits, not a generic template.",
                "Todo gran paisaje comienza con un plan. Nuestro proceso de diseño toma en cuenta la disposición de su propiedad, el clima y cómo realmente quiere usar el espacio — ya sea un jardín delantero de bajo mantenimiento, un área para entretener pensada para las cálidas noches de Santa Maria, o una transformación completa de la propiedad. Primero recorremos el terreno junto a usted, para que el plan que le entreguemos esté diseñado según cómo es realmente su jardín, y no una plantilla genérica.",
            ),
        ],
        "intro_image_note": "design process / rendering example",
        "intro_image": {
            "src": "luna-sons-planting-bed-03.jpg", "width": 1600, "height": 1120,
            "alt": (
                "Luna & Sons landscape design featuring a front-entry bed with hostas, coral bells, and ornamental grasses",
                "Diseño de paisaje de Luna & Sons con un jardín de entrada con hostas, campanillas de coral y pastos ornamentales",
            ),
        },
        "blocks": [
            {
                "heading": ("From Concept to Detailed Plans", "Del Concepto a Planes Detallados"),
                "body": [
                    (
                        "We handle everything from initial concept to detailed design plans, including drought-tolerant planting layouts, hardscape placement, irrigation zones, and lighting. Each plan lays out exactly which materials we're using and where every feature goes, so you can see the finished space before any of it is built.",
                        "Nos encargamos de todo, desde el concepto inicial hasta los planes de diseño detallados, incluyendo la distribución de plantas resistentes a la sequía, la ubicación del hardscape, las zonas de riego y la iluminación. Cada plan detalla exactamente qué materiales usaremos y dónde irá cada elemento, para que pueda ver el espacio terminado antes de que se construya.",
                    ),
                ],
                "image_side": "right",
                "image_note": "design plan sketch or rendering",
                "image": {
                    "src": "luna-sons-flagstone-patio-02.jpg", "width": 1600, "height": 1120,
                    "alt": (
                        "Irregular flagstone patio with a yellow bistro set beside a moss-covered boulder accent",
                        "Patio de piedra laja irregular con un juego de bistró amarillo junto a una roca decorativa cubierta de musgo",
                    ),
                },
            },
            {
                "heading": ("Know Before We Break Ground", "Sepa Antes de Comenzar la Obra"),
                "body": [
                    (
                        "You'll know exactly what you're getting before we break ground. That means a clear plan and a real quote in hand — not a verbal estimate — so there are no surprises once construction starts.",
                        "Sabrá exactamente qué va a recibir antes de que comencemos la obra. Eso significa un plan claro y una cotización real en mano — no un estimado verbal — para que no haya sorpresas una vez que inicie la construcción.",
                    ),
                ],
                "image_side": "left",
                "image_note": "finished outdoor living space built from a Luna & Sons design plan",
                "image": {
                    "src": "luna-sons-pergola-01.jpg", "width": 1600, "height": 1120,
                    "alt": (
                        "Hardtop pergola over a paver patio with a stone-clad seating area and gravel bed",
                        "Pérgola con techo sobre un patio de adoquines, con área de asientos revestida de piedra y jardín de grava",
                    ),
                },
            },
            {
                "heading": ("Water-Wise, Low-Maintenance Choices", "Opciones Inteligentes con el Agua y de Bajo Mantenimiento"),
                "body": [
                    (
                        "Central Coast summers are long and dry, so every design leans on drought-tolerant plants grouped by water need, with irrigation zoned to match. The result is a landscape that holds its color through the dry months without running up your water bill or demanding a weekend of upkeep every week.",
                        "Los veranos en la Costa Central son largos y secos, por lo que cada diseño se apoya en plantas resistentes a la sequía agrupadas según su necesidad de agua, con el riego zonificado para coincidir. El resultado es un paisaje que mantiene su color durante los meses secos sin disparar su factura de agua ni exigir un fin de semana de mantenimiento cada semana.",
                    ),
                ],
                "image_side": "right",
                "image_note": "drought-tolerant rock garden bed",
                "image": {
                    "src": "luna-sons-planting-bed-01.jpg", "width": 1600, "height": 1292,
                    "alt": (
                        "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
                        "Jardín de rocas resistente a la sequía con algodoncillo en flor y pastos ornamentales junto a un borde curvo de césped",
                    ),
                },
            },
        ],
        "cta_heading": ("Ready to plan your space?", "¿Listo para planificar su espacio?"),
        "cta_button_text": ("Get a Free Estimate", "Obtenga una Cotización Gratis"),
    },
    {
        "slug": "landscape-construction",
        "meta_title": "Landscape Construction | Luna &amp; Sons Landscaping",
        "meta_description": "Full-service landscape construction in Santa Maria, CA — hardscaping, irrigation, planting, drainage, and grading, built to last by a licensed &amp; insured crew.",
        "title": ("Landscape Construction", "Construcción de Paisaje"),
        "subheading": (
            "Built right the first time — hardscape, irrigation, and planting that lasts.",
            "Construido bien desde la primera vez — hardscape, riego y plantación que perduran.",
        ),
        "hero_image_note": "full-width hero photo of a completed construction project",
        "intro_paragraphs": [
            (
                "A good design only matters if it's built well. Our construction crews handle the full installation: hardscaping (patios, walkways, retaining walls), irrigation systems, planting, drainage, and grading — all done to hold up against Central Coast conditions for years to come.",
                "Un buen diseño solo importa si se construye bien. Nuestros equipos de construcción se encargan de la instalación completa: hardscape (patios, senderos, muros de contención), sistemas de riego, plantación, drenaje y nivelación — todo hecho para resistir las condiciones de la Costa Central durante muchos años.",
            ),
        ],
        "intro_image_note": "hardscape/patio installation",
        "intro_image": {
            "src": "luna-sons-paver-patio-02.jpg", "width": 1123, "height": 1600,
            "alt": (
                "Paver patio with a lounge sofa and dining set beneath a brick chimney backdrop",
                "Patio de adoquines con sofá lounge y juego de comedor frente a una chimenea de ladrillo",
            ),
        },
        "blocks": [
            {
                "heading": ("Licensed, Insured &amp; Fully Managed", "Con Licencia, Asegurados y Totalmente Gestionados"),
                "body": [
                    (
                        "We're licensed and insured, and we manage every phase of the build so you're not coordinating multiple contractors.",
                        "Contamos con licencia y seguro, y gestionamos cada fase de la construcción para que usted no tenga que coordinar con múltiples contratistas.",
                    ),
                ],
                "image_side": "left",
                "image_note": "crew managing a job site",
                "image": {
                    "src": "luna-sons-retaining-wall-01.jpg", "width": 1600, "height": 1292,
                    "alt": (
                        "A Luna & Sons retaining wall build — curved segmental block planters framing a brick-home entry",
                        "Construcción de un muro de contención de Luna & Sons — jardineras curvas de bloque enmarcando la entrada de una casa de ladrillo",
                    ),
                },
            },
            {
                "heading": ("Ground-Breaking to Final Walkthrough", "Desde el Inicio de la Obra Hasta la Revisión Final"),
                "body": [
                    (
                        "From ground-breaking to final walkthrough, we keep the process straightforward and the communication clear.",
                        "Desde el inicio de la obra hasta la revisión final, mantenemos el proceso sencillo y la comunicación clara.",
                    ),
                ],
                "image_side": "right",
                "image_note": "irrigation or planting work in progress",
                "image": {
                    "src": "luna-sons-paver-walkway-01.jpg", "width": 971, "height": 1600,
                    "alt": (
                        "Square concrete paver walkway set in pea gravel along a side-yard privacy fence",
                        "Camino de adoquines de concreto cuadrados sobre grava junto a una cerca lateral privada",
                    ),
                },
            },
        ],
        "cta_heading": ("Ready to build?", "¿Listo para construir?"),
        "cta_button_text": ("Get a Free Estimate", "Obtenga una Cotización Gratis"),
    },
    {
        "slug": "landscape-management",
        "meta_title": "Landscape Management | Luna &amp; Sons Landscaping",
        "meta_description": "Ongoing landscape management and maintenance in Santa Maria, CA — mowing, seasonal planting refreshes, irrigation checks, fertilization, and year-round upkeep.",
        "title": ("Landscape Management", "Manejo de Paisaje"),
        "subheading": (
            "Ongoing care to keep your landscape looking its best, year-round.",
            "Cuidado continuo para que su paisaje luzca lo mejor posible durante todo el año.",
        ),
        "hero_image_note": "full-width hero photo of a well-maintained landscape",
        "intro_paragraphs": [
            (
                "A landscape is an investment — regular maintenance is what protects it.",
                "Un paisaje es una inversión — el mantenimiento regular es lo que la protege.",
            ),
        ],
        "intro_image_note": "maintenance crew at work",
        "intro_image": {
            "src": "luna-sons-planting-bed-01.jpg", "width": 1600, "height": 1292,
            "alt": (
                "Drought-tolerant rock garden bed with flowering milkweed and ornamental grasses along a curved lawn edge",
                "Jardín de rocas resistente a la sequía con algodoncillo en flor y pastos ornamentales junto a un borde curvo de césped",
            ),
        },
        "blocks": [
            {
                "heading": ("Management", "Gestión"),
                "body": [
                    (
                        "Our management services include routine mowing and trimming, seasonal planting refreshes, irrigation checks and repairs, fertilization, and general upkeep tailored to your property's needs.",
                        "Nuestros servicios de gestión incluyen corte y poda de rutina, renovación estacional de plantas, revisión y reparación de riego, fertilización, y mantenimiento general adaptado a las necesidades de su propiedad.",
                    ),
                ],
                "image_side": "right",
                "image_note": "maintenance crew at work",
                "image": {
                    "src": "luna-sons-retaining-wall-03.jpg", "width": 1123, "height": 1600,
                    "alt": (
                        "Curved stone retaining wall planter with purple-flowering shrubs above an artificial turf lawn",
                        "Jardinera curva de muro de piedra con arbustos de flores púrpuras sobre un césped artificial",
                    ),
                },
            },
            {
                "heading": ("Maintenance", "Mantenimiento"),
                "body": [
                    (
                        "Whether you need a one-time cleanup or a standing maintenance schedule, our team treats every property like it's our own — because in a lot of ways, it is. Family-owned since 2019, we've built our reputation on doing the small things right, consistently.",
                        "Ya sea que necesite una limpieza única o un programa de mantenimiento continuo, nuestro equipo trata cada propiedad como si fuera propia — porque en muchos sentidos, lo es. Familia local desde 2019, hemos construido nuestra reputación haciendo bien las pequeñas cosas, de manera constante.",
                    ),
                ],
                "image_side": None,
            },
        ],
        "cta_heading": ("Ready for ongoing care?", "¿Listo para el cuidado continuo?"),
        "cta_button_text": ("Get a Free Estimate", "Obtenga una Cotización Gratis"),
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
