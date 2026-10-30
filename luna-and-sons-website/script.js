// =========================================================
// LUNA & SONS LANDSCAPING — SITE SCRIPT
// =========================================================

document.addEventListener('DOMContentLoaded', () => {
  initIcons();
  initAOS();
  initHeaderScroll();
  initMobileNav();
  initServicesDropdown();
  initLangToggle();
  initFAQ();
  initForms();
  initHeroSlideshow();
  const yr = document.getElementById('year');
  if (yr) yr.textContent = new Date().getFullYear();
  initGallery();
});

// ---------------------------------------------------------
// Header: transparent over the hero, solid once scrolled past a small threshold
// ---------------------------------------------------------
function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const THRESHOLD = 60;

  function update() {
    header.classList.toggle('scrolled', window.scrollY > THRESHOLD);
  }

  update();
  window.addEventListener('scroll', update, { passive: true });
}

// ---------------------------------------------------------
// Hero background slideshow — crossfades through images/hero-slide-*.jpg
// ---------------------------------------------------------
function initHeroSlideshow() {
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length < 2) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  let current = 0;
  setInterval(() => {
    slides[current].classList.remove('is-active');
    current = (current + 1) % slides.length;
    slides[current].classList.add('is-active');
  }, 5000);
}

// ---------------------------------------------------------
// Lucide icons
// ---------------------------------------------------------
function initIcons() {
  if (window.lucide) window.lucide.createIcons();
}

// ---------------------------------------------------------
// AOS (Animate On Scroll) — restrained fade-up only
// ---------------------------------------------------------
function initAOS() {
  if (window.AOS) {
    window.AOS.init({
      duration: 550,
      easing: 'ease-out',
      once: true,
      offset: 60,
    });
  }
}

// ---------------------------------------------------------
// Mobile nav toggle
// ---------------------------------------------------------
function initMobileNav() {
  const toggle = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.innerHTML = `<i data-lucide="${isOpen ? 'x' : 'menu'}" aria-hidden="true"></i>`;
    if (window.lucide) window.lucide.createIcons();
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.innerHTML = '<i data-lucide="menu" aria-hidden="true"></i>';
      if (window.lucide) window.lucide.createIcons();
    });
  });
}

// ---------------------------------------------------------
// Services dropdown (click-to-toggle; also hoverable on desktop via CSS)
// ---------------------------------------------------------
function initServicesDropdown() {
  document.querySelectorAll('.has-dropdown').forEach((item) => {
    const toggle = item.querySelector('.dropdown-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = item.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  });

  document.addEventListener('click', (e) => {
    document.querySelectorAll('.has-dropdown.open').forEach((item) => {
      if (!item.contains(e.target)) {
        item.classList.remove('open');
        item.querySelector('.dropdown-toggle').setAttribute('aria-expanded', 'false');
      }
    });
  });
}

// ---------------------------------------------------------
// EN / ES language toggle
// data-en / data-es attributes hold the two text variants.
// ---------------------------------------------------------
function initLangToggle() {
  const STORAGE_KEY = 'luna-sons-lang';
  let currentLang = localStorage.getItem(STORAGE_KEY) || 'en';

  function applyLang(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;
    document.querySelectorAll('[data-en]').forEach((el) => {
      const value = lang === 'es' ? el.dataset.es : el.dataset.en;
      if (value !== undefined) el.innerHTML = value;
    });
    document.querySelectorAll('[data-alt-en]').forEach((el) => {
      const value = lang === 'es' ? el.dataset.altEs : el.dataset.altEn;
      if (value !== undefined) el.setAttribute('alt', value);
    });
    document.querySelectorAll('.lang-en-flag').forEach((el) => el.setAttribute('data-active', String(lang === 'en')));
    document.querySelectorAll('.lang-es-flag').forEach((el) => el.setAttribute('data-active', String(lang === 'es')));
    document.querySelectorAll('.form-lang').forEach((el) => { el.value = lang; });
    localStorage.setItem(STORAGE_KEY, lang);
  }

  document.querySelectorAll('.lang-toggle').forEach((btn) => {
    btn.addEventListener('click', () => applyLang(currentLang === 'en' ? 'es' : 'en'));
  });

  if (currentLang !== 'en') applyLang(currentLang);
}

// ---------------------------------------------------------
// FAQ accordion
// ---------------------------------------------------------
function initFAQ() {
  document.querySelectorAll('.faq-item').forEach((item) => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
      const isOpen = item.getAttribute('data-open') === 'true';
      document.querySelectorAll('.faq-item').forEach((other) => {
        other.setAttribute('data-open', 'false');
        other.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
      });
      item.setAttribute('data-open', String(!isOpen));
      question.setAttribute('aria-expanded', String(!isOpen));
    });
  });
}

// ---------------------------------------------------------
// Consultation form
// - Spam trap: a hidden field real visitors never see or fill. If it has a value,
//   the submission is silently dropped (no error shown to a bot).
// - FORM_ENDPOINT lives on the form as data-endpoint (see tools/shell.py). While it is
//   empty the form works in PREVIEW mode: it validates, but sends nothing and says so.
// ---------------------------------------------------------
const FORM_TEXT = {
  en: {
    sending: 'Sending…',
    ok: "Thank you — we've received your request and will be in touch soon.",
    fail: 'Something went wrong sending your request. Please call (805) 268-2808 and we will help right away.',
    preview: "Preview mode: the form is filled in correctly, but it isn't connected yet — nothing was sent.",
  },
  es: {
    sending: 'Enviando…',
    ok: 'Gracias — recibimos su solicitud y nos pondremos en contacto pronto.',
    fail: 'Algo salió mal al enviar su solicitud. Llámenos al (805) 268-2808 y con gusto le ayudamos.',
    preview: 'Modo de vista previa: el formulario está completo, pero aún no está conectado — no se envió nada.',
  },
};

function initForms() {
  document.querySelectorAll('.consult-form').forEach((form) => {
    const status = form.querySelector('.form-status');
    const button = form.querySelector('.consult-submit');
    const langField = form.querySelector('.form-lang');
    if (langField) langField.value = document.documentElement.lang === 'es' ? 'es' : 'en';

    function show(text, kind) {
      status.hidden = false;
      status.textContent = text;
      status.dataset.kind = kind;
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const lang = document.documentElement.lang === 'es' ? 'es' : 'en';
      const t = FORM_TEXT[lang];

      const trap = form.querySelector('.trap-answer');
      if (trap && trap.value.trim() !== '') {
        // Spam: pretend it worked, send nothing.
        show(t.ok, 'ok');
        form.reset();
        return;
      }

      const endpoint = (form.dataset.endpoint || '').trim();
      if (!endpoint) {
        show(t.preview, 'preview');
        return;
      }

      button.disabled = true;
      show(t.sending, 'sending');
      try {
        const res = await fetch(endpoint, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' },
        });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        show(t.ok, 'ok');
        form.reset();
        if (langField) langField.value = lang;
      } catch (err) {
        show(t.fail, 'error');
      } finally {
        button.disabled = false;
      }
    });
  });
}

// ---------------------------------------------------------
// Our Work gallery: category filter + lightbox (native <dialog>)
// ---------------------------------------------------------
function initGallery() {
  const grid = document.querySelector('.gallery-grid');
  if (!grid) return;
  const items = Array.from(grid.querySelectorAll('.gallery-item'));
  const chips = document.querySelectorAll('.filter-chip');
  const dialog = document.getElementById('lightbox');
  const lbImg = dialog ? dialog.querySelector('.lb-img') : null;
  const lbCount = dialog ? dialog.querySelector('.lb-count') : null;
  let visible = items.slice();
  let index = 0;

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      const cat = chip.dataset.filter;
      chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
      items.forEach((it) => { it.hidden = !(cat === 'all' || it.dataset.cat === cat); });
      visible = items.filter((it) => !it.hidden);
    });
  });

  function openAt(i) {
    if (!dialog || !visible.length) return;
    index = (i + visible.length) % visible.length;
    const thumb = visible[index].querySelector('img');
    const lang = document.documentElement.lang === 'es' ? 'es' : 'en';
    lbImg.src = visible[index].dataset.full;
    lbImg.alt = lang === 'es' ? thumb.dataset.altEs : thumb.dataset.altEn;
    lbCount.textContent = (index + 1) + ' / ' + visible.length;
    if (!dialog.open) dialog.showModal();
  }

  items.forEach((it) => it.addEventListener('click', () => openAt(visible.indexOf(it))));
  if (!dialog) return;
  dialog.querySelector('.lb-prev').addEventListener('click', () => openAt(index - 1));
  dialog.querySelector('.lb-next').addEventListener('click', () => openAt(index + 1));
  dialog.querySelector('.lb-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (e) => { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') openAt(index - 1);
    if (e.key === 'ArrowRight') openAt(index + 1);
  });
}
