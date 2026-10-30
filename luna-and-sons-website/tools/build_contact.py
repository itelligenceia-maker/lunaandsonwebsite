#!/usr/bin/env python3
"""Generates contact/index.html. Run from the site root."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import *  # noqa: F401,F403


def page():
    title = "Schedule a Consultation | Luna &amp; Sons Landscaping"
    desc = "Schedule a consultation with Luna &amp; Sons Landscaping in Santa Maria, CA. Tell us about your property, priorities and the outdoor space you envision."
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{render_head(title, desc, depth="../", og_image="images/luna-sons-flagstone-patio-01.jpg")}
</head>
<body>
{render_header("contact", depth="../")}
<main>
  <section class="page-banner" style="background-image:url('../images/hero-slide-1.jpg')">
    <div class="page-banner-scrim"></div>
    <div class="container page-banner-inner">
      <p class="eyebrow eyebrow-light" {bi(("Contact", "Contacto"))}</p>
      <h1 {bi(("Your Outdoor Living Starts Here.", "Su Vida al Aire Libre Comienza Aquí."))}</h1>
      <p {bi(("Tell us about your property, priorities and the space you envision.", "Cuéntenos sobre su propiedad, sus prioridades y el espacio que imagina."))}</p>
    </div>
  </section>

  <section class="consult consult-page" id="consultation">
    <div class="container consult-grid">
      <div class="consult-card" data-aos="fade-up">
        {render_consultation_form("p")}
      </div>
      <aside class="consult-side" data-aos="fade-up" data-aos-delay="100">
        <img class="consult-photo" src="../images/luna-sons-flagstone-patio-01.jpg" width="1600" height="1292" alt="Flagstone patio with a natural stone accent feature in a completed Luna &amp; Sons backyard" data-alt-en="Flagstone patio with a natural stone accent feature in a completed Luna &amp; Sons backyard" data-alt-es="Patio de piedra laja con un elemento decorativo de piedra natural en un patio terminado por Luna &amp; Sons" loading="lazy">
        <ul class="consult-contact">
          <li><i data-lucide="phone" aria-hidden="true"></i><a href="{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
          <li><i data-lucide="mail" aria-hidden="true"></i><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><i data-lucide="map-pin" aria-hidden="true"></i><span {bi(("Santa Maria, CA — serving a 50-mile radius", "Santa Maria, CA — atendemos en un radio de 50 millas"))}</span></li>
          <li><i data-lucide="shield-check" aria-hidden="true"></i><span {bi(("Licensed & Insured · CA LIC #" + LICENSE, "Con Licencia y Seguro · Lic. CA #" + LICENSE))}</span></li>
        </ul>
        <div class="map-wrap">
          <iframe src="https://www.google.com/maps?q=Santa+Maria,+CA&amp;output=embed" width="100%" height="240" style="border:0;" allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Map of Santa Maria, CA service area"></iframe>
        </div>
      </aside>
    </div>
  </section>
</main>
{render_footer(depth="../")}
{render_scripts("../")}
</body>
</html>
"""


if __name__ == "__main__":
    write_page("contact/index.html", page())
