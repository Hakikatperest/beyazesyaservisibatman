# -*- coding: utf-8 -*-
"""Rebase/pull sonrası çalışma ağacını onarır.  python3 _src/onar.py

⛔ NEDEN GEREKLİ: bu depo kısmi klon (--filter=blob:none) + seyrek ödemeli.
`git rebase` / `git pull` seyrek ödeme kurallarını YENİDEN UYGULAR ve
_src/, assets/, images/w*/, images/logo/ ile 57 sayfa klasörünü çalışma
ağacından siler; üstelik skip-worktree bitini geri koyduğu için sonraki
`git add` düzenlemeleri SESSİZCE görmez. Bu betik ikisini de düzeltir.

Sıra: git rebase → python3 _src/onar.py → python3 _src/denetim.py → git add --sparse -A .
"""
import os, subprocess, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Bit temizlenecek yollar — ⛔ images/ ve video/ EKLEME, git 84 MB'ı yönetmeye kalkar.
IZLENEN = ("_src/", "assets/")


def git(*a, **kw):
    return subprocess.run(["git"] + list(a), cwd=KOK, capture_output=True, text=True, **kw)


def main():
    # 1) silinmiş kaynak dosyaları commit'ten geri al
    geri = [y for y in ("_src", "assets", "images/logo")
            if not os.path.isdir(os.path.join(KOK, y)) or not os.listdir(os.path.join(KOK, y))]
    if geri:
        print("geri alınıyor:", ", ".join(geri))
        git("checkout", "--ignore-skip-worktree-bits", "HEAD", "--", *geri)

    # 2) görsel türevleri (ağ gerekmez, Pillow ile)
    sys.path.insert(0, os.path.join(KOK, "_src"))
    import media
    media.turevleri_uret()

    # 3) sayfaları yeniden üret
    import uret
    uret.main()

    # 4) skip-worktree bitlerini temizle — yoksa git düzenlemeleri görmez
    sw = [l[2:] for l in git("ls-files", "-v").stdout.splitlines() if l.startswith("S ")]
    hedef = [f for f in sw
             if f.startswith(IZLENEN) or f.endswith("/index.html")]
    yok = [f for f in hedef if not os.path.exists(os.path.join(KOK, f))]
    if yok:
        print(f"✗ {len(yok)} dosya hâlâ diskte yok, bit temizlenmedi: {yok[:3]}")
        return 1
    for i in range(0, len(hedef), 200):
        git("update-index", "--no-skip-worktree", *hedef[i:i + 200])
    print(f"✓ {len(hedef)} dosyada skip-worktree biti temizlendi")

    d = git("status", "--porcelain").stdout.splitlines()
    print(f"✓ onarım bitti — git {len(d)} değişiklik görüyor "
          f"(0 ise rebase öncesi durumla aynısınız)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
