/* Saudi Utility Hub — cookie consent notice and Google Analytics loader.
   Stores the visitor's choice in localStorage, passes it to Google through
   Consent Mode (Analytics + AdSense), and loads Google Analytics once for the
   whole site. Loaded with `defer` on every page. */
(function () {
  var KEY = 'suh-cookie-consent';
  var GA_ID = 'G-MX4J28KBE6';
  // EEA, UK and Switzerland: nothing beyond essentials until the visitor accepts.
  var OPT_IN_REGIONS = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','GR','HU','IE','IT','LV','LT',
                        'LU','MT','NL','PL','PT','RO','SK','SI','ES','SE','IS','LI','NO','GB','CH'];
  var choice = null;
  try { choice = window.localStorage.getItem(KEY); } catch (e) { choice = null; }

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  var DENIED = { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' };
  var GRANTED = { ad_storage: 'granted', ad_user_data: 'granted', ad_personalization: 'granted', analytics_storage: 'granted' };
  var ESSENTIAL = { ad_storage: 'granted', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied' };

  gtag('consent', 'default', Object.assign({ region: OPT_IN_REGIONS, wait_for_update: 500 }, DENIED));
  gtag('consent', 'default', GRANTED);

  function applyChoice(value) {
    if (value === 'declined') {
      window.adsbygoogle = window.adsbygoogle || [];
      window.adsbygoogle.requestNonPersonalizedAds = 1;
      gtag('consent', 'update', ESSENTIAL);
    } else if (value === 'accepted') {
      gtag('consent', 'update', GRANTED);
    }
  }

  applyChoice(choice);

  (function loadAnalytics() {
    if (document.querySelector('script[src*="googletagmanager.com/gtag/js"]')) return;
    var ga = document.createElement('script');
    ga.async = true;
    ga.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(ga);
    gtag('js', new Date());
    gtag('config', GA_ID);
  })();

  if (choice === 'accepted' || choice === 'declined') return;

  function save(value) {
    try { window.localStorage.setItem(KEY, value); } catch (e) {}
    applyChoice(value);
  }

  function build() {
    if (document.getElementById('suh-cookie-banner')) return;

    var css = document.createElement('style');
    css.textContent =
      '#suh-cookie-banner{position:fixed;left:0;right:0;bottom:0;z-index:9999;background:#1a1a2e;color:#f1f5f9;' +
      'padding:1rem 1.25rem;box-shadow:0 -2px 14px rgba(0,0,0,.28);font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;' +
      'font-size:.9rem;line-height:1.55}' +
      '#suh-cookie-banner .suh-cc-inner{max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:.9rem;align-items:center;justify-content:space-between}' +
      '#suh-cookie-banner p{margin:0;flex:1 1 420px}' +
      '#suh-cookie-banner a{color:#ffd166;text-decoration:underline}' +
      '#suh-cookie-banner .suh-cc-actions{display:flex;gap:.6rem;flex-wrap:wrap}' +
      '#suh-cookie-banner button{cursor:pointer;border-radius:6px;font-size:.88rem;font-weight:600;padding:.55rem 1.1rem;border:1px solid rgba(255,255,255,.35);' +
      'font-family:inherit;background:transparent;color:#f1f5f9}' +
      '#suh-cookie-banner button.suh-cc-accept{background:#0a7c3e;border-color:#0a7c3e;color:#fff}' +
      '#suh-cookie-banner button:focus-visible{outline:2px solid #ffd166;outline-offset:2px}' +
      '@media(max-width:640px){#suh-cookie-banner .suh-cc-inner{flex-direction:column;align-items:flex-start}}';
    document.head.appendChild(css);

    var bar = document.createElement('div');
    bar.id = 'suh-cookie-banner';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-live', 'polite');
    bar.setAttribute('aria-label', 'Cookie notice');
    var isAr = (document.documentElement.getAttribute('lang') || '').indexOf('ar') === 0;
    var text = isAr
      ? 'نستخدم ملفات الارتباط لتشغيل الموقع، ولقياس الزيارات عبر Google Analytics، ولإظهار الإعلانات عبر Google AdSense. بيانات الحاسبات تبقى داخل متصفحك ولا تُرسل إلينا. اطلع على <a href="https://www.saudiutilityhub.com/privacy.html">سياسة الخصوصية</a>.'
      : 'We use cookies for basic site function, for visit statistics (Google Analytics) and for advertising (Google AdSense). Calculator inputs stay in your browser and are never sent to us. Choose “Essential only” to turn off analytics and get non-personalised ads. Read our <a href="https://www.saudiutilityhub.com/privacy.html">Privacy Policy</a>.';
    var accept = isAr ? 'قبول الكل' : 'Accept all';
    var decline = isAr ? 'الضروري فقط' : 'Essential only';
    if (isAr) bar.setAttribute('dir', 'rtl');
    bar.innerHTML =
      '<div class="suh-cc-inner">' +
      '<p>' + text + '</p>' +
      '<div class="suh-cc-actions">' +
      '<button type="button" class="suh-cc-decline">' + decline + '</button>' +
      '<button type="button" class="suh-cc-accept">' + accept + '</button>' +
      '</div></div>';
    document.body.appendChild(bar);

    function close(value) {
      save(value);
      if (bar.parentNode) bar.parentNode.removeChild(bar);
    }
    bar.querySelector('.suh-cc-accept').addEventListener('click', function () { close('accepted'); });
    bar.querySelector('.suh-cc-decline').addEventListener('click', function () { close('declined'); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }

  window.suhOpenCookieSettings = function () {
    try { window.localStorage.removeItem(KEY); } catch (e) {}
    build();
  };
})();
