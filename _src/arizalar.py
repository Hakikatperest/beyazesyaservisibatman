# -*- coding: utf-8 -*-
"""Arıza rehberi içerikleri.

Kaynak: _src/bilgi.md — işletmenin kendi saha anlatımı.
⚠️ Buraya UYDURMA teknik bilgi ekleme. Yeni arıza eklenecekse önce işletmeye sor.

Her kayıt:
  slug, cihaz(slug), soru(H1), kisa(meta+kart özeti), govde(HTML), gorsel, video, poster
"""

ARIZALAR = [

# ============================================================ BUZDOLABI
{
 "slug": "buzdolabi-sogutmuyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Soğutmuyor?",
 "kisa": "Buzdolabı soğutmuyorsa sebep genellikle gaz kaçağı veya kompresör (motor) arızasıdır. "
         "Batman'da aynı gün yerinde tespit ediyoruz.",
 "gorsel": "buzdolabi-motor-degisim.webp",
 "video": "buzdolabi-koprosor-degisimi.mp4", "poster": "buzdolabi-motor-degisim2.webp",
 "video_etiket": "Kompresör değişimi — saha çekimi",
 "govde": """
<p>Buzdolabının çalışıp da soğutmamasının arkasında pratikte iki sebep vardır:
<strong>gazla ilgili bir sorun</strong> veya <strong>kompresörün (halk arasındaki adıyla motorun)</strong>
görevini yapamaması. Dolabın içi ışık yanıyor, fan dönüyor olabilir — bu cihazın soğuttuğu anlamına gelmez.
Soğutmayı yapan şey motorun çalışıp gazı sisteme dağıtmasıdır.</p>

<h2>Motor kaynaklı soğutmama</h2>
<p>Motor devreye girmiyorsa ya da girip de basınç üretemiyorsa dolap soğumaz. Bu durumda sistem açılır,
gerekli noktaya <strong>kaynak</strong> yapılır, hattaki <strong>tıkanma</strong> giderilir, ardından
<strong>vakum</strong> çekilip gaz basılır. Bu işlem sırasında sistemin içindeki nemin tamamen alınması
gerekir; vakum atlanırsa yeni gaz da kısa sürede sorun çıkarır.</p>

<h2>Gaz kaçağı kaynaklı soğutmama</h2>
<p>Gaz kaçağında belirleyici olan, <strong>kaçağın nerede olduğudur</strong>:</p>
<ul>
<li><strong>Gözle görünen bir noktadaysa</strong> kaynak yapılır ve iş çoğu zaman evinizde biter.</li>
<li><strong>Görünmeyen bir yerdeyse</strong> dolabın arkasının kesilmesi gerekir. Bu, uğraş ve masraf
isteyen bir iştir; cihaz atölyeye çekilir.</li>
</ul>

<div class="kutu"><b>Dürüst tavsiyemiz</b>
<p>Kaçak görünmeyen bir yerdeyse maliyet yaklaşık 5.000 TL'yi buluyor (≈3.000 TL parça + nakliye).
Cihazın yaşına ve değerine göre bu masrafın mantıklı olmadığı durumlar oluyor ve
<strong>müşterilerimize açıkça "bunu yaptırmayın" dediğimiz de oluyor.</strong>
Kararı verebilmeniz için maliyeti işleme başlamadan söylüyoruz.</p></div>

<h2>Kompresör değişimi ne kadar tutuyor?</h2>
<p>Buzdolabı kompresör değişimi <strong>8.000 – 11.000 TL</strong> aralığında değişir. Fiyatı belirleyen
üç şey var: kullanılan gazın tipi, motorun büyüklüğü ve dolabın kaç litre olduğu. Derin dondurucularda
bu rakam genelde daha aşağıda kalır.</p>
<p>Kompresör değişimini <strong>çoğunlukla evinizde</strong> yapabiliyoruz; cihazın atölyeye çekilmesi
istisna bir durumdur.</p>
""",
},

{
 "slug": "buzdolabi-ses-yapiyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Ses Yapıyor?",
 "kisa": "Buzdolabındaki sesin neredeyse tek kaynağı fandır; bazen buzmatik ses yapar. "
         "Batman'da fan değişimi ortalama 2.000 TL.",
 "gorsel": "buzdolabi-fan-degisim.webp",
 "video": "buzdolabi-arka-fan-sesi.mp4", "poster": "buzdolabi-fan-degisim2.webp",
 "video_etiket": "Arıza yapan buzdolabı fanının sesi",
 "govde": """
<p>Buzdolabından gelen anormal sesin kaynağını daraltmak aslında kolaydır:
<strong>dolabın içinde ses üretebilecek hareketli parça neredeyse yalnızca fandır.</strong>
Sekiz yılı aşkın sahada, ses şikâyetiyle gittiğimiz cihazların çok büyük bölümünde sorun fandan çıktı.</p>

<h2>Fan neden ses yapar?</h2>
<ul>
<li><strong>Fan buza çarpıyordur.</strong> Etrafında oluşan buz kütlesine kanat değdiğinde ritmik,
tekrar eden bir ses duyulur.</li>
<li><strong>Arka pervane sıkışmıştır.</strong> Yatağı zorlanan fan zorlanma sesi verir.</li>
<li><strong>Fan yatağı yorulmuştur.</strong> Fan sürekli çalışan bir parçadır; üzerinden geçen
elektriksel akım yükseldiğinde arızalanır.</li>
</ul>

<h2>Buzmatikten gelen ses</h2>
<p>Buz yapma ünitesi (buzmatik) bulunan modellerde ses bu üniteden de gelebilir. Bu ihtimal fandan
sonra ikinci sırada gelir ve ayırt edilmesi tecrübe ister — sesin dolabın hangi bölmesinden geldiği
ve hangi çevrimde ortaya çıktığı belirleyicidir.</p>

<h2>Fan değişimi ücretleri</h2>
<ul>
<li><strong>Standart modeller:</strong> parça 600–700 TL, işçilikle birlikte yaklaşık
<strong>2.000 TL</strong>.</li>
<li><strong>Üst segment modeller:</strong> yalnızca parça 3.000–3.200 TL'ye çıkabiliyor; bu durumda
işçilik 1.000–1.100 TL ekleniyor ve toplam <strong>5.000 TL'ye</strong> kadar çıkabiliyor.</li>
</ul>
<p>Fan değişimi evde yapılan bir iştir; cihazı götürmemize gerek kalmaz.</p>

<div class="kutu"><b>Sesi görmezden gelmeyin</b>
<p>Buza çarpan bir fan zamanla kanatlarını ve yatağını yorar. Erken müdahalede yalnızca buz
çözülerek çözülen bir sorun, beklendiğinde fan değişimine dönüşebiliyor.</p></div>
""",
},

{
 "slug": "buzdolabi-su-akitiyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Su Akıtıyor?",
 "kisa": "Buzdolabı su akıtıyorsa sebep genellikle tıkanmış arka giderdir. "
         "Parça gerektirmeyen, çoğu zaman tek ziyarette biten bir iştir.",
 "gorsel": "buzdolabi-mentese-degisimi.webp",
 "video": "buzdolabi-arka-hortum-gider-temizligi.mp4", "poster": "buzdolabi-mentese-degisimi2.webp",
 "video_etiket": "Arka gider hortumu temizliği",
 "govde": """
<p>Buzdolabında su birikmesi kulağa ciddi gelse de, aslında <strong>en ucuz çözülen arızalardan
biridir</strong> — çünkü çoğu zaman parça değişimi gerektirmez.</p>

<h2>Suyun kaynağı</h2>
<p>Buzdolabı çalışırken soğutucu yüzeyde buz oluşur, çevrim değiştiğinde bu buz çözülür. Çözülen su
rastgele akmaz; <strong>dolabın arkasındaki gider kanalından</strong> tahliye edilir. Bu kanal
zamanla yemek artığı, toz ve buz kalıntısıyla tıkanır.</p>
<p>Gider tıkandığında su gidecek yer bulamaz ve dolabın içinde birikir.
<strong>Gider tamamen kapalıysa su ön taraftan, kapağın altından dışarı akmaya başlar</strong> —
mutfak zemininde gördüğünüz su genellikle budur.</p>

<h2>Çözüm</h2>
<p>Gider kanalı açıldığında sorun biter. Bu, parça değişimi olmayan bir iştir; bu tür ziyaretlerde
genellikle yalnızca <strong>servis ücreti</strong> alıyoruz.</p>

<div class="kutu"><b>Neden kendiniz denememelisiniz</b>
<p>Gider kanalını açmak için kullanılan yanlış bir alet, kanalın arkasındaki tahliye kabını veya
soğutucu boruyu delebiliyor. O noktadan sonra iş gaz kaçağına dönüşüyor ve maliyet katlanıyor.</p></div>
""",
},

{
 "slug": "buzdolabi-buzlanma-yapiyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Buzlanma Yapıyor?",
 "kisa": "Statik buzdolaplarında buzlanma normal; no-frost modellerde rezistans arızasını gösterir. "
         "Batman'da yerinde tespit.",
 "gorsel": "buzdolabi-termostat-degisimi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Buzlanma şikâyetinde ilk sorduğumuz şey şudur: <strong>cihazınız statik mi, no-frost mu?</strong>
Çünkü ikisinde buzlanmanın anlamı tamamen farklıdır.</p>

<h2>Statik buzdolapları</h2>
<p>Statik modellerde soğutma, dolabın iç yüzeyinden yayılarak gerçekleşir. Bu yapıda
<strong>etraftan buzlanma olması cihazın doğasında vardır.</strong> Buz kalınlaştıkça soğutma verimi
düşer, bu yüzden düzenli olarak çözdürülmesi gerekir. Bu bir arıza değildir.</p>

<h2>No-frost buzdolapları</h2>
<p>No-frost modellerde buzlanma olasılığı çok düşüktür — sistem zaten buz oluşumunu engellemek üzere
kurulmuştur. Bu cihazlarda buzlanma görüyorsanız akla gelen ilk şey
<strong>rezistansın çalışmamasıdır.</strong> Rezistans, oluşan buzu belirli aralıklarla eriten
ısıtıcı parçadır; devre dışı kaldığında buz birikmeye başlar ve fanın önünü kapatır.</p>

<div class="kutu"><b>Buzlanma tek başına gelmez</b>
<p>No-frost bir dolapta buz biriktikçe fan buza çarpmaya başlar. Bu yüzden buzlanma şikâyeti çoğu zaman
bir süre sonra <a href="/buzdolabi-ses-yapiyor/">ses şikâyetine</a> dönüşür. İki belirti birlikte
görülüyorsa tespit netleşir.</p></div>

<h2>Termostat ihtimali</h2>
<p>Buzlanmayla birlikte dolap hiç durmadan çalışıyorsa devreye
<a href="/buzdolabi-surekli-calisiyor/">termostat arızası</a> girer. Termostat değişimi işçilik dahil
yaklaşık <strong>1.500 TL</strong>; parçası pahalı modellerde 2.000 TL'ye kadar çıkabiliyor.</p>
""",
},

{
 "slug": "buzdolabi-surekli-calisiyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Sürekli Çalışıyor, Hiç Durmuyor?",
 "kisa": "Buzdolabı hiç durmadan çalışıyorsa termostat arızalıdır. Değişimi işçilik dahil ortalama 1.500 TL.",
 "gorsel": "buzdolabi-termostat-degisimi2.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Sağlıklı bir buzdolabı sürekli çalışmaz. İç sıcaklık hedeflenen dereceye indiğinde motor durur,
sıcaklık yükseldiğinde tekrar devreye girer. Bu açılıp kapanmayı yöneten parça
<strong>termostattır.</strong></p>

<h2>Termostat bozulunca ne olur?</h2>
<p>Termostat iki farklı şekilde arızalanabilir ve ikisi de birbirinin tam tersi belirti verir:</p>
<ul>
<li><strong>Motoru hiç durdurmaz.</strong> Dolap kesintisiz çalışır. Elektrik faturası yükselir,
kompresör dinlenemediği için ömrü kısalır.</li>
<li><strong>Motoru hiç devreye almaz.</strong> Bu durumda dolap <a href="/buzdolabi-sogutmuyor/">hiç
soğutmaz</a>.</li>
</ul>
<p>Yani "hiç durmuyor" ile "hiç soğutmuyor" şikâyetleri aynı parçadan kaynaklanabiliyor.</p>

<div class="kutu uyari"><b>Beklemek pahalıya patlıyor</b>
<p>Sürekli çalışan bir kompresör dinlenemez. Termostat arızasını uzun süre görmezden gelmek,
1.500 TL'lik bir işi <a href="/buzdolabi-kompresor-arizasi/">8.000–11.000 TL'lik kompresör
değişimine</a> dönüştürebiliyor. Dolabınız günlerdir hiç durmuyorsa bekletmeyin.</p></div>

<h2>Ücret</h2>
<p>Termostat değişimi işçilik dahil ortalama <strong>1.500 TL</strong>'dir. Parçası pahalı olan
modellerde toplam 2.000 TL'ye kadar çıkabilir. İşlem evde yapılır.</p>
""",
},

{
 "slug": "buzdolabi-calismiyor", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Neden Hiç Çalışmıyor?",
 "kisa": "Buzdolabı hiç çalışmıyorsa sebep motor, elektrik tesisatı veya karttır. "
         "Batman merkezde genellikle 2 saat içinde yerindeyiz.",
 "gorsel": "buzdolabi-kart-degisim.webp",
 "video": "buzdolabi-kart-degisim.mp4", "poster": "buzdolabi-kart-degisimi.webp",
 "video_etiket": "Buzdolabı kart değişimi",
 "govde": """
<p>Dolap tamamen sessizse ve içi ışık dahil hiç tepki vermiyorsa üç ihtimal üzerinde duruyoruz.</p>

<h2>1. Elektriksel sebepler</h2>
<p>En basit ihtimalle başlıyoruz: priz, kablo ve sigorta. Bu kontrolü siz de yapabilirsiniz —
dolabı farklı bir prize takmak birçok çağrıyı gereksiz kılıyor.</p>

<h2>2. Kart arızası</h2>
<p>Elektrik geliyor ama cihaz komut üretmiyorsa devreye kart girer.
<strong>Kart motora elektrik vermiyorsa dolap çalışmaz</strong> — motor sağlam olsa bile.
Bu yüzden "motor yandı" teşhisini koymadan önce kartın çıkışını kontrol etmek gerekir.</p>

<div class="kutu"><b>Doğru sıralama para kazandırır</b>
<p>Kart kontrolü atlanıp doğrudan motor değişimine gidilirse, 8.000–11.000 TL'lik bir masraf
gereksiz yere yapılmış olur. Biz her zaman önce kartın motora çıkış verip vermediğine bakıyoruz.</p></div>

<h2>3. Kompresör (motor) arızası</h2>
<p>Kart sağlamsa ve motora elektrik gidiyor ama motor dönmüyorsa sorun
<a href="/buzdolabi-kompresor-arizasi/">kompresördedir</a>.</p>

<h2>Bu arızada aciliyet</h2>
<p>Hiç çalışmayan bir buzdolabı, içindeki gıdanın bozulması demektir. Bu yüzden
<strong>buzdolabı ve derin dondurucu çağrılarını her zaman öne alıyoruz.</strong> Batman merkezde
genellikle 2 saat içinde adresteyiz.</p>
""",
},

{
 "slug": "buzdolabi-kompresor-arizasi", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Kompresörü (Motoru) Neden Yanar?",
 "kisa": "Kompresör tıkanma, fazla akım, fazla gaz veya gaz kaçağı yüzünden yanar. "
         "Değişimi 8.000–11.000 TL, çoğunlukla evde yapılır.",
 "gorsel": "buzdolabi-motor-degisim3.webp",
 "video": "buzdolabi-koprosor-degisimi.mp4", "poster": "buzdolabi-motor-degisim.webp",
 "video_etiket": "Kompresör (motor) değişimi",
 "govde": """
<p>Kompresör buzdolabının kalbidir; gazı sıkıştırıp sisteme dağıtan parçadır.
Müşterilerimizle konuşurken biz de kısaca <strong>"motor"</strong> diyoruz.
Yanması nadir ama pahalı bir arızadır — ve neredeyse her zaman
<strong>başka bir sorunun sonucudur.</strong></p>

<h2>Kompresörü yakan dört sebep</h2>
<ol>
<li><strong>Tıkanma.</strong> Soğutucu hattı tıkalıysa kompresör basamadığı bir yüke karşı çalışır
ve zorlanarak yanar.</li>
<li><strong>Fazla akım.</strong> Şebekeden gelen aşırı akım sargıları bozar.</li>
<li><strong>Fazla gaz.</strong> Sisteme gereğinden çok gaz basılmışsa kompresör sürekli aşırı
basınca karşı çalışır.</li>
<li><strong>Gaz kaçağı.</strong> Gaz azaldıkça kompresör soğuyamaz; yağlama ve soğutma görevini
gazın kendisi yaptığı için susuz kalmış gibi çalışır ve yanar.</li>
</ol>

<div class="kutu uyari"><b>Sonuç değil, sebep önemli</b>
<p>Dördüncü maddeye dikkat: <strong>gaz kaçağı giderilmeden takılan yeni kompresör de yanar.</strong>
Bu yüzden motor değiştirilirken kaçağın bulunup kapatılması, sistemin vakumlanması ve doğru miktarda
gaz basılması şart. "Sadece motoru değiştirelim" yaklaşımı parayı ikinci kez ödetiyor.</p></div>

<h2>Kompresör değişimi ücreti</h2>
<p><strong>8.000 – 11.000 TL</strong> aralığındadır. Fiyatı belirleyen üç etken: gazın tipi, motorun
büyüklüğü ve dolabın litresi. <a href="/derin-dondurucu-motor-arizasi/">Derin dondurucularda</a>
bu rakam 8.000–10.000 TL bandında kalıyor.</p>
<p>Kompresör değişimini <strong>müşterinin evinde</strong> yapabiliyoruz. Cihazın atölyeye çekilmesi
yalnızca gaz kaçağının görünmeyen bir yerde olduğu durumlarda gerekiyor.</p>
""",
},

{
 "slug": "buzdolabi-gaz-kacagi", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Gaz Kaçağı Nasıl Anlaşılır ve Onarılır?",
 "kisa": "Gaz kaçağının maliyeti kaçağın yerine bağlı: görünen noktada kaynak yeterli, "
         "görünmüyorsa dolap kesiliyor ve ~5.000 TL tutuyor.",
 "gorsel": "buzdolabi-motor-karti-degisimi.webp",
 "video": "buzdolabi-gaz-kacagi-govde-degisim.mp4", "poster": "buzdolabi-motor-karti-degisimi2.webp",
 "video_etiket": "Gaz kaçağı — gövde değişimi",
 "govde": """
<p>Buzdolabının çalışma mantığı tek cümleyle şudur: <strong>motor çalışır, gazı sisteme dağıtır.</strong>
Gaz eksildiğinde bu döngü bozulur; dolap çalışır ama soğutmaz ya da yeterince soğutmaz.</p>

<h2>Belirtiler</h2>
<ul>
<li>Motor çalışıyor, ses geliyor ama iç sıcaklık düşmüyor</li>
<li>Dondurucu bir miktar soğutuyor, alt bölme hiç soğumuyor</li>
<li>Dolap hiç durmadan çalışıyor ama hedef sıcaklığa ulaşamıyor</li>
</ul>

<h2>Maliyeti belirleyen tek soru: kaçak nerede?</h2>
<p>Gaz kaçağı onarımında işin zorluğu ve fiyatı, kaçağın <strong>görülebilir bir noktada olup
olmadığına</strong> bağlıdır.</p>
<ul>
<li><strong>Görünen noktada:</strong> kaçak kaynak edilir, sistem vakumlanır, gaz basılır.
İş çoğunlukla evinizde biter.</li>
<li><strong>Görünmeyen noktada:</strong> kaçak dolabın gövdesinin içindeki hatta demektir. Bu durumda
<strong>dolabın arkası kesilir.</strong> Cihaz atölyeye çekilir, işlem uzun sürer.</li>
</ul>

<div class="kutu"><b>Bu işi her zaman önermiyoruz</b>
<p>Görünmeyen kaçak onarımı toplamda yaklaşık <strong>5.000 TL</strong> tutuyor — yaklaşık 3.000 TL
parça, üstüne nakliye ve işçilik. Cihazın yaşı ve değeri bu masrafı karşılamıyorsa müşterimize
açıkça <strong>"bunu yaptırmayın"</strong> diyoruz. Sekiz yıllık işimizi müşteri memnuniyeti üzerine
kurduk; gereksiz masraf çıkarmak o memnuniyeti bozar.</p></div>

<h2>Gaz kaçağı kompresörü de yakar</h2>
<p>Gaz, kompresörün soğutma ve yağlama görevini de üstlenir. Kaçak sürerse
<a href="/buzdolabi-kompresor-arizasi/">kompresör yanar</a> ve masraf ikiye katlanır. Soğutmama
şikâyetini bekletmemenizin asıl sebebi budur.</p>
""",
},

{
 "slug": "buzdolabi-kapak-lastigi", "cihaz": "buzdolabi",
 "soru": "Buzdolabı Kapak Lastiği Bozulursa Ne Olur?",
 "kisa": "Şeklini kaybetmiş kapak lastiği çoğu zaman değiştirilmeden kurtarılabiliyor. "
         "Batman'da yerinde değerlendiriyoruz.",
 "gorsel": "buzdolabi-mentese-degisimi3.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Kapak lastiği buzdolabının en çok küçümsenen parçasıdır. Görevi kapağı kapatmak değil,
<strong>soğuk havayı içeride tutmaktır.</strong> Şeklini kaybetmiş bir lastik sürekli dışarıdan
sıcak hava sızdırır ve şu zinciri başlatır:</p>
<ul>
<li>Dolap hedef sıcaklığa ulaşamaz, <a href="/buzdolabi-surekli-calisiyor/">sürekli çalışır</a></li>
<li>Elektrik tüketimi belirgin şekilde artar</li>
<li>Nem içeri girdiği için <a href="/buzdolabi-buzlanma-yapiyor/">buzlanma</a> hızlanır</li>
<li>Dinlenemeyen kompresörün ömrü kısalır</li>
</ul>

<h2>Lastik her zaman değişmez</h2>
<p>İyi haber şu: <strong>şeklini kaybetmiş bir kapak lastiği çoğu zaman değiştirilmeden geri
kazanılabiliyor.</strong> Lastiğin yapısı ısıyla yumuşuyor; doğru uygulandığında eski formuna dönüp
kapağa yeniden tam oturuyor. Bu, yeni lastik masrafından kurtaran bir yöntem.</p>

<div class="kutu uyari"><b>Denemeden önce mutlaka okuyun</b>
<p>Bu işlemde <strong>ilk adım cihazın fişini çekmektir.</strong> Buzdolabı elektrikli bir cihazdır ve
kapak çevresinde yapılan işlemler doğru sırayla yapılmazsa hem cihaza hem size zarar verebilir.</p>
<p><strong>Tarifi burada adım adım vermiyoruz — bilerek.</strong> Yanlış uygulanan bir yöntem lastiği
tamamen kullanılamaz hâle getirebiliyor. Kapak lastiğinizde sorun varsa bizi arayın; yerinde bakıp
kurtarılabilir mi, değişmesi mi gerekiyor söyleyelim.</p></div>

<h2>Lastiğiniz sorunlu mu, basit bir test</h2>
<p>Bir kâğıt parçasını kapağın arasına sıkıştırıp kapatın, sonra çekin. Kâğıt hiç direnç göstermeden
çıkıyorsa lastik o noktada kapatmıyor demektir. Testi kapağın dört kenarında birkaç noktada tekrarlayın.</p>
""",
},

# ============================================================ DERİN DONDURUCU
{
 "slug": "derin-dondurucu-sogutmuyor", "cihaz": "derin-dondurucu",
 "soru": "Derin Dondurucu Neden Soğutmuyor?",
 "kisa": "Derin dondurucularda en sık üç arıza: termostat, gaz kaçağı ve kompresör. "
         "400–800 litre modellerde onarım yapıyoruz.",
 "gorsel": "buzmatik-ariza-tespit.webp",
 "video": "derin-dondurucu-motor-arizasi.mp4", "poster": "buzmatik-ariza-tespit-ve-tamir.webp",
 "video_etiket": "Derin dondurucu motor arızası",
 "govde": """
<p>Derin dondurucu arızaları buzdolabına göre daha dar bir alanda toplanır. Sahada gördüğümüz kadarıyla
şikâyetlerin neredeyse tamamı <strong>üç sebepten</strong> çıkıyor.</p>

<h2>1. Termostat arızası</h2>
<p>En sık karşılaştığımız sebep. Termostat motoru devreye almazsa cihaz hiç soğutmaz; hiç durdurmazsa
kesintisiz çalışır. İkisi de aynı parçanın arızasıdır.</p>

<h2>2. Gaz kaçağı</h2>
<p>Gaz azaldıkça soğutma zayıflar. Kaçağın görünen bir yerde olup olmaması, tıpkı
<a href="/buzdolabi-gaz-kacagi/">buzdolabında</a> olduğu gibi maliyeti belirleyen ana etkendir.</p>

<h2>3. Kompresör (motor) arızası</h2>
<p>Motor dönmüyorsa ya da basınç üretemiyorsa cihaz soğumaz.
<a href="/derin-dondurucu-motor-arizasi/">Kompresör değişimi</a> derin dondurucularda
<strong>8.000–10.000 TL</strong> aralığındadır; fiyat cihazın litresine göre değişir.</p>

<div class="kutu uyari"><b>Derin dondurucuda zaman daha kritik</b>
<p>Bir derin dondurucunun içinde genellikle aylık, hatta yıllık gıda stoğu bulunur — et, sebze, hazır
yemek. Cihaz durduğunda kayıp, onarım masrafının çok üzerine çıkabiliyor.</p>
<p>Bu yüzden <strong>dondurucu ve buzdolabı çağrılarını sıranın önüne alıyoruz.</strong> Batman
merkezde genellikle 2 saat içinde adresteyiz.</p></div>

<h2>Hangi hacimlere bakıyoruz?</h2>
<p>400, 500, 600 ve 800 litre modellerde onarım yapıyoruz. Cihazın litresi hem parça seçimini hem
fiyatı doğrudan etkiliyor.</p>
""",
},

{
 "slug": "derin-dondurucu-motor-arizasi", "cihaz": "derin-dondurucu",
 "soru": "Derin Dondurucu Motor (Kompresör) Arızası",
 "kisa": "Derin dondurucu kompresör değişimi 8.000–10.000 TL; fiyat cihazın litresine göre değişiyor.",
 "gorsel": "buzmatik-ariza-tespit-ve-tamir.webp",
 "video": "derin-dondurucu-motor-arizasi.mp4", "poster": "buzmatik-ariza-tespit.webp",
 "video_etiket": "Derin dondurucu motor arızası — saha çekimi",
 "govde": """
<p>Derin dondurucularda kompresör, buzdolabındakine göre daha ağır çalışır: hedef sıcaklık daha düşük,
kapak daha seyrek açılsa da yük daha süreklidir. Bu yüzden motor arızası bu cihazlarda gördüğümüz
başlıca üç sorundan biridir.</p>

<h2>Motorun yanma sebepleri</h2>
<p>Sebepler <a href="/buzdolabi-kompresor-arizasi/">buzdolabındakiyle aynıdır</a>: hatta tıkanma,
şebekeden gelen fazla akım, sisteme fazla gaz basılmış olması ve gaz kaçağı. Bunların içinde en sinsi
olanı gaz kaçağıdır — çünkü belirti vermeden motoru yavaş yavaş yorar.</p>

<h2>Değişim ücreti</h2>
<p>Derin dondurucu kompresör değişimi <strong>8.000 – 10.000 TL</strong> aralığındadır.
Fiyatı belirleyen ana etken <strong>cihazın litresidir</strong>: 400 litrelik bir cihazla 800 litrelik
bir cihazın motoru aynı değildir. 400, 500, 600 ve 800 litre modellerde çalışıyoruz.</p>

<div class="kutu"><b>Değişimden önce mutlaka sorulması gereken</b>
<p>Motor yandıysa <strong>neden yandığı</strong> bulunmadan yenisi takılmamalı. Sebep gaz kaçağıysa
ve kaçak kapatılmazsa yeni motor da aynı yolu izler. Biz her motor değişiminde önce sebebi tespit
ediyoruz; bu adım atlandığında müşteri aynı parayı ikinci kez ödüyor.</p></div>

<h2>İşlem nerede yapılıyor?</h2>
<p>Kompresör değişimini çoğunlukla <strong>cihazın bulunduğu adreste</strong> yapabiliyoruz.
Atölyeye çekme ihtiyacı, yalnızca gaz kaçağının gövde içinde olduğu ve arkanın kesilmesi gereken
durumlarda doğuyor.</p>
""",
},

# ============================================================ ÇAMAŞIR MAKİNESİ
{
 "slug": "camasir-makinesi-calismiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Çalışmıyor?",
 "kisa": "Çamaşır makinesine hiç elektrik gelmiyorsa sebep priz, kablo veya karttır. "
         "Batman'da aynı gün yerinde tespit.",
 "gorsel": "camasir-makinesi-karti.webp",
 "video": "camasir-makinesi-on-panel-degisim.mp4", "poster": "camasir-makinesi-karti2.webp",
 "video_etiket": "Ön panel değişimi",
 "govde": """
<p>Makine hiçbir tepki vermiyorsa — ekran yanmıyor, düğmeler çalışmıyor, hiç ses yok — sorun
büyük ihtimalle mekanik değil <strong>elektrikseldir.</strong> Üç noktaya bakıyoruz.</p>

<h2>1. Priz ve kablo</h2>
<p>En basit ihtimalle başlamak gerekir. Makineyi başka bir prize takmak, sigortayı kontrol etmek
birçok çağrıyı gereksiz kılıyor. Kablonun makineye girdiği noktada ezilme veya kopma da sık görülür.</p>

<h2>2. Kart arızası</h2>
<p>Elektrik geliyor ama makine komut üretmiyorsa devreye kart girer. Kart makinenin beynidir;
düğmelerden gelen komutu motora, ventile ve kilide dağıtır. Kart arızalandığında makine tamamen
sessiz kalabildiği gibi, bazı fonksiyonların çalışıp bazılarının çalışmadığı karışık tablolar da
oluşturur.</p>

<div class="kutu"><b>Kartı yakan en sık sebep: kapı kilidi</b>
<p>Sahada çok sık gördüğümüz bir zincir var: <strong>kapı kilidi arızalanıyor ve kartı patlatıyor.</strong>
Bu yüzden kilit arızası yaşadığınızda kilitle oynamamanızı, zorlamamanızı özellikle söylüyoruz.
Ayrıntısı <a href="/camasir-makinesi-kapi-kilidi-arizasi/">kapı kilidi arızası sayfamızda</a>.</p></div>

<h2>3. Program başlamıyor ama makine açılıyor</h2>
<p>Makine açılıyor ama program ilerlemiyorsa sorun "çalışmama" değil, koşulların sağlanmamasıdır.
Makine <a href="/camasir-makinesi-su-almiyor/">su alamıyorsa</a> veya
<a href="/camasir-makinesi-su-bosaltmiyor/">içindeki suyu boşaltamıyorsa</a> programa devam etmez.
Bu durumda kart sağlamdır, engel başka yerdedir.</p>
""",
},

{
 "slug": "camasir-makinesi-su-almiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Su Almıyor?",
 "kisa": "Çamaşır makinesi su almıyorsa sebep su ventilidir; ventil sağlamsa kart ventile elektrik "
         "vermiyordur. Ventil değişimi 1.100 TL.",
 "gorsel": "camasir-makinesi-deterjan-kutusu-degisimi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Çamaşır makinesi su almadan çalışmaz — program başlar gibi olur ama ilerlemez. Bu arızanın
adresi neredeyse her zaman aynıdır: <strong>makinenin arkasındaki su ventili.</strong></p>

<h2>Su ventili nedir, ne yapar?</h2>
<p>Ventil, şebeke suyunu makinenin içine bırakan elektrikli vanadır. Kart komut verdiğinde açılır,
istenen su alındığında kapanır. Bozulduğunda suyu hiç iletmez ve makine su almadığı için programa
devam edemez.</p>

<h2>Ventil sağlamsa sıradaki: kart</h2>
<p>Burada dikkat edilmesi gereken bir ayrım var. Ventil fiziksel olarak sağlam olabilir ama
<strong>kart ventile elektrik vermiyorsa</strong> sonuç yine aynıdır: su gelmez. Bu yüzden ventili
değiştirmeden önce üzerine gerilim gelip gelmediğine bakmak gerekir. Bu adım atlanırsa yeni ventil
takılır, sorun devam eder ve para boşa gider.</p>

<h2>Kontrol edebileceğiniz basit şeyler</h2>
<ul>
<li><strong>Musluk açık mı?</strong> Basit ama sık görülüyor.</li>
<li><strong>Giriş hortumundaki filtre tıkalı mı?</strong> Hortumun musluğa bağlandığı yerde küçük bir
süzgeç vardır, kireç ve tortu ile tıkanabilir.</li>
<li><strong>Su basıncı düşük mü?</strong> Basınç düşükse makine su almakta zorlanır. Bu aynı zamanda
<a href="/camasir-makinesi-deterjan-almiyor/">deterjanı almama</a> şikâyetinin de sebebidir.</li>
</ul>

<h2>Ücret</h2>
<p>Çamaşır makinesi su ventili değişimi <strong>1.100 TL</strong>'dir (parça 400 TL, işçilik dahil
toplam fiyat). İşlem evde yapılır, kısa sürer.</p>
""",
},

{
 "slug": "camasir-makinesi-su-bosaltmiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Su Boşaltmıyor?",
 "kisa": "Çamaşır makinesi suyu boşaltmıyorsa pompa motoru tıkalı veya arızalıdır. "
         "Pompa değişimi 2.500 TL, işlem evde yapılır.",
 "gorsel": "su-bosaltma-motoru-degisimi.webp",
 "video": "camasir-makinesi-su-bosaltma-motoru-arizasi.mp4", "poster": "su-bosaltma-motoru-degisimi2.webp",
 "video_etiket": "Su boşaltma motoru arızası",
 "govde": """
<p>Program bitiyor ama kazanda su kalıyorsa, ya da makine sıkma aşamasına hiç geçmiyorsa sorumlu
parça bellidir: <strong>pompa motoru.</strong> Genellikle makinenin alt sağ köşesinde bulunur.</p>

<h2>En sık sebep: pompanın tıkanması</h2>
<p>Pompanın içinde suyu çeken küçük bir pervane vardır. Bu pervanenin dönmesini engelleyen her şey
arıza üretir ve sahada bulduklarımız neredeyse hep aynıdır:</p>
<ul>
<li><strong>Bozuk para</strong> — açık ara birinci sırada</li>
<li><strong>Çorap</strong> — özellikle ince ve kısa olanlar</li>
<li>Ceplerde unutulan kâğıt, toka, düğme, kürdan</li>
<li>Saç ve tüy birikintisi</li>
</ul>

<div class="kutu"><b>Basit bir alışkanlık masrafı önlüyor</b>
<p>Yıkamadan önce cepleri boşaltmak ve çorapları file içinde yıkamak, bu arızayı büyük ölçüde
ortadan kaldırıyor. Pompa değişimi 2.500 TL; cep kontrolü bedava.</p></div>

<h2>Su boşaltmamak başka arızalar doğurur</h2>
<p>Makine içindeki suyu atamazsa <a href="/camasir-makinesi-sikma-yapmiyor/">sıkma aşamasına
geçmez</a> — çünkü su doluyken sıkma yapmak makineye zarar verir, bu bir güvenlik davranışıdır.
Aynı şekilde bekleyen su zamanla <a href="/camasir-makinesi-koku-yapiyor/">koku</a> da yapar.
Yani tek bir pompa arızası üç ayrı şikâyet olarak karşımıza çıkabiliyor.</p>

<h2>Ücret</h2>
<p>Çamaşır makinesi pompa değişimi <strong>2.500 TL</strong>'dir (parça 800–900 TL, işçilik dahil
toplam fiyat). Pompa yalnızca tıkanmışsa ve parça sağlamsa temizlik yeterli olur; bu durumda
maliyet servis ücretinde kalır.</p>
""",
},

{
 "slug": "camasir-makinesi-sikma-yapmiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Sıkma Yapmıyor?",
 "kisa": "Sıkma yapmamanın iki sebebi var: motor kömürlerinin zayıflaması veya makinenin suyu "
         "boşaltamaması. Batman'da yerinde tespit.",
 "gorsel": "camasir-makinesi-motor-degisimi.webp",
 "video": "camasir-makinesi-arizali-motor-sesi.mp4", "poster": "motoru-arizali-camasir-makinesi.webp",
 "video_etiket": "Arızalı çamaşır makinesi motorunun sesi",
 "govde": """
<p>Çamaşırlar sırılsıklam çıkıyorsa iki ihtimal var ve ikisi birbirinden tamamen farklı işler.
Doğru teşhis burada doğrudan paraya dokunuyor.</p>

<h2>1. Makine suyu boşaltamıyor</h2>
<p>Bu ihtimali önce elemek gerekir çünkü <strong>daha ucuz ve daha yaygındır.</strong> Makine
içindeki suyu atamazsa sıkma aşamasına hiç geçmez — bu bir arıza değil, koruma davranışıdır.
Su doluyken yüksek devirde dönmek kazana ve amortisörlere zarar verir.</p>
<p>Kazanda su kalıyorsa sorun sıkmada değil, <a href="/camasir-makinesi-su-bosaltmiyor/">pompadadır</a>.
Pompa temizlendiğinde veya değiştiğinde sıkma da düzelir.</p>

<h2>2. Motor kömürleri zayıflamış</h2>
<p>Kazan boşalıyor ama makine yine de yüksek devre çıkamıyorsa devreye motor girer. Motorun kömürleri
zamanla aşınır; kısaldıklarında motor düşük devirde döner ama sıkma için gereken yüksek devre
ulaşamaz.</p>
<p>Bu arızanın tipik seyri kademelidir: önce sıkma zayıflar, sonra tamamen kaybolur. Makine
yıkamaya devam ediyor ama çamaşırlar giderek daha ıslak çıkıyorsa bu tabloya uyuyor demektir.</p>

<div class="kutu"><b>Teşhis sırası neden önemli?</b>
<p>Bu iki sebebin maliyeti farklı. Pompa tarafı çoğu zaman temizlikle veya 2.500 TL'lik pompa
değişimiyle çözülüyor. Doğrudan motora yönelen bir teşhis, aslında pompadan kaynaklanan bir sorun için
gereksiz masraf çıkarır. Biz her zaman önce suyun boşalıp boşalmadığına bakıyoruz.</p></div>
""",
},

{
 "slug": "camasir-makinesi-ses-yapiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Ses Yapıyor ve Sallanıyor?",
 "kisa": "Çamaşır makinesinde ses ve sallanma aynı kökten gelir: kazan-rulman veya amortisör. "
         "Batman'da yerinde tespit ediyoruz.",
 "gorsel": "arizali-camasir-makinesi.webp",
 "video": "camasir-makinesi-kazan-arizasi.mp4", "poster": "motoru-arizali-camasir-makinesi.webp",
 "video_etiket": "Çamaşır makinesi kazan arızası",
 "govde": """
<p>"Makine çok ses yapıyor" ve "makine çok sallanıyor" şikâyetleri ayrı gibi görünse de sahada
<strong>aynı iki sebepten</strong> çıkar. Bu yüzden ikisini birlikte değerlendiriyoruz.</p>

<h2>1. Kazan ve rulman</h2>
<p>Kazanı taşıyan rulmanlar zamanla aşınır. Aşındıkça kazan kendi ekseninde tam oturmaz; özellikle
sıkma devrinde metalik, giderek yükselen bir uğultu duyulur. Bu ses zamanla artar — bir gün ortaya
çıkıp ertesi gün kaybolan bir ses rulman sesi değildir.</p>

<h2>2. Amortisörler</h2>
<p>Amortisörler kazanın hareketini sönümler. <strong>Dengesiz veya yorulmuş amortisörlerde kazan
dengesiz çalışır</strong>; makine yürümeye başlar, zemine vurur, gürültü çıkarır. Genellikle önce
sıkma devrinde belli olur.</p>

<div class="kutu"><b>Servisi çağırmadan önce iki kontrol</b>
<p><strong>Makinenin ayakları terazide mi?</strong> Dengesiz duran bir makine sağlam olsa bile
sallanır ve gürültü yapar. Ayakları ayarlayıp makinenin dört köşesinin de zemine tam bastığından
emin olun.</p>
<p><strong>Yük dengeli mi?</strong> Tek bir ağır parçayı (halı, yorgan, bornoz) tek başına yıkamak
kazanı dengesiz döndürür. Bu, arıza değil kullanım kaynaklıdır.</p></div>

<h2>Yanık kokusuyla birlikte geliyorsa</h2>
<p>Sesle birlikte <strong>yanık kokusu</strong> da alıyorsanız tablo değişir: bu, kazanın körük
lastiğine sürtmesinin işaretidir. Ayrıntısı
<a href="/camasir-makinesi-koku-yapiyor/">koku sayfamızda</a>. Bu durumda makineyi çalıştırmayı
bırakıp bize haber verin — sürtme devam ettikçe lastik yırtılır ve
<a href="/camasir-makinesi-su-kaciriyor/">su kaçağı</a> başlar.</p>
"""
},

{
 "slug": "camasir-makinesi-su-kaciriyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Su Kaçırıyor?",
 "kisa": "Çamaşır makinesinde su kaçağının iki adresi var: körük lastiği ve arka hortum bağlantıları.",
 "gorsel": "camasir-makinesi-conta-degisimi.webp",
 "video": "camasir-makinesi-gider-hortumu-degisimi.mp4", "poster": "camasir-makinesi-pas-temizligi.webp",
 "video_etiket": "Gider hortumu değişimi",
 "govde": """
<p>Makinenin altında su görüyorsanız, suyun <strong>nereden değil, ne zaman</strong> geldiğine
bakmak teşhisi çok hızlandırır.</p>

<h2>1. Körük lastiği</h2>
<p>Kapağın çevresindeki büyük lastiğe körük lastiği denir. Yırtıldığında ya da deforme olduğunda
yıkama sırasında öne doğru su sızdırır. Yırtığın en sık sebebi kazanın lastiğe sürtmesidir — bu da
genelde <a href="/camasir-makinesi-ses-yapiyor/">rulman veya amortisör arızasının</a> devamıdır.</p>
<p><strong>Ayırt edici işaret:</strong> su makine çalışırken, kapağın alt kenarından geliyorsa
körük lastiğine bakılır.</p>

<h2>2. Arka hortum bağlantıları</h2>
<p>Makinenin arkasında giriş ve tahliye hortumları vardır. Kelepçelerin gevşemesi, hortumun
yaşlanıp çatlaması veya tahliye hortumunun bağlantı noktasından çıkması su kaçağı yapar.</p>
<p><strong>Ayırt edici işaret:</strong> su makinenin arkasında birikiyorsa ve makine
çalışmıyorken de sızıyorsa hortum ve bağlantılara bakılır.</p>

<div class="kutu uyari"><b>Su kaçağını bekletmeyin</b>
<p>Su kaçağı yalnızca zemine zarar vermez. Makinenin altına akan su elektrikli parçalara ulaşabilir
ve elektriksel arıza üretebilir. Kaçak fark ettiğinizde makinenin fişini çekip musluğunu kapatın,
sonra bize haber verin.</p></div>

<h2>Kaçak nereden geliyor, nasıl anlarsınız?</h2>
<p>Makinenin altına kuru bir kâğıt havlu serin ve bir program çalıştırın. Islanan bölge öndeyse körük
lastiği, arkadaysa hortumlar öncelikli şüpheli olur. Bu basit test, teknisyen geldiğinde tespiti
hızlandırır.</p>
"""
},

{
 "slug": "camasir-makinesi-koku-yapiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Kötü Kokuyor?",
 "kisa": "Çamaşır makinesi suyu ısıtmıyorsa koku yapar. Yanık kokusu ise kazanın körük lastiğine "
         "sürtmesini gösterir — bu acildir.",
 "gorsel": "camasir-makinesi-pas-temizligi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Çamaşır makinesindeki kokuda <strong>iki tamamen farklı tablo</strong> var ve aralarındaki fark
aciliyeti belirliyor. Önce kokunun cinsini ayırt etmek gerekiyor.</p>

<h2>1. Küf / bayat koku — makine suyu ısıtmıyor</h2>
<p>Makine <strong>suyu ısıtmıyorsa</strong> koku yapar. Hep düşük sıcaklıkta çalışan bir makine
içindeki kalıntıyı ve yağı çözemez; kazanda, körük lastiğinin kıvrımlarında ve deterjan çekmecesinde
birikinti kalır. Bu birikinti zamanla kokar.</p>
<p>Aynı sebep <a href="/camasir-makinesi-temiz-yikamiyor/">çamaşırların temiz yıkanmaması</a> olarak
da karşınıza çıkar — ikisi aynı arızanın iki yüzüdür. Suyu ısıtan parça
<a href="/camasir-makinesi-rezistans-arizasi/">rezistanstır</a>.</p>

<div class="kutu uyari"><b>2. Yanık kokusu — bu farklı ve acildir</b>
<p>Aldığınız koku <strong>yanık</strong> gibiyse durum değişir: bu, <strong>kazanın körük lastiğine
sürttüğünü</strong> gösterir. Sürtme devam ettikçe lastik aşınır, yırtılır ve
<a href="/camasir-makinesi-su-kaciriyor/">su kaçağı</a> başlar.</p>
<p>Yanık kokusu alıyorsanız makineyi çalıştırmayı bırakın ve bize haber verin. Bu koku genellikle
<a href="/camasir-makinesi-ses-yapiyor/">artan bir sesle</a> birlikte gelir.</p></div>

<h2>Koku için yapabilecekleriniz</h2>
<ul>
<li>Ayda bir <strong>en yüksek sıcaklıkta boş program</strong> çalıştırın.</li>
<li>Körük lastiğinin kıvrımını kuru bezle silin — birikinti en çok orada toplanır.</li>
<li>Deterjan çekmecesini çıkarıp yıkayın.</li>
<li>Program bitince kapağı bir süre <strong>aralık bırakın.</strong></li>
</ul>
<p>Bunlara rağmen koku geçmiyorsa makine muhtemelen suyu ısıtmıyordur; bu bir bakım değil onarım
konusudur.</p>
""",
},

{
 "slug": "camasir-makinesi-deterjan-almiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Deterjan Almıyor?",
 "kisa": "Çamaşır makinesi deterjanı almıyorsa su basıncı düşüktür; sebep ventil veya kireçtir. "
         "Ventil değişimi 1.100 TL.",
 "gorsel": "camasir-makinesi-deterjan-kutusu-degisimi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Program bittiğinde çekmecede deterjan duruyorsa, sorun deterjanda ya da çekmecede değil,
<strong>suyun basıncındadır.</strong></p>

<h2>Deterjan nasıl alınır?</h2>
<p>Makine deterjanı emmez — <strong>üzerinden geçen su onu sürükler.</strong> Yeterli basınçta gelen
su çekmeceden geçerken deterjanı alıp kazana taşır. Basınç düşükse su çekmeceden zayıf akar ve
deterjanın bir kısmı yerinde kalır.</p>

<h2>Basıncı düşüren iki sebep</h2>
<ul>
<li><strong>Su ventili.</strong> Ventil tam açılmıyorsa makineye giren su azalır. Bu aynı zamanda
<a href="/camasir-makinesi-su-almiyor/">su almama</a> şikâyetinin de kaynağıdır — ventil kısmen
çalıştığında "az su alıyor", tamamen bozulduğunda "hiç su almıyor" olur.</li>
<li><strong>Kireç.</strong> Su yolunda ve çekmece kanallarında biriken kireç kesiti daraltır.
Zamanla gelişen, yavaş yavaş kötüleşen bir şikâyettir.</li>
</ul>

<h2>Kendiniz kontrol edebilecekleriniz</h2>
<ul>
<li>Musluğu sonuna kadar açın.</li>
<li>Giriş hortumunun musluk tarafındaki <strong>süzgeci</strong> sökün ve temizleyin.</li>
<li>Deterjan çekmecesini tamamen çıkarıp kanallarını temizleyin.</li>
<li>Evdeki diğer musluklardan da su zayıf geliyorsa sorun makinede değil, tesisattadır.</li>
</ul>

<h2>Ücret</h2>
<p>Su ventili değişimi <strong>1.100 TL</strong>'dir (parça 400 TL, işçilik dahil). Sorun yalnızca
kireç kaynaklıysa temizlik yeterli olur ve maliyet servis ücretinde kalır.</p>
""",
},

{
 "slug": "camasir-makinesi-temiz-yikamiyor", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Neden Temiz Yıkamıyor?",
 "kisa": "Çamaşır makinesi suyu ısıtmıyorsa temiz yıkayamaz. Rezistans arızası en sık sebeptir.",
 "gorsel": "camasir-makinesi-kart-degisimi-arizasi.webp",
 "video": "camasir-makinesi-isitici-rezidans-degisim.mp4", "poster": "camasir-makinesi-karti.webp",
 "video_etiket": "Isıtıcı (rezistans) değişimi",
 "govde": """
<p>Çamaşırlar programdan lekeli, kirli ya da kokulu çıkıyorsa akla gelen ilk şey makinenin
<strong>suyu ısıtmamasıdır.</strong></p>

<h2>Sıcak su neden bu kadar önemli?</h2>
<p>Deterjan soğuk suda görevini yapamaz. Yağ ve kirin çözülmesi için suyun belirli bir sıcaklığa
ulaşması gerekir. Makine hep aynı düşük sıcaklıkta çalışıyorsa program süresi ne olursa olsun
sonuç değişmez — kir çözülmez, çamaşır temizlenmez.</p>
<p>Suyu ısıtan parça <a href="/camasir-makinesi-rezistans-arizasi/">rezistanstır</a>. Rezistans
devre dışıysa makine yıkamaya devam eder, program normal görünür, ama su hiç ısınmaz. Bu yüzden
arıza fark edilmesi en geç olan arızalardan biridir.</p>

<div class="kutu"><b>Basit bir test</b>
<p>60 derecelik bir program başlatın ve 20–25 dakika sonra kapağın camına elinizle dokunun.
Cam ılık bile değilse makine suyu ısıtmıyor demektir.</p></div>

<h2>Diğer ihtimaller</h2>
<ul>
<li><strong>Makine fazla dolduruluyor.</strong> Sıkışan çamaşır kendi içinde dönemez, deterjan her
yere ulaşamaz.</li>
<li><strong>Su basıncı düşük.</strong> Bu durumda makine <a href="/camasir-makinesi-deterjan-almiyor/">
deterjanı da tam almıyordur</a>; iki şikâyet birlikte geliyorsa sebep büyük ihtimalle budur.</li>
<li><strong>Kireç birikmesi.</strong> Uzun süre düşük sıcaklıkta çalışan makinede kireç ve kalıntı
birikir; bu da <a href="/camasir-makinesi-koku-yapiyor/">koku</a> yapar.</li>
</ul>
""",
},

{
 "slug": "camasir-makinesi-kapi-kilidi-arizasi", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Kapı Kilidi Arızası",
 "kisa": "Kapı kilidi arızasında kilidi ZORLAMAYIN — kapı kilidi çok sık kartı da patlatıyor. "
         "Batman'da yerinde onarım.",
 "gorsel": "bulasik-makinesi-kapi-kilidi-arizasi.webp",
 "video": "camasir-makines-kapi-kilidi-arizasi.mp4", "poster": "camasir-makinesi-karti2.webp",
 "video_etiket": "Kapı kilidi arızası",
 "govde": """
<p>Kapak açılmıyor, kapanmıyor ya da makine kapağı kilitleyemediği için programa hiç başlamıyorsa
sorun kapı kilidindedir. Bu, sık gelen bir arıza — ama <strong>yanlış müdahalede en pahalıya
patlayan</strong> arızalardan biri.</p>

<div class="kutu uyari"><b>En önemli uyarı: kilitle oynamayın</b>
<p>Sahada gördüğümüz en net zincir şu: <strong>kapı kilidi çok sık kartı da patlatıyor.</strong>
Arızalı bir kilit, karta hatalı sinyal göndererek onu yakabiliyor.</p>
<p>Bu yüzden kilit sıkıştığında <strong>zorlamayın, açmaya çalışmayın, defalarca deneme yapmayın.</strong>
Her zorlama denemesi kartı riske atıyor. Tek başına 1.000 TL civarında çözülecek bir iş, kart
değişimiyle birlikte katlanabiliyor.</p></div>

<h2>Arızanın iki kaynağı</h2>
<ul>
<li><strong>Kilidin içindeki mekanizma.</strong> Kapının orada küçük bir mekanizma var; yorulduğunda
kilit görevini yapamaz. Kilit değiştirildiğinde sorun düzelir. En sık görülen durum budur.</li>
<li><strong>Kart.</strong> Bazen sorunun kaynağı karttır — ya da kilit arızası kartı önceden
patlatmıştır. Bu yüzden kilidi değiştirmeden önce kartın kilide doğru sinyal verip vermediğine
bakıyoruz.</li>
</ul>

<h2>Kapak kapalı kaldıysa çamaşırlar ne olacak?</h2>
<p>Kapağı zorla açmaya çalışmak yerine bizi arayın. Kilit açma işlemi doğru yapıldığında hem
çamaşırlarınızı çıkarıyor hem kilidi değiştiriyoruz. Zorlama sonucu kırılan bir kapak mandalı,
işi kilit değişiminin ötesine taşıyor.</p>

<h2>İlgili arızalar</h2>
<p>Kilit arızasında makine programa başlamadığı için şikâyet çoğu zaman
"<a href="/camasir-makinesi-calismiyor/">makine çalışmıyor</a>" şeklinde geliyor. İkisini birlikte
değerlendirmek gerekiyor.</p>
""",
},

{
 "slug": "camasir-makinesi-pompa-arizasi", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Pompa Arızası",
 "kisa": "Pompa suyu boşaltan parçadır; içine para ve çorap girdiğinde arızalanır. "
         "Değişimi 2.500 TL, çoğu zaman temizlik yeterli.",
 "gorsel": "su-bosaltma-motoru-degisimi3.webp",
 "video": "camasir-makinesi-pompa-motoru-arizasi.mp4", "poster": "su-bosaltma-motoru-degisimi.webp",
 "video_etiket": "Pompa motoru arızası",
 "govde": """
<p>Pompa, çamaşır makinesinde <strong>suyu boşaltan parçadır.</strong> Görevi tek ve nettir; bu
yüzden arızası da kolay teşhis edilir: makine suyu atamıyorsa şüpheli bellidir.</p>

<h2>Pompayı bozan şey neredeyse hep aynı</h2>
<p>Pompanın içinde suyu çeken bir pervane var. Bu pervaneyi engelleyen her cisim arıza üretiyor ve
sahada bulduklarımız hep aynı listeden çıkıyor:</p>
<ul>
<li><strong>Bozuk para</strong> — açık ara birinci</li>
<li><strong>Çorap</strong> — özellikle kısa ve ince olanlar</li>
<li>Ceplerde kalan kâğıt, toka, düğme, kürdan</li>
<li>Saç, tüy ve kumaş lifi birikintisi</li>
</ul>

<h2>Pompa arızasının belirtileri</h2>
<ul>
<li>Program bitiyor ama kazanda su kalıyor</li>
<li>Makine <a href="/camasir-makinesi-sikma-yapmiyor/">sıkma yapmıyor</a> — su doluyken sıkmaya
geçmez, bu bir korumadır</li>
<li>Boşaltma sırasında normalden yüksek, zorlanan bir ses geliyor</li>
<li>Bekleyen su zamanla <a href="/camasir-makinesi-koku-yapiyor/">koku</a> yapıyor</li>
</ul>

<div class="kutu"><b>Her pompa arızası parça değişimi değildir</b>
<p>Pompa yalnızca tıkanmışsa ve parçanın kendisi sağlamsa <strong>temizlik yeterli oluyor.</strong>
Bu durumda maliyet servis ücretinde kalıyor. Parça gerçekten bozulmuşsa pompa değişimi
<strong>2.500 TL</strong>'dir (parça 800–900 TL, işçilik dahil).</p></div>

<h2>Tekrarını önlemek</h2>
<p>Yıkamadan önce cepleri boşaltmak ve çorapları file içinde yıkamak bu arızayı büyük ölçüde
ortadan kaldırıyor. Ayrıca çoğu makinede alt kapakta bir <strong>pompa filtresi</strong> vardır;
düzenli açılıp temizlenmesi pompayı korur.</p>
""",
},

{
 "slug": "camasir-makinesi-rezistans-arizasi", "cihaz": "camasir-makinesi",
 "soru": "Çamaşır Makinesi Rezistans (Isıtıcı) Arızası",
 "kisa": "Rezistans suyu ısıtan parçadır; kireç ve kalıntı yüzünden bozulur. Sık değişen "
         "parçalardan biridir.",
 "gorsel": "camasir-makinesi-karti2.webp",
 "video": "camasir-makinesi-isitici-rezidans-degisim.mp4", "poster": "camasir-makinesi-kart-degisimi-arizasi.webp",
 "video_etiket": "Isıtıcı rezistans değişimi",
 "govde": """
<p><strong>Rezistans</strong>, çamaşır makinesinde suyu ısıtan parçadır. Kazanın altında durur ve
her programda çalışır. Sık değiştirdiğimiz parçalardan biri — çünkü çalışma koşulları ağır.</p>

<h2>Rezistansı bozan şey: kireç ve kalıntı</h2>
<p>Makine uzun süre çalıştıkça içinde kalıntı ve <strong>kireç</strong> birikir. Bu birikinti
rezistansın üzerini kaplar. Kaplanan rezistans ısısını suya veremez, kendi üzerinde tutar ve
zamanla yanar.</p>
<p>Düşük sıcaklıkta çalışan makinelerde bu süreç hızlanır: kalıntı hiç çözülmediği için birikme
daha hızlı olur. Yani "hep 30 derecede yıkıyorum" alışkanlığı rezistansın ömrünü kısaltıyor.</p>

<h2>Rezistans bozulunca ne olur?</h2>
<p>Makine yıkamaya devam eder — program normal görünür, süre normal işler. Ama su hiç ısınmaz.
Sonuçlar şunlar:</p>
<ul>
<li><a href="/camasir-makinesi-temiz-yikamiyor/">Çamaşırlar temiz çıkmaz</a> — deterjan soğuk suda
işini yapamaz</li>
<li><a href="/camasir-makinesi-koku-yapiyor/">Makine koku yapar</a> — kalıntı çözülmeden birikir</li>
<li>Lekeler çıkmaz, beyazlar zamanla grileşir</li>
</ul>

<div class="kutu"><b>Rezistans arızası geç fark edilir</b>
<p>Makine çalışmaya devam ettiği için insanlar çoğu zaman aylarca fark etmiyor; deterjanı ya da
programı suçluyor. 60 derece programda 25 dakika sonra kapak camı ılık bile değilse rezistans
çalışmıyordur.</p></div>

<h2>Ömrünü uzatmak için</h2>
<p>Ayda bir kez <strong>en yüksek sıcaklıkta boş program</strong> çalıştırın. Bu, hem rezistans
üzerindeki birikintiyi çözer hem kazandaki kalıntıyı temizler. Hiçbir masrafı olmayan, en etkili
bakım adımıdır.</p>
""",
},

# ============================================================ BULAŞIK MAKİNESİ
{
 "slug": "bulasik-makinesi-su-almiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Su Almıyor?",
 "kisa": "Bulaşık makinesi su almıyorsa su ventili değişmelidir. Batman'da aynı gün yerinde onarım.",
 "gorsel": "bulasik-makinesi-ariza.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Bulaşık makinesi su almadan programa devam etmez. Mantık çamaşır makinesindekiyle aynıdır ve
sorumlu parça da aynıdır: <strong>su ventili.</strong></p>

<h2>Su ventili ne yapar?</h2>
<p>Ventil, şebeke suyunu makineye alan elektrikli vanadır. Kart komut verdiğinde açılır, gereken su
alındığında kapanır. Bozulduğunda suyu hiç geçirmez ve makine su alamadığı için programda takılır
ya da hiç başlamaz.</p>
<p>Bu durumda <strong>su ventilinin değişmesi gerekir.</strong></p>

<h2>Servisi çağırmadan önce kontrol edin</h2>
<ul>
<li><strong>Musluk açık mı?</strong> Bulaşık makinesinin musluğu genellikle tezgâh altında kaldığı
için farkında olmadan kapanabiliyor.</li>
<li><strong>Giriş hortumundaki süzgeç tıkalı mı?</strong> Hortumun musluk tarafında küçük bir filtre
vardır; kireç ve tortu ile tıkanır.</li>
<li><strong>Hortum ezilmiş mi?</strong> Makine yerinden oynatıldığında arkadaki hortum sıkışabiliyor.</li>
</ul>

<h2>Su almamanın diğer sonucu</h2>
<p>Makine su alamadığında <a href="/bulasik-makinesi-calismiyor/">hiç çalışmıyor</a> gibi görünür.
"Makine çalışmıyor" şikâyetiyle gittiğimiz cihazların bir kısmında sorun aslında su girişindedir.</p>

<h2>Ücret</h2>
<p>Bulaşık makinesi parça değişimleri <strong>1.000 – 2.000 TL</strong> aralığındadır; markaya ve
değişen parçaya göre değişir. Kesin fiyatı yerinde tespitten sonra, işleme başlamadan söylüyoruz.</p>
""",
},

{
 "slug": "bulasik-makinesi-su-bosaltmiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Su Boşaltmıyor?",
 "kisa": "Bulaşık makinesi suyu boşaltmıyorsa pompa motoru tıkalıdır — genellikle limon kabuğu ve "
         "yemek artığı yüzünden.",
 "gorsel": "bulasik-makinesi-sepet-degisimi.webp",
 "video": "bulasik-makinesi-motor-ariza-sesi.mp4", "poster": "bulasik-makinesi-ariza.webp",
 "video_etiket": "Bulaşık makinesi motor arıza sesi",
 "govde": """
<p>Program bittiğinde makinenin altında su kalıyorsa sorumlu parça <strong>pompa motorudur.</strong>
Pompa, bulaşık ve çamaşır makinelerinde suyu boşaltmaya yarayan parçadır.</p>

<h2>Pompayı tıkayan şeyler</h2>
<p>Bulaşık makinesinde pompayı tıkayanlar çamaşır makinesindekinden farklıdır — burada suçlu
mutfak artıklarıdır:</p>
<ul>
<li><strong>Limon kabuğu</strong> — sahada en sık bulduğumuz şey</li>
<li>Yemek artığı, pirinç, makarna parçaları</li>
<li>Kırılmış cam ve porselen parçacıkları</li>
<li>Etiket, çekirdek, kemik parçası</li>
</ul>
<p>Bu artıklar önce filtreyi, sonra pompayı tıkıyor. Genellikle parça da bu yüzden bozuluyor:
zorlanan pompa motoru zamanla yanıyor.</p>

<div class="kutu"><b>Bunu önleyen tek alışkanlık</b>
<p>Bulaşıkları makineye koymadan önce <strong>kaba artıkları sıyırın</strong> ve
<a href="/bulasik-makinesi-filtre-temizligi/">alttaki filtreyi üç ayda bir açıp temizleyin.</a>
Filtre bakımı, pompayı koruyan en ucuz önlemdir — hiçbir masrafı yok.</p></div>

<h2>Su boşaltmamak zincirleme sorun çıkarır</h2>
<p>Makine suyu atamadığında:</p>
<ul>
<li><a href="/bulasik-makinesi-calismiyor/">Programa devam etmez</a> — bu bir korumadır</li>
<li><a href="/bulasik-makinesi-kurutmuyor/">Kurutma yapmaz</a> — sistemdeki su boşalmadan kurutma
aşaması çalışmaz</li>
<li>Bekleyen su <a href="/bulasik-makinesi-koku-yapiyor/">koku</a> yapar</li>
</ul>
<p>Yani tek bir pompa arızası üç ayrı şikâyet olarak karşımıza gelebiliyor.</p>
""",
},

{
 "slug": "bulasik-makinesi-calismiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Çalışmıyor?",
 "kisa": "Bulaşık makinesi çalışmıyorsa sebep kart arızası olabilir; ayrıca su alamıyor veya "
         "boşaltamıyorsa programa girmez.",
 "gorsel": "bulasik-makinesi-kart-degisim-arizasi.webp",
 "video": "bulasik-makinesi-kart-degisim.mp4", "poster": "bulasik-makinesi-kart-degisim-arizasi.webp",
 "video_etiket": "Bulaşık makinesi kart değişimi",
 "govde": """
<p>"Makine çalışmıyor" şikâyeti aslında iki farklı durumu kapsıyor ve ayırt etmek önemli:
makine <strong>hiç açılmıyor</strong> mu, yoksa <strong>açılıyor ama programa girmiyor</strong> mu?</p>

<h2>1. Hiç açılmıyor — kart arızası</h2>
<p>Makine hiçbir tepki vermiyorsa önce priz, kablo ve sigortaya bakılır. Bunlar sağlamsa devreye
<strong>kart</strong> girer. Kart makinenin beynidir; düğmelerden gelen komutu pompaya, ventile ve
rezistansa dağıtır. Arızalandığında makine tamamen sessiz kalabilir ya da bazı fonksiyonlar çalışıp
bazıları çalışmayabilir.</p>

<h2>2. Açılıyor ama program ilerlemiyor</h2>
<p>Bu durumda kart sağlamdır, engel başka yerdedir. Bulaşık makinesi iki koşul sağlanmadan programa
devam etmez — ikisi de güvenlik amaçlıdır:</p>
<ul>
<li><strong><a href="/bulasik-makinesi-su-almiyor/">Suyu alamıyorsa</a></strong> çalışmaz. Su
olmadan yıkama yapmak rezistansı ve pompayı yakar.</li>
<li><strong><a href="/bulasik-makinesi-su-bosaltmiyor/">Suyu boşaltamıyorsa</a></strong> çalışmaz.
İçinde su varken yeni program başlatmaz.</li>
</ul>

<div class="kutu"><b>Teşhis sırası masrafı belirliyor</b>
<p>Doğrudan "kart bozulmuş" teşhisi koymak, aslında tıkalı bir pompadan kaynaklanan sorun için
gereksiz masraf çıkarır. Biz her zaman önce suyun girip çıktığına bakıyoruz; kart en son
şüphelidir.</p></div>

<h2>Kapı kilidi ihtimali</h2>
<p>Makine kapağı tam kilitleyemiyorsa da programa başlamaz. Kapak kapanırken tık sesi gelmiyorsa
kilit mekanizması kontrol edilmelidir.</p>
""",
},

{
 "slug": "bulasik-makinesi-iyi-yikamiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden İyi Yıkamıyor, Kirli Bırakıyor?",
 "kisa": "Bulaşık makinesi kirli bırakıyorsa pervaneler (fıskiyeler) tıkalıdır veya dönmüyordur. "
         "Düzenli temizlik gerektiren parçalardır.",
 "gorsel": "bulasik-makinesi-pervane-degisimi.webp",
 "video": "bulasik-makinesi-svic-arizasi.mp4", "poster": "bulasik-makinesi-pervane-degisimi2.webp",
 "video_etiket": "Bulaşık makinesi svic arızası",
 "govde": """
<p>Bulaşıklar programdan kirli, lekeli ya da kum gibi kalıntıyla çıkıyorsa sorumlu parça
neredeyse her zaman aynıdır: <strong>suyu püskürten dönen kollar.</strong></p>

<h2>Pervane mi, fıskiye mi?</h2>
<p>Teknik adı <strong>fıskiye</strong> olan bu parçalara biz sahada <strong>pervane</strong> diyoruz.
Makinenin altında ve üst sepetin altında bulunan, üzerinde delikler olan dönen kollardır. Suyu
basınçla püskürtüp bulaşıklara ulaştırırlar.</p>

<h2>Neden kirli bırakır?</h2>
<ul>
<li><strong>Pervaneler dönmüyordur.</strong> Dönmeyen kol suyu tek noktaya sıkar; bulaşığın büyük
kısmına su hiç ulaşmaz.</li>
<li><strong>Delikleri tıkalıdır.</strong> Kireç ve yemek artığı delikleri kapatır, püskürtme basıncı
düşer.</li>
<li><strong>Durulama yeterli olmuyordur.</strong> Su akışı zayıfsa deterjan tam durulanmaz, bulaşıkta
kalıntı bırakır.</li>
<li><strong>Deterjan kaynaklı olabilir.</strong> Yanlış veya yetersiz deterjan da aynı sonucu verir.</li>
</ul>
<p>Pervaneler <strong>düzenli açılıp temizlenmesi gereken parçalardır.</strong> Değiştirildiklerinde
daha hızlı ve düzgün dönerler, yıkama belirgin şekilde iyileşir.</p>

<div class="kutu"><b>Kendiniz yapabileceğiniz kontrol</b>
<p>Makine boşken alttaki ve üstteki kolları elinizle çevirin — takılmadan, serbestçe dönmeleri
gerekir. Sonra deliklere bakın; tıkalı olanları ince bir kürdanla açabilirsiniz. Bu basit bakım
çağrıların bir kısmını gereksiz kılıyor.</p>
<p>Aynı anda <a href="/bulasik-makinesi-filtre-temizligi/">alttaki filtreyi de</a> açıp temizleyin —
ikisi birlikte yapıldığında sonuç çok daha iyi oluyor.</p></div>

<h2>Yükleme hatası da olabilir</h2>
<p>Büyük bir tencere veya tepsi, dönen kolun önünü kapatıyorsa arkasındaki bulaşıklara su ulaşmaz.
Makineyi çalıştırmadan önce kolları elinizle çevirip hiçbir şeye çarpmadıklarından emin olun.</p>
""",
},

{
 "slug": "bulasik-makinesi-koku-yapiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Koku Yapıyor?",
 "kisa": "Bulaşık makinesinde koku genellikle alt taraftaki contadan gelir; uzun süre "
         "değişmeyen conta kötü koku yapar.",
 "gorsel": "camasir-makinesi-conta-degisimi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Bulaşık makinesi koku şikâyeti, sahada <strong>en az geldiğimiz</strong> arızalardan biri —
ama geldiğinde sebebi genellikle bellidir.</p>

<h2>Ana sebep: alt taraftaki conta</h2>
<p>Cihazın alt tarafında bir <strong>conta</strong> bulunur. Bu conta uzun süre değişmediğinde
yapısı bozulur, kıvrımlarında nem ve kalıntı tutar ve <strong>kötü koku yapar.</strong>
Contayı değiştirmek kokuyu kökünden çözer.</p>

<h2>Diğer koku kaynakları</h2>
<ul>
<li><strong>Bekleyen su.</strong> Makine <a href="/bulasik-makinesi-su-bosaltmiyor/">suyu tam
boşaltamıyorsa</a> altta kalan su zamanla kokar. Koku şikâyetiyle birlikte altta su görüyorsanız
sebep pompadır, conta değil.</li>
<li><strong>Filtre.</strong> <a href="/bulasik-makinesi-filtre-temizligi/">Üç ayda bir
temizlenmeyen filtre</a> yemek artığı tutar ve kokar.</li>
<li><strong>Kapı çevresi.</strong> Kapağın iç kenarındaki oluk sıkça gözden kaçar; orada da
kalıntı birikir.</li>
</ul>

<div class="kutu"><b>Servisi çağırmadan önce deneyin</b>
<p>Filtreyi çıkarıp yıkayın, kapı çevresindeki oluğu silin, makineyi boş olarak en yüksek
sıcaklıkta çalıştırın. Program bitince kapağı bir süre aralık bırakın — içeride kalan nem
kokunun asıl sebebi.</p>
<p>Bunlara rağmen koku devam ediyorsa conta yorulmuş demektir; o zaman bizi arayın.</p></div>

<h2>Kullanmadığınız dönemler</h2>
<p>Makineyi uzun süre çalıştırmadığınızda içindeki durgun su kokar. Tatilden dönüşteki koku
genellikle bu yüzdendir ve boş bir program çalıştırmak yeterli olur.</p>
""",
},

{
 "slug": "bulasik-makinesi-su-kaciriyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Su Kaçırıyor?",
 "kisa": "Bulaşık makinesinde su kaçağı alttaki dört yollu vanalardan, conta aralarından veya "
         "su girişlerinden gelir.",
 "gorsel": "bulasik-makinesi-kart-degisim-arizasi.webp",
 "video": "bulasik-makinesi-su-kacak-tespiti.mp4", "poster": "bulasik-makinesi-ariza.webp",
 "video_etiket": "Bulaşık makinesi su kaçağı tespiti",
 "govde": """
<p>Bulaşık makinesi baştan sona <strong>suyla çalışan bir cihazdır</strong> — içinden sürekli su
geçer, her yeri suyla temas hâlindedir. Bu yüzden su kaçağı bu cihazda en sık gelen arıza
sebeplerinden biridir.</p>

<h2>Kaçağın geldiği noktalar</h2>
<ul>
<li><strong>Alttaki dört yollu vanalar.</strong> Suyun dağıtıldığı bu bağlantı noktaları zamanla
sızdırır. En sık bulduğumuz kaynak burasıdır.</li>
<li><strong>Conta araları.</strong> Bağlantılardaki contalar yorulduğunda aralarından su geçer.</li>
<li><strong>Su girişleri.</strong> Suyun makineye girdiği noktalardaki bağlantılar gevşer veya
yaşlanır.</li>
<li><strong>Patlak pervane veya fıskiye.</strong> Bu parçalar çatladığında su basınçla yanlış yöne
gider ve <strong>alttan akıtır.</strong> Bu ihtimal sık atlanıyor.</li>
</ul>

<div class="kutu uyari"><b>Su kaçağını bekletmeyin</b>
<p>Bulaşık makinesi genellikle ahşap mutfak dolabının içine gömülüdür. Sızan su önce dolabın
tabanını, sonra zemini bozar; mutfak dolabı onarımı çoğu zaman makinenin onarımından pahalıya
gelir.</p>
<p>Kaçak fark ettiğinizde makinenin fişini çekin, musluğunu kapatın ve bizi arayın.</p></div>

<h2>Kaçak nereden geliyor, nasıl anlarsınız?</h2>
<p>Makinenin altına kuru kâğıt havlu serin ve bir program çalıştırın. Islanan bölge:</p>
<ul>
<li><strong>Ön tarafsa</strong> — kapı contası ya da patlak pervane</li>
<li><strong>Arka tarafsa</strong> — su girişleri ve hortum bağlantıları</li>
<li><strong>Tam altsa</strong> — dört yollu vanalar</li>
</ul>
<p>Bu bilgi teknisyen geldiğinde tespiti hızlandırır ve işlem süresini kısaltır.</p>
""",
},

{
 "slug": "bulasik-makinesi-ses-yapiyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Ses Yapıyor?",
 "kisa": "Bulaşık makinesinde aşırı ses pompa motorundan ya da bir yere çarpan pervaneden gelir.",
 "gorsel": "bulasik-makinesi-pervane-degisimi2.webp",
 "video": "bulasik-makinesi-motor-ariza-sesi.mp4", "poster": "bulasik-makinesi-sepet-degisimi.webp",
 "video_etiket": "Pompa motorundan gelen arıza sesi",
 "govde": """
<p>Önce bir yanlış anlamayı düzeltelim: <strong>bulaşık makinesi tamamen sessiz çalışmaz.</strong>
Çalışırken su sesi duyulması normaldir — hatta suyun basınçla dönmesi makinenin düzgün yıkadığının
işaretidir. Sorun, sesin <strong>anormal derecede artmasıdır.</strong></p>

<h2>Aşırı sesin iki kaynağı</h2>
<ul>
<li><strong>Pompa motoru.</strong> Zorlanan ya da yorulmuş pompa yüksek, düzensiz bir ses çıkarır.
Bu ses genellikle boşaltma aşamasında belirginleşir. Aynı arıza kısa sürede
<a href="/bulasik-makinesi-su-bosaltmiyor/">su boşaltmama</a> şikâyetine dönüşür.</li>
<li><strong>Pervanenin bir yere çarpması.</strong> Dönen kol, uzun bir bıçağa, sarkan bir kaba veya
yanlış yerleştirilmiş bir tepsiye çarpıyorsa ritmik bir vurma sesi duyulur. Bu, arıza değil
<strong>yükleme hatasıdır</strong> ve düzeltmesi bedavadır.</li>
</ul>

<div class="kutu"><b>Önce bunu deneyin</b>
<p>Makineyi durdurun, kapağı açın ve alttaki-üstteki dönen kolları elinizle çevirin. Bir yere
çarpıyorlarsa sesin sebebi bulundu demektir — o kabı yeniden yerleştirin. Uzun bıçak ve saplı
kapaklar en sık suçlu.</p></div>

<h2>Sesin cinsi ipucu verir</h2>
<ul>
<li><strong>Ritmik vurma:</strong> pervane bir şeye çarpıyor</li>
<li><strong>Sürekli uğultu / zorlanma:</strong> pompa motoru</li>
<li><strong>Metalik takırtı:</strong> sepette gevşek bir kap veya çatal</li>
<li><strong>Su emme sesi:</strong> makine su almakta zorlanıyor — <a href="/bulasik-makinesi-su-almiyor/">
su girişine</a> bakılmalı</li>
</ul>
""",
},

{
 "slug": "bulasik-makinesi-kopuruyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Aşırı Köpürüyor?",
 "kisa": "Bulaşık makinesinde aşırı köpüğün sebebi yanlış deterjan kullanımıdır — özellikle "
         "elde yıkama deterjanı eklemek.",
 "gorsel": "bulasik-makinesi-ariza.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Makineden köpük taşıyorsa sebep neredeyse her zaman cihazda değil,
<strong>kullanılan üründedir.</strong> Bu, onarım gerektirmeyen ama cihaza zarar veren bir
durumdur.</p>

<h2>Ana sebep: yanlış deterjan</h2>
<p>Bulaşık makinesi deterjanları <strong>az köpürecek şekilde</strong> üretilir. Elde bulaşık
yıkama deterjanı ise tam tersine bol köpük yapmak üzere tasarlanmıştır. İkisi birbirinin yerine
kullanılamaz.</p>

<div class="kutu uyari"><b>Sahada çok gördüğümüz hata</b>
<p>Bazı kullanıcılar <strong>"daha iyi temizlesin" diye makineye farklı ürünler ekliyor</strong> —
elde yıkama deterjanı, çamaşır suyu, sabun, karbonat. Bunlar temizliği artırmıyor;
<strong>aşırı köpük yapıyor ve cihaza zarar veriyor.</strong></p>
<p>Aşırı köpük pompayı zorlar, contalardan taşarak <a href="/bulasik-makinesi-su-kaciriyor/">su
kaçağı</a> görüntüsü yaratır ve durulamayı bozarak
<a href="/bulasik-makinesi-iyi-yikamiyor/">bulaşığın kirli kalmasına</a> sebep olur.</p></div>

<h2>Diğer sebepler</h2>
<ul>
<li><strong>Fazla deterjan.</strong> Önerilenden çok koymak temizliği artırmaz, köpüğü artırır.</li>
<li><strong>Parlatıcı ayarı yüksek.</strong> Bazı modellerde parlatıcı dozu ayarlanabilir; yüksek
ayarda köpük artar.</li>
<li><strong>Yağlı bulaşıkların hiç sıyrılmaması.</strong> Aşırı yağ, deterjanla birleşince köpüğü
artırabilir.</li>
</ul>

<h2>Köpük taştıysa ne yapmalı?</h2>
<p>Programı durdurun, kapağı açıp köpüğün sönmesini bekleyin, kalan suyu boşaltıp makineyi
<strong>deterjansız</strong> kısa bir programda çalıştırın. Bu genellikle yeterli oluyor.
Köpük taşması sürekli tekrarlıyorsa ve doğru deterjan kullanıyorsanız bizi arayın.</p>
""",
},

{
 "slug": "bulasik-makinesi-kurutmuyor", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Neden Kurutmuyor?",
 "kisa": "Bulaşık makinesi kurutmuyorsa pompa sistemdeki suyu boşaltmıyordur — pompa motoru "
         "arızalıdır.",
 "gorsel": "bulasik-makinesi-sepet-degisimi.webp",
 "video": "bulasik-makinesi-kart-degisim2.mp4", "poster": "bulasik-makinesi-kart-degisim-arizasi.webp",
 "video_etiket": "Bulaşık makinesi kart değişimi",
 "govde": """
<p>Program bitiyor ama bulaşıklar ıslak çıkıyorsa, ilk bakılacak yer kurutma sistemi değil
<strong>su tahliyesidir.</strong></p>

<h2>Kurutma neden çalışmıyor?</h2>
<p>Kurutma aşaması, sistemdeki suyun tamamen boşaltılmış olmasını gerektirir.
<strong>Pompa sistemdeki suyu boşaltmıyorsa makine kurutma yapamaz.</strong> Bu da
<a href="/bulasik-makinesi-su-bosaltmiyor/">pompa motorunun arızalı olduğu</a> anlamına gelir.</p>
<p>Yani "kurutmuyor" şikâyeti çoğu zaman kurutma arızası değil, gizlenmiş bir pompa arızasıdır.
Makinenin altında bir miktar su kalıp kalmadığına bakmak teşhisi hemen netleştiriyor.</p>

<div class="kutu"><b>Önce şuna bakın</b>
<p>Program bittiğinde makinenin en altında, filtrenin çevresinde su birikmiş mi? Birikmişse sorun
pompadadır ve kurutma bunun sonucudur. Alt tamamen kuruysa başka bir sebep aranmalıdır.</p></div>

<h2>Diğer ihtimaller</h2>
<ul>
<li><strong>Parlatıcı bitmiş.</strong> Parlatıcı suyun yüzeyden akmasını sağlar; bittiğinde tabaklarda
damla kalır. En basit ve en sık atlanan sebep.</li>
<li><strong>Program seçimi.</strong> Kısa ve eko programların bir kısmında kurutma ya hiç yoktur ya
da çok zayıftır.</li>
<li><strong>Plastik kaplar.</strong> Plastik ısıyı tutmadığı için üzerindeki su buharlaşmaz;
cam ve porselen kururken plastiklerin ıslak kalması <strong>normaldir.</strong></li>
<li><strong>Program biter bitmez boşaltma.</strong> Kapak birkaç dakika kapalı kaldığında kalan ısı
kurutmayı tamamlar. Hemen açıp boşaltmak ıslaklık hissini artırır.</li>
</ul>
""",
},

{
 "slug": "bulasik-makinesi-filtre-temizligi", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Filtre Temizliği Nasıl Yapılır?",
 "kisa": "Bulaşık makinesinin alt filtresi 3 ayda bir açılıp temizlenmeli. Hiçbir masrafı olmayan, "
         "en etkili bakım adımı.",
 "gorsel": "bulasik-makinesi-sepet-degisimi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Bulaşık makinesiyle ilgili size söyleyebileceğimiz <strong>en değerli tavsiye</strong> bu:
alttaki filtreyi <strong>üç ayda bir</strong> açıp temizleyin. Hiçbir masrafı yok ve makinenin
ömrünü doğrudan uzatıyor.</p>

<h2>Filtre ne işe yarar?</h2>
<p>Filtre, bulaşıklardan gelen yemek artıklarını tutar ve pompaya gitmelerini engeller. Makinenin
en alt tarafında, dönen kolun altındadır ve genellikle elle çevrilerek çıkar.</p>

<h2>Temizlenmezse ne olur?</h2>
<ul>
<li>Yıkama verimi düşer — <a href="/bulasik-makinesi-iyi-yikamiyor/">bulaşıklar kirli kalır</a></li>
<li>Tutulamayan artık pompaya gider ve
<a href="/bulasik-makinesi-su-bosaltmiyor/">pompayı tıkar</a></li>
<li>Biriken artık <a href="/bulasik-makinesi-koku-yapiyor/">koku yapar</a></li>
<li>Zorlanan pompa motoru zamanla yanar — <strong>1.000–2.000 TL'lik bir parça değişimi</strong></li>
</ul>
<p>Yani üç ayda bir yapılan beş dakikalık bir bakım, binlerce liralık bir arızayı önlüyor.</p>

<h2>Nasıl temizlenir?</h2>
<ol>
<li>Alt sepeti çıkarın.</li>
<li>Filtre grubunu saat yönünün tersine çevirerek çıkarın (modele göre değişebilir).</li>
<li>Parçaları ayırın, akan su altında yumuşak bir fırçayla yıkayın.</li>
<li>Filtrenin oturduğu yuvadaki kalıntıyı da silin — burası çoğu zaman atlanıyor.</li>
<li>Kurutup yerine takın, <strong>tam oturduğundan emin olun.</strong></li>
</ol>

<div class="kutu"><b>Aynı anda pervaneleri de kontrol edin</b>
<p>Filtreyi çıkarmışken dönen kolları elinizle çevirin ve deliklerine bakın. Tıkalı delikleri ince
bir kürdanla açın. Bu ikisi birlikte yapıldığında yıkama kalitesindeki fark hemen fark ediliyor.</p></div>

<div class="kutu uyari"><b>Filtresiz çalıştırmayın</b>
<p>Temizlik sonrası filtreyi mutlaka yerine takın ve kilitlendiğinden emin olun. Filtresiz çalışan
makinede artıklar doğrudan pompaya gider — bu, en hızlı pompa yakma yöntemidir.</p></div>
""",
},

{
 "slug": "bulasik-makinesi-rezistans-arizasi", "cihaz": "bulasik-makinesi",
 "soru": "Bulaşık Makinesi Rezistans Arızası ve Markaya Göre Maliyet Farkı",
 "kisa": "Bosch, Siemens ve Profilo'da rezistans motorun içindedir, komple motor değişir. "
         "Arçelik ve Vestel'de ayrı değişir, daha ucuzdur.",
 "gorsel": "bulasik-makinesi-kart-degisim-arizasi.webp",
 "video": None, "poster": None, "video_etiket": "",
 "govde": """
<p>Bulaşık makinesinde <strong>rezistans</strong> suyu ısıtan parçadır. Arızalandığında makine
yıkamaya devam eder ama su ısınmaz; yağ çözülmez, bulaşık temiz çıkmaz.</p>
<p>Bu arızada asıl önemli olan teşhis değil — <strong>markanızın hangi grupta olduğu.</strong>
Çünkü maliyet doğrudan buna bağlı.</p>

<h2>Markaya göre yapı farkı</h2>
<p>Bu, sahada net olarak ayrıştırdığımız bir konu:</p>
<div class="tbl-sar"><table>
<thead><tr><th scope="col">Marka grubu</th><th scope="col">Rezistansın yeri</th>
<th scope="col">Değişimde ne olur?</th></tr></thead>
<tbody>
<tr><td><strong>Bosch, Siemens, Profilo</strong></td><td>Motorun <strong>içinde</strong></td>
<td>Rezistans ayrı değiştirilemez — <strong>komple motor değişir.</strong> Maliyet yüksektir.</td></tr>
<tr><td><strong>Arçelik, Beko, Vestel, Altus, Regal, Grundig, SEG</strong></td>
<td>Motorun <strong>yanında</strong></td>
<td>Yalnızca rezistans değişir. <strong>Daha makul ve daha ucuz.</strong></td></tr>
</tbody></table></div>

<div class="kutu"><b>Neden bunu önceden söylüyoruz</b>
<p>Aynı şikâyet — "makine ısıtmıyor" — bir <a href="/batman-bosch-servisi/">Bosch</a> makinede
<a href="/batman-arcelik-servisi/">Arçelik</a> makineye göre belirgin şekilde pahalıya geliyor.
Bu, servisin fiyat farkı değil, cihazın yapı farkı.</p>
<p>Telefonda markanızı sorduğumuzda sebebi bu: maliyeti daha yola çıkmadan söyleyebilmek için.
Sürprizle karşılaşmanızı istemiyoruz.</p></div>

<h2>Rezistansı ne bozar?</h2>
<p>Çamaşır makinesindekiyle aynı: <strong>kireç ve kalıntı birikmesi.</strong> Rezistansın üzerini
kaplayan birikinti ısıyı suya geçirmesini engeller; parça kendi üzerinde ısınır ve yanar.
<a href="/bulasik-makinesi-filtre-temizligi/">Düzenli filtre bakımı</a> bu birikmeyi yavaşlatır.</p>

<h2>Ücret</h2>
<p>Bulaşık makinesi parça değişimleri <strong>1.000 – 2.000 TL</strong> aralığındadır. Bosch grubu
cihazlarda komple motor değişimi gerektiği için maliyet üst banda yaklaşır. Kesin fiyatı yerinde
tespitten sonra, işleme başlamadan söylüyoruz.</p>
""",
},

]
