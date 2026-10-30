#!/usr/bin/env python3
"""Generates index.html (homepage). Run from the site root: python3 tools/build_home.py"""
import json
import os
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import *  # noqa: F401,F403
import shell
from work_data import WORK, FEATURED

W = {w[0]: w for w in WORK}


def img(fn, cls="", sizes="", loading="lazy"):
    f, w, h, _c, aen, aes = W[fn if fn in W else "images/" + fn]
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{quote(f)}" width="{w}" height="{h}" alt="{attr(aen)}" '
            f'data-alt-en="{attr(aen)}" data-alt-es="{attr(aes)}" loading="{loading}" decoding="async">')


def svc(slug):
    return next(s for s in SERVICES if s[0] == slug)


# ------------------------------------------------------------------ sections
def hero():
    return f"""<section class="hero hero-v2">
    <div class="hero-media" role="img" aria-label="Photos of completed Luna &amp; Sons landscaping projects">
      <div class="hero-slide is-active" style="background-image:url('images/hero-slide-1.jpg')"></div>
      <div class="hero-slide" style="background-image:url('images/hero-slide-5.jpg')"></div>
      <div class="hero-slide" style="background-image:url('images/hero-slide-7.jpg')"></div>
      <div class="hero-slide" style="background-image:url('images/hero-slide-8.jpg')"></div>
    </div>
    <div class="hero-scrim"></div>
    <div class="container hero-content hero-content-v2">
      <p class="hero-eyebrow"><span {bi(("Central Coast", "Costa Central"))}</span><i class="dot" aria-hidden="true"></i><span {bi(("Landscape Design + Construction", "Diseño + Construcción de Paisaje"))}</span></p>
      <h1 {bi(("Exceptional Outdoor Living. Built Around You.", "Vida al Aire Libre Excepcional. Hecha a Su Medida."))}</h1>
      <p class="hero-sub" {bi(("Thoughtful design, quality materials and expert craftsmanship. Outdoor spaces created for gathering, relaxing and enjoying life at home.", "Diseño cuidadoso, materiales de calidad y mano de obra experta. Espacios exteriores creados para reunirse, relajarse y disfrutar la vida en casa."))}</p>
      <div class="hero-cta-row">
        <a href="#consultation" class="btn btn-primary btn-lg"><span {bi((CTA_EN, CTA_ES))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a>
        <a href="work/index.html" class="btn btn-outline-light btn-lg"><span {bi(("Explore Our Work", "Conozca Nuestro Trabajo"))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a>
      </div>
      <a class="hero-phone" href="{PHONE_HREF}"><i data-lucide="phone" aria-hidden="true"></i><span>{PHONE_DISPLAY}</span></a>
      <p class="hero-trust"><strong {bi(("Family-Owned & Operated", "Empresa Familiar"))}</strong><span {bi(("Licensed & Insured · CA LIC #" + LICENSE, "Con Licencia y Seguro · Lic. CA #" + LICENSE))}</span></p>
    </div>
  </section>"""


def intro():
    rows = [
        ("outdoor-living-patios", "sofa"),
        ("pavers-retaining-walls", "brick-wall"),
        ("planting-irrigation", "sprout"),
    ]
    row_html = "\n".join(
        f"""          <li><a class="intro-row" href="services/{s}/index.html"><span class="intro-row-icon"><i data-lucide="{ic}" aria-hidden="true"></i></span><span class="intro-row-label" {bi((svc(s)[1], svc(s)[2]))}</span><i data-lucide="chevron-right" class="intro-row-arrow" aria-hidden="true"></i></a></li>"""
        for s, ic in rows)
    return f"""<section class="intro" id="intro">
    <div class="container intro-grid">
      <div class="intro-copy" data-aos="fade-up">
        <p class="eyebrow" {bi(("Designed for the way you live", "Diseñado para su forma de vivir"))}</p>
        <h2 {bi(("Outdoor Living, Thoughtfully Crafted.", "Espacios Exteriores, Cuidadosamente Elaborados."))}</h2>
        <p class="lead" {bi(("A welcoming place to entertain. A quiet space to unwind. A landscape that brings your home together.", "Un lugar acogedor para recibir invitados. Un espacio tranquilo para descansar. Un paisaje que une su hogar."))}</p>
        <p {bi(("Luna & Sons Landscaping combines thoughtful design with careful construction to create outdoor spaces tailored to your property and lifestyle. From custom patios to complete landscape transformations, we bring attention to every detail.", "Luna & Sons Landscaping combina un diseño cuidadoso con una construcción esmerada para crear espacios exteriores adaptados a su propiedad y estilo de vida. Desde patios a la medida hasta transformaciones completas del paisaje, cuidamos cada detalle."))}</p>
        <ul class="intro-rows">
{row_html}
        </ul>
        <a href="work/index.html" class="btn btn-primary"><span {bi(("Explore Our Work", "Conozca Nuestro Trabajo"))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a>
      </div>
      <div class="intro-media" data-aos="fade-up" data-aos-delay="100">
        {img("luna-sons-paver-patio-02.jpg", "intro-img")}
      </div>
    </div>
  </section>"""


def services():
    cards = [
        ("outdoor-living-patios", "luna-sons-pergola-01.jpg",
         ("Patios, pergolas and gathering spaces designed around how you entertain and unwind.",
          "Patios, pérgolas y espacios para reunirse, diseñados según cómo usted recibe y descansa.")),
        ("landscape-design", "luna-sons-planting-bed-03.jpg",
         ("Custom plans that bring planting, hardscape, lighting and irrigation together.",
          "Planes a la medida que integran plantación, hardscape, iluminación y riego.")),
        ("landscape-construction", "luna-sons-retaining-wall-01.jpg",
         ("Careful installation of complete landscapes, from first excavation to final walkthrough.",
          "Instalación esmerada de paisajes completos, desde la excavación inicial hasta la revisión final.")),
        ("pavers-retaining-walls", "luna-sons-retaining-wall-03.jpg",
         ("Pavers, walkways and retaining walls built for lasting strength and clean lines.",
          "Adoquines, senderos y muros de contención construidos para durar, con líneas limpias.")),
        ("planting-irrigation", "luna-sons-planting-bed-01.jpg",
         ("Water-wise planting and efficient irrigation suited to the Central Coast.",
          "Plantación eficiente en agua y riego adecuado para la Costa Central.")),
    ]
    out = []
    for i, (s, fn, desc) in enumerate(cards):
        _, en, es = svc(s)
        out.append(f"""        <a class="svc-card" href="services/{s}/index.html" data-aos="fade-up" data-aos-delay="{(i % 3) * 80}">
          <span class="svc-card-media">{img(fn)}</span>
          <span class="svc-card-body">
            <h3 {bi((en, es))}</h3>
            <p {bi(desc)}</p>
            <span class="svc-card-link"><span {bi(("Learn more", "Más información"))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></span>
          </span>
        </a>""")
    cards_html = "\n".join(out)
    _, men, mes = svc("landscape-maintenance")
    return f"""<section class="services-v2" id="services">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <p class="eyebrow" {bi(("What We Do", "Lo Que Hacemos"))}</p>
        <h2 {bi(("Complete landscapes, designed and built with care.", "Paisajes completos, diseñados y construidos con esmero."))}</h2>
      </div>
      <div class="svc-grid">
{cards_html}
      </div>
      <a class="maint-strip" href="services/landscape-maintenance/index.html" data-aos="fade-up">
        <i data-lucide="leaf" aria-hidden="true"></i>
        <span class="maint-copy"><strong {bi((men, mes))}</strong><span {bi(("Ongoing care to keep your landscape looking its best, year-round.", "Cuidado continuo para que su paisaje luzca lo mejor posible durante todo el año."))}</span></span>
        <i data-lucide="arrow-right" aria-hidden="true"></i>
      </a>
    </div>
  </section>"""


def work_teaser():
    tiles = []
    for i, fn in enumerate(FEATURED):
        tiles.append(f'        <a class="wt wt-{i + 1}" href="work/index.html" aria-label="View all projects">{img(fn, sizes="")}</a>')
    return f"""<section class="work-teaser" id="work">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <p class="eyebrow" {bi(("Our Work", "Nuestro Trabajo"))}</p>
        <h2 {bi(("Recent projects.", "Proyectos recientes."))}</h2>
        <p {bi(("A look at recent patios, walls and landscapes built by our crew.", "Un vistazo a patios, muros y paisajes recientes construidos por nuestro equipo."))}</p>
      </div>
      <div class="wt-grid" data-aos="fade-up">
{chr(10).join(tiles)}
      </div>
      <div class="center-row"><a href="work/index.html" class="btn btn-primary"><span {bi(("View All Projects", "Ver Todos los Proyectos"))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a></div>
    </div>
  </section>"""


def process():
    # Illustrations from luna photos/ (consulting / design / build and transform).
    # They are renderings, not project photos, so the alt text says so.
    steps = [
        ("luna%20photos/consulting%20.png", ("Consultation", "Consulta"),
         ("We walk your property with you, talk through your goals, and put together honest recommendations.",
          "Recorremos su propiedad con usted, hablamos sobre sus objetivos y preparamos recomendaciones honestas."),
         ("Illustration of a Luna & Sons team member discussing a project with a homeowner on site",
          "Ilustración de un integrante de Luna & Sons conversando sobre un proyecto con un propietario en el sitio")),
        ("luna%20photos/design%20.png", ("Design & Planning", "Diseño y Planificación"),
         ("We turn that conversation into a clear plan and quote, so you know exactly what you're getting before work starts.",
          "Convertimos esa conversación en un plan y cotización claros, para que sepa exactamente qué recibirá antes de comenzar."),
         ("Illustration of a landscape plan drawing with a lawn, patio and planting beds",
          "Ilustración de un plano de paisaje con césped, patio y jardineras")),
        ("luna%20photos/build%20and%20transform%20.png", ("Build & Transform", "Construcción y Transformación"),
         ("Our crew executes the plan on schedule, cleans up after itself, and walks you through the finished result.",
          "Nuestro equipo ejecuta el plan a tiempo, limpia después de trabajar y le muestra el resultado final."),
         ("Illustration of a landscape plan with material samples on a work table",
          "Ilustración de un plano de paisaje con muestras de materiales sobre una mesa de trabajo")),
    ]
    cards = []
    for i, (src, title, body, alt) in enumerate(steps):
        cards.append(f"""        <div class="process-step" data-aos="fade-up" data-aos-delay="{i * 100}">
          <div class="process-photo"><img src="{src}" alt="{attr(alt[0])}" data-alt-en="{attr(alt[0])}" data-alt-es="{attr(alt[1])}" loading="lazy" decoding="async"></div>
          <p class="step-num">0{i + 1}</p>
          <h3 {bi(title)}</h3>
          <p {bi(body)}</p>
        </div>""")
    return f"""<section class="process process-v2">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <p class="eyebrow" {bi(("Our Process", "Nuestro Proceso"))}</p>
        <h2 {bi(("From first conversation to final walkthrough.", "Desde la primera conversación hasta la revisión final."))}</h2>
      </div>
      <div class="process-grid">
{chr(10).join(cards)}
      </div>
    </div>
  </section>"""


REVIEWS = [
    ("Anelieze C.",
     "From quote to project completion, Luna & Sons Landscaping gets 5 stars. Great communication with Brian — he answered all questions promptly.",
     "Desde la cotización hasta la finalización del proyecto, Luna & Sons Landscaping merece 5 estrellas. Excelente comunicación con Brian — respondió todas nuestras preguntas rápidamente."),
    ("Ambrose J.",
     "Brian Luna and his father Jose did a terrific job on our sprinkler system. They repaired three broken lines and several holes in the drip tubing system.",
     "Brian Luna y su padre Jose hicieron un trabajo excelente en nuestro sistema de riego. Repararon tres líneas rotas y varios agujeros en el sistema de goteo."),
    ("Emily M.",
     "We are so thankful for the amazing work Luna and Sons did on our backyard! They were professional, hardworking, efficient, and incredibly kind.",
     "¡Estamos muy agradecidos por el increíble trabajo que Luna and Sons hizo en nuestro patio trasero! Fueron profesionales, trabajadores, eficientes e increíblemente amables."),
    ("Molly D.",
     "We hired Luna and Son for a garden refresh after 2.5 years of growth and we had a great experience from start to finish! Professional, quick, efficient and for a great price!",
     "Contratamos a Luna and Son para renovar nuestro jardín después de 2.5 años de crecimiento y tuvimos una excelente experiencia de principio a fin. ¡Profesionales, rápidos, eficientes y a muy buen precio!"),
]


def reviews():
    stars = '<span class="stars" role="img" aria-label="5 out of 5 stars">' + '<i data-lucide="star" aria-hidden="true"></i>' * 5 + "</span>"
    cards = []
    for i, (name, en, es) in enumerate(REVIEWS):
        cards.append(f"""        <figure class="review" data-aos="fade-up" data-aos-delay="{(i % 2) * 80}">
          {stars}
          <blockquote {bi((en, es))}</blockquote>
          <figcaption><span class="review-name">{esc(name)}</span><span class="review-src" {bi(("Google Review", "Reseña de Google"))}</span></figcaption>
        </figure>""")
    badge = ""
    if REVIEW_COUNT and REVIEW_RATING:
        badge = (f'<p class="review-badge"><strong>{esc(str(REVIEW_RATING))}</strong>{stars}'
                 f'<span><span {bi((f"{REVIEW_COUNT} Google reviews", f"{REVIEW_COUNT} reseñas en Google"))}</span></span></p>')
    link = ""
    if GOOGLE_REVIEWS_URL:
        link = (f'<div class="center-row"><a class="btn btn-outline" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">'
                f'<span {bi(("Read All Reviews on Google", "Lea Todas las Reseñas en Google"))}</span><i data-lucide="external-link" aria-hidden="true"></i></a></div>')
    return f"""<section class="reviews" id="reviews">
    <div class="container">
      <div class="section-head" data-aos="fade-up">
        <p class="eyebrow" {bi(("Client Reviews", "Reseñas de Clientes"))}</p>
        <h2 {bi(("What homeowners say.", "Lo que dicen nuestros clientes."))}</h2>
        {badge}
      </div>
      <div class="review-grid">
{chr(10).join(cards)}
      </div>
      {link}
    </div>
  </section>"""


def about():
    return f"""<section class="about-v2" id="about">
    <div class="container about-v2-inner" data-aos="fade-up">
      <p class="eyebrow" {bi(("About Luna & Sons", "Sobre Luna & Sons"))}</p>
      <h2 {bi(("Our Family Name. Our Commitment.", "Nuestro Apellido. Nuestro Compromiso."))}</h2>
      <p {bi(("As a family-owned landscape design and construction company, we take personal pride in the spaces we create and the relationships we build.", "Como empresa familiar de diseño y construcción de paisajes, nos enorgullecemos personalmente de los espacios que creamos y de las relaciones que construimos."))}</p>
      <p {bi(("Our approach combines thoughtful planning, quality materials and careful workmanship to create outdoor living spaces that are beautiful, functional and suited to California's Central Coast.", "Nuestro enfoque combina una planificación cuidadosa, materiales de calidad y mano de obra esmerada para crear espacios de vida al aire libre hermosos, funcionales y adecuados para la Costa Central de California."))}</p>
      <p {bi(("From the first conversation to the final walkthrough, we focus on clear communication, attention to detail and bringing your vision to life.", "Desde la primera conversación hasta la revisión final, nos enfocamos en una comunicación clara, la atención al detalle y en hacer realidad su visión."))}</p>
      <ul class="pillars">
        <li><span class="pillar-icon"><i data-lucide="sprout" aria-hidden="true"></i></span><span {bi(("Thoughtful Design", "Diseño Cuidadoso"))}</span></li>
        <li><span class="pillar-icon"><i data-lucide="brick-wall" aria-hidden="true"></i></span><span {bi(("Lasting Craftsmanship", "Mano de Obra Duradera"))}</span></li>
        <li><span class="pillar-icon"><i data-lucide="users" aria-hidden="true"></i></span><span {bi(("Personal Attention", "Atención Personal"))}</span></li>
      </ul>
      <p class="about-license"><i data-lucide="shield-check" aria-hidden="true"></i><span {bi(("Licensed & Insured · CA LIC #" + LICENSE, "Con Licencia y Seguro · Lic. CA #" + LICENSE))}</span></p>
      <a href="#consultation" class="btn btn-primary btn-lg"><span {bi((CTA_EN, CTA_ES))}</span><i data-lucide="arrow-right" aria-hidden="true"></i></a>
    </div>
  </section>"""


def faq():
    items = [
        (("Are you licensed and insured?", "¿Están licenciados y asegurados?"),
         (f"Yes — Luna & Sons Landscaping is fully licensed (License #{LICENSE}) and insured for every job we take on, big or small.",
          f"Sí — Luna & Sons Landscaping está completamente licenciado (Licencia #{LICENSE}) y asegurado para cada trabajo que realizamos, grande o pequeño.")),
        (("How does the consultation work?", "¿Cómo funciona la consulta?"),
         ("We start with a conversation about your property, goals and timeline, then walk the site with you. From there we put together a clear plan and quote, so you know what to expect before work begins.",
          "Comenzamos con una conversación sobre su propiedad, sus metas y su calendario, y luego recorremos el sitio con usted. De ahí preparamos un plan y una cotización claros, para que sepa qué esperar antes de comenzar.")),
        (("How are projects priced?", "¿Cómo se determina el precio de un proyecto?"),
         ("Every project is priced on its scope, the materials selected and the conditions of your site. After the consultation you receive a clear written quote.",
          "El precio de cada proyecto depende de su alcance, los materiales elegidos y las condiciones de su sitio. Después de la consulta recibe una cotización escrita y clara.")),
        (("Do you offer a warranty on your work?", "¿Ofrecen garantía en su trabajo?"),
         ("Yes. Workmanship is guaranteed on every project, and we'll walk you through the specific plant and material warranties during your consultation.",
          "Sí. La mano de obra está garantizada en cada proyecto, y le explicaremos las garantías específicas de plantas y materiales durante su consulta.")),
        (("What areas do you serve?", "¿Qué áreas atienden?"),
         ("We're based in Santa Maria and serve within a 50-mile radius across the greater Central Coast, including Orcutt, Nipomo, Lompoc, and Arroyo Grande.",
          "Estamos ubicados en Santa Maria y atendemos dentro de un radio de 50 millas por toda la Costa Central, incluyendo Orcutt, Nipomo, Lompoc y Arroyo Grande.")),
        (("Is Luna & Sons family-owned?", "¿Luna & Sons es una empresa familiar?"),
         ("Yes. Luna & Sons is a family-owned company proudly serving the Central Coast.",
          "Sí. Luna & Sons es una empresa familiar que sirve con orgullo a la Costa Central.")),
    ]
    out = []
    for q, a in items:
        out.append(f"""        <div class="faq-item">
          <button class="faq-question" aria-expanded="false"><span {bi(q)}</span><i data-lucide="chevron-down" aria-hidden="true"></i></button>
          <div class="faq-answer"><p {bi(a)}</p></div>
        </div>""")
    return f"""<section class="faq">
    <div class="container faq-layout">
      <div class="faq-head" data-aos="fade-up">
        <p class="eyebrow" {bi(("FAQ", "Preguntas Frecuentes"))}</p>
        <h2 {bi(("Common questions.", "Preguntas comunes."))}</h2>
      </div>
      <div class="faq-list" data-aos="fade-up" data-aos-delay="100">
{chr(10).join(out)}
      </div>
    </div>
  </section>"""


def consultation():
    return f"""<section class="consult" id="consultation">
    <div class="container consult-grid">
      <div class="consult-intro" data-aos="fade-up">
        <p class="eyebrow" {bi(("Schedule a Consultation", "Programe una Consulta"))}</p>
        <h2 {bi(("Your Outdoor Living Starts Here.", "Su Vida al Aire Libre Comienza Aquí."))}</h2>
        <p {bi(("Tell us about your property, priorities and the space you envision.", "Cuéntenos sobre su propiedad, sus prioridades y el espacio que imagina."))}</p>
        <ul class="consult-contact">
          <li><i data-lucide="phone" aria-hidden="true"></i><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
          <li><i data-lucide="mail" aria-hidden="true"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><i data-lucide="map-pin" aria-hidden="true"></i><span {bi(("Santa Maria, CA — serving a 50-mile radius", "Santa Maria, CA — atendemos en un radio de 50 millas"))}</span></li>
        </ul>
      </div>
      <div class="consult-card" data-aos="fade-up" data-aos-delay="100">
        {render_consultation_form("h")}
      </div>
    </div>
  </section>"""


def schema():
    data = {
        "@context": "https://schema.org",
        "@type": "LandscapingBusiness",
        "name": "Luna & Sons Landscaping",
        "url": SITE_URL,
        "telephone": "+1-805-268-2808",
        "email": EMAIL,
        "image": f"{SITE_URL}/images/luna-sons-pergola-01.jpg",
        "address": {"@type": "PostalAddress", "addressLocality": "Santa Maria", "addressRegion": "CA", "addressCountry": "US"},
        "areaServed": ["Santa Maria", "Orcutt", "Nipomo", "Lompoc", "Arroyo Grande"],
        "sameAs": [FACEBOOK_URL, INSTAGRAM_URL],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def page():
    title = "Luna &amp; Sons Landscaping | Outdoor Living &amp; Landscape Design in Santa Maria, CA"
    desc = ("Family-owned landscape design and construction in Santa Maria and California's Central Coast — "
            "patios, pavers, retaining walls and complete landscape transformations. Licensed &amp; insured. Schedule a consultation.")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(title, desc)}
{schema()}
</head>
<body>
{render_header("home", home=True)}
<main>
  {hero()}
  {intro()}
  {services()}
  {work_teaser()}
  {process()}
  {reviews()}
  {about()}
  {faq()}
  {consultation()}
</main>
{render_footer()}
{render_scripts()}
</body>
</html>
"""


if __name__ == "__main__":
    write_page("index.html", page())
