# -*- coding: utf-8 -*-
"""Yayın öncesi denetim.  python3 _src/denetim.py

Hata bulursa 1 döner. Commit'ten ÖNCE çalıştır.
Kontroller: kırık iç link · eksik görsel/video · yinelenen title/description ·
geçersiz JSON-LD · H1 sayısı · sayfa ağırlığı · dış kaynak · yetim sayfa ·
sessizce düşen görsel/video ·
canonical doğruluğu · title/description uzunluğu · alt metni · OG/Twitter ·
sitemap kapsaması ve lastmod · şema düğüm bütünlüğü.
"""
import os, re, sys, json, gzip
from collections import defaultdict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://beyazesyaservisibatman.com"
DIS_BEYAZ_LISTE = {"www.web4medya.com", "wa.me", "www.google.com",
                   "beyazesyaservisibatman.com"}
AGIRLIK_SINIRI = 260_000      # gzip'siz HTML
GZIP_SINIRI = 60_000

hatalar, uyarilar = [], []


def sayfalar():
    yol = os.path.join(KOK, "index.html")
    if os.path.exists(yol):
        yield "/", yol
    for ad in sorted(os.listdir(KOK)):
        d = os.path.join(KOK, ad)
        if os.path.isdir(d) and not ad.startswith((".", "_")) and ad not in (
                "images", "video", "assets"):
            f = os.path.join(d, "index.html")
            if os.path.exists(f):
                yield "/" + ad + "/", f


def main():
    sayfa = dict(sayfalar())
    url_kume = set(sayfa)
    basliklar, aciklamalar = defaultdict(list), defaultdict(list)
    gelen_link = defaultdict(set)

    for url, yol in sayfa.items():
        s = open(yol, encoding="utf-8").read()
        ham = len(s.encode()); gz = len(gzip.compress(s.encode()))
        if ham > AGIRLIK_SINIRI:
            uyarilar.append(f"{url} ağır: {ham/1000:.0f} KB")
        if gz > GZIP_SINIRI:
            uyarilar.append(f"{url} gzip ağır: {gz/1000:.0f} KB")

        t = re.search(r"<title>(.*?)</title>", s, re.S)
        if not t:
            hatalar.append(f"{url} title YOK")
        else:
            basliklar[t.group(1).strip()].append(url)
        dsc = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
        if not dsc:
            hatalar.append(f"{url} description YOK")
        else:
            v = dsc.group(1).strip()
            aciklamalar[v].append(url)
            if len(v) > 175:
                uyarilar.append(f"{url} description uzun ({len(v)} kr)")

        for y in re.findall(r"<!-- eksik [^>]*>", s):
            hatalar.append(f"{url} SESSİZ DÜŞEN VARLIK: {y}")

        h1 = re.findall(r"<h1[ >]", s)
        if len(h1) != 1:
            hatalar.append(f"{url} H1 sayısı {len(h1)} (1 olmalı)")

        # canonical gerçekten bu sayfayı mı gösteriyor?
        c = re.search(r'<link rel="canonical" href="([^"]+)"', s)
        if c:
            bekle = SITE + url
            if c.group(1) != bekle:
                hatalar.append(f"{url} canonical yanlış: {c.group(1)} (beklenen {bekle})")

        # title uzunluğu — SERP'te ~60 karakterde kesiliyor
        if t:
            tv = t.group(1).strip()
            if len(tv) > 70:
                uyarilar.append(f"{url} title uzun ({len(tv)} kr)")
            if len(tv) < 20:
                hatalar.append(f"{url} title çok kısa ({len(tv)} kr)")
        if dsc and len(dsc.group(1).strip()) < 70:
            uyarilar.append(f"{url} description kısa ({len(dsc.group(1).strip())} kr)")

        # görsellerde alt metni
        for etiket in re.findall(r"<img[^>]*>", s):
            al = re.search(r'alt="([^"]*)"', etiket)
            if al is None:
                hatalar.append(f"{url} alt ÖZNİTELİĞİ olmayan <img>")
            elif not al.group(1).strip():
                uyarilar.append(f"{url} boş alt metni")
            if 'width=' not in etiket or 'height=' not in etiket:
                uyarilar.append(f"{url} ölçüsüz <img> (CLS riski)")

        # sosyal etiketler
        for etiket in ("og:title", "og:description", "og:image", "og:url", "twitter:card"):
            if f'"{etiket}"' not in s:
                hatalar.append(f"{url} {etiket} yok")

        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        if not m:
            hatalar.append(f"{url} JSON-LD yok")
        else:
            try:
                g = json.loads(m.group(1))["@graph"]
                tipler = set()
                for n in g:
                    tp = n.get("@type")
                    tipler.update(tp if isinstance(tp, list) else [tp])
                if "WebPage" not in tipler:
                    hatalar.append(f"{url} WebPage düğümü yok")
                if "LocalBusiness" not in tipler:
                    hatalar.append(f"{url} LocalBusiness düğümü yok")
                if url != "/" and "BreadcrumbList" not in tipler:
                    hatalar.append(f"{url} BreadcrumbList yok")
                for n in g:
                    if n.get("@type") == "VideoObject":
                        for alan in ("name", "description", "thumbnailUrl",
                                     "contentUrl", "uploadDate"):
                            if not n.get(alan):
                                hatalar.append(f"{url} VideoObject eksik alan: {alan}")
            except Exception as e:
                hatalar.append(f"{url} JSON-LD geçersiz: {e}")

        if not re.search(r'<link rel="canonical"', s):
            hatalar.append(f"{url} canonical yok")

        # iç linkler
        for href in re.findall(r'href="(/[^"#?]*)"', s):
            if href.startswith(("/assets/", "/images/", "/video/")) or href.endswith(
                    (".png", ".webp", ".xml", ".txt", ".pdf", ".mp4", ".woff2",
                     ".webmanifest", ".ico", ".svg", ".json", ".html")):
                hedef = os.path.join(KOK, href.lstrip("/"))
                if not os.path.exists(hedef):
                    hatalar.append(f"{url} → eksik dosya {href}")
                continue
            if href not in url_kume:
                hatalar.append(f"{url} → KIRIK LİNK {href}")
            elif href != url:
                gelen_link[href].add(url)

        # görsel / video varlığı
        for src in re.findall(r'src="(/(?:images|video)/[^"]+)"', s):
            if not os.path.exists(os.path.join(KOK, src.lstrip("/"))):
                hatalar.append(f"{url} → eksik varlık {src}")
        for sset in re.findall(r'srcset="([^"]+)"', s):
            for parca in sset.split(","):
                p = parca.strip().split(" ")[0]
                if p.startswith("/") and not os.path.exists(os.path.join(KOK, p.lstrip("/"))):
                    hatalar.append(f"{url} → srcset eksik {p}")
        for dv in re.findall(r'data-video="(/video/[^"]+)"', s):
            if not os.path.exists(os.path.join(KOK, dv.lstrip("/"))):
                hatalar.append(f"{url} → eksik video {dv}")

        # dış kaynak
        for host in re.findall(r'(?:src|href)="https?://([^/"]+)', s):
            if host not in DIS_BEYAZ_LISTE:
                hatalar.append(f"{url} → beyaz listede olmayan dış kaynak: {host}")

    for b, u in basliklar.items():
        if len(u) > 1:
            hatalar.append(f"YİNELENEN title: {b!r} → {u}")
    for a, u in aciklamalar.items():
        if len(u) > 1:
            hatalar.append(f"YİNELENEN description → {u}")

    # --- site haritası: her sayfa var mı, lastmod düşmüş mü, fazlalık var mı
    sm_yol = os.path.join(KOK, "sitemap.xml")
    if not os.path.exists(sm_yol):
        hatalar.append("sitemap.xml YOK")
    else:
        sm = open(sm_yol, encoding="utf-8").read()
        loclar = set(re.findall(r"<loc>([^<]+)</loc>", sm))
        for u in url_kume:
            if SITE + u not in loclar:
                hatalar.append(f"sitemap'te eksik: {u}")
        for l in loclar:
            if l.replace(SITE, "") not in url_kume:
                hatalar.append(f"sitemap'te olmayan sayfa: {l}")
        if sm.count("<lastmod>") != len(loclar):
            hatalar.append("sitemap: her URL'de lastmod yok")
        if "sitemap-image" not in sm:
            uyarilar.append("sitemap: görsel eklentisi yok")
        if "sitemap-video" not in sm:
            uyarilar.append("sitemap: video eklentisi yok")

    for gerekli in ("robots.txt", "404.html", "site.webmanifest", "CNAME", ".nojekyll"):
        if not os.path.exists(os.path.join(KOK, gerekli)):
            hatalar.append(f"kök dosya eksik: {gerekli}")
    rb = os.path.join(KOK, "robots.txt")
    if os.path.exists(rb) and "Sitemap:" not in open(rb, encoding="utf-8").read():
        hatalar.append("robots.txt içinde Sitemap satırı yok")

    # yetim sayfa (ana sayfa hariç iç linki olmayan)
    for u in url_kume:
        if u != "/" and not gelen_link[u]:
            hatalar.append(f"YETİM SAYFA (hiç iç link almıyor): {u}")

    print(f"sayfa: {len(sayfa)}")
    if uyarilar:
        print(f"\n⚠ {len(uyarilar)} uyarı")
        for x in uyarilar[:20]:
            print("   " + x)
    if hatalar:
        print(f"\n✗ {len(hatalar)} HATA")
        for x in hatalar[:40]:
            print("   " + x)
        return 1
    print("\n✓ tüm denetimler geçti")
    return 0


if __name__ == "__main__":
    sys.exit(main())
