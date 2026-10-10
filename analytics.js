/*
 * Loptor CRE — analítica de la landing (PostHog, región UE).
 *
 * Sin SDK, sin cookies y sin almacenamiento del navegador: cada evento se envía a la
 * API pública de captura de PostHog UE con un identificador anónimo que vive solo en
 * memoria mientras la página está abierta (no crea perfiles de persona).
 *
 *  - Solo eventos explícitos y propiedades de lista blanca (ver ALLOWED). Nada de
 *    texto libre ni datos personales.
 *  - Respeta «No rastrear» (Do Not Track).
 *  - Solo mide en producción (loptorcre.com / www.loptorcre.com): los Previews de
 *    Vercel y localhost no ensucian las métricas.
 *  - Propaga la campaña (utm_*) y `source=landing` a los enlaces hacia la app, para
 *    atribuir cada alta sin cookies.
 *  - Falla en silencio: la analítica nunca bloquea la página.
 *
 * La clave del proyecto es pública por diseño (solo permite enviar eventos).
 */
(function () {
  'use strict';

  var POSTHOG_KEY = 'phc_nYqkQM3LVkDALV3jqzMov3Abzp4dbjjT3b3gC5xt9Fne';
  var CAPTURE_URL = 'https://eu.i.posthog.com/capture/';
  var APP_ORIGIN = 'https://app.loptorcre.com';
  var PRODUCTION_HOSTS = ['loptorcre.com', 'www.loptorcre.com'];
  var CAMPAIGN_KEYS = ['utm_source', 'utm_medium', 'utm_campaign'];

  // Evento → propiedades permitidas.
  var ALLOWED = {
    $pageview: ['lang', 'utm_source', 'utm_medium', 'utm_campaign'],
    cta_clicked: ['location', 'target', 'plan', 'lang'],
    language_changed: ['language'],
    billing_toggled: ['billing'],
    walkthrough_interacted: ['control', 'step'],
    faq_opened: ['index'],
    section_viewed: ['section']
  };

  function trackingOn() {
    try {
      if (PRODUCTION_HOSTS.indexOf(window.location.hostname) === -1) return false;
      var dnt = navigator.doNotTrack || window.doNotTrack || navigator.msDoNotTrack;
      if (dnt === '1' || dnt === 'yes') return false;
      return true;
    } catch (_) {
      return false;
    }
  }

  var enabled = trackingOn();

  function randomId() {
    try {
      var bytes = new Uint8Array(16);
      crypto.getRandomValues(bytes);
      return Array.prototype.map.call(bytes, function (b) { return ('0' + b.toString(16)).slice(-2); }).join('');
    } catch (_) {
      return String(Date.now()) + Math.random().toString(16).slice(2);
    }
  }

  // Un identificador por carga de página; nunca se guarda en el navegador.
  var anonymousId = randomId();
  var sessionId = randomId();

  function currentLang() {
    var active = document.querySelector('.lang-btn.is-active');
    return (active && active.getAttribute('data-lang')) || document.documentElement.lang || 'en';
  }

  function campaign() {
    var out = {};
    try {
      var params = new URLSearchParams(window.location.search);
      CAMPAIGN_KEYS.forEach(function (key) {
        var value = params.get(key);
        if (value) out[key] = value.slice(0, 64);
      });
    } catch (_) { /* silencio */ }
    return out;
  }

  function sanitize(event, props) {
    var allowed = ALLOWED[event] || [];
    var clean = {};
    Object.keys(props || {}).forEach(function (key) {
      if (allowed.indexOf(key) === -1) return;
      var value = props[key];
      if (typeof value === 'number' && isFinite(value)) clean[key] = value;
      else if (typeof value === 'boolean') clean[key] = value;
      else if (typeof value === 'string' && value.length > 0) clean[key] = value.slice(0, 64);
    });
    return clean;
  }

  function track(event, props) {
    if (!enabled || !ALLOWED[event]) return;
    try {
      var properties = sanitize(event, props);
      properties.$process_person_profile = false;
      properties.$lib = 'loptor-landing';
      properties.$session_id = sessionId;
      properties.$current_url = window.location.origin + window.location.pathname;
      properties.$host = window.location.host;
      properties.$pathname = window.location.pathname;
      if (document.referrer) {
        try { properties.$referrer = new URL(document.referrer).origin; } catch (_) { /* silencio */ }
      }
      properties.site = 'landing';
      var body = JSON.stringify({
        api_key: POSTHOG_KEY,
        event: event,
        distinct_id: anonymousId,
        properties: properties,
        timestamp: new Date().toISOString()
      });
      // sendBeacon sobrevive a la navegación (clic en un CTA que abre la app);
      // fetch con keepalive es el respaldo.
      if (navigator.sendBeacon && navigator.sendBeacon(CAPTURE_URL, new Blob([body], { type: 'text/plain' }))) return;
      fetch(CAPTURE_URL, { method: 'POST', body: body, keepalive: true, headers: { 'Content-Type': 'text/plain' } }).catch(function () {});
    } catch (_) { /* La analítica nunca bloquea la página. */ }
  }

  // Exposición mínima para otros scripts de la página (no-op si está desactivada).
  window.loptorTrack = track;

  function ctaLocation(link) {
    if (link.closest('.price-card')) return 'pricing';
    if (link.closest('.final-cta')) return 'final_cta';
    if (link.closest('.hero')) return 'hero';
    if (link.closest('.seller-card')) return 'sell_side';
    if (link.closest('.site-header')) return 'header';
    if (link.closest('.site-footer')) return 'footer';
    return 'other';
  }

  function planOf(link) {
    var card = link.closest('.price-card');
    var label = card && card.querySelector('.price-label');
    var text = label ? label.textContent.toUpperCase() : '';
    if (text.indexOf('SOLO') !== -1) return 'solo';
    if (text.indexOf('BOUTIQUE') !== -1) return 'boutique';
    if (text.indexOf('FAMILY') !== -1) return 'family_office';
    return undefined;
  }

  function ctaTarget(href) {
    if (href.indexOf('mailto:') === 0) return 'contact';
    if (href.indexOf(APP_ORIGIN) !== 0) return null;
    return /[?&]action=login/.test(href) ? 'login' : 'register';
  }

  // Los enlaces hacia la app llevan `source=landing` y la campaña de la visita.
  function decorateAppLinks() {
    var extra = campaign();
    var links = document.querySelectorAll('a[href^="' + APP_ORIGIN + '"]');
    Array.prototype.forEach.call(links, function (link) {
      try {
        var url = new URL(link.getAttribute('href'));
        if (!url.searchParams.has('source')) url.searchParams.set('source', 'landing');
        Object.keys(extra).forEach(function (key) {
          if (!url.searchParams.has(key)) url.searchParams.set(key, extra[key]);
        });
        link.setAttribute('href', url.toString());
      } catch (_) { /* silencio */ }
    });
  }

  function observeSections() {
    if (!('IntersectionObserver' in window)) return;
    var seen = {};
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        if (!entry.isIntersecting || !id || seen[id]) return;
        seen[id] = true;
        track('section_viewed', { section: id });
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.35 });
    ['how-it-works', 'sell-side', 'buy-side', 'pricing', 'faq'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) observer.observe(el);
    });
  }

  function onClick(event) {
    var target = event.target;
    if (!target || !target.closest) return;

    var link = target.closest('a[href]');
    if (link) {
      var kind = ctaTarget(link.getAttribute('href') || '');
      if (kind) track('cta_clicked', { location: ctaLocation(link), target: kind, plan: planOf(link), lang: currentLang() });
      return;
    }
    var langButton = target.closest('.lang-btn');
    if (langButton) { track('language_changed', { language: langButton.getAttribute('data-lang') }); return; }
    var billingButton = target.closest('.billing-btn');
    if (billingButton) { track('billing_toggled', { billing: billingButton.getAttribute('data-billing') }); return; }
    var stepButton = target.closest('.step-button');
    if (stepButton) { track('walkthrough_interacted', { control: 'step', step: Number(stepButton.getAttribute('data-step')) }); return; }
    if (target.closest('#step-next')) { track('walkthrough_interacted', { control: 'next' }); return; }
    if (target.closest('#step-prev')) { track('walkthrough_interacted', { control: 'prev' }); return; }
    var faq = target.closest('.faq-question');
    if (faq) {
      var all = Array.prototype.slice.call(document.querySelectorAll('.faq-question'));
      // El clic de la página ya cambió el estado: solo cuenta al abrir.
      window.setTimeout(function () {
        if (faq.getAttribute('aria-expanded') === 'true') track('faq_opened', { index: all.indexOf(faq) + 1 });
      }, 0);
    }
  }

  function start() {
    decorateAppLinks();
    if (!enabled) return;
    var props = campaign();
    props.lang = currentLang();
    track('$pageview', props);
    observeSections();
    document.addEventListener('click', onClick, true);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
