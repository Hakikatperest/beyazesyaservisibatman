# -*- coding: utf-8 -*-
"""Tüm siteyi üretir.

    python3 _src/uret.py

⛔ Kök dizindeki HTML dosyalarını ELLE DÜZENLEME — bu betik hepsini yeniden yazar.
"""
import os, re, sys, shutil, json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
import data as D
import arizalar as A
import anasayfa
import sayfalar as S

KOK = B.KOK
I = B.I
SITE = B.SITE

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0B5FA5"/>
<path fill="#fff" d="M20 14h24a4 4 0 014 4v28a4 4 0 01-4 4H20a4 4 0 01-4-4V18a4 4 0 014-4zm2 5v10h20V19H22zm0 15v11h20V34H22zm3-12h3v4h-3v-4zm0 15h3v5h-3v-5z"/>
</svg>"""


def varliklar():
    os.makedirs(os.path.join(KOK, "assets"), exist_ok=True)
    shutil.copyfile(os.path.join(KOK, "_src", "style.css"),
                    os.path.join(KOK, "assets", "style.css"))
    with open(os.path.join(KOK, "assets", "app.js"), "w", encoding="utf-8") as f:
        f.write(B.JS)
    # font @font-face — style.css başına eklenir
    yol = os.path.join(KOK, "assets", "style.css")
    with open(yol, encoding="utf-8") as f:
        css = f.read()
    if "@font-face" not in css:
        css = ("""@font-face{font-family:"Plus Jakarta Sans";
src:url("/assets/fonts/pjs-var-tr.woff2") format("woff2");
font-weight:200 800;font-style:normal;font-display:swap;
unicode-range:U+0000-00FF,U+0100-017F,U+011E-011F,U+0130-0131,U+015E-015F,U+2000-206F,U+20BA,U+2122}\n""" + css)
        with open(yol, "w", encoding="utf-8") as f:
            f.write(css)


def uret_anasayfa():
    kir, kir_sema = "", None
    B.video_sifirla()
    govde = anasayfa.govde()
    html = B.iskelet(
        slug="", baslik=anasayfa.BASLIK, aciklama=anasayfa.ACIKLAMA,
        govde=govde, semalar=anasayfa.semalar() + B.video_semalari(""),
        lcp_gorsel="batman-beyaz-esya-servisi-hero.webp")
    return [("", B.yaz("", html))]


def uret_arizalar():
    cikti = []
    cihaz_ad = {c["slug"]: c for c in D.CIHAZLAR}
    for a in A.ARIZALAR:
        c = cihaz_ad[a["cihaz"]]
        kir, kir_sema = B.kirinti([
            ("Ana Sayfa", "/"),
            (c["baslik"], f"/batman-{c['slug']}-tamircisi/"),
            (a["soru"], None),
        ])
        # ilgili arızalar (aynı cihaz)
        digerleri = [x for x in A.ARIZALAR if x["cihaz"] == a["cihaz"] and x["slug"] != a["slug"]]
        yan_liste = "".join(f'<li><a href="/{x["slug"]}/">{B.k(x["soru"])}</a></li>'
                            for x in digerleri[:8])
        B.video_sifirla()
        gorsel = B.resim(a["gorsel"], a["soru"] + " — Batman beyaz eşya servisi",
                         boy="(max-width:980px) 92vw, 700px", oran="4/3") if a.get("gorsel") else ""
        video = ""
        if a.get("video"):
            video = ('<div style="margin:26px 0;max-width:400px">'
                     + B.video_kapak(a["video"], a["poster"], a["video_etiket"]) + '</div>')

        govde = f"""<section><div class="kap"><div class="yan">
<div class="metin">
{B.h1_tel(a['soru'])}
{gorsel}
<!--ICINDEKILER-->
{a['govde']}
{video}
{B.ana_baglanti(a['slug'])}
<div class="kutu"><b>Batman'da bu arıza için bize ulaşın</b>
<p>Batman merkezde <strong>genellikle 2 saat içinde</strong> adresinizdeyiz; Beşiri, Gercüş,
Hasankeyf, Kozluk ve Sason'a en geç 1 gün içinde geliyoruz. Arızayı yerinde tespit edip maliyeti
işleme başlamadan söylüyoruz. Taktığımız parçalar <strong>1 yıl garantili.</strong></p>
<p><a class="dg dg-ara" href="tel:{I['tel_link']}">{B.IKON['tel']}{I['tel_yazi']}</a></p></div>
</div>
<aside class="yan-kutu">
{S.one_cikan_blok()}
<div class="yan-blok"><h3>{B.k(c['ad'])} arızaları</h3>
<ul>{yan_liste}</ul>
<p style="margin:14px 0 0"><a class="devam" href="/batman-{c['slug']}-tamircisi/">
{B.k(c['baslik'])} {B.IKON['okd']}</a></p></div>
<div class="yan-blok koyu"><h3>Hemen arayın</h3>
<p>7/24 acil beyaz eşya servisi — tatil ve pazar dahil.</p>
<a class="dg dg-ara" href="tel:{I['tel_link']}" style="background:#fff;color:var(--lacivert)">{B.IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="{B.WA_LINK}" rel="noopener" target="_blank">{B.IKON['wa']}WhatsApp</a>
</div></aside>
</div></div></section>
""" + B.capraz_ag(a["slug"], cihaz_slug=a["cihaz"], haric_ariza=a["slug"])

        semalar = [
            B.yerel_isletme_sema(), kir_sema,
            {"@type": "TechArticle", "@id": SITE + "/" + a["slug"] + "/#yazi",
             "headline": a["soru"],
             "description": a["kisa"],
             "author": {"@id": SITE + "/#isletme"},
             "publisher": {"@id": SITE + "/#isletme"},
             "mainEntityOfPage": {"@id": SITE + "/" + a["slug"] + "/#sayfa"},
             "image": f"{SITE}/images/{a['gorsel']}" if a.get("gorsel") else None,
             "datePublished": B.YAYIN_TARIHI, "dateModified": B.GUNCELLEME_TARIHI,
             "articleSection": c["ad"], "proficiencyLevel": "Beginner",
             "inLanguage": "tr-TR"},
        ] + B.video_semalari(a["slug"])
        html = B.iskelet(
            slug=a["slug"],
            baslik=B.baslik_kes(a["soru"]),
            aciklama=a["kisa"], govde=govde, semalar=semalar,
            kirinti_html=kir, og_gorsel=a.get("gorsel"), lcp_gorsel=a.get("gorsel"),
            sayfa_tipi="WebPage")
        cikti.append((a["slug"], B.yaz(a["slug"], html)))
    return cikti


def uret_cihazlar():
    cikti = []
    for c in D.CIHAZLAR:
        slug = f"batman-{c['slug']}-tamircisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"), (c["baslik"], None)])
        B.video_sifirla()
        govde = S.cihaz_sayfasi(c)
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "@id": SITE + "/" + slug + "/#hizmet",
                    "serviceType": f"Batman {c['ad_tamlama']} tamiri",
                    "name": c["baslik"], "description": c["ozet"],
                    "provider": {"@id": SITE + "/#isletme"},
                    "areaServed": [{"@type": "AdministrativeArea", "name": b["ad"]}
                                   for b in D.BOLGELER],
                    "offers": {"@type": "Offer", "priceCurrency": "TRY",
                               "priceSpecification": {
                                   "@type": "PriceSpecification",
                                   "price": D.SERVIS_UCRETI["merkez"], "priceCurrency": "TRY",
                                   "valueAddedTaxIncluded": True,
                                   "description": "Servis (yol) ücreti — parça ve işçilik ayrıca, "
                                                  "yerinde tespit sonrası bildirilir."},
                               "availability": "https://schema.org/InStock"},
                    "hasOfferCatalog": {
                        "@type": "OfferCatalog", "name": f"{c['ad']} arıza rehberi",
                        "itemListElement": [
                            {"@type": "Offer", "itemOffered": {
                                "@type": "Service", "name": a["soru"],
                                "url": SITE + "/" + a["slug"] + "/"}}
                            for a in A.ARIZALAR if a["cihaz"] == c["slug"]]}},
                   B.faq_sema(S.CIHAZ_SSS[c["slug"]])] + B.video_semalari(slug)
        html = B.iskelet(
            slug=slug, baslik=f"{c['baslik']} | Aynı Gün Yerinde Servis",
            aciklama=f"{c['baslik']}: {c['ozet']} Merkezde 2 saat içinde, "
                     f"1 yıl garanti. {I['tel_yazi']}",
            govde=govde, semalar=semalar, kirinti_html=kir,
            og_gorsel=S.CIHAZ_HERO[c["slug"]], lcp_gorsel=S.CIHAZ_HERO[c["slug"]])
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


def uret_markalar():
    cikti = []
    for m in D.MARKALAR:
        slug = f"batman-{m['slug']}-servisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"), (f"Batman {m['ad']} Servisi", None)])
        B.video_sifirla()
        govde = S.marka_sayfasi(m)
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "serviceType": f"Batman {m['ad']} beyaz eşya servisi",
                    "provider": {"@id": SITE + "/#isletme"},
                    "brand": {"@type": "Brand", "name": m["ad"]}},
                   B.faq_sema(S.marka_sss(m))] + B.video_semalari(slug)
        html = B.iskelet(
            slug=slug, baslik=f"Batman {m['ad']} Servisi | Beyaz Eşya Teknik Servisi",
            aciklama=f"Batman {m['ad']} servisi: buzdolabı, çamaşır ve bulaşık makinesi, derin "
                     f"dondurucu onarımı. Merkezde 2 saat içinde, 1 yıl garanti. {I['tel_yazi']}",
            govde=govde, semalar=semalar, kirinti_html=kir)
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


def uret_bolgeler():
    cikti = []
    for b in D.BOLGELER:
        slug = f"{b['slug']}-beyaz-esya-servisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"),
                                   (f"{b['ad']} Beyaz Eşya Servisi", None)])
        B.video_sifirla()
        govde = S.bolge_sayfasi(b)
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "serviceType": "Beyaz eşya teknik servisi",
                    "provider": {"@id": SITE + "/#isletme"},
                    "areaServed": {"@type": "AdministrativeArea", "name": b["ad"]}},
                   B.faq_sema(S.bolge_sss(b))] + B.video_semalari(slug)
        html = B.iskelet(
            slug=slug, baslik=B.baslik_kes(f"{b['ad']} Beyaz Eşya Servisi",
                                           ("Buzdolabı, Çamaşır ve Bulaşık Makinesi",
                                            "Aynı Gün Yerinde Servis", "Batman")),
            aciklama=f"{b['ad']} beyaz eşya servisi: buzdolabı, çamaşır ve bulaşık makinesi, "
                     f"derin dondurucu onarımı. Varış {b['sure']}. {I['tel_yazi']}",
            govde=govde, semalar=semalar, kirinti_html=kir)
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


XML_KACIS = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;"}


def xk(t):
    return "".join(XML_KACIS.get(c, c) for c in str(t))


# Sayfa tipine göre öncelik ve tazelenme sıklığı — hepsi 0.8 olması sinyali köreltiyordu.
ONCELIK = {
    "": ("1.0", "weekly"),
    "cihaz": ("0.9", "monthly"),
    "bolge": ("0.8", "monthly"),
    "ariza": ("0.7", "monthly"),
    "marka": ("0.6", "monthly"),
}


def sayfa_varliklari(dosya):
    """Yazılmış HTML'den görselleri ve JSON-LD'deki VideoObject'leri toplar."""
    h = open(dosya, encoding="utf-8").read()
    gorseller, gorulen = [], set()
    for src in re.findall(r'<img[^>]+src="(/images/[^"]+)"', h):
        tam = SITE + src
        if tam not in gorulen:
            gorulen.add(tam)
            gorseller.append(tam)
    videolar = []
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    if m:
        try:
            for n in json.loads(m.group(1))["@graph"]:
                if isinstance(n, dict) and n.get("@type") == "VideoObject":
                    videolar.append(n)
        except Exception:
            pass
    return gorseller, videolar


def tip_bul(slug):
    if slug == "":
        return ""
    if slug.endswith("-tamircisi"):
        return "cihaz"
    if slug.endswith("-beyaz-esya-servisi"):
        return "bolge"
    if slug.startswith("batman-") and slug.endswith("-servisi"):
        return "marka"
    return "ariza"


def sitemap(sayfalar):
    """Google Image + Video eklentili site haritası."""
    bugun = B.GUNCELLEME_TARIHI
    u = []
    for slug, dosya in sayfalar:
        loc = SITE + "/" + (slug + "/" if slug else "")
        oncelik, siklik = ONCELIK[tip_bul(slug)]
        gorseller, videolar = sayfa_varliklari(dosya)
        ek = ""
        for g in gorseller[:40]:          # Google sayfa başına 1.000 kabul ediyor; 40 fazlasıyla yeter
            ek += f"\n  <image:image><image:loc>{xk(g)}</image:loc></image:image>"
        for v in videolar:
            sure = v.get("duration", "")
            sn = re.sub(r"[^0-9]", "", sure) or "0"
            ek += (f"\n  <video:video>"
                   f"<video:thumbnail_loc>{xk(v['thumbnailUrl'])}</video:thumbnail_loc>"
                   f"<video:title>{xk(v['name'])}</video:title>"
                   f"<video:description>{xk(v['description'])}</video:description>"
                   f"<video:content_loc>{xk(v['contentUrl'])}</video:content_loc>"
                   f"<video:duration>{sn}</video:duration>"
                   f"<video:publication_date>{v['uploadDate']}</video:publication_date>"
                   f"<video:family_friendly>yes</video:family_friendly>"
                   f"<video:live>no</video:live>"
                   f"</video:video>")
        u.append(f"<url>\n  <loc>{loc}</loc>\n  <lastmod>{bugun}</lastmod>"
                 f"\n  <changefreq>{siklik}</changefreq>\n  <priority>{oncelik}</priority>"
                 f"{ek}\n</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
           '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"\n'
           '        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
           + "\n".join(u) + "\n</urlset>\n")
    with open(os.path.join(KOK, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    # robots.txt — YZ tarayıcılarına açık; içerik AI yanıtlarında görünsün diye bilinçli
    with open(os.path.join(KOK, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\n"
            "Allow: /\n"
            "Disallow: /_src/\n\n"
            "# Yapay zekâ tarayıcıları — içeriğin YZ yanıtlarında görünmesi için açık\n"
            "User-agent: Google-Extended\nAllow: /\n\n"
            "User-agent: GPTBot\nAllow: /\n\n"
            "User-agent: OAI-SearchBot\nAllow: /\n\n"
            "User-agent: ChatGPT-User\nAllow: /\n\n"
            "User-agent: ClaudeBot\nAllow: /\n\n"
            "User-agent: Claude-SearchBot\nAllow: /\n\n"
            "User-agent: PerplexityBot\nAllow: /\n\n"
            "User-agent: Applebot-Extended\nAllow: /\n\n"
            "User-agent: Bingbot\nAllow: /\n\n"
            "User-agent: YandexBot\nAllow: /\n\n"
            f"Sitemap: {SITE}/sitemap.xml\n")


def webmanifest():
    veri = {
        "name": I["ad"], "short_name": "Batman Beyaz Eşya",
        "description": "Batman beyaz eşya teknik servisi — buzdolabı, çamaşır makinesi, "
                       "bulaşık makinesi ve derin dondurucu onarımı.",
        "start_url": "/", "scope": "/", "display": "standalone",
        "background_color": "#FFFFFF", "theme_color": "#0E2436", "lang": "tr-TR",
        "icons": [
            {"src": "/favicon-96.png", "sizes": "96x96", "type": "image/png"},
            {"src": "/favicon-512.png", "sizes": "512x512", "type": "image/png"},
            {"src": "/favicon-512.png", "sizes": "512x512", "type": "image/png",
             "purpose": "maskable"},
        ],
    }
    with open(os.path.join(KOK, "site.webmanifest"), "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=1)


def hata_sayfasi():
    """GitHub Pages 404 — indekslenmemeli."""
    govde = f"""<section><div class="kap" style="text-align:center;max-width:680px">
<span class="etiket" style="color:var(--mavi);font-weight:800;letter-spacing:.14em">404</span>
<h1>Aradığınız sayfa bulunamadı</h1>
<p style="color:var(--gri);font-size:1.08rem">Bağlantı taşınmış veya adres yanlış yazılmış olabilir.
Aşağıdan devam edebilir ya da arızanızı doğrudan telefonda anlatabilirsiniz.</p>
<div class="cta-dgler" style="margin:30px 0 40px">
<a class="dg dg-ara" href="tel:{I['tel_link']}">{B.IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="{B.WA_LINK}" rel="noopener" target="_blank">{B.IKON['wa']}WhatsApp</a>
<a class="dg dg-bos" href="/">Ana sayfaya dön</a>
</div>
<div class="izgara iz-2" style="text-align:left">""" + "".join(
        f'<a class="kart" href="/batman-{c["slug"]}-tamircisi/"><h3>{B.k(c["baslik"])}</h3>'
        f'<p>{B.k(c["ozet"])}</p></a>' for c in D.CIHAZLAR
    ) + """</div>
</div></section>"""
    html = B.iskelet(slug="404", baslik="Sayfa bulunamadı (404) | Batman Beyaz Eşya Servisi",
                     aciklama="Aradığınız sayfa bulunamadı.", govde=govde,
                     semalar=[B.yerel_isletme_sema()])
    html = html.replace('<meta name="robots" content="index,follow,max-image-preview:large,'
                        'max-snippet:-1,max-video-preview:-1">',
                        '<meta name="robots" content="noindex,follow">')
    html = html.replace('<link rel="canonical" href="' + SITE + '/404/">', "")
    with open(os.path.join(KOK, "404.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    varliklar()
    sayfalar = []
    sayfalar += uret_anasayfa()
    sayfalar += uret_cihazlar()
    sayfalar += uret_markalar()
    sayfalar += uret_bolgeler()
    sayfalar += uret_arizalar()
    sitemap(sayfalar)
    webmanifest()
    hata_sayfasi()
    print(f"✓ {len(sayfalar)} sayfa üretildi")
    for s, _ in sayfalar:
        print("   /" + (s + "/" if s else ""))


if __name__ == "__main__":
    main()
