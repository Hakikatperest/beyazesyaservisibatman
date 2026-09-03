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


# --------------------------------------------------------------- saha videoları
# Hepsi Batman'da kendi yaptığımız onarımlardan. Kapak deseni: tıklanana kadar
# tek bayt inmez. Etiketler videonun İÇERİĞİNİ anlatır — iddia değil.
CIHAZ_VIDEO = {
"buzdolabi": [
 ("buzdolabi-koprosor-degisimi.mp4", "buzdolabi-motor-degisim3.webp",
  "Buzdolabı kompresör (motor) değişimi"),
 ("buzdolabi-kart-degisim2.mp4", "buzdolabi-kart-degisimi2.webp",
  "Buzdolabı elektronik kart değişimi"),
 ("buzdolabi-kacak-arizasi.mp4", "buzdolabi-motor-karti-degisimi.webp",
  "Buzdolabında kaçak tespiti"),
],
"camasir-makinesi": [
 ("camasir-makinesi-tamiri.mp4", "camasir-makinesi-motor-degisimi.webp",
  "Çamaşır makinesi tamiri"),
 ("camasir-makinesi-kazan-arizasi2.mp4", "arizali-camasir-makinesi.webp",
  "Çamaşır makinesi kazan arızası"),
 ("camasir-makinesi-sase-degisim.mp4", "camasir-makinesi-pas-temizligi.webp",
  "Çamaşır makinesi şase değişimi"),
 ("camasir-makinesi-cocuk-kilidi-arizasi.mp4", "camasir-makinesi-karti.webp",
  "Çamaşır makinesi çocuk kilidi arızası"),
 # ⛔ Bu videonun dosya adında arıza kodu geçiyor; ETİKETTE geçmiyor —
 #    "arıza kodları sayfaya girmeyecek" kararı bozulmasın.
 ("camasir-makinesi-3e-arizasi.mp4", "camasir-makinesi-kart-degisimi-arizasi.webp",
  "Çamaşır makinesi arıza tespiti"),
],
"bulasik-makinesi": [
 ("bulasik-makinesi-svic-arizasi.mp4", "bulasik-makinesi-pervane-degisimi.webp",
  "Bulaşık makinesi sviç arızası"),
 ("bulasik-makinesi-su-kacak-tespiti.mp4", "bulasik-makinesi-ariza.webp",
  "Bulaşık makinesinde su kaçağı tespiti"),
 ("bulasik-makinesi-kart-degisim2.mp4", "bulasik-makinesi-kart-degisim-arizasi.webp",
  "Bulaşık makinesi kart değişimi"),
],
"derin-dondurucu": [
 ("derin-dondurucu-motor-arizasi.mp4", "buzmatik-ariza-tespit.webp",
  "Derin dondurucu motor arızası"),
 ("buzdolabi-koprosor-degisimi.mp4", "buzdolabi-motor-degisim.webp",
  "Kompresör (motor) değişimi"),
 ("buzdolabi-gaz-kacagi-govde-degisim.mp4", "buzdolabi-motor-karti-degisimi3.webp",
  "Gaz kaçağında gövde onarımı"),
],
}

BOLGE_VIDEO = {
"batman-merkez": [
 ("beyaz-esya-servisi.mp4", "batman-beyaz-esya-servisi-nasil-calisir.webp", "Sahada çalışırken"),
 ("camasir-makinesi-servisi.mp4", "camasir-makinesi-motor-degisimi.webp", "Çamaşır makinesi servisi"),
],
"besiri": [
 ("camasir-makinesi-tamir.mp4", "camasir-makinesi-karti.webp", "Çamaşır makinesi tamiri"),
 ("buzdolabi-arka-fan-sesi.mp4", "buzdolabi-fan-degisim.webp", "Buzdolabı arka fan sesi"),
],
"gercus": [
 ("arizali-camasir-makinesi-sesi.mp4", "arizali-camasir-makinesi.webp", "Arızalı çamaşır makinesi sesi"),
 ("bulasik-makinesi-motor-ariza-sesi.mp4", "bulasik-makinesi-ariza.webp", "Bulaşık makinesi motor arıza sesi"),
],
"hasankeyf": [
 ("camasir-makinesi-kazan-arizasi3.mp4", "motoru-arizali-camasir-makinesi.webp", "Çamaşır makinesi kazan arızası"),
 ("buzdolabi-arka-hortum-gider-temizligi.mp4", "buzdolabi-mentese-degisimi.webp", "Buzdolabı arka gider temizliği"),
],
"kozluk": [
 ("camasir-makinesi-kapi-kilit-arizasi.mp4", "camasir-makinesi-karti2.webp", "Çamaşır makinesi kapı kilidi arızası"),
 ("camasir-makinesi-gider-hortumu-degisimi.mp4", "camasir-makinesi-conta-degisimi.webp", "Çamaşır makinesi gider hortumu değişimi"),
],
"sason": [
 ("camasir-makinesi-su-bosaltma-motoru-arizasi.mp4", "su-bosaltma-motoru-degisimi3.webp",
  "Çamaşır makinesi su boşaltma motoru arızası"),
 ("bulasik-makinesi-su-kacak-tespiti.mp4", "bulasik-makinesi-sepet-degisimi.webp",
  "Bulaşık makinesinde su kaçağı tespiti"),
],
}


def saha_videolari(liste, baslik, giris, alt=True):
    """Kapak desenli video şeridi. Dosya yoksa video_kapak sessizce yorum düşer."""
    kutular = "".join(video_kapak(v, p, e) for v, p, e in liste)
    if "video-kutu" not in kutular:
        return ""
    return f"""<section{' class="alt"' if alt else ''}><div class="kap">
<div class="bas"><span class="etiket">Sahadan</span><h2>{k(baslik)}</h2>
<p>{k(giris)} Videolar <strong>siz oynatana kadar yüklenmez</strong>, sayfayı yavaşlatmaz.</p></div>
<div class="izgara iz-3">{kutular}</div>
</div></section>"""


def sss_bolumu(sorular, baslik, alt=False):
    return f"""<section{' class="alt"' if alt else ''}><div class="kap">
<div class="bas"><span class="etiket">Sık sorulanlar</span><h2>{k(baslik)}</h2></div>
{sss_blok(sorular)}
</div></section>"""


# --------------------------------------------------------------- cihaz SSS
# ⚠️ Tüm cevaplar _src/bilgi.md'deki işletme anlatımına dayanır. Yeni iddia YOK.
CIHAZ_SSS = {
"buzdolabi": [
 ("Buzdolabım soğutmuyor, sebebi ne olabilir?",
  "<p>İki ana sebep var: <strong>gazla ilgili bir sorun</strong> veya "
  "<strong>kompresörün (halk arasında 'motor') çalışmaması.</strong> Motor kaynaklıysa sistem "
  "açılır, kaynak yapılır, tıkanma giderilir, vakum çekilir ve gaz basılır.</p>"),
 ("Buzdolabı ses yapıyor, ne olmuş olabilir?",
  "<p>Neredeyse her zaman <strong>fan</strong> kaynaklıdır — buzdolabında ses çıkarabilecek "
  "başka bir parça pek yoktur. Fan buza çarpıyor veya arka pervane sıkışmış olabilir. "
  "Bazen <strong>buzmatik</strong> (buz yapma ünitesi) ses yapar.</p>"),
 ("Buzdolabının altında su birikiyor, ne yapmalıyım?",
  "<p>Buzlar çözüldükten sonra suyun aktığı <strong>arka gider tıkanmıştır.</strong> Gider "
  "kapalıysa su ön taraftan da akabilir. Gider açılınca sorun biter; bu genelde parça "
  "gerektirmeyen, yalnızca servis ücreti alınan bir iştir.</p>"),
 ("Buzdolabı hiç durmadan çalışıyor, normal mi?",
  "<p>Değil. <strong>Termostat arızalıdır</strong> ve kompresörü dinlendirmiyordur. "
  "Termostat değişimi işçilikle beraber yaklaşık <strong>1.500 TL</strong>; parçası pahalı "
  "modellerde 2.000 TL'ye kadar çıkabilir.</p>"),
 ("Buzdolabında buzlanma neden olur?",
  "<p><strong>Statik</strong> buzdolaplarında etraftan komple buzlanma normaldir. "
  "<strong>No-frost</strong> modellerde buzlanma olasılığı düşüktür; buz görüyorsanız akla ilk "
  "gelen, buzu eriten <strong>rezistansın çalışmamasıdır.</strong></p>"),
 ("Kompresör (motor) değişimi ne kadar tutuyor?",
  "<p><strong>8.000 – 11.000 TL</strong> aralığında. Fiyat gaz tipine, motor büyüklüğüne ve "
  "dolabın litresine göre değişir. Kesin rakamı arıza yerinde tespit edildikten sonra, "
  "işleme başlamadan önce söylüyoruz.</p>"),
 ("Kompresör neden yanar?",
  "<p>Dört sebebi var: <strong>tıkanma, fazla akım, fazla gaz ve gaz kaçağı.</strong> "
  "Bu yüzden kompresör değiştirirken yalnızca motoru takıp geçmiyor, sistemin tamamına "
  "bakıyoruz — sebep duruyorsa yeni motor da aynı yolu izler.</p>"),
 ("Gaz kaçağı onarılır mı, yoksa dolabı değiştireyim mi?",
  "<p>Kaçak <strong>gözle görünen bir yerdeyse</strong> kaynak edilir ve iş evinizde biter. "
  "Kaçak görünmüyorsa <strong>dolabın arkasının kesilmesi</strong> gerekir; cihaz atölyeye "
  "çekilir ve maliyet yaklaşık 5.000 TL'yi bulur. Bu durumda masraf çoğu zaman cihazın "
  "değerine yaklaştığı için <strong>onarım yaptırmamanızı kendimiz öneriyoruz.</strong></p>"),
 ("Kapak lastiği bozulduysa mutlaka değişmesi gerekir mi?",
  "<p>Her zaman değil — kapak lastiği ısıtılınca gevşeyip eski formunu geri alabiliyor. "
  "Ancak bunu kendi başınıza denemeyin: <strong>önce cihazın fişini çekin</strong> ve "
  "yine de bize haber verin. Lastiğin kurtarılıp kurtarılamayacağına yerinde bakıp "
  "söylüyoruz.</p>"),
 ("Buzdolabı arızası ne kadar acil sayılıyor?",
  "<p>Bizde en acil çağrı buzdolabıdır. <strong>Buzdolabı ve derin dondurucu çağrılarını "
  "her zaman sıranın önüne alıyoruz</strong>, çünkü duran bir dolapta gıdanın tamamı bozulur. "
  "Bu bizim kendi çalışma önceliğimizdir.</p>"),
],
"camasir-makinesi": [
 ("Çamaşır makinesi su almıyor, sebebi ne?",
  "<p>Arkadaki <strong>su ventili</strong> suyu iletmiyordur — makine su almadan çalışmaz. "
  "Ventil sağlamsa <strong>kart ventile elektrik vermiyordur.</strong> Ventilin parçası "
  "yaklaşık 400 TL, değişimiyle birlikte <strong>1.100 TL</strong> tutuyor.</p>"),
 ("Çamaşır makinesi suyu boşaltmıyor?",
  "<p>Genelde alt sağdaki <strong>pompa motoru</strong> kaynaklıdır; içindeki pervane suyu "
  "çekmiyordur. En yaygın sebep <strong>para, çorap ve ceplerden çıkan atıkların</strong> "
  "pompayı tıkamasıdır. Pompa değişimi parçayla birlikte yaklaşık "
  "<strong>2.500 TL</strong>.</p>"),
 ("Makine sıkma yapmıyor, neden?",
  "<p>İki sebep var: <strong>motor kömürleri</strong> zayıflamıştır, ya da makine "
  "<strong>suyu boşaltamadığı için</strong> sıkmaya hiç girmiyordur. Sıkma şikâyetiyle "
  "gittiğimiz cihazlarda sorun çoğu zaman sıkmada değil, suyu boşaltamamaktadır.</p>"),
 ("Çamaşır makinesi çok ses yapıyor ve sallanıyor?",
  "<p>İki kökten gelir: <strong>kazan ve rulman</strong> bozulması, veya "
  "<strong>amortisörler.</strong> Amortisörler dengesizse kazan dengesiz çalışır — "
  "ses ve sallanma aynı sebebin iki görünümüdür.</p>"),
 ("Makinenin altından su geliyor?",
  "<p>İki noktaya bakıyoruz: <strong>körük lastiği</strong> ve "
  "<strong>arka hortum bağlantıları.</strong> Kaçağın yerini bulmak için makinenin bir "
  "program boyunca çalıştırılması gerekebiliyor.</p>"),
 ("Çamaşırlarım kötü kokuyor, makineden mi?",
  "<p>Makine <strong>suyu ısıtmıyorsa</strong> koku yapar; hep düşük sıcaklıkta çalışan makine "
  "iyi temizleyemez. Sıcak su hem temizler hem kokuyu önler. "
  "<strong>Yanık kokusu</strong> gelmesi ise ayrı bir durumdur: kazan körük lastiğine "
  "sürtüyor olabilir.</p>"),
 ("Makine deterjanı çekmiyor?",
  "<p><strong>Su basıncı düşüktür.</strong> Sebep genelde <strong>ventil</strong> "
  "veya <strong>kireçtir.</strong></p>"),
 ("Çamaşırlar temiz çıkmıyor?",
  "<p>Makine <strong>suyu ısıtmıyordur.</strong> Sıcak su olmadan deterjan işini görmez — "
  "programı değiştirmek çözmüyorsa rezistansa bakılması gerekir.</p>"),
 ("Kapı kilidi arızasında kilidi zorlayabilir miyim?",
  "<p><strong>Zorlamayın.</strong> Sahadaki en önemli uyarımız bu: kapı kilidi arızası "
  "<strong>çok sık kartı da patlatıyor.</strong> Kilit sıkıştığında zorlamak, kilit "
  "değişimiyle bitecek bir işi kart değişimine kadar büyütebiliyor. Kapı açılmıyorsa "
  "bize haber verin.</p>"),
 ("Rezistans neden bozuluyor?",
  "<p>Makine uzun süre çalıştıkça içinde <strong>kalıntı ve kireç</strong> birikir; bu da "
  "rezistansı bozar. Sık değişen parçalardan biridir.</p>"),
],
"bulasik-makinesi": [
 ("Bulaşık makinesi su almıyor?",
  "<p><strong>Su ventili</strong> değişmelidir — çamaşır makinesindeki mantığın aynısı "
  "geçerlidir.</p>"),
 ("Bulaşık makinesi suyu boşaltmıyor?",
  "<p><strong>Pompa motoru</strong> kaynaklıdır. İçine <strong>limon kabuğu</strong>, yemek "
  "artığı ve pislik girer, pompayı tıkar.</p>"),
 ("Bulaşık makinesi hiç çalışmıyor?",
  "<p><strong>Kart arızası</strong> olabilir. Ayrıca makine suyu alamıyorsa veya "
  "boşaltamıyorsa <strong>programa hiç girmez</strong> — yani \"çalışmıyor\" görünen "
  "cihazın sorunu çoğu zaman su tarafındadır.</p>"),
 ("Bulaşıklar kirli çıkıyor?",
  "<p>Suyu püskürten dönen kollar — bizim deyişimizle <strong>pervane</strong>, teknik adıyla "
  "<strong>fıskiye</strong> — tıkanmış veya dönmüyordur. Bunlar düzenli açılıp temizlenmesi "
  "gereken parçalardır; değiştiğinde daha hızlı ve düzgün döner. Bazen sebep yanlış veya "
  "az deterjandır.</p>"),
 ("Bulaşık makinesi koku yapıyor?",
  "<p>Nadir gelen bir şikâyet. Sebebi cihazın <strong>alt tarafındaki contadır</strong>; "
  "uzun süre değişmezse koku yapar.</p>"),
 ("Bulaşık makinesi su kaçırıyor, nereden?",
  "<p>Cihazın içi baştan sona suyla çalışır; kaçak noktaları şunlardır: alttaki "
  "<strong>dört yollu vanalar</strong>, <strong>conta araları</strong>, "
  "<strong>su girişleri</strong> ve <strong>patlak pervane/fıskiye.</strong></p>"),
 ("Makine aşırı köpürüyor?",
  "<p>Sebep <strong>yanlış deterjan kullanımıdır.</strong> Bazı kullanıcılar \"daha iyi "
  "temizlesin\" diye makineye farklı ürünler ekliyor; bu köpüğü artırıyor ve cihaza "
  "zarar veriyor.</p>"),
 ("Bulaşık makinesi kurutmuyor?",
  "<p><strong>Pompa sistemdeki suyu boşaltmıyordur</strong> — yani pompa motoru "
  "arızalıdır.</p>"),
 ("Filtreyi ne sıklıkla temizlemeliyim?",
  "<p><strong>3 ayda bir</strong> alttaki filtre açılıp temizlenmeli. İhmal edilince yıkama "
  "verimi düşer; uzun vadede pompa arızasına kadar gidebiliyor. Hiçbir masrafı olmayan tek "
  "bakım adımı budur.</p>"),
 ("Rezistans arızası neden markaya göre farklı fiyatlanıyor?",
  "<p>Yapı farkından. <strong>Bosch'ta rezistans motorun içindedir</strong> — arızalandığında "
  "komple motor değişir, maliyet yükselir. <strong>Arçelik, Vestel ve diğer markalarda "
  "rezistans motorun yanındadır</strong> — ayrı değişir, daha makul olur.</p>"),
 ("Bulaşık makinesi parça değişimi ne kadar?",
  "<p>Markaya göre değişmekle birlikte genelde <strong>1.000 – 2.000 TL</strong> civarında. "
  "Kesin fiyatı yerinde tespitten sonra, işleme başlamadan önce söylüyoruz.</p>"),
],
"derin-dondurucu": [
 ("Derin dondurucuda en sık hangi arızalar çıkıyor?",
  "<p>Üç arıza öne çıkıyor: <strong>termostat</strong>, <strong>gaz kaçağı</strong> ve "
  "<strong>kompresör (motor).</strong></p>"),
 ("Derin dondurucu kompresör değişimi ne kadar?",
  "<p><strong>8.000 – 10.000 TL</strong> aralığında. Fiyat cihazın litresine göre değişir; "
  "400, 500, 600 ve 800 litre modellerde onarım yapıyoruz. Buzdolabına göre genelde biraz "
  "daha düşük kalıyor.</p>"),
 ("Derin dondurucu soğutmuyor, ne olmuş olabilir?",
  "<p>Buzdolabındaki mantığın aynısı geçerli: ya <strong>gazla ilgili bir sorun</strong> "
  "ya da <strong>kompresör</strong> çalışmıyordur. Motor kaynaklıysa sistem açılır, kaynak "
  "yapılır, tıkanma giderilir, vakum çekilir ve gaz basılır.</p>"),
 ("Derin dondurucu çağrısı öncelikli mi?",
  "<p>Evet. Derin dondurucu ve buzdolabı çağrılarını <strong>her zaman sıranın önüne "
  "alıyoruz</strong>, çünkü içindeki gıdanın tamamı bozulur. Bu bizim kendi çalışma "
  "önceliğimizdir.</p>"),
 ("Soğutma sistemlerinde belgeli misiniz?",
  "<p>Evet. <strong>T.C. Millî Eğitim Bakanlığı İş Yeri Açma Belgesi</strong> sahibiyiz; "
  "meslek alanı Tesisat Teknolojisi ve İklimlendirme, <strong>meslek dalı Soğutma "
  "Sistemleri.</strong> Soğutma bizim asıl uzmanlık alanımız.</p>"),
],
}


def marka_sss(m):
    """Marka sayfası SSS'i — ortak gerçekler + markanın ailesine göre değişen madde."""
    ad = m["ad"]
    if m["aile"] == "bsh":
        yapi = (f"<p>{ad} bulaşık makinelerinde <strong>rezistans (ısıtıcı) motorun "
                f"içindedir.</strong> Arızalandığında ayrı değiştirilemez, "
                f"<strong>komple motor değişir</strong> — bu da onarımı Arçelik veya Vestel gibi "
                f"markalara göre belirgin şekilde pahalı hâle getirir. Bunu telefonda arızayı "
                f"dinlediğimizde söylüyoruz ki sürprizle karşılaşmayın.</p>")
    elif m["aile"] == "kore":
        yapi = (f"<p>{ad} buzdolaplarında <strong>no-frost</strong> sistem yaygındır. No-frost "
                f"modellerde buzlanma olasılığı düşüktür; buz görüyorsanız akla ilk gelen, buzu "
                f"eriten <strong>rezistansın çalışmamasıdır.</strong> Bu markalarda elektronik "
                f"kart ve fan kaynaklı arızalar da öne çıkıyor; kart arızasında motoru "
                f"değiştirmeden önce <strong>kartın motora çıkış verip vermediğine</strong> "
                f"bakıyoruz.</p>")
    else:
        yapi = (f"<p>{ad} bulaşık makinelerinde <strong>rezistans motorun yan tarafındadır.</strong> "
                f"Arızalandığında motorun tamamı değil yalnızca rezistans değişir; bu da aynı "
                f"arızanın Bosch, Siemens ve Profilo gibi markalara göre "
                f"<strong>çok daha uygun</strong> çözülmesi demektir.</p>")
    return [
     (f"Batman'da {ad} servisi aynı gün geliyor mu?",
      "<p>Batman merkezde arıza bildiriminden sonra <strong>genellikle 2 saat içinde</strong> "
      "adreste oluyoruz. Beşiri, Gercüş, Hasankeyf, Kozluk ve Sason'a <strong>en geç 1 gün "
      "içinde</strong> geliyoruz.</p>"),
     (f"{ad} yetkili servisi misiniz?",
      f"<p>Hayır, biz <strong>özel (bağımsız) teknik servisiz.</strong> Cihazınız garanti "
      f"kapsamındaysa önce {ad} yetkili servisine gitmenizi kendimiz öneriyoruz — işlem ücretsiz "
      f"olabilir ve bağımsız bir servise yaptıracağınız müdahale garantinizi düşürebilir. "
      f"<strong>Garanti süresi dolmuşsa</strong> bize gelmeniz genellikle hem daha hızlı hem "
      f"daha uygun oluyor.</p>"),
     (f"{ad} cihazlarda dikkat ettiğiniz özel bir nokta var mı?", yapi),
     (f"{ad} yedek parçası bulunuyor mu?",
      "<p>Parça elimizde yoksa sipariş ediyor, <strong>1–2 gün içinde</strong> takılmasını "
      "sağlıyoruz. Süreç boyunca sizi bilgilendiriyoruz.</p>"),
     (f"{ad} onarımına garanti veriyor musunuz?",
      "<p>Evet. Kullandığımız <strong>tüm parçalar 1 yıl garantilidir.</strong></p>"),
     (f"Hangi {ad} cihazlarına bakıyorsunuz?",
      f"<p>Dört cihaz grubunda çalışıyoruz: <strong>buzdolabı, çamaşır makinesi, bulaşık "
      f"makinesi ve derin dondurucu.</strong> {ad} markasında da bu dört cihazın onarımını "
      f"yapıyoruz.</p>"),
     (f"{ad} onarımı evde mi yapılıyor?",
      "<p>Onarımların <strong>büyük çoğunluğunu cihazı yerinden oynatmadan evinizde</strong> "
      "tamamlıyoruz; parçayı orada takıyoruz. Atölyeye çekmek istisnai bir durumdur — en tipik "
      "örneği buzdolabında gaz kaçağının gövde içinde olması ve arkanın kesilmesi gereken "
      "hâllerdir.</p>"),
     ("Servis ücreti ne kadar, onarım yaptırmazsam da alınıyor mu?",
      "<p>Servis ücreti Batman merkezde ve ilçelerde <strong>600 TL</strong>, Batman köylerinde "
      "<strong>1.000 TL</strong>'dir. İlçeler için ayrıca yol ücreti almıyoruz. "
      "Arızayı yerinde tespit edip maliyeti söylüyoruz; onarımı "
      "yaptırmak istemezseniz yalnızca bu ücret alınır. <strong>Onarımı bize yaptırırsanız "
      "çağrı ücretinde indirim uygulanır.</strong></p>"),
    ]


def bolge_sss(b):
    """Bölge sayfası SSS'i — merkez ve ilçe için varış/ücret cevapları ayrışır."""
    ad = b["ad"]
    if b["merkez_mi"]:
        varis = ("<p>Batman merkezde arıza bildiriminden sonra <strong>genellikle 2 saat "
                 "içinde</strong> adreste oluyoruz; en kötü ihtimalle 2–3 saat. Servis genelde "
                 "aynı ziyarette sonuçlanıyor.</p>")
        ucret = ("<p>Batman merkez için servis ücretimiz <strong>600 TL</strong>. Aynı ücret "
                 "<strong>ilçelerde de geçerlidir</strong> — ilçe için ayrıca yol ücreti "
                 "almıyoruz. Batman'a bağlı <strong>köy adreslerinde 1.000 TL</strong>'dir. "
                 "Bu ücret arızanın yerinde "
                 "tespiti karşılığıdır; onarımı yaptırmak istemezseniz yalnızca bunu ödersiniz. "
                 "<strong>Onarımı bize yaptırırsanız çağrı ücretinde indirim uygulanır.</strong></p>")
        nerede = ("<p>Dükkânımız <strong>Fatih Mahallesi 3206. Sokak No:12, Batman Merkez</strong> "
                  "adresinde. Cihazı getirmenize gerek yok; onarımların büyük çoğunluğunu "
                  "evinizde tamamlıyoruz.</p>")
    else:
        varis = (f"<p>{ad} adreslerine varış süremiz <strong>en geç 1 gündür.</strong> Merkezdeki "
                 f"gibi aynı saat içinde olmuyor, ama çağrınız sıraya alınır ve bir günü "
                 f"geçmez.</p>")
        ucret = (f"<p><strong>600 TL</strong> — Batman merkezle aynı. {ad} ilçe olduğu için "
                 f"<strong>ayrıca yol ya da mesafe ücreti almıyoruz.</strong> Bu ücret arızanın "
                 f"yerinde tespiti karşılığıdır; onarımı yaptırmak istemezseniz yalnızca bunu "
                 f"ödersiniz. <strong>Onarımı bize yaptırırsanız çağrı ücretinde indirim "
                 f"uygulanır.</strong> (Batman'a bağlı köy adreslerinde ücret 1.000 TL'dir.)</p>")
        nerede = (f"<p>Dükkânımız Batman Merkez'de (Fatih Mahallesi 3206. Sokak No:12), ama "
                  f"{ad} dahil tüm ilçelere gidiyoruz. Onarımların büyük çoğunluğunu cihazı "
                  f"yerinden oynatmadan evinizde tamamlıyoruz.</p>")
    return [
     (f"{ad} bölgesine ne kadar sürede geliyorsunuz?", varis),
     (f"{ad} için servis ücreti ne kadar?", ucret),
     (f"{ad} dışında nerelere gidiyorsunuz?", nerede),
     ("Telefonda arızayı nasıl anlatmalıyım?",
      "<p>Cihazın <strong>markasını, modelini ve belirtiyi</strong> mümkün olduğunca ayrıntılı "
      "anlatın. Mümkünse arızanın <strong>sesini veya görüntüsünü WhatsApp'tan gönderin</strong> "
      "— tespiti oradan büyük ölçüde yapabiliyoruz. Bunu isteme sebebimiz, olası parçayı "
      "önceden hazırlayıp tek ziyarette işi bitirmek.</p>"),
     ("Hangi cihazları onarıyorsunuz?",
      "<p>Dört cihaz grubunda çalışıyoruz: <strong>buzdolabı, çamaşır makinesi, bulaşık "
      "makinesi ve derin dondurucu.</strong> Marka ayrımı yapmıyoruz.</p>"),
     ("Aynı anda birden fazla çağrı olursa hangisi öne geçiyor?",
      "<p><strong>Buzdolabı ve derin dondurucu.</strong> Bir çamaşır makinesi bir gün "
      "bekleyebilir, ama duran bir buzdolabındaki gıdanın tamamı bozulur. Bu, sahada "
      "uyguladığımız gerçek sıralamadır.</p>"),
     ("Takılan parçalar garantili mi?",
      "<p>Evet. Kullandığımız <strong>tüm parçalar 1 yıl garantilidir.</strong></p>"),
     ("Onarım yaptırmazsam ne ödüyorum?",
      "<p>Yalnızca <strong>servis (yol) ücretini.</strong> Arızayı tespit edip maliyeti "
      "işleme başlamadan önce söylüyoruz; onarımı istemezseniz başka bir bedel çıkmaz. "
      "Masraf cihazın değerine yaklaşıyorsa bunu da açıkça belirtiyoruz.</p>"),
    ]


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

    govde += saha_videolari(
        CIHAZ_VIDEO.get(c["slug"], []),
        f"Batman'da yaptığımız {c['ad_tamlama']} onarımları",
        "Aşağıdaki görüntüler stok video değil — Batman'da kendi yaptığımız onarımlardan.",
        alt=False)
    govde += sss_bolumu(CIHAZ_SSS[c["slug"]],
                        f"Batman {c['ad_tamlama']} tamiri hakkında sık sorulan sorular",
                        alt=True)
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
</div></div></section>

{sss_bolumu(marka_sss(m), f"Batman {m['ad']} servisi hakkında sık sorulan sorular", alt=True)}"""


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
    ucret_sat = ("<strong>600 TL</strong>" if b["merkez_mi"] else
                 "<strong>600 TL</strong> — ilçe olduğu için ayrıca yol ücreti almıyoruz")

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
</div></section>

{saha_videolari(BOLGE_VIDEO.get(b['slug'], []), "Sahadan görüntüler",
                "Aşağıdaki görüntüler stok video değil — Batman'da kendi yaptığımız onarımlardan.")}
{sss_bolumu(bolge_sss(b), f"{b['ad']} beyaz eşya servisi hakkında sık sorulan sorular")}"""
