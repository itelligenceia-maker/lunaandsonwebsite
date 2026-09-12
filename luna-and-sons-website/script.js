// =========================================================
// LUNA & SONS LANDSCAPING — SITE SCRIPT
// =========================================================

document.addEventListener('DOMContentLoaded', () => {
  initIcons();
  initAOS();
  initMobileNav();
  initLangToggle();
  initCountUp();
  initFAQ();
  initForms();
  document.getElementById('year').textContent = new Date().getFullYear();
});

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
    document.querySelectorAll('.lang-en-flag').forEach((el) => el.setAttribute('data-active', String(lang === 'en')));
    document.querySelectorAll('.lang-es-flag').forEach((el) => el.setAttribute('data-active', String(lang === 'es')));
    localStorage.setItem(STORAGE_KEY, lang);
  }

  document.querySelectorAll('.lang-toggle').forEach((btn) => {
    btn.addEventListener('click', () => applyLang(currentLang === 'en' ? 'es' : 'en'));
  });

  if (currentLang !== 'en') applyLang(currentLang);
}

// ---------------------------------------------------------
// Trust bar count-up on scroll into view
// ---------------------------------------------------------
function initCountUp() {
  const numbers = document.querySelectorAll('.trust-number[data-count], .trust-number[data-count-since]');
  if (!numbers.length) return;

  const animate = (el) => {
    const target = el.dataset.countSince
      ? new Date().getFullYear() - parseInt(el.dataset.countSince, 10)
      : parseInt(el.dataset.count, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1400;
    const start = performance.now();

    function tick(now) {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animate(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.4 });

  numbers.forEach((el) => observer.observe(el));
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
// Form submission (front-end only — no backend wired up yet)
// ---------------------------------------------------------
function initForms() {
  const forms = [document.getElementById('quick-quote-form'), document.getElementById('contact-form')];
  forms.forEach((form) => {
    if (!form) return;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const lang = document.documentElement.lang;
      alert(lang === 'es'
        ? 'Gracias. Nos pondremos en contacto pronto. (Este formulario aún no está conectado a un backend.)'
        : "Thanks — we'll be in touch soon. (This form isn't wired up to a backend yet.)");
      form.reset();
    });
  });
}
