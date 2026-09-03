# -*- coding: utf-8 -*-
"""Görsel türevleri üretir: images/w<genişlik>/<ad>.webp

Yalnızca images/ içine yeni dosya eklendiğinde çalıştır:
    python3 _src/media.py

⚠️ cwebp KULLANMA — varsayılan ayarı görsel başına saniyeler yiyor ve dosyayı büyütüyor.
Pillow ile üretiliyor (seyrannakliyat'taki aynı karar).
"""
import os, sys
from PIL import Image, ImageOps

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "images")
GENISLIKLER = (420, 640, 900, 1280)
KALITE = 78


def turevleri_uret(zorla=False):
    if not os.path.isdir(KAYNAK):
        print("images/ yok"); return
    uretilen = atlanan = 0
    for ad in sorted(os.listdir(KAYNAK)):
        if not ad.lower().endswith(".webp"):
            continue
        kaynak_yol = os.path.join(KAYNAK, ad)
        if not os.path.isfile(kaynak_yol):
            continue
        try:
            with Image.open(kaynak_yol) as im:
                im = ImageOps.exif_transpose(im)      # EXIF yön tuzağı
                im = im.convert("RGB")
                asil_g = im.width
                for g in GENISLIKLER:
                    if g >= asil_g:
                        continue                      # büyütme yok
                    klasor = os.path.join(KAYNAK, f"w{g}")
                    os.makedirs(klasor, exist_ok=True)
                    hedef = os.path.join(klasor, ad)
                    if os.path.exists(hedef) and not zorla:
                        atlanan += 1
                        continue
                    oran = g / asil_g
                    yeni = im.resize((g, max(1, round(im.height * oran))), Image.LANCZOS)
                    yeni.save(hedef, "WEBP", quality=KALITE, method=4)
                    uretilen += 1
        except Exception as e:
            print(f"  ! {ad}: {e}")
    print(f"türev: {uretilen} üretildi, {atlanan} zaten vardı")


def olcu(ad):
    """Kaynak görselin (genişlik, yükseklik) ölçüsü — CLS önlemek için."""
    yol = os.path.join(KAYNAK, ad)
    try:
        with Image.open(yol) as im:
            im = ImageOps.exif_transpose(im)
            return im.size
    except Exception:
        return (1200, 1600)


if __name__ == "__main__":
    turevleri_uret(zorla="--zorla" in sys.argv)
