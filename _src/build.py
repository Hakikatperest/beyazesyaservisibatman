# -*- coding: utf-8 -*-
"""Batman Beyaz Eşya Servisi — site üreticisi.

    python3 _src/build.py

⛔ Kök dizindeki HTML dosyalarını ELLE DÜZENLEME — bu betik hepsini yeniden yazar.
"""
import os, re, json, html, hashlib, shutil, struct, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data as D
import arizalar as A
import media

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
I = D.ISLETME
SITE = D.SITE
# WhatsApp'a hazır mesajla giriş — dönüşümü artırır, kullanıcı boş ekrana bakmaz
# ⛔ batman-beyaz-esya-servisi-nasil-calisir.webp KULLANILMIYOR: o afişteki telefon
#    (0554 166 25 72) sitedeki numaradan farklı. Yerine 2026-09-03'te yüklenen,
#    doğru numarayı (0553 711 83 21) taşıyan hero afişi kullanılıyor.
VARSAYILAN_OG = "batman-beyaz-esya-servisi-hero.webp"

YAYIN_TARIHI = "2026-09-03"
GUNCELLEME_TARIHI = os.environ.get("SITE_TARIHI") or __import__("datetime").date.today().isoformat()

WA_LINK = ("https://wa.me/" + I["wa"] +
           "?text=Merhaba%2C%20Batman%20Beyaz%20E%C5%9Fya%20Servisi%27nden%20"
           "ar%C4%B1za%20i%C3%A7in%20yaz%C4%B1yorum.")

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


def h1_tel(baslik, sinif=""):
    """İç sayfa H1'i + tıklanabilir telefon satırı (kullanıcı isteği, 2026-09-03)."""
    return (f'<h1 class="h1-tel {sinif}">{k(baslik)}'
            f'<a href="tel:{I["tel_link"]}" aria-label="Telefonla ara: {I["tel_yazi"]}">'
            f'{IKON["tel"]}{I["tel_yazi"]}</a></h1>')


def baslik_kes(ana, ekler=("Batman Beyaz Eşya Servisi", "Batman Servisi"), sinir=65):
    """SERP ~60-65 karakterde kesiyor. Marka eki sığmıyorsa kısaltır, yine sığmazsa düşürür."""
    for ek in ekler:
        aday = f"{ana} | {ek}"
        if len(aday) <= sinir:
            return aday
    return ana


def turevler(ad):
    """srcset dizesi — <link rel=preload imagesrcset> için."""
    kaynak = os.path.join(KOK, "images", ad)
    if not os.path.exists(kaynak):
        return ""
    g, _ = media.olcu(ad)
    setler = [f"/images/w{w}/{ad} {w}w" for w in media.GENISLIKLER
              if os.path.exists(os.path.join(KOK, "images", f"w{w}", ad))]
    setler.append(f"/images/{ad} {g}w")
    return ", ".join(setler)


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
    # ⛔ KIRPMA YOK (kullanıcı kararı 2026-09-03): görselin tamamı görünmeli.
    # Dikey fotoğraflar sayfayı ele geçirmesin diye .dikey sınıfıyla genişlik sınırlanıyor.
    stil = ' style="height:auto"'
    if y > g * 1.15:
        sinif = (sinif + " dikey").strip()
    return (
        f'<picture class="{sinif}">'
        f'<img src="/images/{ad}" srcset="{", ".join(setler)}" sizes="{boy}" '
        f'width="{g}" height="{y}" alt="{k(alt)}" {yukleme}{stil}>'
        f'</picture>'
    )


# --- video: kapak + VideoObject şeması --------------------------------------
# Çekim tarihleri bilinmiyor; depoya yüklendikleri gün kullanılıyor (uydurma tarih YOK).
VIDEO_TARIHI = "2026-09-03"

# Sayfa üretilirken o sayfaya konan videolar burada birikir; iskelet çağrılmadan
# önce video_semalari() ile alınır. uret.py her sayfadan önce video_sifirla() çağırır.
_SAYFA_VIDEO = []


def video_sifirla():
    _SAYFA_VIDEO.clear()


def mp4_sure(video_ad):
    """MP4 mvhd atomundan süre (saniye). ffprobe yok, başlığın ilk 4 KB'ı yetiyor."""
    yol = os.path.join(KOK, "video", video_ad)
    try:
        with open(yol, "rb") as f:
            veri = f.read(4096)
        i = veri.find(b"mvhd")
        if i < 0:
            return None
        p = i + 4
        surum = veri[p]
        p += 4
        if surum == 1:
            p += 16
            olcek = struct.unpack(">I", veri[p:p + 4])[0]; p += 4
            sure = struct.unpack(">Q", veri[p:p + 8])[0]
        else:
            p += 8
            olcek = struct.unpack(">I", veri[p:p + 4])[0]; p += 4
            sure = struct.unpack(">I", veri[p:p + 4])[0]
        return sure / olcek if olcek else None
    except Exception:
        return None


def video_semalari(slug):
    """O sayfaya yerleşen videoların VideoObject listesi."""
    url = SITE + "/" + (slug + "/" if slug else "")
    liste = []
    for video_ad, poster, etiket, aciklama in _SAYFA_VIDEO:
        s = {
            "@type": "VideoObject",
            "name": etiket + " — Batman Beyaz Eşya Servisi",
            "description": aciklama,
            "thumbnailUrl": SITE + poster,
            "contentUrl": f"{SITE}/video/{video_ad}",
            "uploadDate": VIDEO_TARIHI,
            "inLanguage": "tr-TR",
            "isFamilyFriendly": True,
            "publisher": {"@id": SITE + "/#isletme"},
            "contentLocation": {"@type": "Place", "name": "Batman"},
            "mainEntityOfPage": url,
        }
        sn = mp4_sure(video_ad)
        if sn:
            s["duration"] = "PT%dS" % round(sn)
        liste.append(s)
    return liste


def video_kapak(video_ad, poster_ad, etiket, dikey=True, aciklama=None):
    """Tıklanana kadar TEK BAYT inmeyen video kapağı. 84 MB video var — asla otomatik yükleme."""
    if not os.path.exists(os.path.join(KOK, "video", video_ad)):
        return f"<!-- eksik video: {video_ad} -->"
    poster = f"/images/w640/{poster_ad}" if os.path.exists(
        os.path.join(KOK, "images", "w640", poster_ad)) else f"/images/{poster_ad}"
    pg, py = media.olcu(poster_ad)
    oran_stil = f' style="aspect-ratio:{pg}/{py}"'   # kutu posterin oranını alır
    _SAYFA_VIDEO.append((video_ad, poster, etiket,
                         aciklama or (etiket + " — Batman'da kendi yaptığımız onarımdan "
                                      "çekilmiş saha görüntüsü.")))
    return (
        f'<div class="video-kutu{" dikey" if dikey else ""}"{oran_stil} data-video="/video/{video_ad}">'
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
    son = yol_listesi[-1][1] or ""
    return nav, {"@type": "BreadcrumbList", "itemListElement": sema}


# ------------------------------------------------------------------ şema

def web_site_sema():
    return {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/",
            "name": I["ad"], "inLanguage": "tr-TR",
            "publisher": {"@id": SITE + "/#isletme"}}


def yerel_isletme_sema():
    return {
        "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
        "@id": SITE + "/#isletme",
        "name": I["ad"],
        "url": SITE + "/",
        "telephone": [I["tel_link"], I["tel2_link"]],
        "image": SITE + "/images/" + VARSAYILAN_OG,
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
        "paymentAccepted": "Nakit, Kredi Kartı, Havale/EFT",
        "description": ("Batman merkez ve ilçelerinde buzdolabı, çamaşır makinesi, bulaşık "
                        "makinesi ve derin dondurucu onarımı yapan beyaz eşya teknik servisi. "
                        "Aynı gün yerinde servis, 1 yıl parça garantisi."),
        "slogan": "Önce teşhis, sonra fiyat.",
        "sameAs": [I["maps"]],
        "numberOfEmployees": {"@type": "QuantitativeValue", "minValue": 1},
        "knowsAbout": [c["ad"] + " tamiri" for c in D.CIHAZLAR],
        "makesOffer": [
            {"@type": "Offer",
             "itemOffered": {"@type": "Service", "name": f"Batman {c['ad'].lower()} tamiri",
                             "serviceType": f"{c['ad']} tamiri", "provider": {"@id": SITE + "/#isletme"}},
             "areaServed": [{"@type": "AdministrativeArea", "name": b["ad"]} for b in D.BOLGELER],
             "availability": "https://schema.org/InStock"} for c in D.CIHAZLAR
        ] + [
            {"@type": "Offer", "name": "Servis (yol) ücreti — Batman merkez ve ilçeler",
             "description": "Arızanın yerinde tespiti karşılığıdır; ilçelere ayrı yol ücreti alınmaz.",
             "priceSpecification": {"@type": "PriceSpecification",
                                    "price": D.SERVIS_UCRETI["merkez"], "priceCurrency": "TRY"}},
            {"@type": "Offer", "name": "Servis (yol) ücreti — Batman köyleri",
             "priceSpecification": {"@type": "PriceSpecification",
                                    "price": D.SERVIS_UCRETI["koy"], "priceCurrency": "TRY"}},
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
    "posta": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 00-2 2v12a2 2 0 002 2h16a2 2 0 002-2V6a2 2 0 00-2-2zm0 4l-8 5-8-5V6l8 5 8-5z"/></svg>',
    "anahtar": '<svg viewBox="0 0 24 24"><path d="M21.7 5.6l-3.4 3.4-2.3-2.3 3.4-3.4a6 6 0 00-7.7 7.3L3 19.3 4.7 21l8.7-8.7a6 6 0 007.3-7.7z"/></svg>',
    "simsek": '<svg viewBox="0 0 24 24"><path d="M13 2L4.5 13.5H11l-1 8.5 8.5-11.5H12z"/></svg>',
    "kamera": '<svg viewBox="0 0 24 24"><path d="M17 10.5V7a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h12a1 1 0 001-1v-3.5l4 3.5V7z"/></svg>',
    "belge": '<svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8l-6-6zm-1 7V3.5L18.5 9H13z"/></svg>',
    "kar": '<svg viewBox="0 0 24 24"><path d="M11 2h2v4.6l2.6-2.6 1.4 1.4L13 9.4v2.1l1.8-1 1.9-3.3 1.9.5-1.1 1.9 2.6-.7.5 1.9-2.6.7 1.4 1.6-1.6 1.1-2.3-2.7-1.8 1 1.8 1-.1 3.3-1.9.5-.5-2.1-2.6 1.5v3l-1 1-1-1v-3L6.8 16l-.5 2.1-1.9-.5-.1-3.3 1.8-1-1.8-1-2.3 2.7L.4 14l1.4-1.6-2.6-.7.5-1.9 2.6.7L1.2 8.6l1.9-.5 1.9 3.3 1.8 1V10.3L2.9 5.4l1.4-1.4L11 6.6z"/></svg>',
}

MENU = [
    ("Cihazlar", "/#cihazlar"),
    ("Markalar", "/#markalar"),
    ("Arıza Rehberi", "/#ariza-rehberi"),
    ("Galeri", "/#galeri"),
    ("Ücretler", "/#ucretler"),
    ("Bölgeler", "/#bolgeler"),
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
<nav class="menu" id="menu" aria-label="Ana menü">{menu}</nav>
<div class="ust-ara">
<a class="tel-kart" href="tel:{I['tel_link']}" aria-label="Telefonla ara: {I['tel_yazi']}">
<i>{IKON['tel']}</i><span><em>7/24 Acil Servis</em><b>{I['tel_yazi']}</b></span></a>
<a class="dg dg-wa dg-kucuk" href="{WA_LINK}" rel="noopener" target="_blank">{IKON['wa']}<span>WhatsApp</span></a>
</div></div></header>"""


def yuzen_iletisim():
    """Sağ kenarda sabit duran hızlı iletişim kartı (geniş ekran)."""
    return f"""<aside class="yuzen" aria-label="Hızlı iletişim">
<a class="dg dg-ara dg-kucuk" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-ara dg-kucuk" href="tel:{I['tel2_link']}">{IKON['tel']}{I['tel2_yazi']}</a>
<a class="dg dg-wa dg-kucuk" href="{WA_LINK}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp</a>
</aside>"""


def alt_bilgi():
    cihaz = "".join(f'<li><a href="/batman-{c["slug"]}-tamircisi/">{k(c["baslik"])}</a></li>'
                    for c in D.CIHAZLAR)
    marka = "".join(f'<li><a href="/batman-{m["slug"]}-servisi/">Batman {k(m["ad"])} Servisi</a></li>'
                    for m in D.MARKALAR[:5])
    bolge = "".join(f'<li><a href="/{b["slug"]}-beyaz-esya-servisi/">{k(b["ad"])} Beyaz Eşya Servisi</a></li>'
                    for b in D.BOLGELER)
    return f"""<footer class="alt-bilgi">
<div class="alt-ust"><div class="kap">
<b>{k(I['ad'])} — 7/24 acil beyaz eşya teknik servisi</b>
<a class="dg dg-wa dg-kucuk" href="{WA_LINK}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp'tan yaz</a>
</div></div>
<div class="kap">
<div class="alt-izgara">
<div>
<div class="alt-logo"><img class="logo-im" src="/images/logo/logo-180.webp" width="180" height="165"
 alt="Batman Beyaz Eşya Servisi" loading="lazy" decoding="async"><span>{k(I['ad'])}</span></div>
<p class="alt-kunye">Batman merkez ve tüm ilçelerde buzdolabı, çamaşır makinesi, bulaşık makinesi
ve derin dondurucu onarımı. Sekiz yılı aşkın saha tecrübesi, 1 yıl parça garantisi.</p>
<p style="margin-top:18px"><a class="dg dg-ara dg-kucuk" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a></p>
</div>
<div><h4>Cihazlar</h4><ul class="alt-liste">{cihaz}</ul></div>
<div><h4>Markalar</h4><ul class="alt-liste">{marka}
<li><a href="/#markalar">Tüm markalar</a></li></ul></div>
<div><h4>İletişim</h4>
<ul class="alt-iletisim">
<li><i>{IKON['pin']}</i><span><em>Adres</em><b>{k(I['adres_sokak'])}<br>{k(I['posta'])} {k(I['adres_ilce'])} / {k(I['adres_il'])}</b></span></li>
<li><i>{IKON['tel']}</i><span><em>Telefon &amp; WhatsApp</em>
<b><a href="tel:{I['tel_link']}">{I['tel_yazi']}</a></b>
<b><a href="tel:{I['tel2_link']}">{I['tel2_yazi']}</a></b></span></li>
<li><i>{IKON['saat']}</i><span><em>Çalışma saatleri</em><b>7 gün 24 saat — tatil ve pazar dahil</b></span></li>
</ul>
</div>
</div>
<div class="alt-izgara" style="padding-top:0;grid-template-columns:1fr">
<div><h4>Hizmet Bölgeleri</h4><ul class="alt-liste"
 style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0 20px">{bolge}</ul></div>
</div>
<div class="telif">
<span>© 2026 {k(I['ad'])}. Tüm hakları saklıdır.</span>
<nav aria-label="Alt bilgi bağlantıları">
<a href="/">Ana Sayfa</a><a href="/#ariza-rehberi">Arıza Rehberi</a>
<a href="/#ucretler">Ücretler</a><a href="/sitemap.xml">Site Haritası</a>
</nav>
</div>
<div class="w4"><span class="w4-bag"><span class="w4-etiket">Web Tasarım:</span><a class="w4-ad"
 href="https://www.web4medya.com/" target="_blank" rel="noopener">Web<span class="w4-d">4</span>Medya</a></span></div>
</div></footer>
<div class="mobil-cubuk">
<a class="dg dg-wa" href="{WA_LINK}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp</a>
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
// alt bilgi görünürken yüzen kart çekilsin — footer linklerini örtmesin
var yz=document.querySelector('.yuzen'),ab=document.querySelector('.alt-bilgi');
if(yz&&ab&&'IntersectionObserver'in window){
 new IntersectionObserver(function(ls){
  yz.classList.toggle('gizli',ls[0].isIntersecting);
 },{threshold:0}).observe(ab);
}
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


def iskelet(*, slug, baslik, aciklama, govde, semalar, kirinti_html="",
            og_gorsel=None, lcp_gorsel=None, sayfa_tipi="WebPage"):
    """slug: "" = ana sayfa, aksi hâlde "batman-buzdolabi-tamircisi" gibi."""
    url = SITE + "/" + (slug + "/" if slug else "")
    og = og_gorsel or VARSAYILAN_OG
    og_boy = media.olcu(og) or (1200, 900)

    # WebPage düğümü: her sayfaya tazelik + sahiplik sinyali
    sayfa = {
        "@type": sayfa_tipi,
        "@id": url + "#sayfa",
        "url": url,
        "name": baslik,
        "description": aciklama,
        "inLanguage": "tr-TR",
        "isPartOf": {"@id": SITE + "/#site"},
        "about": {"@id": SITE + "/#isletme"},
        "primaryImageOfPage": {"@type": "ImageObject", "url": f"{SITE}/images/{og}",
                               "width": og_boy[0], "height": og_boy[1]},
        "datePublished": YAYIN_TARIHI,
        "dateModified": GUNCELLEME_TARIHI,
    }
    for n in semalar:
        if isinstance(n, dict) and n.get("@type") == "BreadcrumbList":
            sayfa["breadcrumb"] = {"@id": n["@id"]} if "@id" in n else n
            break
    varsa = {n.get("@id") for n in semalar if isinstance(n, dict)}
    on = [sayfa] if SITE + "/#site" in varsa else [sayfa, web_site_sema()]
    semalar = on + [n for n in semalar if n]

    def temiz(x):
        """null alanları grafikten düşür — geçersiz değil ama gürültü."""
        if isinstance(x, dict):
            return {a: temiz(v) for a, v in x.items() if v is not None}
        if isinstance(x, list):
            return [temiz(v) for v in x if v is not None]
        return x

    sema_json = json.dumps(
        {"@context": "https://schema.org", "@graph": temiz(semalar)},
        ensure_ascii=False, separators=(",", ":"))

    on_yukle = ""
    if lcp_gorsel:
        t = turevler(lcp_gorsel)
        if t:
            on_yukle = (f'\n<link rel="preload" as="image" href="/images/{lcp_gorsel}"'
                        f' imagesrcset="{t}" imagesizes="(max-width:900px) 92vw, 46vw"'
                        f' fetchpriority="high">')

    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{k(baslik)}</title>
<meta name="description" content="{k(aciklama)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="author" content="{k(I['ad'])}">
<meta name="theme-color" content="#0E2436">
<meta name="geo.region" content="TR-72">
<meta name="geo.placename" content="Batman">
<meta name="geo.position" content="{I['lat']};{I['lng']}">
<meta name="ICBM" content="{I['lat']}, {I['lng']}">
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="{k(I['ad'])}">
<meta property="og:title" content="{k(baslik)}">
<meta property="og:description" content="{k(aciklama)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{og}">
<meta property="og:image:width" content="{og_boy[0]}">
<meta property="og:image:height" content="{og_boy[1]}">
<meta property="og:image:alt" content="{k(baslik)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{k(baslik)}">
<meta name="twitter:description" content="{k(aciklama)}">
<meta name="twitter:image" content="{SITE}/images/{og}">
<link rel="preload" href="/assets/fonts/pjs-var-tr.woff2" as="font" type="font/woff2" crossorigin>{on_yukle}
<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">
<link rel="icon" href="/favicon-96.png" sizes="96x96" type="image/png">
<link rel="icon" href="/favicon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<link rel="stylesheet" href="/assets/style.css{damga('assets/style.css')}">
<script>document.documentElement.className+=' js'</script>
<script type="application/ld+json">{sema_json}</script>
</head>
<body>
{ust_bar()}
{kirinti_html}
<main id="icerik">
{govde}
</main>
{yuzen_iletisim()}
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
