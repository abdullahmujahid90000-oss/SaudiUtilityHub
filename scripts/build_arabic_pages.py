#!/usr/bin/env python3
"""Generate Arabic guide/calculator pages in /ar from page data in ar_content_*.py.
Run from repo root: python3 scripts/build_arabic_pages.py
"""
import json, sys, html, os
sys.path.insert(0, os.path.dirname(__file__))
from ar_content_a import PAGES as A
from ar_content_b import PAGES as B
PAGES = A + B
SITE = "https://www.saudiutilityhub.com"
UPDATED = "2026-11-20"
STYLE = open(os.path.join(os.path.dirname(__file__), "ar_head_style.html"), encoding="utf8").read()

# slug -> (short name, card title, card blurb). Includes existing Arabic pages.
ARM = {
 "salary-calculator": ("حاسبة الراتب", "حاسبة الراتب", "صافي الراتب بعد الاستقطاعات والبدلات."),
 "gosi-calculator": ("التأمينات", "حاسبة التأمينات (GOSI)", "اشتراك الموظف وصاحب العمل بالنِسب الحالية."),
 "ksa-eos-calculator": ("نهاية الخدمة", "حاسبة نهاية الخدمة", "مكافأة نهاية الخدمة حسب المادتين 84 و85."),
 "iqama-expiry-calculator": ("الإقامة", "حاسبة انتهاء الإقامة", "الأيام المتبقية على انتهاء الإقامة."),
 "notice-period-saudi-labour-law": ("فترة الإشعار", "فترة الإشعار في نظام العمل", "30 يومًا للاستقالة و60 يومًا عند إنهاء صاحب العمل."),
 "iqama-renewal-fees": ("رسوم تجديد الإقامة", "رسوم تجديد الإقامة", "التكلفة الحقيقية بندًا بندًا ومن يدفع كل بند."),
 "final-settlement-calculator": ("المستحقات النهائية", "حاسبة المستحقات النهائية", "اجمع راتبك ومكافأتك وإجازتك قبل أن توقّع."),
 "leave-calculator": ("الإجازة السنوية", "حاسبة الإجازة السنوية", "21 أو 30 يومًا، وتعويض الأيام غير المستخدمة."),
 "overtime-calculator": ("العمل الإضافي", "حاسبة العمل الإضافي", "الأجر بالساعة + 50% وفق المادة 107."),
 "exit-reentry-calculator": ("تأشيرة الخروج والعودة", "حاسبة تأشيرة الخروج والعودة", "رسوم المفردة والمتعددة لك ولعائلتك."),
 "dependent-levy-calculator": ("رسوم المرافقين", "حاسبة رسوم المرافقين", "400 ريال شهريًا عن كل فرد من عائلتك."),
 "what-happens-to-iqama-if-you-resign": ("الإقامة بعد الاستقالة", "ماذا يحدث لإقامتك بعد الاستقالة؟", "مهلة 60 يومًا، النقل عبر قوى، وتجنّب بلاغ التغيّب."),
 "salary-not-paid-saudi-arabia": ("تأخر الراتب", "الراتب غير مدفوع؟ حقوقك", "الشكوى، نقل الخدمات، والمادة 81."),
 "final-exit-vs-exit-reentry-visa": ("الخروج النهائي أم الخروج والعودة", "الخروج النهائي أم الخروج والعودة؟", "الفرق في الرسوم والإقامة والعودة."),
}
HUB_SLUG = "guides"

def e(s): return html.escape(s, quote=True)
def u(slug): return f"{SITE}/ar/{slug}.html"

def nav():
    items = [("", "الرئيسية"), ("salary-calculator.html", "حاسبة الراتب"), ("gosi-calculator.html", "التأمينات"),
             ("ksa-eos-calculator.html", "نهاية الخدمة"), ("iqama-expiry-calculator.html", "الإقامة"), ("guides.html", "الأدلة")]
    lis = "\n".join(f'<li><a href="{SITE}/ar{("/" + p) if p else ""}">{t}</a></li>' for p, t in items)
    return f'<header>\n<div class="header-inner">\n<a class="logo" href="{SITE}/ar">Saudi<span>Utility</span>Hub</a>\n<nav aria-label="التنقل الرئيسي">\n<ul>\n{lis}\n</ul>\n</nav>\n</div>\n</header>'

def related(slugs):
    cards = "\n".join(f'<div class="related-card"><h3>{ARM[s][1]}</h3><p>{ARM[s][2]}</p><a href="{u(s)}">افتح الصفحة ←</a></div>' for s in slugs)
    return f'<h2>أدوات وأدلة ذات صلة</h2>\n<div class="related-grid">\n{cards}\n</div>'

def footer():
    col = "\n".join(f'<li><a href="{u(s)}">{ARM[s][1]}</a></li>' for s in ["salary-calculator","gosi-calculator","ksa-eos-calculator","iqama-expiry-calculator","final-settlement-calculator","leave-calculator","overtime-calculator"])
    col2 = "\n".join(f'<li><a href="{u(s)}">{ARM[s][1]}</a></li>' for s in ["notice-period-saudi-labour-law","iqama-renewal-fees","exit-reentry-calculator","dependent-levy-calculator","what-happens-to-iqama-if-you-resign","salary-not-paid-saudi-arabia","final-exit-vs-exit-reentry-visa"])
    return f'''<footer>
<div class="footer-grid">
<div class="footer-col"><h3>الحاسبات</h3><ul>
{col}
</ul></div>
<div class="footer-col"><h3>أدلة</h3><ul>
{col2}
<li><a href="{SITE}/ar/guides.html">كل الأدلة</a></li>
</ul></div>
<div class="footer-col"><h3>الموقع</h3><ul>
<li><a href="{SITE}/ar">الصفحة الرئيسية بالعربية</a></li>
<li><a href="{SITE}/">English site</a></li>
<li><a href="{SITE}/about.html">من نحن</a></li>
<li><a href="{SITE}/contact.html">اتصل بنا</a></li>
<li><a href="{SITE}/privacy.html">سياسة الخصوصية</a> · <a href="{SITE}/disclaimer.html">إخلاء المسؤولية</a></li>
</ul></div>
</div>
<p style="color:#cbd5e1;font-size:.9rem;max-width:900px;margin:1rem auto;padding:0 16px">هذه الأدوات والأدلة تقديرية للاسترشاد فقط وليست جهة رسمية، ولا تُغني عن الأنظمة الصادرة عن وزارة الموارد البشرية والتنمية الاجتماعية أو المؤسسة العامة للتأمينات الاجتماعية.</p>
<div class="copyright">© 2026 Saudi Utility Hub — جميع الحقوق محفوظة</div>
</footer>'''

AUTHOR = f'''<div style="max-width:900px;margin:2rem auto 0;padding:1rem 16px;border-top:1px solid #e2e8f0;font-size:.9rem;color:#334155;line-height:1.7">
<p style="margin:0 0 .3rem"><strong>إعداد ومراجعة: <a href="{SITE}/about.html#team">فريق Saudi Utility Hub</a></strong></p>
<p style="margin:0">فريق صغير مقيم في الرياض. نراجع كل صفحة على ما تنشره وزارة الموارد البشرية والتنمية الاجتماعية ومنصات قوى وأبشر ومقيم والتأمينات الاجتماعية، ونصحّح أي خطأ يصلنا. آخر مراجعة: 20 نوفمبر 2026.</p>
</div>'''

def page(p):
    s = p["slug"]; en = p["en"]
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","inLanguage":"ar",
              "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faq"]]}
    web_ld = {"@context":"https://schema.org","@type":"Article" if not p.get("calc") else "WebPage","name":p["title"],"headline":p["h1_plain"],
              "inLanguage":"ar","url":u(s),"description":p["desc"],"dateModified":UPDATED,
              "author":{"@type":"Organization","name":"Saudi Utility Hub","url":SITE+"/"},
              "isPartOf":{"@type":"WebSite","name":"Saudi Utility Hub","url":SITE+"/"}}
    bc_ld = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"الرئيسية","item":SITE+"/ar"},
        {"@type":"ListItem","position":2,"name":"الأدلة","item":SITE+"/ar/guides.html"},
        {"@type":"ListItem","position":3,"name":p["crumb"]}]}
    lds = [web_ld, faq_ld, bc_ld]
    if p.get("calc"):
        lds.append({"@context":"https://schema.org","@type":"WebApplication","name":p["h1_plain"],"inLanguage":"ar","url":u(s),
                    "description":p["desc"],"applicationCategory":"FinanceApplication","operatingSystem":"Web",
                    "offers":{"@type":"Offer","price":"0","priceCurrency":"SAR"}})
    ld = "\n".join('<script type="application/ld+json">\n'+json.dumps(x,ensure_ascii=False,indent=2)+'\n</script>' for x in lds)
    faq_html = "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q,a in p["faq"])
    src = "\n".join(f'<li><a href="{url}" rel="noopener" target="_blank">{t}</a></li>' for t,url in p["sources"])
    calc = p.get("calc","")
    head = f'''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta content="ca-pub-5391037132181133" name="google-adsense-account"/>
<script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5391037132181133"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{e(p["title"])}</title>
<meta content="{e(p["desc"])}" name="description"/>
<link href="{u(s)}" rel="canonical"/>
<link href="{u(s)}" hreflang="ar" rel="alternate"/>
<link href="{SITE}/{en}.html" hreflang="en" rel="alternate"/>
<link href="{SITE}/{en}.html" hreflang="x-default" rel="alternate"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="{e(p["title"])}" property="og:title"/>
<meta content="{e(p["desc"])}" property="og:description"/>
<meta content="{u(s)}" property="og:url"/>
<meta content="website" property="og:type"/>
<meta content="ar_SA" property="og:locale"/>
<meta content="en_US" property="og:locale:alternate"/>
<meta content="{SITE}/og-image.png" property="og:image"/>
<meta content="Saudi Utility Hub" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{e(p["title"])}" name="twitter:title"/>
<meta content="{e(p["desc"])}" name="twitter:description"/>
<meta content="{SITE}/og-image.png" name="twitter:image"/>
{ld}
{STYLE}'''
    body = f'''
<body>
{nav()}
<div class="container">
<nav aria-label="مسار التنقل" class="breadcrumb"><a href="{SITE}/ar">الرئيسية</a> › <a href="{SITE}/ar/guides.html">الأدلة</a> › <span>{p["crumb"]}</span></nav>
<a class="lang-switch" href="{SITE}/{en}.html" hreflang="en">🇬🇧 View this page in English</a>
<div class="hero">
<h1>{p["h1"]}</h1>
<p>{p["sub"]}</p>
<span class="badge">{p["badge"]}</span>
</div>
<div class="quick-answer">{p["quick"]}</div>
{calc}
{p["body"]}
{related(p["related"])}
<h2>المصادر الرسمية</h2>
<ul class="source-list">
{src}
</ul>
<h2>الأسئلة الشائعة</h2>
{faq_html}
</div>
{AUTHOR}
{footer()}
</body>
</html>
'''
    return head + body

def hub():
    groups = [
      ("حاسبات الراتب والتأمينات", ["salary-calculator","gosi-calculator","overtime-calculator"]),
      ("نهاية الخدمة والمستحقات والإجازات", ["ksa-eos-calculator","final-settlement-calculator","leave-calculator","notice-period-saudi-labour-law","salary-not-paid-saudi-arabia"]),
      ("الإقامة والتأشيرات والعائلة", ["iqama-expiry-calculator","iqama-renewal-fees","dependent-levy-calculator","exit-reentry-calculator","final-exit-vs-exit-reentry-visa","what-happens-to-iqama-if-you-resign"]),
    ]
    secs = "\n".join(f'<h2>{g}</h2>\n<div class="related-grid">\n' + "\n".join(f'<div class="related-card"><h3>{ARM[s][1]}</h3><p>{ARM[s][2]}</p><a href="{u(s)}">افتح الصفحة ←</a></div>' for s in ss) + "\n</div>" for g,ss in groups)
    title = "أدلة وحاسبات للمقيمين في السعودية بالعربية"
    desc = "أدلة عملية وحاسبات مجانية للمقيم في السعودية: الراتب والتأمينات ونهاية الخدمة والإجازات وتجديد الإقامة وتأشيرات الخروج ورسوم المرافقين."
    ld = {"@context":"https://schema.org","@type":"CollectionPage","name":title,"inLanguage":"ar","url":u("guides"),"description":desc,"isPartOf":{"@type":"WebSite","name":"Saudi Utility Hub","url":SITE+"/"}}
    head = f'''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta content="ca-pub-5391037132181133" name="google-adsense-account"/>
<script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5391037132181133"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<meta content="{desc}" name="description"/>
<link href="{u("guides")}" rel="canonical"/>
<link href="{u("guides")}" hreflang="ar" rel="alternate"/>
<link href="{SITE}/guides.html" hreflang="en" rel="alternate"/>
<link href="{SITE}/guides.html" hreflang="x-default" rel="alternate"/>
<meta content="index,follow,max-image-preview:large" name="robots"/>
<meta content="{title}" property="og:title"/>
<meta content="{desc}" property="og:description"/>
<meta content="{u("guides")}" property="og:url"/>
<meta content="website" property="og:type"/>
<meta content="ar_SA" property="og:locale"/>
<meta content="{SITE}/og-image.png" property="og:image"/>
<meta content="Saudi Utility Hub" property="og:site_name"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="{title}" name="twitter:title"/>
<meta content="{desc}" name="twitter:description"/>
<script type="application/ld+json">
{json.dumps(ld,ensure_ascii=False,indent=2)}
</script>
{STYLE}'''
    body = f'''
<body>
{nav()}
<div class="container">
<nav aria-label="مسار التنقل" class="breadcrumb"><a href="{SITE}/ar">الرئيسية</a> › <span>الأدلة</span></nav>
<a class="lang-switch" href="{SITE}/guides.html" hreflang="en">🇬🇧 View this page in English</a>
<div class="hero">
<h1>📚 أدلة وحاسبات للمقيمين في السعودية</h1>
<p>إجابات واضحة بالأرقام والأمثلة عن الراتب ونهاية الخدمة والإقامة والتأشيرات، مبنية على الأنظمة المعلنة.</p>
</div>
<div class="quick-answer">اختر ما يناسب حالتك: <strong>تستلم راتبك</strong> أو <strong>تفكر في الاستقالة</strong> أو <strong>تجدد إقامتك وإقامة عائلتك</strong>. كل صفحة تحتوي على مثال محلول وأسئلة شائعة وروابط للخطوة التالية.</div>
{secs}
<h2>من أين تبدأ؟</h2>
<ul>
<li><strong>تفكر في الاستقالة:</strong> اقرأ <a href="{u("what-happens-to-iqama-if-you-resign")}">ماذا يحدث لإقامتك بعد الاستقالة</a> ثم <a href="{u("notice-period-saudi-labour-law")}">فترة الإشعار</a>، واحسب مكافأتك في <a href="{u("ksa-eos-calculator")}">حاسبة نهاية الخدمة</a>. شهر إضافي من الخدمة قد يغيّر مكافأة الاستقالة.</li>
<li><strong>أُنهي عقدك أو انتهى:</strong> اجمع كل ما تستحقه في <a href="{u("final-settlement-calculator")}">حاسبة المستحقات النهائية</a> وتحقق من مهلة الدفع قبل أن توقّع أي ورقة.</li>
<li><strong>راتبك متأخر:</strong> اتبع الترتيب في <a href="{u("salary-not-paid-saudi-arabia")}">الراتب غير مدفوع</a> ثم قدّم الشكوى عبر قوى.</li>
<li><strong>تخطط لسفر إلى بلدك:</strong> قارن <a href="{u("final-exit-vs-exit-reentry-visa")}">الخروج النهائي والخروج والعودة</a> واحسب الرسم في <a href="{u("exit-reentry-calculator")}">حاسبة الخروج والعودة</a>.</li>
<li><strong>تكفل عائلتك:</strong> ميزانية رسم المرافقين في <a href="{u("dependent-levy-calculator")}">حاسبة رسوم المرافقين</a> وفاتورة التجديد كاملة في <a href="{u("iqama-renewal-fees")}">رسوم تجديد الإقامة</a>، وموعد الانتهاء في <a href="{u("iqama-expiry-calculator")}">حاسبة انتهاء الإقامة</a>.</li>
</ul>
<h2>كيف نضمن دقة الأدلة؟</h2>
<p>نراجع كل دليل على ما تنشره وزارة الموارد البشرية والتنمية الاجتماعية ومنصات قوى وأبشر ومقيم والتأمينات الاجتماعية، ونضع تاريخ آخر مراجعة. وحين تتغير القواعد، كما في تعديلات نظام العمل في فبراير 2025، نذكر ما الذي تغيّر ومنذ متى، لأن مقالات قديمة ورسائل واتساب كثيرة ما زالت تكرر القاعدة السابقة. والحاسبات للتخطيط والتقدير، والمنصة الرسمية هي المرجع النهائي للرقم. وإن وجدت ما لا يطابق خدمة رسمية فراسلنا عبر <a href="{SITE}/contact.html">صفحة الاتصال</a> وسنصحّحه.</p>
</div>
{AUTHOR}
{footer()}
</body>
</html>
'''
    return head + body

def main():
    bad = []
    for p in PAGES:
        if len(p["title"]) > 60 or len(p["desc"]) > 155: bad.append((p["slug"], len(p["title"]), len(p["desc"])))
        for r in p["related"]:
            assert r in ARM, (p["slug"], r)
    if bad: print("TOO LONG", bad); sys.exit(1)
    for p in PAGES:
        open(f"ar/{p['slug']}.html","w",encoding="utf8").write(page(p))
    open("ar/guides.html","w",encoding="utf8").write(hub())
    print("built", len(PAGES), "pages + hub")
if __name__ == "__main__": main()
