#!/usr/bin/env python3
"""
Shared pieces for every generated page: head, header/nav, closing CTA band,
consultation form, footer. One definition => identical nav/footer sitewide.

Everything the client or agency may need to change lives in the CONFIG block.
"""
import html
import os
import re

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- CONFIG
PHONE_DISPLAY = "(805) 268-2808"
PHONE_HREF = "tel:+18052682808"
EMAIL = "lunaandsonslandscape@gmail.com"
LICENSE = "1160930"
SITE_URL = "https://lunaandsonslandscaping.com"
FACEBOOK_URL = "https://www.facebook.com/LunaAndSonsLandscape"
INSTAGRAM_URL = "https://www.instagram.com/lunaandsonslandscaping"

# Google Business Profile. Fill these in ONLY with confirmed values.
#   GOOGLE_REVIEWS_URL : the public "see all reviews" link (or write-a-review link)
#   REVIEW_COUNT / REVIEW_RATING : numbers read from the live Google profile
# While any of these is None the site simply doesn't show that element —
# nothing is guessed.
GOOGLE_REVIEWS_URL = None
REVIEW_COUNT = None      # e.g. 27
REVIEW_RATING = None     # e.g. "5.0"

# Where the consultation form POSTs (Formspree, Web3Forms, Netlify, own API...).
# Empty = preview mode: the form validates but shows "not connected" and sends nothing.
FORM_ENDPOINT = ""

# The three blog posts are still placeholders ("Placeholder post — replace with real content").
# Keep the Blog out of the nav/footer until real articles exist, then set this to True.
SHOW_BLOG = False

# Primary services first, maintenance deliberately last (secondary service).
SERVICES = [
    ("outdoor-living-patios", "Outdoor Living & Patios", "Vida al Aire Libre y Patios"),
    ("landscape-design", "Landscape Design", "Diseño de Paisaje"),
    ("landscape-construction", "Landscape Construction", "Construcción de Paisaje"),
    ("pavers-retaining-walls", "Pavers & Retaining Walls", "Adoquines y Muros de Contención"),
    ("planting-irrigation", "Planting & Irrigation", "Plantación y Riego"),
    ("landscape-maintenance", "Landscape Maintenance", "Mantenimiento de Paisaje"),
]

CTA_EN, CTA_ES = "Schedule a Consultation", "Programar una Consulta"


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def bi(pair):
    """(en, es) -> 'data-en=".." data-es="..">EN text' — close the tag yourself with </tag>."""
    en, es = pair
    return f'data-en="{attr(en)}" data-es="{attr(es)}">{esc(en)}'


def tx(en, es, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    e = f" {extra}" if extra else ""
    return f'<{tag}{c}{e} {bi((en, es))}</{tag}>'


def strip_comments(page):
    """Remove HTML comments from the shipped page (also keeps developer notes
    — e.g. the spam-trap explanation — out of anything that renders page text)."""
    return re.sub(r"<!--.*?-->\s*", "", page, flags=re.S)


# ---------------------------------------------------------------- head
def render_head(title, description, depth="", og_image="images/luna-sons-pergola-01.jpg"):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE_URL}/{og_image}">
<meta name="theme-color" content="#4B1D63">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.css">
<link rel="stylesheet" href="{depth}style.css">"""


# ---------------------------------------------------------------- header
def render_header(active, depth="", home=False):
    """active: 'home' | 'work' | 'about' | 'blog' | 'contact' | 'services:<slug>' | None"""
    is_service = bool(active) and active.startswith("services:")
    active_slug = active.split(":", 1)[1] if is_service else None

    def cls(key):
        return ' class="active" aria-current="page"' if active == key else ""

    drop = []
    for slug, en, es in SERVICES:
        a = ' class="active" aria-current="page"' if slug == active_slug else ""
        drop.append(f'            <li><a href="{depth}services/{slug}/index.html"{a} {bi((en, es))}</a></li>')
    drop_html = "\n".join(drop)
    cta_href = "#consultation" if home else f"{depth}contact/index.html"
    home_href = "#top" if home else f"{depth}index.html"
    about_href = "#about" if home else f"{depth}index.html#about"
    svc_href = "#services" if home else f"{depth}index.html#services"
    svc_cls = ' class="active" aria-current="page"' if is_service else ""
    blog_li = f'<li><a href="{depth}blog/index.html"{cls("blog")} {bi(("Blog", "Blog"))}</a></li>' if SHOW_BLOG else ""

    return f"""<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="{home_href}" class="logo" aria-label="Luna &amp; Sons Landscaping home">
      <img class="logo-mark" src="{depth}images/logo-moon.png" width="54" height="54" alt="Luna &amp; Sons moon logo">
      <span class="logo-text">
        <span class="logo-name">Luna &amp; Sons</span>
        {tx("Landscaping", "Paisajismo", cls="logo-sub")}
      </span>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Primary">
      <ul>
        <li><a href="{home_href}"{cls("home")} {bi(("Home", "Inicio"))}</a></li>
        <li class="has-dropdown">
          <div class="nav-link-wrap">
            <a href="{svc_href}"{svc_cls} {bi(("Services", "Servicios"))}</a>
            <button class="dropdown-toggle" type="button" aria-expanded="false" aria-controls="services-dropdown" aria-label="Toggle services menu">
              <i data-lucide="chevron-down" aria-hidden="true"></i>
            </button>
          </div>
          <ul class="dropdown-menu" id="services-dropdown">
{drop_html}
          </ul>
        </li>
        <li><a href="{depth}work/index.html"{cls("work")} {bi(("Our Work", "Nuestro Trabajo"))}</a></li>
        <li><a href="{about_href}"{cls("about")} {bi(("About", "Nosotros"))}</a></li>
        {blog_li}
        <li><a href="{depth}contact/index.html"{cls("contact")} {bi(("Contact", "Contacto"))}</a></li>
        <li class="nav-cta-item"><a class="btn btn-primary nav-cta" href="{cta_href}"><span {bi((CTA_EN, CTA_ES))}</span></a></li>
      </ul>
    </nav>

    <div class="header-actions">
      <a class="header-phone" href="{PHONE_HREF}" aria-label="Call {PHONE_DISPLAY}">
        <i data-lucide="phone" aria-hidden="true"></i>
        <span class="header-phone-number">{PHONE_DISPLAY}</span>
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


# ---------------------------------------------------------------- closing CTA band
def render_closing_cta(depth="", home=False):
    href = "#consultation" if home else f"{depth}contact/index.html"
    return f"""  <section class="closing-cta">
    <div class="container closing-cta-inner" data-aos="fade-up">
      <h2 {bi(("Exceptional Outdoor Living. Built Around You.", "Vida al Aire Libre Excepcional. Hecha a Su Medida."))}</h2>
      <p {bi(("Family-owned landscape design and construction serving Santa Maria and California's Central Coast.", "Diseño y construcción de paisajes de una empresa familiar, al servicio de Santa Maria y la Costa Central de California."))}</p>
      <a class="btn btn-primary btn-lg" href="{href}"><span {bi((CTA_EN, CTA_ES))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a>
    </div>
  </section>"""


# ---------------------------------------------------------------- consultation form
PROJECT_TYPES = [
    ("outdoor-living-patio", "Outdoor Living & Patio", "Vida al Aire Libre y Patio"),
    ("pavers-retaining-walls", "Pavers & Retaining Walls", "Adoquines y Muros de Contención"),
    ("complete-transformation", "Complete Landscape Transformation", "Transformación Completa del Paisaje"),
    ("landscape-design", "Landscape Design", "Diseño de Paisaje"),
    ("planting-irrigation", "Planting & Irrigation", "Plantación y Riego"),
    ("landscape-maintenance", "Landscape Maintenance", "Mantenimiento de Paisaje"),
    ("other", "Other / Not sure yet", "Otro / Aún no lo sé"),
]
INVESTMENTS = [
    ("under-10k", "Under $10,000", "Menos de $10,000"),
    ("10k-25k", "$10,000 – $25,000", "$10,000 – $25,000"),
    ("25k-50k", "$25,000 – $50,000", "$25,000 – $50,000"),
    ("50k-100k", "$50,000 – $100,000", "$50,000 – $100,000"),
    ("100k-plus", "$100,000+", "Más de $100,000"),
    ("not-sure", "Not sure yet", "Aún no lo sé"),
]
TIMELINES = [
    ("asap", "As soon as possible", "Lo antes posible"),
    ("1-3-months", "Within 1–3 months", "En 1–3 meses"),
    ("3-6-months", "In 3–6 months", "En 3–6 meses"),
    ("6-plus-months", "6+ months / planning ahead", "Más de 6 meses / planificando"),
    ("exploring", "Just exploring ideas", "Solo explorando ideas"),
]


def _options(items, placeholder):
    out = [f'<option value="" {bi(placeholder)}</option>']
    out += [f'<option value="{v}" {bi((en, es))}</option>' for v, en, es in items]
    return "\n              ".join(out)


def render_consultation_form(pid="c"):
    """pid prefixes element ids so two forms can exist on one page."""
    return f"""<form class="consult-form" id="{pid}-form" data-endpoint="{attr(FORM_ENDPOINT)}">
          <div class="hp-wrap" aria-hidden="true">
            <input type="text" name="website_url" id="{pid}-hp" class="trap-answer" tabindex="-1" autocomplete="off">
          </div>
          <input type="hidden" name="page_language" class="form-lang" value="en">
          <input type="hidden" name="_subject" value="New consultation request — Luna &amp; Sons website">

          <div class="field">
            <label for="{pid}-name" {bi(("Full Name", "Nombre Completo"))}</label>
            <input type="text" id="{pid}-name" name="name" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="{pid}-phone" {bi(("Phone", "Teléfono"))}</label>
            <input type="tel" id="{pid}-phone" name="phone" autocomplete="tel" inputmode="tel" required>
          </div>
          <div class="field">
            <label for="{pid}-email" {bi(("Email", "Correo Electrónico"))}</label>
            <input type="email" id="{pid}-email" name="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="{pid}-address" {bi(("Project Address", "Dirección del Proyecto"))}</label>
            <input type="text" id="{pid}-address" name="address" autocomplete="street-address" required>
          </div>
          <div class="field">
            <label for="{pid}-type" {bi(("Project Type", "Tipo de Proyecto"))}</label>
            <select id="{pid}-type" name="project_type" required>
              {_options(PROJECT_TYPES, ("Select a service", "Seleccione un servicio"))}
            </select>
          </div>
          <div class="field">
            <label for="{pid}-invest" {bi(("Anticipated Investment", "Inversión Estimada"))}</label>
            <select id="{pid}-invest" name="anticipated_investment">
              {_options(INVESTMENTS, ("Select a range", "Seleccione un rango"))}
            </select>
          </div>
          <div class="field field--wide">
            <label for="{pid}-timeline" {bi(("Preferred Timeline", "Plazo Preferido"))}</label>
            <select id="{pid}-timeline" name="preferred_timeline">
              {_options(TIMELINES, ("Select a timeframe", "Seleccione un plazo"))}
            </select>
          </div>
          <div class="field field--wide">
            <label for="{pid}-details" {bi(("Tell Us About Your Project", "Cuéntenos Sobre Su Proyecto"))}</label>
            <textarea id="{pid}-details" name="project_details" rows="4"></textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-block consult-submit">
            <span {bi(("Request a Consultation", "Solicitar una Consulta"))}</span>
            <i data-lucide="arrow-right" aria-hidden="true"></i>
          </button>
          <p class="form-status" role="status" aria-live="polite" hidden></p>
          <p class="form-note" {bi(("Project pricing is based on scope, materials and site conditions.", "El precio de cada proyecto depende del alcance, los materiales y las condiciones del sitio."))}</p>
        </form>"""


# ---------------------------------------------------------------- footer
def render_footer(depth=""):
    svc = "\n".join(
        f'          <li><a href="{depth}services/{s}/index.html" {bi((en, es))}</a></li>'
        for s, en, es in SERVICES
    )
    footer_blog = f'<li><a href="{depth}blog/index.html" {bi(("Blog", "Blog"))}</a></li>' if SHOW_BLOG else ""
    review_btn = ""
    if GOOGLE_REVIEWS_URL:
        review_btn = f"""
      <a class="sf-review" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">
        <i data-lucide="star" aria-hidden="true"></i><span {bi(("Read our Google reviews", "Lea nuestras reseñas en Google"))}</span>
      </a>"""
    return f"""<footer class="sf">
  <div class="container sf-grid">
    <div class="sf-brand">
      <a href="{depth}index.html" class="sf-logo" aria-label="Luna &amp; Sons Landscaping home">
        <img src="{depth}images/logo-moon.png" width="64" height="64" alt="Luna &amp; Sons moon logo" loading="lazy">
        <span class="sf-wordmark"><span class="sf-name">Luna &amp; Sons</span>{tx("Landscaping", "Paisajismo", cls="sf-sub")}</span>
      </a>
      <p class="sf-tagline" {bi(("Family-owned landscape design and construction serving Santa Maria and California's Central Coast.", "Diseño y construcción de paisajes de una empresa familiar, al servicio de Santa Maria y la Costa Central de California."))}</p>
      <div class="sf-social">
        <a href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Luna &amp; Sons on Facebook"><i data-lucide="facebook" aria-hidden="true"></i></a>
        <a href="{INSTAGRAM_URL}" target="_blank" rel="noopener" aria-label="Luna &amp; Sons on Instagram"><i data-lucide="instagram" aria-hidden="true"></i></a>
      </div>{review_btn}
    </div>

    <div class="sf-col">
      <h4 {bi(("Explore", "Explorar"))}</h4>
      <ul>
        <li><a href="{depth}index.html" {bi(("Home", "Inicio"))}</a></li>
        <li><a href="{depth}work/index.html" {bi(("Our Work", "Nuestro Trabajo"))}</a></li>
        <li><a href="{depth}index.html#about" {bi(("About Us", "Sobre Nosotros"))}</a></li>
        {footer_blog}
        <li><a href="{depth}contact/index.html" {bi(("Contact", "Contacto"))}</a></li>
      </ul>
    </div>

    <div class="sf-col">
      <h4 {bi(("Services", "Servicios"))}</h4>
      <ul>
{svc}
      </ul>
    </div>

    <div class="sf-col">
      <h4 {bi(("Contact", "Contacto"))}</h4>
      <ul class="sf-contact">
        <li><i data-lucide="phone" aria-hidden="true"></i><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
        <li><i data-lucide="mail" aria-hidden="true"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><i data-lucide="map-pin" aria-hidden="true"></i><span>Santa Maria, CA</span></li>
      </ul>
    </div>
  </div>

  <div class="sf-bottom">
    <div class="container sf-bottom-inner">
      <p>&copy; <span id="year"></span> <span {bi(("Luna & Sons Landscaping. All rights reserved.", "Luna & Sons Landscaping. Todos los derechos reservados."))}</span> &middot; <span {bi(("Licensed & Insured · CA LIC #" + LICENSE, "Con Licencia y Seguro · Lic. CA #" + LICENSE))}</span></p>
      <button class="lang-toggle" type="button" aria-label="Switch language / Cambiar idioma">
        <span class="lang-en-flag" data-active="true">EN</span>/<span class="lang-es-flag">ES</span>
      </button>
    </div>
  </div>
</footer>"""


def render_scripts(depth=""):
    return f"""<script src="https://unpkg.com/lucide@0.462.0/dist/umd/lucide.js"></script>
<script src="https://cdn.jsdelivr.net/npm/aos@2.3.4/dist/aos.js"></script>
<script src="{depth}script.js"></script>"""


def write_page(rel_path, page):
    out = os.path.join(SITE_ROOT, rel_path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(strip_comments(page))
    print("wrote", rel_path)
