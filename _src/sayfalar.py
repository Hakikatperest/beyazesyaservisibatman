# -*- coding: utf-8 -*-
"""Cihaz, marka ve bölge sayfaları.

Örümcek ağı kuralı: her sayfa (a) ana sayfaya, (b) kendi cihaz/marka/bölge kardeşlerine,
(c) ilgili arıza rehberlerine bağlanır. Tek yönlü link bırakılmaz.
"""
import data as D
import arizalar as A
from build import (IKON, resim, video_kapak, sss_blok, faq_sema, yerel_isletme_sema, k, SITE, I,
                   bulunma, ayrilma, yonelme)

# --------------------------------------------------------------- ortak parçalar

def yan_kutu(baslik_liste, ust_baslik="İlgili sayfalar"):
    liste = "".join(f'<li><a href="{u}">{k(a)}</a></li>' for a, u in baslik_liste)
    return f"""<aside class="yan-kutu">
<h3>Hemen destek alın</h3>
<a class="dg dg-ara" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp</a>
<h3 style="margin-top:22px">{k(ust_baslik)}</h3>
<ul>{liste}</ul></aside>"""


def cta_kutu(nerede="Batman"):
    return f"""<div class="kutu"><b>{bulunma(k(nerede))} bize ulaşın</b>
<p>Arızayı telefonda dinleyip yaklaşık maliyeti söylüyoruz. Acil durumlarda
<strong>7 gün 24 saat</strong> ulaşabilirsiniz. Taktığımız parçalar <strong>1 yıl garantili.</strong></p>
<p><a class="dg dg-ara" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a></p></div>"""


def sure_tablosu():
    satir = "".join(f"<tr><td>{k(a)}</td><td class='ucret'>{k(s)}</td>"
                    f"<td class='aciklama'>{k(x)}</td></tr>" for a, s, x in D.SURELER)
    return (f'<div class="tbl-sar"><table><thead><tr><th scope="col">Arıza tipi</th>'
            f'<th scope="col">Süre</th><th scope="col">Örnek işler</th></tr></thead>'
            f'<tbody>{satir}</tbody></table></div>')


def belge_blok():
    bg = I["belge"]
    return f"""<div class="izgara iz-2" style="align-items:center;margin:30px 0">
<div>{resim(bg['gorsel'], 'Batman Beyaz Eşya Servisi iş yeri açma belgesi — meslek dalı Soğutma Sistemleri',
            boy="(max-width:640px) 92vw, 480px")}</div>
<div><h3>Belgeli teknik servis</h3>
<p><strong>{k(bg['ad'])}</strong> sahibiyiz. Belgedeki meslek alanı
<strong>{k(bg['alan'])}</strong>, meslek dalı ise <strong>{k(bg['dal'])}</strong>.</p>
<p>Soğutma sistemleri üzerine belgeli olmamız, buzdolabı ve derin dondurucu çağrılarını neden
sıranın önüne aldığımızı da açıklıyor: soğutma bizim asıl uzmanlık alanımız.</p>
<p>Belge, 3308 sayılı Mesleki Eğitim Kanunu gereğince <strong>ustalık belgesine tanınan bütün
hakları</strong> kapsıyor. Görselde kişisel bilgiler gizlilik gereği kapatılmıştır.</p></div>
</div>"""


# --------------------------------------------------------------- cihaz sayfaları

CIHAZ_ICERIK = {
"buzdolabi": """
<p>Buzdolabı, evdeki tek <strong>durması mümkün olmayan</strong> cihazdır. Çamaşır makinesi bir gün
bekleyebilir; duran bir buzdolabındaki gıdanın tamamı bozulur. Bu yüzden Batman'da buzdolabı
çağrılarını <strong>her zaman sıranın önüne alıyoruz.</strong></p>
<p>Soğutma sistemleri bizim belgeli uzmanlık alanımız — Millî Eğitim Bakanlığı iş yeri açma
belgemizde meslek dalı olarak <strong>"Soğutma Sistemleri"</strong> yazıyor.</p>
<h2>Buzdolabında en sık gördüğümüz arızalar</h2>
<p>Sahada gittiğimiz çağrıların büyük bölümü şu başlıklarda toplanıyor. Her birinin sebebini ve
yaklaşık maliyetini ayrı ayrı anlattık:</p>
""",
"camasir-makinesi": """
<p>Çamaşır makinesi arızaları, belirtisi birbirine en çok karışan arızalardır. "Sıkma yapmıyor"
şikâyetiyle gittiğimiz bir cihazda sorun çoğu zaman sıkmada değil, <strong>suyu boşaltamamaktadır.</strong>
Bu yüzden teşhis sırası burada doğrudan cebinize dokunuyor.</p>
<p>Batman'da çamaşır makinesi onarımlarının büyük çoğunluğunu <strong>cihazı yerinden oynatmadan,
evinizde</strong> tamamlıyoruz.</p>
<h2>Çamaşır makinesinde en sık gördüğümüz arızalar</h2>
""",
"bulasik-makinesi": """
<p>Bulaşık makinesi baştan sona suyla çalışan bir cihazdır — içinden sürekli su geçer. Bu yüzden
arızalarının çoğu <strong>su almak, su boşaltmak ve suyu doğru püskürtmek</strong> etrafında
toplanır.</p>
<p>Bir de markaya bağlı önemli bir maliyet farkı var: <strong>Bosch, Siemens ve Profilo'da rezistans
motorun içindedir</strong>, arızalandığında komple motor değişir. Arçelik, Vestel ve diğer
markalarda rezistans motorun yanındadır, ayrı değişir ve çok daha uygun olur.</p>
<h2>Bulaşık makinesinde en sık gördüğümüz arızalar</h2>
""",
"derin-dondurucu": """
<p>Derin dondurucu, içinde en yüksek değerdeki gıdanın saklandığı cihazdır — aylık, hatta yıllık
et ve sebze stoğu. Durduğunda ortaya çıkan kayıp, çoğu zaman onarım masrafının çok üzerine çıkar.
Bu yüzden dondurucu çağrılarını <strong>buzdolabıyla birlikte sıranın önüne alıyoruz.</strong></p>
<p>400, 500, 600 ve 800 litre modellerde çalışıyoruz. Cihazın litresi hem parça seçimini hem fiyatı
doğrudan etkiliyor.</p>
<h2>Derin dondurucuda en sık gördüğümüz arızalar</h2>
""",
}


def cihaz_sayfasi(c):
    ilgili = [a for a in A.ARIZALAR if a["cihaz"] == c["slug"]]
    kartlar = "".join(
        f'<a class="kart gel" href="/{a["slug"]}/"><h3>{k(a["soru"])}</h3>'
        f'<p>{k(a["kisa"])}</p><span class="devam">Oku {IKON["okd"]}</span></a>'
        for a in ilgili)
    diger = [(x["baslik"], f"/batman-{x['slug']}-tamircisi/")
             for x in D.CIHAZLAR if x["slug"] != c["slug"]]
    bolge = [(f"{b['ad']} beyaz eşya servisi", f"/{b['slug']}-beyaz-esya-servisi/")
             for b in D.BOLGELER]
    fiyat = [f for f in D.FIYATLAR
             if c["ad"].split()[0].lower() in f[0].lower() or "Servis" in f[0]]
    fsatir = "".join(f"<tr><td>{k(a)}</td><td class='ucret'>{k(u)}</td>"
                     f"<td class='aciklama'>{k(x)}</td></tr>" for a, u, x in fiyat)
    g, alt = {"buzdolabi": ("buzdolabi-motor-degisim2.webp", "Batman buzdolabı tamircisi"),
              "camasir-makinesi": ("camasir-makinesi-motor-degisimi.webp", "Batman çamaşır makinesi tamircisi"),
              "bulasik-makinesi": ("bulasik-makinesi-pervane-degisimi2.webp", "Batman bulaşık makinesi tamircisi"),
              "derin-dondurucu": ("buzmatik-ariza-tespit-ve-tamir.webp", "Batman derin dondurucu tamircisi"),
              }[c["slug"]]

    govde = f"""<section><div class="kap"><div class="yan">
<div class="metin">
<h1>{k(c['baslik'])}</h1>
{resim(g, alt, boy="(max-width:980px) 92vw, 700px", oran="4/3")}
{CIHAZ_ICERIK[c['slug']]}
</div>
{yan_kutu(diger + bolge[:3], "Diğer cihazlar ve bölgeler")}
</div></div></section>

<section class="alt"><div class="kap">
<div class="bas"><h2>{k(c['ad'])} arıza rehberi</h2>
<p>Belirtinize en yakın başlığı seçin; sebebini, çözümünü ve yaklaşık maliyetini anlattık.</p></div>
<div class="izgara iz-3">{kartlar}</div>
</div></section>

<section><div class="kap">
<div class="bas"><h2>Batman {k(c['ad_tamlama'])} tamir ücretleri</h2></div>
<div class="tbl-sar"><table><thead><tr><th scope="col">İşlem</th><th scope="col">Ücret</th>
<th scope="col">Açıklama</th></tr></thead><tbody>{fsatir}</tbody></table></div>
<p class="tbl-not">Kesin fiyat, arıza yerinde tespit edildikten sonra ve işleme başlanmadan önce
bildirilir. Onarımı yaptırırsanız çağrı ücretinde indirim uygulanır.</p>
<h2 style="margin-top:1.8em">Tamir ne kadar sürer?</h2>
{sure_tablosu()}
{cta_kutu()}
</div></section>

<section class="alt"><div class="kap">
<div class="bas"><h2>Batman'ın her yerinde {k(c['ad_tamlama'])} servisi</h2>
<p>Batman merkezde genellikle 2 saat içinde, ilçelerde en geç 1 gün içinde adresinizdeyiz.</p></div>
<div class="izgara iz-3">""" + "".join(
        f'<a class="kart gel" href="/{b["slug"]}-beyaz-esya-servisi/">'
        f'<span class="kart-ik">{IKON["pin"]}</span><h3>{k(b["ad"])}</h3>'
        f'<p>{k(c["ad"])} onarımı — {k(b["sure"])}.</p>'
        f'<span class="devam">Bölge sayfası {IKON["okd"]}</span></a>' for b in D.BOLGELER
    ) + f"""</div>
<div class="bas" style="margin-top:44px"><h2>Marka fark etmiyor</h2></div>
<div class="izgara iz-4">""" + "".join(
        f'<a class="kart gel" href="/batman-{m["slug"]}-servisi/"><h3>{k(m["ad"])}</h3>'
        f'<p>Batman {k(m["ad"])} {k(c["ad_tamlama"])} servisi.</p></a>' for m in D.MARKALAR
    ) + """</div>
</div></section>"""
    return govde


# --------------------------------------------------------------- marka sayfaları

AILE_METIN = {
"bsh": """
<h2>{ad} cihazlarda dikkat ettiğimiz nokta</h2>
<p>{ad}, bulaşık makinesi tarafında önemli bir yapı farkına sahip:
<strong>rezistans (ısıtıcı) motorun içindedir.</strong> Rezistans arızalandığında ayrı olarak
değiştirilemez, <strong>komple motor değişir.</strong> Bu da onarımı Arçelik veya Vestel gibi
markalara göre belirgin şekilde pahalı hâle getirir.</p>
<p>Bunu telefonda arızayı dinlediğimizde söylüyoruz — çünkü {ad} bir bulaşık makinesinde "makine
ısıtmıyor" şikâyeti, diğer markalardakiyle aynı maliyette değil. Sürprizle karşılaşmamanız için
maliyeti işleme başlamadan önce net veriyoruz.</p>
""",
"yerli": """
<h2>{ad} cihazlarda maliyet avantajı</h2>
<p>{ad} bulaşık makinelerinde <strong>rezistans (ısıtıcı) motorun yan tarafındadır.</strong>
Arızalandığında motorun tamamı değil, yalnızca rezistans değişir. Bu, aynı arızanın
Bosch, Siemens ve Profilo gibi markalara göre <strong>çok daha uygun</strong> çözülmesi demektir —
o markalarda rezistans motorun içinde olduğu için komple motor değişmek zorunda kalıyor.</p>
<p>Yedek parça bulunabilirliği de {ad} tarafında genelde daha rahat. Parça elimizde yoksa sipariş
edip <strong>1–2 gün içinde</strong> takıyoruz.</p>
""",
"kore": """
<h2>{ad} cihazlarda öne çıkan arızalar</h2>
<p>{ad} buzdolaplarında <strong>no-frost</strong> sistem yaygın. No-frost modellerde buzlanma
olasılığı düşüktür; buz görüyorsanız akla ilk gelen, buzu eriten
<strong>rezistansın çalışmamasıdır</strong>. Buz biriktikçe fanın önünü kapatır ve şikâyet kısa
sürede <a href="/buzdolabi-ses-yapiyor/">ses sorununa</a> dönüşür.</p>
<p>Bu markalarda elektronik kart ve fan kaynaklı arızalar da öne çıkıyor. Kart arızasında,
motoru değiştirmeden önce <strong>kartın motora çıkış verip vermediğine</strong> bakıyoruz —
bu adım atlandığında gereksiz yere kompresör masrafı çıkıyor.</p>
""",
}


def marka_sayfasi(m):
    kardes = [(f"Batman {x['ad']} Servisi", f"/batman-{x['slug']}-servisi/")
              for x in D.MARKALAR if x["slug"] != m["slug"]]
    cihaz_kart = "".join(
        f'<a class="kart gel" href="/batman-{c["slug"]}-tamircisi/"><h3>{k(m["ad"])} {k(c["ad"])}</h3>'
        f'<p>{k(c["ozet"])}</p><span class="devam">{k(c["baslik"])} {IKON["okd"]}</span></a>'
        for c in D.CIHAZLAR)
    ariza_kart = "".join(
        f'<li><a href="/{a["slug"]}/">{k(a["soru"])}</a></li>' for a in A.ARIZALAR[:10])
    ayni_grup = [x for x in D.MARKALAR if x["grup"] == m["grup"] and x["slug"] != m["slug"]]
    grup_notu = ""
    if ayni_grup:
        adlar = ", ".join(x["ad"] for x in ayni_grup)
        grup_notu = (f'<p>{k(m["ad"])}, <strong>{k(m["grup"])}</strong> çatısı altındaki '
                     f'{k(adlar)} ile aynı parça ve servis mantığını paylaşıyor; '
                     f'bu markalarda edindiğimiz tecrübe doğrudan {k(m["ad"])} cihazlarına da yansıyor.</p>')

    return f"""<section><div class="kap"><div class="yan">
<div class="metin">
<h1>Batman {k(m['ad'])} Servisi</h1>
<p>Batman merkez ve ilçelerinde <strong>{k(m['ad'])}</strong> buzdolabı, çamaşır makinesi,
bulaşık makinesi ve derin dondurucu onarımı yapıyoruz. Marka ayrımı yapmıyor, sekiz yılı aşkın
saha tecrübemizle tüm modellere bakıyoruz.</p>
{grup_notu}
<p>Batman merkezde <strong>genellikle 2 saat içinde</strong> adresinizdeyiz; Beşiri, Gercüş,
Hasankeyf, Kozluk ve Sason'a en geç 1 gün içinde geliyoruz. Acil durumlarda
<strong>7 gün 24 saat</strong> ulaşabilirsiniz.</p>
{AILE_METIN[m['aile']].format(ad=m['ad'])}
<h2>Yetkili servis mi, biz mi?</h2>
<p>Cihazınız <strong>garanti kapsamındaysa</strong> önce {k(m['ad'])} yetkili servisine gitmenizi
öneriyoruz — işlem ücretsiz olabilir ve bağımsız bir servise yaptıracağınız müdahale garantinizi
düşürebilir. <strong>Garanti süresi dolmuşsa</strong> bize gelmeniz genellikle hem daha hızlı hem
daha uygun oluyor.</p>
<h2>Parça bulunamazsa</h2>
<p>{k(m['ad'])} için gereken parça elimizde yoksa sipariş ediyor, <strong>1–2 gün içinde</strong>
takılmasını sağlıyoruz. Süreç boyunca sizi bilgilendiriyoruz. Taktığımız her parça
<strong>1 yıl garantilidir.</strong></p>
{cta_kutu()}
</div>
{yan_kutu(kardes[:8], "Diğer markalar")}
</div></div></section>

<section class="alt"><div class="kap">
<div class="bas"><h2>Batman {k(m['ad'])} servisi — baktığımız cihazlar</h2></div>
<div class="izgara iz-4">{cihaz_kart}</div>
</div></section>

<section><div class="kap"><div class="izgara iz-2" style="align-items:start">
<div><div class="bas"><h2>{k(m['ad'])} cihazlarda sık gelen arızalar</h2>
<p>Aşağıdaki rehberler marka bağımsızdır; belirtiniz hangisine uyuyorsa oradan başlayın.</p></div>
<div class="kart"><ul class="ariza-liste">{ariza_kart}</ul>
<a class="devam" href="/#ariza-rehberi">Tüm arıza rehberi {IKON['okd']}</a></div></div>
<div><div class="bas"><h2>Tamir ne kadar sürer?</h2></div>{sure_tablosu()}
<p class="tbl-not">Onarımı bize yaptırırsanız çağrı ücretinde indirim uygulanır.</p></div>
</div></div></section>"""


# --------------------------------------------------------------- bölge sayfaları

BOLGE_NOT = {
"batman-merkez": """
<p>Dükkânımız <strong>Fatih Mahallesi 3206. Sokak No:12</strong>, Batman Merkez'de. Merkez içindeki
adreslere <strong>genellikle 2 saat içinde</strong>, en kötü ihtimalle 2–3 saat içinde ulaşıyoruz
ve çoğu arızayı aynı ziyarette çözüyoruz.</p>
<p>Merkez için servis ücretimiz <strong>600 TL</strong>'dir. Bu ücret arızanın yerinde tespiti
karşılığıdır; onarımı yaptırmak istemezseniz yalnızca bunu ödersiniz.
<strong>Onarımı bize yaptırırsanız çağrı ücretinde indirim uygulanır.</strong></p>
<p>Batman'a bağlı <strong>köy adreslerinde</strong> servis ücreti 1.000 TL'dir.</p>
""",
"varsayilan": """
<p>{yon} gidiyoruz. İlçe adreslerinde varış süremiz <strong>en geç 1 gündür</strong> — merkezdeki
gibi aynı saat içinde olmuyor, ama çağrınız sıraya alınır ve bir günü geçmez.</p>
<p>{yon} giderken <strong>parçayı yanımızda götürmeye</strong> özen gösteriyoruz. Telefonda arızayı
ayrıntılı dinlememizin sebebi bu: olası parçayı önceden hazırlayıp tek ziyarette işi bitirmek,
sizi ikinci bir gün beklemekten kurtarıyor.</p>
<p>Bu yüzden {ayr} arayacaksanız cihazın <strong>markasını, modelini ve belirtiyi</strong>
mümkün olduğunca ayrıntılı anlatın. Mümkünse arızanın sesini veya görüntüsünü WhatsApp'tan
gönderin — tespiti oradan büyük ölçüde yapabiliyoruz.</p>
""",
}


def bolge_sayfasi(b):
    kardes = [(f"{x['ad']} beyaz eşya servisi", f"/{x['slug']}-beyaz-esya-servisi/")
              for x in D.BOLGELER if x["slug"] != b["slug"]]
    cihaz_kart = "".join(
        f'<a class="kart gel" href="/batman-{c["slug"]}-tamircisi/">'
        f'<h3>{k(b["ad"])} {k(c["ad"])} Tamiri</h3><p>{k(c["ozet"])}</p>'
        f'<span class="devam">{k(c["baslik"])} {IKON["okd"]}</span></a>' for c in D.CIHAZLAR)
    marka_kart = "".join(
        f'<a class="kart gel" href="/batman-{m["slug"]}-servisi/"><h3>{k(m["ad"])}</h3>'
        f'<p>{k(b["ad"])} {k(m["ad"])} beyaz eşya servisi.</p></a>' for m in D.MARKALAR)
    metin = BOLGE_NOT.get(b["slug"], BOLGE_NOT["varsayilan"]).format(
        ad=b["ad"], yon=yonelme(b["ad"]), ayr=ayrilma(b["ad"]), bul=bulunma(b["ad"]))
    ucret_sat = ("<strong>600 TL</strong> (Batman merkez)" if b["merkez_mi"]
                 else "arızayı dinledikten sonra telefonda net olarak söylüyoruz")

    return f"""<section><div class="kap"><div class="yan">
<div class="metin">
<h1>{k(b['ad'])} Beyaz Eşya Servisi</h1>
<p>{k(b['ad'])} bölgesinde buzdolabı, çamaşır makinesi, bulaşık makinesi ve derin dondurucu
onarımı yapıyoruz. Varış süremiz <strong>{k(b['sure'])}</strong>.</p>
{metin}
<h2>{bulunma(k(b['ad']))} hangi cihazlara bakıyoruz?</h2>
<p>Dört cihaz grubunda çalışıyoruz: buzdolabı, çamaşır makinesi, bulaşık makinesi ve derin
dondurucu. Marka ayrımı yapmıyoruz — Arçelik, Beko, Bosch, Siemens, Vestel, Profilo, Altus,
Regal, Samsung, LG, Grundig ve SEG dahil tüm markalara bakıyoruz.</p>
<h2>Öncelik sıramız</h2>
<p>Aynı anda birden fazla çağrı geldiğinde <strong>buzdolabı ve derin dondurucuyu her zaman öne
alıyoruz.</strong> Sebebi basit: bir çamaşır makinesi bir gün bekleyebilir, ama duran bir
buzdolabındaki gıdanın tamamı bozulur. Bu, sahada uyguladığımız gerçek sıralamadır.</p>
<h2>{k(b['ad'])} servis ücreti</h2>
<p>Servis ücretimiz {ucret_sat}. Bu ücret arızanın yerinde tespiti karşılığıdır; onarımı
yaptırmak istemezseniz yalnızca bunu ödersiniz. <strong>Onarımı bize yaptırırsanız çağrı
ücretinde indirim uygulanır.</strong> Taktığımız parçalar <strong>1 yıl garantili.</strong></p>
{cta_kutu(b['ad'])}
</div>
{yan_kutu(kardes, "Diğer hizmet bölgeleri")}
</div></div></section>

<section class="alt"><div class="kap">
<div class="bas"><h2>{bulunma(k(b['ad']))} onardığımız cihazlar</h2></div>
<div class="izgara iz-4">{cihaz_kart}</div>
<div class="bas" style="margin-top:44px"><h2>{bulunma(k(b['ad']))} baktığımız markalar</h2></div>
<div class="izgara iz-4">{marka_kart}</div>
</div></section>

<section><div class="kap">
<div class="bas"><h2>Tamir ne kadar sürer?</h2>
<p>{k(b['ad'])} adreslerinde de aynı süreler geçerli — fark yalnızca yola çıkma süresinde.</p></div>
{sure_tablosu()}
</div></section>"""
