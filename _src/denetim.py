# -*- coding: utf-8 -*-
"""Yayın öncesi denetim.  python3 _src/denetim.py

Hata bulursa 1 döner. Commit'ten ÖNCE çalıştır.
Kontroller: kırık iç link · eksik görsel/video · yinelenen title/description ·
geçersiz JSON-LD · H1 sayısı · sayfa ağırlığı · dış kaynak · yetim sayfa.
"""
import os, re, sys, json, gzip
from collections import defaultdict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

        h1 = re.findall(r"<h1[ >]", s)
        if len(h1) != 1:
            hatalar.append(f"{url} H1 sayısı {len(h1)} (1 olmalı)")

        m = re.search(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
        if not m:
            hatalar.append(f"{url} JSON-LD yok")
        else:
            try:
                json.loads(m.group(1))
            except Exception as e:
                hatalar.append(f"{url} JSON-LD geçersiz: {e}")

        if not re.search(r'<link rel="canonical"', s):
            hatalar.append(f"{url} canonical yok")

        # iç linkler
        for href in re.findall(r'href="(/[^"#?]*)"', s):
            if href.startswith(("/assets/", "/images/", "/video/")) or href.endswith(
                    (".png", ".webp", ".xml", ".txt", ".pdf", ".mp4", ".woff2")):
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
