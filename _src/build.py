# -*- coding: utf-8 -*-
"""Batman Beyaz Eşya Servisi — site üreticisi.

    python3 _src/build.py

⛔ Kök dizindeki HTML dosyalarını ELLE DÜZENLEME — bu betik hepsini yeniden yazar.
"""
import os, re, json, html, hashlib, shutil, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
import arizalar as A
import media

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I = D.ISLETME
SITE = D.SITE

# ------------------------------------------------------------------ yardımcılar

def damga(yol):
    """Varlık sürümleme — GitHub Pages CSS'i 10 dk cache'liyor, damgasız düzeltme ulaşmıyor."""
    tam = os.path.join(KOK, yol)
    if not os.path.exists(tam):
        return ""
    with open(tam, "rb") as f:
        return "?v=" + hashlib.sha1(f.read()).hexdigest()[:8]


def k(s):
    return html.escape(str(s), quote=True)


# --- Türkçe ek uyumu (ilçe/il adlarına kesme işaretiyle ek) -----------------
_SESLI = "aeıioöuü"
_KALIN = "aıou"
_SERT = "fstkçşhp"


def _kucult(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def _son_sesli(ad):
    for h in reversed(_kucult(ad)):
        if h in _SESLI:
            return h
    return "a"


def bulunma(ad):
    """Kozluk'ta, Gercüş'te, Beşiri'de, Sason'da, Batman Merkez'de"""
    a = "a" if _son_sesli(ad) in _KALIN else "e"
    d = "t" if _kucult(ad)[-1] in _SERT else "d"
    return f"{ad}'{d}{a}"


def ayrilma(ad):
    """Kozluk'tan, Gercüş'ten, Beşiri'den, Sason'dan"""
    return bulunma(ad) + "n"


def yonelme(ad):
    """Kozluk'a, Gercüş'e, Beşiri'ye, Sason'a"""
    a = "a" if _son_sesli(ad) in _KALIN else "e"
    y = "y" if _kucult(ad)[-1] in _SESLI else ""
    return f"{ad}'{y}{a}"


def resim(ad, alt, sinif="", boy="100vw", oncelik=False, oran=None):
    """images/ içindeki dosyadan srcset'li <picture> üretir.
    ⚠️ srcset dosya sisteminden okunur — olmayan türev için 404 üretme."""
    kaynak = os.path.join(KOK, "images", ad)
    if not os.path.exists(kaynak):
        return f'<!-- eksik görsel: {ad} -->'
    g, y = media.olcu(ad)
    setler = []
    for w in media.GENISLIKLER:
        if os.path.exists(os.path.join(KOK, "images", f"w{w}", ad)):
            setler.append(f"/images/w{w}/{ad} {w}w")
    setler.append(f"/images/{ad} {g}w")
    yukleme = 'loading="eager" fetchpriority="high"' if oncelik else 'loading="lazy" decoding="async"'
    stil = f' style="aspect-ratio:{oran}"' if oran else ""
    return (
        f'<picture class="{sinif}">'
        f'<img src="/images/{ad}" srcset="{", ".join(setler)}" sizes="{boy}" '
        f'width="{g}" height="{y}" alt="{k(alt)}" {yukleme}{stil}>'
        f'</picture>'
    )


def video_kapak(video_ad, poster_ad, etiket, dikey=True):
    """Tıklanana kadar TEK BAYT inmeyen video kapağı. 84 MB video var — asla otomatik yükleme."""
    if not os.path.exists(os.path.join(KOK, "video", video_ad)):
        return f"<!-- eksik video: {video_ad} -->"
    poster = f"/images/w640/{poster_ad}" if os.path.exists(
        os.path.join(KOK, "images", "w640", poster_ad)) else f"/images/{poster_ad}"
    return (
        f'<div class="video-kutu{" dikey" if dikey else ""}" data-video="/video/{video_ad}">'
        f'<img src="{poster}" alt="{k(etiket)}" loading="lazy" decoding="async" width="640" height="853">'
        f'<button class="oynat" type="button" aria-label="{k(etiket)} videosunu oynat">'
        f'<i><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></i></button>'
        f'<span class="etiket">{k(etiket)}</span></div>'
    )


def sss_blok(sorular):
    """<details> listesi + FAQPage şeması için veri döndürür."""
    ic = "".join(
        f"<details><summary>{k(s)}</summary><div class=\"cevap\">{c}</div></details>"
        for s, c in sorular
    )
    return f'<div class="sss">{ic}</div>'


def faq_sema(sorular):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": s,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", " ", c).strip()}}
            for s, c in sorular
        ],
    }


def kirinti(yol_listesi):
    """yol_listesi: [(ad, url|None), ...] — son eleman linksiz."""
    ogeler, sema = [], []
    for i, (ad, url) in enumerate(yol_listesi, 1):
        if url:
            ogeler.append(f'<li><a href="{url}">{k(ad)}</a></li>')
        else:
            ogeler.append(f'<li><span aria-current="page">{k(ad)}</span></li>')
        sema.append({"@type": "ListItem", "position": i, "name": ad,
                     **({"item": SITE + url} if url else {})})
    nav = (f'<nav class="kirinti" aria-label="Site haritası"><div class="kap">'
           f'<ol>{"".join(ogeler)}</ol></div></nav>')
    return nav, {"@type": "BreadcrumbList", "itemListElement": sema}


# ------------------------------------------------------------------ şema

def yerel_isletme_sema():
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": SITE + "/#isletme",
        "name": I["ad"],
        "url": SITE + "/",
        "telephone": I["tel_link"],
        "image": SITE + "/images/batman-beyaz-esya-servisi-nasil-calisir.webp",
        "logo": SITE + "/images/logo/logo-380.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": I["adres_sokak"],
            "addressLocality": I["adres_il"],
            "addressRegion": I["adres_il"],
            "postalCode": I["posta"],
            "addressCountry": "TR",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": I["lat"], "longitude": I["lng"]},
        "hasMap": I["maps"],
        "areaServed": [{"@type": "AdministrativeArea", "name": b["ad"]} for b in D.BOLGELER],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "priceRange": "₺₺",
        "founder": {"@type": "Person", "name": I["sahip"]},
        "hasCredential": {
            "@type": "EducationalOccupationalCredential",
            "name": I["belge"]["ad"],
            "credentialCategory": "Ustalık / İş Yeri Açma Belgesi",
            "about": I["belge"]["dal"],
        },
        "currenciesAccepted": "TRY",
        "knowsAbout": [c["ad"] + " tamiri" for c in D.CIHAZLAR],
        "makesOffer": [
            {"@type": "Offer", "itemOffered": {"@type": "Service",
             "name": f"Batman {c['ad'].lower()} tamiri"}} for c in D.CIHAZLAR
        ],
    }


# ------------------------------------------------------------------ kabuk

IKON = {
    "tel": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 006.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.2.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 013 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.3 2.2z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.1-1.3A10 10 0 1012 2zm5.8 14.2c-.2.7-1.2 1.3-1.9 1.4-.5.1-1.2.2-3.5-.7-2.9-1.2-4.8-4.2-5-4.4-.1-.2-1.2-1.6-1.2-3s.8-2.1 1-2.4c.3-.3.6-.4.8-.4h.6c.2 0 .5 0 .7.5l.9 2.2c.1.2.1.4 0 .6l-.4.6-.3.3c-.1.2-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.4 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.2.4-.2.6-.1l2 1c.3.1.5.2.5.4.1.1.1.7-.1 1.4z"/></svg>',
    "saat": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 100 20 10 10 0 000-20zm1 10.6l3.5 2-1 1.7-4.5-2.6V6h2z"/></svg>',
    "kalkan": '<svg viewBox="0 0 24 24"><path d="M12 2l8 3.5v5.6c0 4.8-3.4 9.3-8 10.4-4.6-1.1-8-5.6-8-10.4V5.5L12 2zm-1 13.4l5.3-5.3-1.4-1.4-3.9 3.9-1.9-1.9-1.4 1.4 3.3 3.3z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 00-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 00-7-7zm0 9.5A2.5 2.5 0 1112 6a2.5 2.5 0 010 5.5z"/></svg>',
    "ok": '<svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg>',
    "okd": '<svg viewBox="0 0 24 24"><path d="M13.2 5.6l6.4 6.4-6.4 6.4-1.4-1.4 4-4H4v-2h11.8l-4-4z"/></svg>',
    "araba": '<svg viewBox="0 0 24 24"><path d="M18.9 6.5A1.5 1.5 0 0017.5 5.5h-11A1.5 1.5 0 005.1 6.5L3 12.5V20a1 1 0 001 1h1a1 1 0 001-1v-1h12v1a1 1 0 001 1h1a1 1 0 001-1v-7.5l-2.1-6zM6.5 16A1.5 1.5 0 118 14.5 1.5 1.5 0 016.5 16zm11 0a1.5 1.5 0 111.5-1.5 1.5 1.5 0 01-1.5 1.5zM5 11l1.5-4.5h11L19 11z"/></svg>',
    "arac": '<svg viewBox="0 0 24 24"><path d="M22 7h-3V5a2 2 0 00-2-2H3a1 1 0 00-1 1v12a1 1 0 001 1h1.2a2.8 2.8 0 005.6 0h4.4a2.8 2.8 0 005.6 0H22a1 1 0 001-1v-6a2 2 0 00-1-2zM7 18.5A1.5 1.5 0 118.5 17 1.5 1.5 0 017 18.5zm10 0a1.5 1.5 0 111.5-1.5 1.5 1.5 0 01-1.5 1.5zm4-5.5h-2V9h2z"/></svg>',
    "arti": '<svg viewBox="0 0 24 24"><path d="M11 5h2v6h6v2h-6v6h-2v-6H5v-2h6z"/></svg>',
}

MENU = [
    ("Cihazlar", "/#cihazlar"),
    ("Markalar", "/#markalar"),
    ("Arıza Rehberi", "/#ariza-rehberi"),
    ("Ücretler", "/#ucretler"),
    ("Bölgeler", "/#bolgeler"),
    ("İletişim", "/#iletisim"),
]


def ust_bar():
    menu = "".join(f'<a href="{u}">{k(a)}</a>' for a, u in MENU)
    return f"""<header class="ust"><div class="kap ust-ic">
<a class="logo" href="/" aria-label="Batman Beyaz Eşya Servisi ana sayfa">
<img class="logo-im" src="/images/logo/logo-180.webp"
 srcset="/images/logo/logo-120.webp 120w, /images/logo/logo-180.webp 180w, /images/logo/logo-260.webp 260w"
 sizes="64px" width="180" height="165" alt="Batman Beyaz Eşya Servisi logosu" fetchpriority="high">
<span class="logo-ad"><b>Batman Beyaz Eşya</b><span>Teknik Servis</span></span></a>
<button class="ham" id="ham" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu">
<svg viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="menu" id="menu">{menu}</nav>
<div class="ust-ara">
<a class="dg dg-wa dg-kucuk" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{IKON['wa']}<span>WhatsApp</span></a>
<a class="dg dg-ara dg-kucuk" href="tel:{I['tel_link']}">{IKON['tel']}<span>{I['tel_yazi']}</span></a>
</div></div></header>"""


def alt_bilgi():
    cihaz = "".join(f'<li><a href="/batman-{c["slug"]}-tamircisi/">{k(c["baslik"])}</a></li>'
                    for c in D.CIHAZLAR)
    marka = "".join(f'<li><a href="/batman-{m["slug"]}-servisi/">Batman {k(m["ad"])} Servisi</a></li>'
                    for m in D.MARKALAR[:6])
    bolge = "".join(f'<li><a href="/{b["slug"]}-beyaz-esya-servisi/">{k(b["ad"])}</a></li>'
                    for b in D.BOLGELER)
    return f"""<footer class="alt-bilgi"><div class="kap">
<div class="alt-izgara">
<div>
<div class="alt-logo"><img class="logo-im" src="/images/logo/logo-180.webp" width="180" height="165"
 alt="Batman Beyaz Eşya Servisi" loading="lazy"><span>{k(I['ad'])}</span></div>
<p class="alt-kunye">{k(I['adres_sokak'])}<br>{k(I['posta'])} {k(I['adres_ilce'])} / {k(I['adres_il'])}</p>
<a class="alt-tel" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a>
<p class="alt-kunye" style="margin-top:14px">Batman merkez ve tüm ilçelere beyaz eşya teknik servisi.</p>
</div>
<div><h4>Cihazlar</h4><ul class="alt-liste">{cihaz}</ul></div>
<div><h4>Markalar</h4><ul class="alt-liste">{marka}
<li><a href="/#markalar">Tüm markalar</a></li></ul></div>
<div><h4>Hizmet Bölgeleri</h4><ul class="alt-liste">{bolge}</ul></div>
</div>
<div class="telif">
<span>© 2026 {k(I['ad'])}</span>
<span>{k(I['adres_sokak'])}, {k(I['adres_ilce'])} / {k(I['adres_il'])}</span>
</div>
<div class="w4"><span class="w4-bag"><span class="w4-etiket">Web Tasarım:</span><a class="w4-ad"
 href="https://www.web4medya.com/" target="_blank" rel="noopener">Web<span class="w4-d">4</span>Medya</a></span></div>
</div></footer>
<div class="mobil-cubuk">
<a class="dg dg-wa" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp</a>
<a class="dg dg-ara" href="tel:{I['tel_link']}">{IKON['tel']}Hemen Ara</a>
</div>"""


JS = """(function(){
document.documentElement.className+=' js';
var h=document.getElementById('ham'),m=document.getElementById('menu');
if(h&&m){h.addEventListener('click',function(){var a=m.classList.toggle('acik');
h.setAttribute('aria-expanded',a);h.setAttribute('aria-label',a?'Menüyü kapat':'Menüyü aç');});
m.addEventListener('click',function(e){if(e.target.tagName==='A')m.classList.remove('acik');});}
// video: tıklanana kadar tek bayt inmez
document.querySelectorAll('.video-kutu').forEach(function(kutu){
 var d=kutu.querySelector('.oynat');if(!d)return;
 d.addEventListener('click',function(){
  var v=document.createElement('video');
  v.src=kutu.dataset.video;v.controls=true;v.autoplay=true;v.playsInline=true;v.preload='auto';
  v.style.width='100%';v.style.height='100%';v.style.objectFit='cover';
  kutu.innerHTML='';kutu.appendChild(v);
 });
});
// ortaya çıkış — uzun bloklara verilmiyor
if('IntersectionObserver'in window){
 var g=new IntersectionObserver(function(ls){ls.forEach(function(l){
  if(l.isIntersecting){l.target.classList.add('gorundu');g.unobserve(l.target);}});},
  {rootMargin:'0px 0px -60px 0px'});
 document.querySelectorAll('.gel').forEach(function(el,i){
  el.style.transitionDelay=(i%4*60)+'ms';g.observe(el);});
 setTimeout(function(){document.querySelectorAll('.gel:not(.gorundu)').forEach(function(el){
  if(el.getBoundingClientRect().top<innerHeight)el.classList.add('gorundu');});},2500);
}
})();"""


def iskelet(*, slug, baslik, aciklama, govde, semalar, kirinti_html="", og_gorsel=None):
    """slug: "" = ana sayfa, aksi hâlde "batman-buzdolabi-tamircisi" gibi."""
    url = SITE + "/" + (slug + "/" if slug else "")
    og = og_gorsel or "batman-beyaz-esya-servisi-nasil-calisir.webp"
    sema_json = json.dumps(
        {"@context": "https://schema.org", "@graph": semalar},
        ensure_ascii=False, separators=(",", ":"))
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{k(baslik)}</title>
<meta name="description" content="{k(aciklama)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="theme-color" content="#0B1F33">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{k(I['ad'])}">
<meta property="og:title" content="{k(baslik)}">
<meta property="og:description" content="{k(aciklama)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="{SITE}">
<link rel="preload" href="/assets/fonts/pjs-var-tr.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="/favicon-96.png" sizes="96x96" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/style.css{damga('assets/style.css')}">
<script>document.documentElement.className+=' js'</script>
<script type="application/ld+json">{sema_json}</script>
</head>
<body>
{ust_bar()}
{kirinti_html}
<main>
{govde}
</main>
{alt_bilgi()}
<script src="/assets/app.js{damga('assets/app.js')}" defer></script>
</body>
</html>"""


def yaz(slug, icerik):
    if slug:
        klasor = os.path.join(KOK, slug)
        os.makedirs(klasor, exist_ok=True)
        yol = os.path.join(klasor, "index.html")
    else:
        yol = os.path.join(KOK, "index.html")
    with open(yol, "w", encoding="utf-8") as f:
        f.write(icerik)
    return yol
