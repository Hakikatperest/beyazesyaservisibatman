# -*- coding: utf-8 -*-
"""Logo türevleri.  python3 _src/logo.py

⚠️ Logo ŞEFFAF zeminli (RGBA). media.py'yi kullanma — o RGB'ye çevirip şeffaflığı siyaha boyar.
Üretilenler:
  images/logo/logo-{120,180,260,380}.webp   (şeffaf)
  images/logo/logo-380.png                  (yedek)
  apple-touch-icon.png  (180×180, opak zemin — iOS şeffaflığı siyah yapar)
  favicon-48.png / favicon-96.png           (kare, rozetin üst kısmından)
"""
import os
from PIL import Image

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "images", "batman-beyaz-esya-servisi-logo.png")
HEDEF = os.path.join(KOK, "images", "logo")
BOYLAR = (120, 180, 260, 380)
ZEMIN = (11, 95, 165)   # --mavi


def uret():
    os.makedirs(HEDEF, exist_ok=True)
    im = Image.open(KAYNAK).convert("RGBA")
    kutu = im.getbbox()                      # şeffaf kenar boşluğunu kırp
    if kutu:
        im = im.crop(kutu)
    g, y = im.size
    for b in BOYLAR:
        if b > g:
            continue
        yeni = im.resize((b, max(1, round(y * b / g))), Image.LANCZOS)
        yeni.save(os.path.join(HEDEF, f"logo-{b}.webp"), "WEBP",
                  quality=88, method=4, lossless=False)
    im.resize((380, max(1, round(y * 380 / g))), Image.LANCZOS).save(
        os.path.join(HEDEF, "logo-380.png"), "PNG", optimize=True)

    # --- kare ikonlar: rozetin üst %62'si (dişli + silüet + cihazlar) ---
    kare_h = int(y * 0.62)
    kare = im.crop((0, 0, g, kare_h))
    kg, ky = kare.size
    kenar = max(kg, ky)
    tuval = Image.new("RGBA", (kenar, kenar), (0, 0, 0, 0))
    tuval.paste(kare, ((kenar - kg) // 2, (kenar - ky) // 2), kare)
    for b in (48, 96, 180, 512):
        opak = Image.new("RGB", (kenar, kenar), ZEMIN)
        opak.paste(tuval, (0, 0), tuval)
        ad = "apple-touch-icon.png" if b == 180 else f"favicon-{b}.png"
        yol = os.path.join(KOK, ad)
        opak.resize((b, b), Image.LANCZOS).save(yol, "PNG", optimize=True)
    print(f"logo türevleri hazır — kaynak {g}×{y}, kırpıldı")


if __name__ == "__main__":
    uret()
