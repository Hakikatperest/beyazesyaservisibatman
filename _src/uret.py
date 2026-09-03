# -*- coding: utf-8 -*-
"""Tüm siteyi üretir.

    python3 _src/uret.py

⛔ Kök dizindeki HTML dosyalarını ELLE DÜZENLEME — bu betik hepsini yeniden yazar.
"""
import os, sys, shutil, json

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
    govde = anasayfa.govde()
    html = B.iskelet(
        slug="", baslik=anasayfa.BASLIK, aciklama=anasayfa.ACIKLAMA,
        govde=govde, semalar=anasayfa.semalar())
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
        gorsel = B.resim(a["gorsel"], a["soru"] + " — Batman beyaz eşya servisi",
                         boy="(max-width:980px) 92vw, 700px", oran="4/3") if a.get("gorsel") else ""
        video = ""
        if a.get("video"):
            video = ('<div style="margin:26px 0;max-width:400px">'
                     + B.video_kapak(a["video"], a["poster"], a["video_etiket"]) + '</div>')

        govde = f"""<section><div class="kap"><div class="yan">
<div class="metin">
<h1>{B.k(a['soru'])}</h1>
{gorsel}
{a['govde']}
{video}
<div class="kutu"><b>Batman'da bu arıza için bize ulaşın</b>
<p>Batman merkezde <strong>genellikle 2 saat içinde</strong> adresinizdeyiz; Beşiri, Gercüş,
Hasankeyf, Kozluk ve Sason'a en geç 1 gün içinde geliyoruz. Arızayı yerinde tespit edip maliyeti
işleme başlamadan söylüyoruz. Taktığımız parçalar <strong>1 yıl garantili.</strong></p>
<p><a class="dg dg-ara" href="tel:{I['tel_link']}">{B.IKON['tel']}{I['tel_yazi']}</a></p></div>
</div>
<aside class="yan-kutu">
<h3>Hemen destek alın</h3>
<a class="dg dg-ara" href="tel:{I['tel_link']}">{B.IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{B.IKON['wa']}WhatsApp</a>
<h3 style="margin-top:22px">{B.k(c['ad'])} arızaları</h3>
<ul>{yan_liste}</ul>
<p style="margin:14px 0 0"><a class="devam" href="/batman-{c['slug']}-tamircisi/">
{B.k(c['baslik'])} {B.IKON['okd']}</a></p>
</aside>
</div></div></section>"""

        semalar = [
            B.yerel_isletme_sema(), kir_sema,
            {"@type": "Article", "headline": a["soru"],
             "description": a["kisa"],
             "author": {"@id": SITE + "/#isletme"},
             "publisher": {"@id": SITE + "/#isletme"},
             "mainEntityOfPage": SITE + "/" + a["slug"] + "/",
             "inLanguage": "tr-TR"},
        ]
        html = B.iskelet(
            slug=a["slug"],
            baslik=f"{a['soru']} | Batman Beyaz Eşya Servisi",
            aciklama=a["kisa"], govde=govde, semalar=semalar,
            kirinti_html=kir, og_gorsel=a.get("gorsel"))
        cikti.append((a["slug"], B.yaz(a["slug"], html)))
    return cikti


def uret_cihazlar():
    cikti = []
    for c in D.CIHAZLAR:
        slug = f"batman-{c['slug']}-tamircisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"), (c["baslik"], None)])
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "serviceType": f"Batman {c['ad_tamlama']} tamiri",
                    "provider": {"@id": SITE + "/#isletme"},
                    "areaServed": [{"@type": "AdministrativeArea", "name": b["ad"]}
                                   for b in D.BOLGELER]}]
        html = B.iskelet(
            slug=slug, baslik=f"{c['baslik']} | Aynı Gün Yerinde Servis",
            aciklama=f"{c['baslik']}: {c['ozet']} Merkezde 2 saat içinde, "
                     f"1 yıl garanti. {I['tel_yazi']}",
            govde=S.cihaz_sayfasi(c), semalar=semalar, kirinti_html=kir)
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


def uret_markalar():
    cikti = []
    for m in D.MARKALAR:
        slug = f"batman-{m['slug']}-servisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"), (f"Batman {m['ad']} Servisi", None)])
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "serviceType": f"Batman {m['ad']} beyaz eşya servisi",
                    "provider": {"@id": SITE + "/#isletme"},
                    "brand": {"@type": "Brand", "name": m["ad"]}}]
        html = B.iskelet(
            slug=slug, baslik=f"Batman {m['ad']} Servisi | Beyaz Eşya Teknik Servisi",
            aciklama=f"Batman {m['ad']} servisi: buzdolabı, çamaşır ve bulaşık makinesi, derin "
                     f"dondurucu onarımı. Merkezde 2 saat içinde, 1 yıl garanti. {I['tel_yazi']}",
            govde=S.marka_sayfasi(m), semalar=semalar, kirinti_html=kir)
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


def uret_bolgeler():
    cikti = []
    for b in D.BOLGELER:
        slug = f"{b['slug']}-beyaz-esya-servisi"
        kir, kir_sema = B.kirinti([("Ana Sayfa", "/"),
                                   (f"{b['ad']} Beyaz Eşya Servisi", None)])
        semalar = [B.yerel_isletme_sema(), kir_sema,
                   {"@type": "Service", "serviceType": "Beyaz eşya teknik servisi",
                    "provider": {"@id": SITE + "/#isletme"},
                    "areaServed": {"@type": "AdministrativeArea", "name": b["ad"]}}]
        html = B.iskelet(
            slug=slug, baslik=f"{b['ad']} Beyaz Eşya Servisi | Buzdolabı, Çamaşır ve Bulaşık Makinesi",
            aciklama=f"{b['ad']} beyaz eşya servisi: buzdolabı, çamaşır ve bulaşık makinesi, "
                     f"derin dondurucu onarımı. Varış {b['sure']}. {I['tel_yazi']}",
            govde=S.bolge_sayfasi(b), semalar=semalar, kirinti_html=kir)
        cikti.append((slug, B.yaz(slug, html)))
    return cikti


def sitemap(sluglar):
    u = []
    for s in sluglar:
        loc = SITE + "/" + (s + "/" if s else "")
        oncelik = "1.0" if s == "" else "0.8"
        u.append(f"<url><loc>{loc}</loc><changefreq>weekly</changefreq>"
                 f"<priority>{oncelik}</priority></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(u) + "\n</urlset>\n")
    with open(os.path.join(KOK, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    with open(os.path.join(KOK, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /_src/\n\n"
                f"Sitemap: {SITE}/sitemap.xml\n")


def main():
    varliklar()
    sayfalar = []
    sayfalar += uret_anasayfa()
    sayfalar += uret_cihazlar()
    sayfalar += uret_markalar()
    sayfalar += uret_bolgeler()
    sayfalar += uret_arizalar()
    sitemap([s for s, _ in sayfalar])
    print(f"✓ {len(sayfalar)} sayfa üretildi")
    for s, _ in sayfalar:
        print("   /" + (s + "/" if s else ""))


if __name__ == "__main__":
    main()
