# -*- coding: utf-8 -*-
"""Ana sayfa gövdesi. H2 sıralaması işletmenin verdiği plana birebir uyar."""

import data as D
import arizalar as A
from build import (IKON, resim, video_kapak, sss_blok, faq_sema,
                   yerel_isletme_sema, k, SITE, I)
from sayfalar import belge_blok

CIHAZ_GORSEL = {
    "buzdolabi": ("buzdolabi-motor-degisim.webp", "Batman'da buzdolabı kompresör değişimi"),
    "camasir-makinesi": ("camasir-makinesi-motor-degisimi.webp", "Batman'da çamaşır makinesi motor değişimi"),
    "bulasik-makinesi": ("bulasik-makinesi-pervane-degisimi.webp", "Batman'da bulaşık makinesi pervane değişimi"),
    "derin-dondurucu": ("buzmatik-ariza-tespit.webp", "Batman'da derin dondurucu arıza tespiti"),
}


def _cihaz_kartlari():
    kartlar = []
    for c in D.CIHAZLAR:
        g, alt = CIHAZ_GORSEL[c["slug"]]
        kartlar.append(f"""<a class="kart cihaz-kart gel" href="/batman-{c['slug']}-tamircisi/">
<span class="gorsel">{resim(g, alt, boy="(max-width:640px) 92vw, (max-width:980px) 45vw, 270px")}</span>
<span class="govde"><h3>{k(c['baslik'])}</h3><p>{k(c['ozet'])}</p>
<span class="devam">Detaya git {IKON['okd']}</span></span></a>""")
    return f'<div class="izgara iz-4">{"".join(kartlar)}</div>'


def _marka_kartlari():
    return '<div class="izgara iz-4">' + "".join(
        f'<a class="kart gel" href="/batman-{m["slug"]}-servisi/"><h3>Batman {k(m["ad"])} Servisi</h3>'
        f'<p>{k(m["ad"])} buzdolabı, çamaşır ve bulaşık makinesi onarımı.</p>'
        f'<span class="devam">İncele {IKON["okd"]}</span></a>'
        for m in D.MARKALAR) + '</div>'


def _bolge_kartlari():
    kartlar = []
    for b in D.BOLGELER:
        kartlar.append(
            f'<a class="kart gel" href="/{b["slug"]}-beyaz-esya-servisi/">'
            f'<span class="kart-ik">{IKON["pin"]}</span>'
            f'<h3>{k(b["ad"])}</h3><p>Varış süresi: <strong>{k(b["sure"])}</strong></p>'
            f'<span class="devam">Bölge sayfası {IKON["okd"]}</span></a>')
    return f'<div class="izgara iz-3">{"".join(kartlar)}</div>'


def _ariza_listesi():
    """Arıza rehberi — cihaza göre gruplanmış iç link ağı."""
    bloklar = []
    for c in D.CIHAZLAR:
        ilgili = [a for a in A.ARIZALAR if a["cihaz"] == c["slug"]]
        if not ilgili:
            continue
        satir = "".join(
            f'<li><a href="/{a["slug"]}/">{k(a["soru"])}</a></li>' for a in ilgili)
        bloklar.append(
            f'<div class="kart gel"><h3>{k(c["ad"])}</h3><ul class="ariza-liste">{satir}</ul>'
            f'<a class="devam" href="/batman-{c["slug"]}-tamircisi/">'
            f'Tüm {k(c["ad_tamlama"])} arızaları {IKON["okd"]}</a></div>')
    return f'<div class="izgara iz-2">{"".join(bloklar)}</div>'


def _fiyat_tablosu():
    satir = "".join(
        f"<tr><td>{k(ad)}</td><td class='ucret'>{k(ucret)}</td><td class='aciklama'>{k(aciklama)}</td></tr>"
        for ad, ucret, aciklama in D.FIYATLAR)
    return f"""<div class="tbl-sar"><table>
<caption class="sr">Batman beyaz eşya servisi ücretleri</caption>
<thead><tr><th scope="col">İşlem</th><th scope="col">Ücret</th><th scope="col">Açıklama</th></tr></thead>
<tbody>{satir}</tbody></table></div>
<p class="tbl-not">Fiyatlar parçaya, modele ve cihazın hacmine göre değişir. Kesin fiyat, arıza
yerinde tespit edildikten sonra ve <strong>işleme başlanmadan önce</strong> size bildirilir.
Son güncelleme: Eylül 2026.</p>"""


def _guven_kartlari():
    return '<div class="izgara iz-3">' + "".join(
        f'<div class="kart gel"><span class="kart-ik">{IKON["kalkan"]}</span>'
        f'<h3>{k(b)}</h3><p>{k(a)}</p></div>' for b, a in D.GUVEN) + '</div>'


SSS = [
 ("Batman'da beyaz eşya servisi aynı gün geliyor mu?",
  "<p>Evet. Batman merkezde arıza bildiriminden sonra <strong>genellikle 2 saat içinde</strong> "
  "adreste oluyoruz; en geç aynı gün müdahale ediyoruz. İlçelerde (Beşiri, Gercüş, Hasankeyf, "
  "Kozluk, Sason) en geç 1 gün içinde geliyoruz.</p>"),
 ("Servis ücreti ne kadar, parça takılmazsa da alınıyor mu?",
  "<p>Servis ücreti Batman merkezde ve <strong>ilçelerde 600 TL</strong>, Batman köylerinde "
  "<strong>1.000 TL</strong>'dir. Beşiri, Gercüş, Hasankeyf, Kozluk ve Sason için "
  "<strong>ayrıca yol ücreti almıyoruz.</strong> Arızayı yerinde tespit edip maliyeti "
  "söylüyoruz; onarımı yaptırmak istemezseniz yalnızca bu ücret alınır, başka bir bedel "
  "çıkmaz.</p>"),
 ("Onarım evde mi yapılıyor, cihaz götürülüyor mu?",
  "<p>Onarımların <strong>büyük çoğunluğunu cihazı yerinden oynatmadan evinizde</strong> "
  "tamamlıyoruz; parçayı orada takıyoruz. Cihazın atölyeye çekilmesi istisnai bir durumdur — "
  "en tipik örneği, buzdolabında gaz kaçağının gövde içinde olması ve arkanın kesilmesi "
  "gerektiği hâllerdir.</p>"),
 ("Takılan parçalar garantili mi?",
  "<p>Evet. Kullandığımız <strong>tüm parçalar 1 yıl garantilidir.</strong></p>"),
 ("Hangi markalara bakıyorsunuz?",
  "<p>Arçelik, Beko, Bosch, Siemens, Vestel, Profilo, Altus, Regal, Samsung, LG, Grundig ve SEG "
  "başta olmak üzere tüm markalara bakıyoruz.</p>"),
 ("Hangi cihazları onarıyorsunuz?",
  "<p>Buzdolabı, çamaşır makinesi, bulaşık makinesi ve derin dondurucu onarıyoruz. "
  "Bu dört cihazda uzmanlaştık.</p>"),
 ("Buzdolabım bozuldu, ne kadar acil?",
  "<p>Buzdolabı ve derin dondurucu çağrılarını <strong>her zaman sıranın önüne alıyoruz</strong>, "
  "çünkü içindeki gıda bozulur. Çamaşır ve bulaşık makinesi çağrıları bu ikisinden sonra gelir. "
  "Bu bizim kendi çalışma önceliğimizdir.</p>"),
 ("Pazar günü ve gece hizmet veriyor musunuz?",
  "<p>Evet. Acil durumlarda <strong>7 gün 24 saat</strong> ulaşabilirsiniz; tatil ve pazar "
  "günleri dahil. Buzdolabı ve derin dondurucu gibi bekletilemeyecek arızalarda gece de "
  "dönüş yapıyoruz.</p>"),
 ("Yedek parça bulunmuyorsa ne oluyor?",
  "<p>Parça elimizde yoksa sipariş ediyor, <strong>1–2 gün içinde</strong> takılmasını "
  "sağlıyoruz. Süreç boyunca sizi bilgilendiriyoruz.</p>"),
 ("Bir tamir ne kadar sürer?",
  "<p>Basit arızalar (kapı contası, filtre değişimi) <strong>30–60 dakika</strong>; motor ve "
  "pompa gibi orta düzey işler <strong>1–2 saat</strong>; kompresör ve elektronik kart "
  "arızaları <strong>2–4 saat</strong> sürer.</p>"),
 ("Servis ücretinde indirim var mı?",
  "<p>Evet. Arızayı tespit ettikten sonra <strong>onarımı bize yaptırırsanız çağrı ücretinde "
  "indirim uyguluyoruz.</strong> Onarım istemezseniz yalnızca çağrı ücretini ödersiniz.</p>"),
 ("Belgeli servis misiniz?",
  "<p>Evet. <strong>T.C. Millî Eğitim Bakanlığı İş Yeri Açma Belgesi</strong> sahibiyiz; "
  "meslek alanı Tesisat Teknolojisi ve İklimlendirme, <strong>meslek dalı Soğutma "
  "Sistemleri</strong>. Belge 3308 sayılı Mesleki Eğitim Kanunu gereğince ustalık belgesine "
  "tanınan bütün hakları kapsar.</p>"),
 ("Fiyatı işlemden önce söylüyor musunuz?",
  "<p>Evet. Arızayı tespit ettikten sonra <strong>işleme başlamadan önce</strong> maliyeti "
  "söylüyoruz. Masraf cihazın değerine yaklaşıyorsa bunu da açıkça belirtiyor, gerektiğinde "
  "onarım yaptırmamanızı öneriyoruz.</p>"),
]


def govde():
    b = []

    # ---------------------------------------------------------- kahraman
    b.append(f"""<section class="kahraman"><div class="kap"><div class="kh-izgara">
<div>
<h1>Batman Beyaz Eşya Servisi — <em>Hızlı ve Güvenilir Teknik Servis</em></h1>
<p class="kh-alt">Buzdolabı, çamaşır makinesi, bulaşık makinesi ve derin dondurucu arızalarında
Batman merkezde <strong>genellikle 2 saat içinde</strong> adresinizdeyiz. Onarımların büyük
çoğunluğunu evinizde tamamlıyor, taktığımız parçalara 1 yıl garanti veriyoruz.</p>
<div class="kh-dgler">
<a class="dg dg-ara" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp'tan yaz</a>
</div>
<div class="kh-rozet">
<span class="rozet">{IKON['saat']}Aynı gün yerinde servis</span>
<span class="rozet">{IKON['kalkan']}Parçalara 1 yıl garanti</span>
<span class="rozet">{IKON['araba']}Batman merkez ve tüm ilçeler</span>
<span class="rozet">{IKON['arti']}8 yılı aşkın tecrübe</span>
<span class="rozet">{IKON['saat']}7 gün 24 saat</span>
</div>
</div>
<div class="kh-gorsel">
{resim("batman-beyaz-esya-servisi-nasil-calisir.webp",
       "Batman beyaz eşya servisi teknisyeni cihaz onarırken",
       boy="(max-width:900px) 92vw, 440px", oncelik=True)}
<div class="kh-kart"><b>2 saat</b><span>Batman merkezde ortalama varış süresi</span></div>
</div>
</div></div></section>""")

    # ---------------------------------------------------------- şerit
    b.append(f"""<div class="serit"><div class="kap serit-ic">
<span>{IKON['pin']}Fatih Mah. 3206. Sk. No:12, Batman Merkez</span>
<span>{IKON['saat']}Buzdolabı çağrıları önce</span>
<span>{IKON['kalkan']}Önce fiyat, sonra işlem</span>
</div></div>""")

    # ---------------------------------------------------------- H2: Nedir?
    b.append(f"""<section id="hakkinda"><div class="kap">
<div class="bas"><span class="etiket">Hakkımızda</span>
<h2>Batman Beyaz Eşya Servisi Nedir?</h2></div>
<div class="izgara iz-2" style="align-items:start">
<div>
<p><strong>Batman Beyaz Eşya Servisi</strong>, Batman merkez ve ilçelerinde buzdolabı, çamaşır
makinesi, bulaşık makinesi ve derin dondurucu onarımı yapan bir teknik servistir. Sekiz yılı aşkın
süredir sahadayız ve dört cihaz grubunda uzmanlaştık.</p>
<p>Beyaz eşya servisi, bozulan cihazınızın arızasını yerinde tespit eden, gereken parçayı değiştirip
cihazı tekrar çalışır hâle getiren hizmettir. Bizim çalışma biçimimizde bunun üç adımı var:
<strong>arızayı yerinde tespit etmek</strong>, <strong>maliyeti işleme başlamadan söylemek</strong> ve
<strong>onarımı mümkün olduğunca cihazı yerinden oynatmadan tamamlamak.</strong></p>
<p>Onarımların büyük çoğunluğunu evinizde bitiriyoruz. Cihazın atölyeye çekilmesi istisnadır —
en tipik örneği buzdolabında gaz kaçağının gövde içinde olması ve dolabın arkasının kesilmesi
gereken durumlardır.</p>
</div>
<div class="kutu" style="margin-top:0">
<b>Bizim önceliğimiz neden buzdolabı?</b>
<p>Aynı anda birden fazla çağrı geldiğinde <strong>her zaman buzdolabı ve derin dondurucuyu öne
alıyoruz.</strong> Sebebi basit: bir çamaşır makinesi bir gün bekleyebilir, ama duran bir buzdolabındaki
gıdanın tamamı bozulur.</p>
<p>Bu, müşteriye söylediğimiz bir slogan değil, sahada uyguladığımız gerçek sıralama:
<strong>önce dolap, sonra çamaşır, sonra bulaşık.</strong></p>
</div>
</div></div></section>""")

    # ---------------------------------------------------------- cihazlar
    b.append(f"""<section id="cihazlar" class="alt"><div class="kap">
<div class="bas"><span class="etiket">Hizmetler</span>
<h2>Batman'da Onardığımız Beyaz Eşyalar</h2>
<p>Dört cihaz grubunda çalışıyoruz. Her cihazın kendi sayfasında o cihaza özel arızaları,
sebeplerini ve güncel ücretleri bulabilirsiniz.</p></div>
{_cihaz_kartlari()}
</div></section>""")

    # ---------------------------------------------------------- H2: Nasıl bulunur?
    b.append(f"""<section><div class="kap">
<div class="bas"><h2>Batman Beyaz Eşya Servisi Nasıl Bulunur?</h2></div>
<p>Batman'da beyaz eşya servisi ararken çoğu kişi tek bir soruya odaklanır: "en yakını hangisi?"
Oysa yakınlık tek başına yeterli değil. Doğru servisi bulmanın pratik yolu şu üç adımdır:</p>
<ol>
<li><strong>Cihazınızın markasına ve tipine bakıp bakmadığını sorun.</strong> Her servis her cihaza
bakmaz. Biz buzdolabı, çamaşır makinesi, bulaşık makinesi ve derin dondurucuda uzmanız.</li>
<li><strong>Servis ücretini ve neyi kapsadığını önceden öğrenin.</strong> Servis ücreti yol ve arıza
tespiti karşılığıdır; onarım yaptırmasanız da alınır. Bunu telefonda net söylemeyen servise dikkat edin.</li>
<li><strong>Parçaya garanti verip vermediğini sorun.</strong> Garantisiz takılan parça, kısa sürede
ikinci kez ödeme yapmanız anlamına gelebilir.</li>
</ol>
<p>Bu üç sorunun cevabını telefonda net alabiliyorsanız doğru yerdesiniz demektir.
Bize <a href="tel:{I['tel_link']}">{I['tel_yazi']}</a> numarasından ulaşıp üçünü de sorabilirsiniz.</p>
</div></section>""")

    # ---------------------------------------------------------- H2: Seçerken dikkat
    b.append(f"""<section class="alt"><div class="kap">
<div class="bas"><h2>Beyaz Eşya Servisi Seçerken Nelere Dikkat Edilmeli?</h2>
<p>Sekiz yıllık sahada, müşterilerin en çok şu noktalarda mağdur olduğunu gördük.</p></div>
{_guven_kartlari()}
<div class="kutu uyari"><b>En sık yapılan hata: sebebi bulmadan parça değiştirmek</b>
<p>Örneğin buzdolabında motor yandıysa, <strong>neden yandığı</strong> bulunmadan yenisi takılmamalı.
Sebep gaz kaçağıysa ve kaçak kapatılmazsa yeni motor da aynı yolu izler — müşteri 8.000 TL'lik
parayı ikinci kez öder. İyi bir servis parçayı değil, önce sebebi bulur.</p></div>
</div></section>""")

    # ---------------------------------------------------------- H2: Hangi servisler var
    b.append(f"""<section><div class="kap">
<div class="bas"><h2>Batman'da Hangi Beyaz Eşya Servisleri Var?</h2></div>
<p>Batman'da beyaz eşya onarımı üç farklı yapı tarafından veriliyor ve bu üçünün çalışma biçimi
birbirinden oldukça farklı:</p>
<div class="izgara iz-3">
<div class="kart"><h3>Marka yetkili servisleri</h3>
<p>Yalnızca kendi markalarına bakarlar. Garanti kapsamındaki cihazlar için doğru adres. Randevu
sırası markanın iş yoğunluğuna bağlıdır.</p></div>
<div class="kart"><h3>Özel (bağımsız) teknik servisler</h3>
<p>Marka ayrımı yapmadan çalışırlar. Garanti süresi dolmuş cihazlarda daha hızlı dönüş ve daha esnek
fiyat sunabilirler. <strong>Biz bu gruptayız.</strong></p></div>
<div class="kart"><h3>Tek kişilik tamirciler</h3>
<p>Genellikle belirli bir cihaz grubunda çalışırlar. Kalite kişiden kişiye çok değiştiği için
referans ve garanti sorusu burada daha kritiktir.</p></div>
</div>
<p style="margin-top:22px">Hangisini seçeceğiniz cihazınızın <strong>garanti durumuna</strong> bağlı.
Cihazınız garantideyse önce yetkili servise gidin — ücretsiz olabilir. Garanti bittiyse özel servis
genellikle daha hızlı ve daha uygun oluyor. Aradaki farkı
<a href="#yetkili-ozel">aşağıda ayrıntılı anlattık</a>.</p>
</div></section>""")

    # ---------------------------------------------------------- markalar
    b.append(f"""<section id="markalar" class="buz"><div class="kap">
<div class="bas"><span class="etiket">Markalar</span>
<h2>Baktığımız Beyaz Eşya Markaları</h2>
<p>Marka ayrımı yapmıyoruz. Aşağıdaki markaların hepsinde buzdolabı, çamaşır makinesi, bulaşık
makinesi ve derin dondurucu onarımı yapıyoruz.</p></div>
{_marka_kartlari()}
</div></section>""")

    # ---------------------------------------------------------- H2: Ücretler
    b.append(f"""<section id="ucretler"><div class="kap">
<div class="bas"><span class="etiket">Şeffaf fiyat</span>
<h2>Batman Beyaz Eşya Servisi Ücretleri Nelerdir?</h2>
<p>Aşağıdaki ücretler Batman'da uyguladığımız güncel fiyatlardır. Telefonda tahmini aralığı,
yerinde tespitten sonra kesin rakamı söylüyoruz.</p></div>
{_fiyat_tablosu()}
</div></section>""")

    # ---------------------------------------------------------- H2: Fiyat nasıl belirlenir
    b.append(f"""<section class="alt"><div class="kap">
<div class="bas"><h2>Beyaz Eşya Tamir Fiyatları Nasıl Belirlenir?</h2></div>
<p>Beyaz eşya onarımında fiyat tek bir kalemden oluşmaz. Ödediğiniz tutarı belirleyen dört etken var:</p>
<div class="izgara iz-2">
<div class="kart"><h3>1. Değişen parçanın kendisi</h3>
<p>Aynı işin parçası modele göre katlanabiliyor. Buzdolabı fanı standart bir modelde 600–700 TL iken,
üst segment bir modelde yalnızca parça 3.000–3.200 TL'ye çıkabiliyor.</p></div>
<div class="kart"><h3>2. Cihazın hacmi ve tipi</h3>
<p>Buzdolabı ve derin dondurucuda litre doğrudan fiyata yansır. 400 litrelik bir cihazın motoruyla
800 litreliğin motoru aynı değildir.</p></div>
<div class="kart"><h3>3. İşin niteliği</h3>
<p>Gider açmak gibi parça gerektirmeyen işlerde yalnızca servis ücreti alınır. Gaz kaçağında ise
sistem açılır, kaynak yapılır, vakum çekilir — işçilik doğal olarak artar.</p></div>
<div class="kart"><h3>4. Markaya bağlı yapı farkları</h3>
<p>Somut örnek: bulaşık makinesinde <strong>Bosch'ta rezistans motorun içindedir</strong>, bu yüzden
komple motor değişir. Arçelik ve Vestel gibi markalarda rezistans motorun yanındadır, ayrı değişir ve
çok daha ucuza gelir.</p></div>
</div>
<div class="kutu"><b>Bizim kuralımız</b>
<p>Arızayı tespit ettikten sonra maliyeti <strong>işleme başlamadan</strong> söylüyoruz. Yaptırmak
istemezseniz yalnızca servis ücreti alınır. Masraf cihazın değerine yaklaşıyorsa bunu da açıkça
söylüyoruz — gereksiz masraf çıkarmak uzun vadede bizim de aleyhimize.</p></div>
</div></section>""")

    # ---------------------------------------------------------- arıza rehberi
    b.append(f"""<section id="ariza-rehberi"><div class="kap">
<div class="bas"><span class="etiket">Arıza rehberi</span>
<h2>Beyaz Eşya Arızaları: Belirti, Sebep ve Çözüm</h2>
<p>Sahada en çok karşılaştığımız arızaları, sebeplerini ve yaklaşık maliyetlerini tek tek anlattık.
Cihazınızın belirtisine en yakın başlığı seçin.</p></div>
{_ariza_listesi()}
</div></section>""")

    # ---------------------------------------------------------- H2: En yakın servis
    b.append(f"""<section id="bolgeler" class="alt"><div class="kap">
<div class="bas"><h2>Batman'da En Yakın Beyaz Eşya Servisi Nasıl Bulunur?</h2></div>
<div class="izgara iz-2" style="align-items:start">
<div>
<p>"En yakın servis" araması aslında iki farklı şeyi sorar: <strong>fiziksel mesafe</strong> ve
<strong>ne kadar çabuk gelinebileceği.</strong> Beyaz eşya onarımında ikincisi çok daha önemlidir,
çünkü cihazı siz getirmiyorsunuz — biz geliyoruz.</p>
<p>Dükkânımız <strong>Fatih Mahallesi 3206. Sokak No:12</strong>, Batman Merkez'de. Batman merkez
içindeki adreslere <strong>genellikle 2 saat içinde</strong>, en kötü ihtimalle 2–3 saat içinde
ulaşıyoruz.</p>
<p>Beşiri, Gercüş, Hasankeyf, Kozluk ve Sason'a da gidiyoruz; ilçe adreslerinde varış süresi
<strong>en geç 1 gündür.</strong></p>
<p><a class="dg dg-bos" href="{I['yol_tarifi']}" target="_blank" rel="noopener">{IKON['pin']}Yol tarifi al</a></p>
</div>
{_bolge_kartlari()}
</div></div></section>""")

    # ---------------------------------------------------------- H2: Eve gelen servis
    b.append(f"""<section><div class="kap">
<div class="bas"><h2>Batman'da Eve Gelen Beyaz Eşya Servisi Nasıl Bulunur?</h2></div>
<p>Beyaz eşya, taşınması zor ve taşınırken zarar görmesi kolay bir cihaz grubudur. Bu yüzden doğru
soru "cihazımı nereye götüreyim" değil, <strong>"kim evime gelip burada onarabilir"</strong> olmalı.</p>
<p>Bizim çalışma biçimimiz baştan bu şekilde kurulu: <strong>onarımların büyük çoğunluğunu cihazı
yerinden oynatmadan, sizin evinizde tamamlıyoruz.</strong> Gerekli parçayı yanımızda getirip orada
takıyoruz; siz de yapılan işi baştan sona görüyorsunuz.</p>
<p>Cihazın atölyeye çekilmesi istisnai bir durumdur. En tipik örneği, buzdolabında
<a href="/buzdolabi-gaz-kacagi/">gaz kaçağının gövde içinde olması</a> ve dolabın arkasının kesilmesi
gereken hâllerdir. Bunun dışında kompresör değişimi dahil çoğu iş evde bitiyor.</p>
<div class="kutu"><b>Eve gelen servis ararken sorulacak tek soru</b>
<p>"Bu işi evimde bitirebiliyor musunuz, yoksa cihazı götürmeniz mi gerekiyor?" Cevap netse
planınızı yapabilirsiniz. Biz bu cevabı telefonda arızayı dinledikten sonra büyük ölçüde verebiliyoruz.</p></div>
</div></section>""")

    # ---------------------------------------------------------- H2: Aynı gün
    b.append(f"""<section class="buz"><div class="kap">
<div class="bas"><h2>Batman Beyaz Eşya Servisi Aynı Gün Hizmet Verir mi?</h2></div>
<p>Evet. Batman merkezde arıza bildiriminden sonra <strong>genellikle 2 saat içinde</strong>
adresteyiz; en kötü ihtimalle 2–3 saat içinde cihaza bakmış oluyoruz. Çoğu arızayı da aynı ziyarette
çözüyoruz.</p>
<p>Bunu mümkün kılan şey, işi <strong>öncelik sırasına göre</strong> yürütmemiz:</p>
<div class="izgara iz-3">
<div class="kart"><h3>1. Buzdolabı ve derin dondurucu</h3>
<p>Her zaman ilk sırada. İçindeki gıda bozulacağı için beklemeye tahammülü olmayan tek cihaz grubu.</p></div>
<div class="kart"><h3>2. Çamaşır makinesi</h3>
<p>Günlük hayatı doğrudan etkiliyor ama bir gün beklemesi geri dönülmez bir kayıp yaratmıyor.</p></div>
<div class="kart"><h3>3. Bulaşık makinesi</h3>
<p>Sıralamada son. Diğer iki grubun çağrısı yoksa aynı gün, çoğu zaman aynı saatlerde bakıyoruz.</p></div>
</div>
<p style="margin-top:22px">İlçelerde durum biraz farklı: Beşiri, Gercüş, Hasankeyf, Kozluk ve Sason
adreslerine <strong>en geç 1 gün içinde</strong> gidiyoruz.</p>
</div></section>""")

    # ---------------------------------------------------------- H2: Güvenilir servis
    b.append(f"""<section><div class="kap">
<div class="bas"><h2>Güvenilir Beyaz Eşya Servisi Nasıl Anlaşılır?</h2></div>
<p>Güvenilir servisi anlamak için teknik bilgiye ihtiyacınız yok. Telefonda ve ilk ziyarette
göreceğiniz birkaç davranış yeterli:</p>
<ul>
<li><strong>Fiyatı işlemden önce söylüyor mu?</strong> Arıza tespit edildikten sonra, parçaya
dokunmadan önce maliyet söylenmeli. "Önce açalım bakalım" cümlesi güvenli değildir.</li>
<li><strong>Yaptırmama seçeneğinizi açıkça söylüyor mu?</strong> Onarımı istemezseniz yalnızca servis
ücreti ödemeniz gerektiği baştan belirtilmeli.</li>
<li><strong>Gerektiğinde "yaptırmayın" diyebiliyor mu?</strong> Masraf cihazın değerine yaklaşıyorsa
bunu söylemek servisin aleyhinedir — ama doğrusu budur. Biz görünmeyen gaz kaçağı onarımında
müşterilerimize sık sık bunu söylüyoruz.</li>
<li><strong>Parçaya garanti veriyor mu, süresi net mi?</strong> Bizde tüm parçalar
<strong>1 yıl garantilidir.</strong></li>
<li><strong>Sebebi mi arıyor, parçayı mı değiştiriyor?</strong> Yanan bir motoru sebebini bulmadan
değiştiren servis, aynı arızayı size ikinci kez ödetir.</li>
</ul>
</div></section>""")

    # ---------------------------------------------------------- H2: Yetkili vs özel
    b.append(f"""<section id="yetkili-ozel" class="alt"><div class="kap">
<div class="bas"><h2>Yetkili Servis ve Özel Servis Arasındaki Fark Nedir?</h2></div>
<div class="tbl-sar"><table>
<thead><tr><th scope="col">Konu</th><th scope="col">Marka yetkili servisi</th>
<th scope="col">Özel (bağımsız) servis</th></tr></thead>
<tbody>
<tr><td>Marka kapsamı</td><td>Yalnızca kendi markası</td><td>Marka ayrımı yok</td></tr>
<tr><td>Garantili cihaz</td><td class="ucret">Doğru adres</td><td>Garantiyi düşürebilir</td></tr>
<tr><td>Garantisi bitmiş cihaz</td><td>Genelde daha pahalı</td><td class="ucret">Genelde daha uygun</td></tr>
<tr><td>Randevu süresi</td><td>Markanın yoğunluğuna bağlı</td><td class="ucret">Genelde daha hızlı</td></tr>
<tr><td>Parça</td><td>Orijinal parça</td><td>Orijinal veya muadil (size sorulur)</td></tr>
<tr><td>Fiyat esnekliği</td><td>Sabit tarife</td><td>İşe göre değişebilir</td></tr>
</tbody></table></div>
<div class="kutu"><b>Basit kural</b>
<p><strong>Cihazınız garantideyse önce yetkili servise gidin</strong> — işlem ücretsiz olabilir ve
bağımsız bir servise yaptıracağınız müdahale garantinizi düşürebilir.
<strong>Garanti süresi dolmuşsa</strong> özel servis genellikle hem daha hızlı hem daha uygun olur.</p>
<p>Biz özel (bağımsız) teknik servisiz. Garantisi devam eden bir cihaz için bize başvurursanız,
önce yetkili servise gitmenizi kendimiz öneriyoruz.</p></div>
{belge_blok()}
</div></section>""")

    # ---------------------------------------------------------- H2: Bilinmesi gerekenler + video
    v1 = video_kapak("beyaz-esya-servisi.mp4", "batman-beyaz-esya-servisi-nasil-calisir.webp",
                     "Sahada çalışırken", dikey=True)
    v2 = video_kapak("camasir-makinesi-kazan-arizasi.mp4", "arizali-camasir-makinesi.webp",
                     "Çamaşır makinesi kazan arızası", dikey=True)
    v3 = video_kapak("buzdolabi-kart-degisim.mp4", "buzdolabi-kart-degisim.webp",
                     "Buzdolabı kart değişimi", dikey=True)
    b.append(f"""<section id="videolar"><div class="kap">
<div class="bas"><span class="etiket">Sahadan</span>
<h2>Batman Beyaz Eşya Servisi Hakkında Bilinmesi Gerekenler</h2>
<p>Aşağıdaki görüntüler stok video değil — Batman'da kendi yaptığımız onarımlardan.
Videolar <strong>siz oynatana kadar yüklenmez</strong>, sayfayı yavaşlatmaz.</p></div>
<div class="izgara iz-3">{v1}{v2}{v3}</div>
<div class="izgara iz-2" style="margin-top:34px;align-items:start">
<div class="kutu"><b>Kapı kilidi arızasında kilidi zorlamayın</b>
<p>Çamaşır makinesinde kapı kilidi arızası çok sık <strong>kartı da patlatıyor.</strong> Kilit
sıkıştığında zorlamak, 1.000 TL'lik bir işi kart değişimine kadar büyütebiliyor. Kapı açılmıyorsa
zorlamayın, <a href="/camasir-makinesi-kapi-kilidi-arizasi/">arızaya bakın</a>.</p></div>
<div class="kutu"><b>Bulaşık makinesi filtresini 3 ayda bir açın</b>
<p>Alttaki filtre üç ayda bir açılıp temizlenirse makine belirgin şekilde daha iyi yıkar. İhmal
edilen filtre, zamanla pompa arızasına kadar gidiyor. Bu, hiçbir masrafı olmayan tek bakım adımı.</p></div>
</div>
</div></section>""")

    # ---------------------------------------------------------- SSS
    b.append(f"""<section class="alt"><div class="kap">
<div class="bas"><span class="etiket">Sık sorulanlar</span>
<h2>Batman Beyaz Eşya Servisi Hakkında Sık Sorulan Sorular</h2></div>
{sss_blok(SSS)}
</div></section>""")

    # ---------------------------------------------------------- iletişim + CTA
    b.append(f"""<section id="iletisim"><div class="kap">
<div class="cta">
<h2>Cihazınız bozulduysa bekletmeyin</h2>
<p>Arızayı telefonda dinleyip yaklaşık maliyeti söylüyoruz. Batman merkezde genellikle 2 saat içinde
adresinizdeyiz. Buzdolabı ve derin dondurucu çağrılarını sıranın önüne alıyoruz.</p>
<div class="cta-dgler">
<a class="dg dg-ara" href="tel:{I['tel_link']}">{IKON['tel']}{I['tel_yazi']}</a>
<a class="dg dg-wa" href="https://wa.me/{I['wa']}" rel="noopener" target="_blank">{IKON['wa']}WhatsApp'tan yaz</a>
</div>
</div>
<div class="izgara iz-3" style="margin-top:34px">
<div class="kart"><span class="kart-ik">{IKON['pin']}</span><h3>Adres</h3>
<p>{k(I['adres_sokak'])}<br>{k(I['posta'])} {k(I['adres_ilce'])} / {k(I['adres_il'])}</p>
<a class="devam" href="{I['yol_tarifi']}" target="_blank" rel="noopener">Yol tarifi al {IKON['okd']}</a></div>
<div class="kart"><span class="kart-ik">{IKON['tel']}</span><h3>Telefon &amp; WhatsApp</h3>
<p>Tek numara üzerinden hem arayabilir hem yazabilirsiniz.</p>
<a class="devam" href="tel:{I['tel_link']}">{I['tel_yazi']} {IKON['okd']}</a></div>
<div class="kart"><span class="kart-ik">{IKON['saat']}</span><h3>Varış süresi</h3>
<p>Batman merkez: genellikle 2 saat içinde.<br>İlçeler: en geç 1 gün içinde.</p></div>
</div>
</div></section>""")

    return "\n".join(b)


def semalar():
    return [
        yerel_isletme_sema(),
        {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/",
         "name": I["ad"], "inLanguage": "tr-TR",
         "publisher": {"@id": SITE + "/#isletme"}},
        faq_sema(SSS),
    ]


BASLIK = "Batman Beyaz Eşya Servisi | Aynı Gün Yerinde Teknik Servis"
ACIKLAMA = ("Batman beyaz eşya servisi: buzdolabı, çamaşır ve bulaşık makinesi, derin dondurucu "
            "onarımı. Merkezde 2 saat içinde yerinde servis, 1 yıl parça garantisi. " + I["tel_yazi"])
