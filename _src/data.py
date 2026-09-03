# -*- coding: utf-8 -*-
"""Batman Beyaz Eşya Servisi — site verisi.

⛔ HTML dosyalarını ELLE DÜZENLEME. Tüm sayfalar build.py tarafından buradan üretilir.
Kaynak bilgi: _src/bilgi.md (işletmenin kendi anlattıkları).
"""

# ---------------------------------------------------------------- işletme

SITE = "https://beyazesyaservisibatman.com"

ISLETME = {
    "ad": "Batman Beyaz Eşya Servisi",
    "sahip": "Barış Kirici",
    "tel_yazi": "0553 711 83 21",
    "tel_link": "+905537118321",
    "wa": "905537118321",
    # İkinci hat — kullanıcı 2026-09-03'te "ikisi de benim" dedi.
    # ⚠️ WhatsApp YALNIZCA birinci numarada; ikincisi için WhatsApp bağlantısı verme.
    "tel2_yazi": "0554 166 25 72",
    "tel2_link": "+905541662572",
    "adres_sokak": "Fatih Mah. 3206. Sk. No:12",
    "adres_ilce": "Merkez",
    "adres_il": "Batman",
    "posta": "72070",
    "lat": 37.899098,
    "lng": 41.140227,
    "tecrube": 8,
    "garanti_ay": 12,
    "yedi_yirmidort": True,
    # MEB İş Yeri Açma Belgesi (3308 sayılı kanun — ustalık belgesi hakları)
    "belge": {
        "ad": "T.C. Millî Eğitim Bakanlığı İş Yeri Açma Belgesi",
        "alan": "Tesisat Teknolojisi ve İklimlendirme",
        "dal": "Soğutma Sistemleri",
        "gorsel": "batman-beyaz-esya-teknik-servis-belgesi.webp",
    },
    "maps": "https://www.google.com/maps/search/?api=1&query=37.899098,41.140227",
    "yol_tarifi": "https://www.google.com/maps/dir/?api=1&destination=37.899098,41.140227",
}

# Servis ücretleri — bölgeye göre (işletme 2026-09-03'te verdi)
# ⚠️ İlçelere AYRI bir yol/mesafe ücreti YOK: ilçede de servis ücreti 600 TL.
SERVIS_UCRETI = {
    "merkez": 600,
    "ilce": 600,
    "koy": 1000,
}

# Tamir süreleri (işletme 2026-09-03'te teyit etti)
SURELER = [
    ("Basit arızalar", "30 – 60 dakika", "Kapı contası, filtre değişimi gibi işler."),
    ("Orta düzey arızalar", "1 – 2 saat", "Motor ve pompa tamiri."),
    ("Karmaşık arızalar", "2 – 4 saat", "Kompresör ve elektronik kart arızaları."),
]

# ---------------------------------------------------------------- cihazlar

CIHAZLAR = [
    {
        "slug": "buzdolabi",
        "ad": "Buzdolabı",
        "ad_tamlama": "buzdolabı",
        "baslik": "Batman Buzdolabı Tamircisi",
        "oncelik": 1,
        "ozet": "Soğutmama, ses, buzlanma ve su akıtma arızalarında aynı gün yerinde müdahale.",
    },
    {
        "slug": "camasir-makinesi",
        "ad": "Çamaşır Makinesi",
        "ad_tamlama": "çamaşır makinesi",
        "baslik": "Batman Çamaşır Makinesi Tamircisi",
        "oncelik": 2,
        "ozet": "Su almama, su boşaltmama, sıkma yapmama, ses ve kapı kilidi arızaları.",
    },
    {
        "slug": "bulasik-makinesi",
        "ad": "Bulaşık Makinesi",
        "ad_tamlama": "bulaşık makinesi",
        "baslik": "Batman Bulaşık Makinesi Tamircisi",
        "oncelik": 3,
        "ozet": "Yıkamama, kurutmama, su kaçırma, koku ve pervane arızaları.",
    },
    {
        "slug": "derin-dondurucu",
        "ad": "Derin Dondurucu",
        "ad_tamlama": "derin dondurucu",
        "baslik": "Batman Derin Dondurucu Tamircisi",
        "oncelik": 1,
        "ozet": "Termostat, gaz kaçağı ve kompresör arızalarında 400–800 litre modellerde onarım.",
    },
]

# ---------------------------------------------------------------- markalar

# aile: rezistans konumu bulaşık makinesi maliyetini doğrudan belirliyor (işletmenin saha bilgisi)
#   "bsh"     → rezistans motorun İÇİNDE, komple motor değişir (pahalı)
#   "yerli"   → rezistans motorun YANINDA, ayrı değişir (uygun)
#   "kore"    → no-frost ağırlıklı, elektronik kart ve fan arızaları öne çıkıyor
MARKALAR = [
    {"slug": "arcelik",  "ad": "Arçelik",  "aile": "yerli", "grup": "Arçelik"},
    {"slug": "beko",     "ad": "Beko",     "aile": "yerli", "grup": "Arçelik"},
    {"slug": "altus",    "ad": "Altus",    "aile": "yerli", "grup": "Arçelik"},
    {"slug": "grundig",  "ad": "Grundig",  "aile": "yerli", "grup": "Arçelik"},
    {"slug": "bosch",    "ad": "Bosch",    "aile": "bsh",   "grup": "BSH"},
    {"slug": "siemens",  "ad": "Siemens",  "aile": "bsh",   "grup": "BSH"},
    {"slug": "profilo",  "ad": "Profilo",  "aile": "bsh",   "grup": "BSH"},
    {"slug": "vestel",   "ad": "Vestel",   "aile": "yerli", "grup": "Vestel"},
    {"slug": "regal",    "ad": "Regal",    "aile": "yerli", "grup": "Vestel"},
    {"slug": "seg",      "ad": "SEG",      "aile": "yerli", "grup": "Vestel"},
    {"slug": "samsung",  "ad": "Samsung",  "aile": "kore",  "grup": "Samsung"},
    {"slug": "lg",       "ad": "LG",       "aile": "kore",  "grup": "LG"},
]

# ---------------------------------------------------------------- bölgeler

BOLGELER = [
    {
        "slug": "batman-merkez",
        "ad": "Batman Merkez",
        "kisa": "Merkez",
        "sure": "genellikle 2 saat içinde",
        "sure_kisa": "2 saat",
        "ucret": 600,
        "merkez_mi": True,
    },
    {
        "slug": "besiri",
        "ad": "Beşiri",
        "kisa": "Beşiri",
        "sure": "en geç 1 gün içinde",
        "sure_kisa": "1 gün",
        "ucret": 600,
        "merkez_mi": False,
    },
    {
        "slug": "gercus",
        "ad": "Gercüş",
        "kisa": "Gercüş",
        "sure": "en geç 1 gün içinde",
        "sure_kisa": "1 gün",
        "ucret": 600,
        "merkez_mi": False,
    },
    {
        "slug": "hasankeyf",
        "ad": "Hasankeyf",
        "kisa": "Hasankeyf",
        "sure": "en geç 1 gün içinde",
        "sure_kisa": "1 gün",
        "ucret": 600,
        "merkez_mi": False,
    },
    {
        "slug": "kozluk",
        "ad": "Kozluk",
        "kisa": "Kozluk",
        "sure": "en geç 1 gün içinde",
        "sure_kisa": "1 gün",
        "ucret": 600,
        "merkez_mi": False,
    },
    {
        "slug": "sason",
        "ad": "Sason",
        "kisa": "Sason",
        "sure": "en geç 1 gün içinde",
        "sure_kisa": "1 gün",
        "ucret": 600,
        "merkez_mi": False,
    },
]

# ---------------------------------------------------------------- fiyatlar

FIYATLAR = [
    ("Servis ücreti — Batman Merkez ve ilçeler", "600 TL",
     "Beşiri, Gercüş, Hasankeyf, Kozluk ve Sason dahil. İlçe için ayrı yol ücreti alınmaz. "
     "Arızayı yerinde tespit ediyoruz; onarımı yaptırmak istemezseniz yalnızca bu ücret alınır."),
    ("Servis ücreti — Batman köyleri", "1.000 TL",
     "Merkez ve ilçe dışındaki köy adresleri için geçerlidir."),
    ("Buzdolabı kompresör (motor) değişimi", "8.000 – 11.000 TL",
     "Gaz tipine, motor büyüklüğüne ve dolabın litresine göre değişir."),
    ("Derin dondurucu kompresör değişimi", "8.000 – 10.000 TL",
     "400, 500, 600 ve 800 litre modellerde hacme göre değişir."),
    ("Buzdolabı gaz kaçağı onarımı", "yaklaşık 5.000 TL",
     "Kaçak gözle görünmüyorsa dolabın arkası kesilir; yaklaşık 3.000 TL parça + nakliye."),
    ("Buzdolabı fan değişimi", "yaklaşık 2.000 TL",
     "Parça 600–700 TL. Üst modellerde parça 3.000–3.200 TL'ye çıkar, toplam 5.000 TL'ye kadar."),
    ("Buzdolabı termostat değişimi", "yaklaşık 1.500 TL",
     "İşçilik dahil. Parçası pahalı modellerde 2.000 TL'ye kadar çıkabilir."),
    ("Çamaşır makinesi pompa değişimi", "2.500 TL",
     "Parça 800–900 TL, işçilik dahil toplam fiyattır."),
    ("Çamaşır makinesi su ventili değişimi", "1.100 TL",
     "Parça 400 TL, işçilik dahil toplam fiyattır."),
    ("Bulaşık makinesi parça değişimleri", "1.000 – 2.000 TL",
     "Markaya ve değişen parçaya göre değişir."),
]

# ---------------------------------------------------------------- güven maddeleri

GUVEN = [
    ("Aynı gün yerinde servis",
     "Batman merkezde arıza bildiriminden sonra genellikle 2 saat içinde adresteyiz."),
    ("Önce buzdolabı kuralı",
     "Buzdolabı ve derin dondurucu çağrılarını her zaman öne alıyoruz — içindeki gıda bozulmasın diye."),
    ("Onarımlar evinizde",
     "Onarımların büyük çoğunluğunu cihazı yerinden oynatmadan, evinizde tamamlıyoruz."),
    ("Parçalara 1 yıl garanti",
     "Taktığımız her parça bir yıl garantilidir."),
    ("Önce fiyat, sonra işlem",
     "Arızayı tespit edip maliyeti söylüyoruz. Yaptırmak istemezseniz yalnızca servis ücreti alınır."),
    ("8 yılı aşkın saha tecrübesi",
     "Batman ve ilçelerinde 8 yılı aşkın süredir beyaz eşya onarımı yapıyoruz."),
    ("7 gün 24 saat ulaşılabilir",
     "Pazar ve tatil günleri dahil, acil durumlarda gece gündüz ulaşabilirsiniz."),
    ("Belgeli teknik servis",
     "Millî Eğitim Bakanlığı İş Yeri Açma Belgesi — meslek dalı: Soğutma Sistemleri."),
    ("Stokta olmayan parça 1–2 günde",
     "Parça elimizde yoksa sipariş edip 1–2 gün içinde takıyor, süreç boyunca sizi bilgilendiriyoruz."),
]
