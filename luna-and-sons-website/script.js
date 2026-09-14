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
  initCountUp();
  initFAQ();
  initForms();
  initHeroSlideshow();
  document.getElementById('year').textContent = new Date().getFullYear();
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
// Simple math anti-spam check — generates "X + Y =" per form and validates
// the answer on submit, without any third-party CAPTCHA service.
// ---------------------------------------------------------
function setUpCaptcha(form) {
  const field = form.querySelector('.captcha-field');
  const questionEl = form.querySelector('.captcha-question');
  const input = form.querySelector('.captcha-answer');
  const errorEl = form.querySelector('.captcha-error');
  if (!field || !questionEl || !input) return null;

  let a, b;
  function newChallenge() {
    a = Math.floor(Math.random() * 20) + 1;
    b = Math.floor(Math.random() * 20) + 1;
    questionEl.textContent = `${a} + ${b} =`;
    input.value = '';
    field.classList.remove('has-error');
    errorEl.hidden = true;
  }

  newChallenge();

  return {
    validate() {
      const answer = parseInt(input.value, 10);
      const correct = !Number.isNaN(answer) && answer === a + b;
      field.classList.toggle('has-error', !correct);
      errorEl.hidden = correct;
      input.setAttribute('aria-invalid', String(!correct));
      return correct;
    },
    reset: newChallenge,
  };
}

// ---------------------------------------------------------
// Honeypot anti-spam field — a real user never sees or fills this input
// (off-screen via CSS, not display:none, so form-filling bots still find it).
// Any value in it means the submission is spam; reject it silently, with no
// visible error, since a real visitor could never trigger this case.
// ---------------------------------------------------------
function isHoneypotTripped(form) {
  const honeypot = form.querySelector('.honeypot-answer');
  return !!(honeypot && honeypot.value.trim() !== '');
}

// ---------------------------------------------------------
// Form submission (front-end only — no backend wired up yet)
// ---------------------------------------------------------
function initForms() {
  const forms = [document.getElementById('quick-quote-form'), document.getElementById('contact-form'), document.getElementById('page-contact-form')];
  forms.forEach((form) => {
    if (!form) return;
    const captcha = setUpCaptcha(form);

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      if (isHoneypotTripped(form)) {
        return; // Silent reject — spam, not a real user, so no error shown.
      }

      if (captcha && !captcha.validate()) {
        form.querySelector('.captcha-answer').focus();
        return;
      }

      const lang = document.documentElement.lang;
      alert(lang === 'es'
        ? 'Gracias. Nos pondremos en contacto pronto. (Este formulario aún no está conectado a un backend.)'
        : "Thanks — we'll be in touch soon. (This form isn't wired up to a backend yet.)");
      form.reset();
      if (captcha) captcha.reset();
    });
  });
}
