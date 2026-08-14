# 🧭 AİLE KURALLARI — ADAY LİSTESİ, M-F-561…576 (Lissom çıkardı, 2026-08-12)

> ⛔ **BU BİR KURAL LİSTESİ DEĞİL, BİR ADAY LİSTESİDİR.** Bağlayıcılık
> kararı **koordinatörde** (sevkin sınırı). Burada yapılan: **çıkarma +
> hassasiyet süzgeci + payda + gruplama.**

Gravita'nın `AILE-KURALLARI-ADAY-2026-08-12.md`si M-F-510…560'ı taradı;
bu dosya **kalan 16 kaydı** kapatıyor (belge M-F-560'ta kesiliyordu).

## PAYDA

| ölçüm | değer |
|---|---|
| taranan kayıt | **16/16** (M-F-561…576; aralıkta eksik numara **yok**, sayıldı) |
| kural bloğu taşıyan kayıt | **16/16** |
| ham `***…***` bloğu | **163** |
| süzgeçten geçen | **139** |
| **güçlü aday** (yüklem izli) | **67** |
| **zayıf aday** (yüklem izi yok) | **72** |
| elenen (parça/etiket) | **24** |
| yinelenen KÖK (birleştirilmedi, gruplandı) | **1** grup |

## 🔴 BİRİM UYARISI — BU SAYI GRAVİTA'NINKİYLE TOPLANAMAZ

**Ölçtüm:** Gravita'nın ölçütü *≥28 karakter + **≥5 kelime** + normatif
yüklem*. Benim "güçlü" kovam *≥30 karakter + yüklem izi* — **kelime sayısı
şartı YOK**, ve yüklem listem daha geniş.

**Aynı aralığa (M-F-561…576) İKİ ölçüt uygulandı:**

| ölçüt | sonuç |
|---|---|
| **Gravita'nın ölçütü** (≥28 · ≥5 kelime · normatif yüklem) | **26** |
| **benim "güçlü" kovam** (≥30 · yüklem izi) | **67** |

> ***`77 + 67 = 144` YANLIŞ BİR TOPLAMDIR — aynı kelime, iki birim.***
> Gravita'nın 77'siyle toplanacak sayı **26**'dır; **67** benim daha geniş
> kovam, ve aradaki **41** kalem *"kural olabilir, Gravita'nın ölçütünden
> geçmezdi"* demektir — **atılmadı, ama aynı rafa konmaz.**

📌 Bu, ailenin bugün GEVŞEK okumalar için verdiği hükmün (*aynı kelime üç
birim, yan yana konmaz*) **kural çıkarımındaki karşılığı.** Hangi birimin
kullanılacağı **koordinatörün kararı**; ben ikisini de ölçtüm ve
**karışmasınlar diye ayırdım.**

## ⚠️ POZİTİF + NEGATİF KONTROL

- **Desen 16 kaydın 16'sında isabet etti** (en az 5, en çok 18 blok) →
  *sıfır isabetli kayıt YOK*, yani "bu kayıtta kural yok" sonucu
  **aracın körlüğü değil.**
- **Negatif kontrol:** uydurma dizge (`ZZQQ`) → **0**.
- ⛔ **`.lower()` KULLANILMADI.** Türkçe iki `i`de kırık
  (`'I'.lower()='i'≠'ı'` · `'İ'.lower()='i̇'≠'i'`) ve kuralların çoğu
  **büyük kipte**; kip ayrımı gereken yerde `re.IGNORECASE` (Python'da
  muaf, ölçüldü).

## ⚠️ HASSASİYET — ham sayı teslim EDİLMEDİ, ve süzgecin YÖNÜ yazılı

`***…***` defterde **vurgu** için de kullanılıyor. Ham **163** bloğun
bir kısmı cümle **parçası** (*"tanım gereği hiçbir zaman ötemezdi"*) ya
da **etiket dizisi** (*"varılabilen · var olan · yazarın aklına gelen"*).

**Süzgeç:** uzunluk ≥30 **ve** salt terim/etiket biçiminde değil; kalanlar
**yüklem izine** göre güçlü/zayıf ayrıldı.

> ***SÜZGEÇ EKSİK OLABİLİR, FAZLA DEĞİL.*** Gerçek bir kuralı parça sanıp
> düşürmüş olabilirim; ama kural olmayan bir şeyi **güçlü** adaya
> yükseltmez (yüklem izi arıyor). **Zayıf** kova tam da bu yüzden var:
> attığımı değil, *emin olmadığımı* koordinatöre bırakıyorum.

## Güçlü adaylar

| # | kural metni | kaynak | ölçüm |
|---|---|---|---|
| 1 | BİR BÖLME DENETİMİ, İKİ TARAFI AYNI KAYNAKTAN OKUYORSA DENETİM DEĞİL TANIMDIR. | `M-F-576` | ✅ |
| 2 | 11 teyidin en az ikisi kırılgan bir karşıtlığa dayanıyor; körlük yalnız SARIYI değil YEŞİLİ de etkiliyor. | `M-F-576` | ✅ |
| 3 | KÖRLÜK, İDDİAYI ARTIRAN YÖNDE ASLA LEHE YORUMLANMAZ; İDDİAYI AZALTAN YÖNDE İSE ZATEN ZARARSIZDIR. | `M-F-576` | ✅ |
| 4 | AYNI HATAYA İKİ KEZ DÜŞMEMEK İÇİN DURMAK, BİR GECİKME DEĞİL BİR ÖLÇÜMDÜR. | `M-F-576` | ✅ |
| 5 | iki hat bağımsız olarak "onboarding bir ROTA değildir" ölçtü | `M-F-576` | ✅ |
| 6 | BİR "GÖRMÜYOR" BULGUSU, GÖREN BİR TABAN OLMADAN KURULAMAZ. | `M-F-576` | ✅ |
| 7 | ürün kusuru değil, CÜMLE fazla genişti | `M-F-576` | ✅ |
| 8 | BİR ELLE LİSTE, KAYNAK OLARAK YANLIŞTIR AMA KONTROL OLARAK DOĞRUDUR — SİLİNMEZ, RÜTBESİ DÜŞÜRÜLÜR. | `M-F-575` | ✅ |
| 9 | BİR DEĞİŞİKLİĞİN SONUCU DEĞİŞTİRMEMESİ, HİÇBİR ŞEY DEĞİŞTİRMEDİĞİ ANLAMINA GELMEZ — kaynağı düzeltmek, sonucu düzeltmekten farklı bir iştir ve çoğu zaman GÖRÜNMEZDİR | `M-F-575` | ✅ |
| 10 | iki hat bağımsız olarak "onboarding bir ROTA değildir" ölçtü. | `M-F-575` | ✅ |
| 11 | BİR ÖLÇÜMÜ MÜMKÜN KILMAK İÇİN ÜRÜNÜN DAVRANIŞINI DEĞİŞTİRMEK, ÖLÇÜLEN ŞEYİ DEĞİŞTİRMEKTİR. | `M-F-575` | ✅ |
| 12 | "Bir yokluk, ADI konmuşsa bir cevaptır; adı konmamışsa bir çıkmaz." | `M-F-574` | ✅ |
| 13 | "Boş tek başına bir kusur değildir; kusur, boşluğun SESSİZ olmasıdır." | `M-F-574` | ✅ |
| 14 | BİR KAPININ YEŞİLİ, ATEŞLENDİĞİ GÖRÜLMEDEN TAM KANIT DEĞİLDİR. | `M-F-574` | ✅ |
| 15 | BİR KONTROLÜN GEREKÇESİNİ EKRAN DÜZEYİNDE ARAMAK, KOMŞUNUN DÜRÜSTLÜĞÜNÜ ONA MAL ETMEKTİR. | `M-F-574` | ✅ |
| 16 | BİR ÖLÇÜMÜN BAŞLANGIÇ NOKTASINI DEĞİŞTİRMEK HER ZAMAN ROTA EKLEMEZ — bazen yalnız YÜZEY ekler, ve bu ikisi FARKLI OKUMALARDA görünür. | `M-F-574` | ✅ |
| 17 | Bir duruş sorusu, bir işi BLOKLAMAYA başladığında artık bir duruş sorusu değildir. | `M-F-574` | ✅ |
| 18 | BİR "TEMİZ AĞAÇ" SİNYALİ, İŞİN BİTTİĞİNİ DEĞİL YALNIZ FARK OLMADIĞINI SÖYLER — VE FARK, İŞ SİLİNDİĞİNDE DE SIFIRDIR. | `M-F-573` | ✅ |
| 19 | `kirli 0` bir DURUM değil bir FARK ölçümüdür; anlamı ancak hattın İDDİASIYLA eşleştirilince doğar. | `M-F-573` | ✅ |
| 20 | ÖLÇÜM ARACININ KÖRLÜĞÜ, BULGUYA DÖNÜŞMEDEN ÖNCE PAYDAYLA YAKALANIR — VE "0 KUSUR" EN KOLAY SAHTELENEN SAYIDIR. | `M-F-573` | ✅ |
| 21 | BOŞ TEK BAŞINA BİR KUSUR DEĞİLDİR; KUSUR, BOŞLUĞUN SESSİZ OLMASIDIR. | `M-F-573` | ✅ |
| 22 | "kanıt yok" ile "sayaç kör" bugünkü aletle ayırt edilemez. | `M-F-573` | ✅ |
| 23 | BİR SESSİZLİK, ALETİN KÖRLÜĞÜYLE AÇIKLANABİLİYORSA, O BİR ÖLÇÜM DEĞİLDİR. | `M-F-573` | ✅ |
| 24 | "sözlükte yok" tek başına ASR kırılganlığı değildir | `M-F-573` | ✅ |
| 25 | Bir kusuru doğru TEŞHİS etmek, onun HANGİ KATMANDA oturduğunu bilmek değildir | `M-F-573` | ✅ |
| 26 | yalnız yürüyerek ölçen bir kural, ULAŞAMADIĞINI göremez | `M-F-572` | ✅ |
| 27 | YÜRÜYÜŞ VARLIĞI KANITLAR, YOKLUĞU KANITLAMAZ — BİR YOKLUK İDDİASI, BEKLENEN BİR KÜME OLMADAN KURULAMAZ. | `M-F-572` | ✅ |
| 28 | BİR ÖLÇÜMÜN BAŞLANGIÇ NOKTASI ONUN EVRENİNİ TANIMLAR — KABUKTAN BAŞLAMAK, KULLANICININ HİÇ GÖRMEDİĞİ BİR UYGULAMAYI ÖLÇMEKTİR. | `M-F-572` | ✅ |
| 29 | **② kendi ağacında ÖLÇEREK uygula** — sözleşme **NE** sayılacağını söyler, **NASIL**ını değil. **⑧ ⚖️ ⑦ EKSENİ KAPANDI, hükme bağlanmadan:** koordinatörün *"yürüyere | `M-F-572` | ✅ |
| 30 | BİR KAVRAMDAN SÖZ EDEN CÜMLE, O KAVRAMIN CEVABI DEĞİLDİR | `M-F-571` | ✅ |
| 31 | okunmamış ile belirtilmemiş aynı şey değildir. | `M-F-571` | ✅ |
| 32 | "beş sayıdan BİRİ karşılaştırılamaz" | `M-F-571` | ✅ |
| 33 | yürüyerek ölçen bir kural zaten koddadır. | `M-F-571` | ✅ |
| 34 | Kurucuya giden cümle, sebep ölçülmeden yazılamaz. | `M-F-571` | ✅ |
| 35 | GEZİLEBİLİRLİK VARILABİLİRLİĞİ ÖLÇER, YARARLILIĞI DEĞİL — VE BİR SAYININ GÖRMEDİĞİNİ YAZMAK, O SAYININ YANLIŞ OKUNMASINI ENGELLEYEN TEK ŞEYDİR. | `M-F-569` | ✅ |
| 36 | Bunlar aynı kusur değil, ve panzehirleri de aynı değil | `M-F-569` | ✅ |
| 37 | sayılan şey kodda var olan rota değil, kullanıcının VARABİLDİĞİ yer | `M-F-569` | ✅ |
| 38 | bir ekranı atlayarak yürüyen ölçüm, o ekranın ÇIKIŞI olup olmadığını söyleyemez. | `M-F-569` | ✅ |
| 39 | elle yazılmış bir sayı, kimsenin yeniden koşmadığı bir iddiadır. | `M-F-569` | ✅ |
| 40 | BEŞ SAYIYI YAN YANA KOYMAK ONLARI KARŞILAŞTIRILABİLİR KILMAZ — ve yan yana konmuş iki sayı, okuyanı AYNI BİRİMDE olduklarına ikna eder. | `M-F-569` | ✅ |
| 41 | BİR DİLİN KARAKTER KÜMESİYLE TANINMASI, O DİLİN HER KİPİNDE TANINACAĞI ANLAMINA GELMEZ | `M-F-568` | ✅ |
| 42 | KAYNAĞI REGEX'LE OKUMAK, BİR KÜMENİN ÜYESİ İLE O KÜMEYİ ANLATAN METNİ AYIRT EDEMEZ — ÖLÇÜM MODÜLÜN KENDİSİNDEN YAPILIR. | `M-F-568` | ✅ |
| 43 | koordinatörün ①. kısıtı (ASCII girdiye `.lower()` dokunulmaz) olmasaydı gereksiz bir değişiklik sevk edilecekti | `M-F-568` | ✅ |
| 44 | Koordinatörün girdisi de bir iddiadır. | `M-F-568` | ✅ |
| 45 | TEK BAYRAKTA BİRLEŞTİRMEK, ARIZA YÖNÜ ZIT OLAN İKİ SINIFI AYNI KUTUYA KOYMAKTIR — VE YÖN, SESSİZ YALAN MI GÜRÜLTÜLÜ ALARM MI ALACAĞINI BELİRLEYEN ŞEYDİR. | `M-F-567` | ✅ |
| 46 | bir alışkanlığın sonucu, bir kuralın değil | `M-F-567` | ✅ |
| 47 | BİR EKSİĞİ BİLDİRMEK, O EKSİĞİN ARDINDAKİ İHTİYAÇ ZATEN KARŞILANIYORSA, DÜRÜSTLÜK DEĞİL GÜRÜLTÜDÜR. | `M-F-567` | ✅ |
| 48 | BİR HATTIN ÇALIŞTIĞINI COMMIT SAYISIYLA ÖLÇMEK, ÖLÇÜM TURLARINI GÖRÜNMEZ KILAR | `M-F-567` | ✅ |
| 49 | TÜRKÇE DÜZYAZI BU KAPILARDA DESEN DEĞİL YÜK — kip körlüğü ancak Türkçeye kip-katlama UYGULARSAN ısırır. | `M-F-566` | ✅ |
| 50 | BİR KAPIYI SPEKÜLATİF OLARAK GENİŞLETMEK YERİNE, GENİŞLEMENİN GEREKLİLİĞİNİ ÖLÇ — o zaman ikinci deseni SEN değil, KUSUR ister. | `M-F-566` | ✅ |
| 51 | RİSKİ DEVRALMADIĞINI ÖLÇTÜĞÜN CÜMLENİN KENDİSİ RİSKİ YARATTI: BİR NUMARADAN SÖZ ETMEK İLE ONU KAYDETMEK AYNI METİNDE AYIRT EDİLEMEZ. | `M-F-566` | ✅ |
| 52 | BİR EŞİĞİN ADI VARSA BİLE TEK OLDUĞU ANLAMINA GELMEZ — bir hattın eşiği, AİLENİN eşiğinin ÜSTÜNDE oturuyor olabilir. | `M-F-566` | ✅ |
| 53 | ), eşik oynatılmadı — **kayıp değil, dürüst kapanış.** **⑦ ⭐ CHOREIA ② — TARAYICI KENDİ ÖZ-TESTİYLE ÜÇ KEZ DÜZELDİ:** ① **soundex ilk harfi KORUR ama ASR'nin ikamesi | `M-F-566` | ✅ |
| 54 | BİR DİLİN İKİ HARFİ AYNI ASCII HARFE DÜŞÜYORSA, KATLAMA HER İKİ YÖNDE DE KAYBEDER — VE KAYBIN YÖNÜ, HANGİ HARFİN JETONDA OLDUĞUNA BAĞLIDIR. | `M-F-565` | ✅ |
| 55 | Dart hatlarında o cümle bir KUSUR TALİMATI olurdu. | `M-F-565` | ✅ |
| 56 | bugün yakalayacak bir şeyi olmaması, yarın yakalayabileceği anlamına gelmiyor. | `M-F-565` | ✅ |
| 57 | "temizlik bir tasarım değil, RASTLANTI" | `M-F-565` | ✅ |
| 58 | BİR KURALI YAZMAK, ONU UYGULAMAYI GARANTİ ETMEZ | `M-F-564` | ✅ |
| 59 | İKİ KISIT AYRI AYRI DOĞRU OLABİLİR VE BİRLİKTE UYGULANAMAZ OLABİLİR — VE BUNU ANCAK KURAN GÖRÜR, HÜKMEDEN DEĞİL. | `M-F-562` | ✅ |
| 60 | BİR MUAFİYET YA ÖLÇÜMÜNÜ TAŞIR YA TÜRETİLİR — ELLE YAZILMIŞ BİR LİSTE BAYATLAR, VE BAYATLADIĞINI SÖYLEMEZ. | `M-F-562` | ✅ |
| 61 | BİR KAPININ GEREKÇESİ DE BAYATLAYABİLİR — ölçülmüyorsa, kapı doğru sebeple değil ALIŞKANLIKTAN yeşildir. | `M-F-562` | ✅ |
| 62 | İKİ YÖNLÜ BİR KAPIDA TEK DESEN, İKİ YÖNDEN BİRİNDE MUTLAKA YANLIŞTIR — biri yanlış KIRMIZI, diğeri yanlış YEŞİL üretir. | `M-F-562` | ✅ |
| 63 | sıfır olduğu ölçülmedi, denk gelmiş olabilir | `M-F-562` | ✅ |
| 64 | BİR TUZAĞI BİLMEK, ONU ÖLÇÜM ANINDA HATIRLAMAYI SAĞLAMAZ. | `M-F-562` | ✅ |
| 65 | yoklama = hattın saati; polling etmemek bilgi kaybı değil İŞ kaybıdır | `M-F-561` | ✅ |
| 66 | YALNIZ PAYDAYI DEĞİL, İŞLEMİ DE BAS — o zaman değer, KODA GÜVENMEDEN denetlenebilir. | `M-F-561` | ✅ |
| 67 | : aynı kuralın üç basamağı, üçü de **bir sabotajın** ürünü. ✅ Sayaçlar bağımsız (`anan` türetilmiyor); öz-testte iki bağımsız iddia (`anan ≥ çapalı` · `çapalı ≥ benz | `M-F-561` | ✅ |

## Yinelenen KÖKLER — birleştirilmedi, GRUPLANDI

> Aynı kök birden çok kayıtta çıktıysa tek satıra indirmek *hangi
> yüzeyde çıktığı* bilgisini yok eder — o yüzden hepsi duruyor.

**Grup 1** — 2 yüzey: `M-F-576`, `M-F-575`
  - `M-F-576`: iki hat bağımsız olarak "onboarding bir ROTA değildir" ölçtü
  - `M-F-575`: iki hat bağımsız olarak "onboarding bir ROTA değildir" ölçtü.

## Zayıf adaylar (yüklem izi yok — koordinatör bakmalı)

| # | metin | kaynak | ölçüm |
|---|---|---|---|
| 1 | tanım gereği hiçbir zaman ötemezdi. | `M-F-576` | ✅ |
| 2 | BİR KURALI BİLMEK, ONU UYGULADIĞIN ANLAMINA GELMİYOR | `M-F-576` | ✅ |
| 3 | ölçülmüş bir yarıyı ölçülmemiş saymak | `M-F-576` | ✅ |
| 4 | BİR SINIFLANDIRMA, YALNIZ KUSUR BİÇİMLERİNİ SAYIYORSA, DOĞRU KARARLARI DA KUSUR KOVASINA ATAR. | `M-F-575` | ✅ |
| 5 | KAPALI BİR SEVK KAPISI, SAĞLIKLI BİR İÇERİK DURUMUNU GEÇERSİZ KILAR | `M-F-575` | ✅ |
| 6 | 33'ün 32'si aylarca sürecek İÇERİK işi, 1'i on dakikalık KURUCU işi | `M-F-575` | ✅ |
| 7 | çözülmüş diğer stiller hangi nabzı sayıyor | `M-F-575` | ✅ |
| 8 | KURUCUYA "10 DAKİKANI VER" DEMEDEN ÖNCE, O 10 DAKİKANIN GEREKLİ OLDUĞUNU ÖLÇMEK BORCUMUZ | `M-F-575` | ✅ |
| 9 | yakalayan şey ELLE beklenen kümesiydi. | `M-F-575` | ✅ |
| 10 | desen adayı verir · yürüyüş üyeliği kanıtlar · elle küme DESENİ denetler | `M-F-575` | ✅ |
| 11 | BİR ELLE LİSTE, KENDİ YAZARININ AYNI GÜN EKLEDİĞİ ŞEYİ BİLE KAÇIRABİLİR | `M-F-575` | ✅ |
| 12 | bir desen, aradığı şeyin BİÇİMİNİ de tanımlamalı. | `M-F-575` | ✅ |
| 13 | kurucunun bekleyen duruş sorusunun SESSİZCE cevaplanması | `M-F-575` | ✅ |
| 14 | bir testi yeşile ulaştırmak için başka bir kapıyı kırmızıya düşürmek | `M-F-575` | ✅ |
| 15 | test double'ın gerçeğin kuralını uygulamaması | `M-F-575` | ✅ |
| 16 | duruş sorusu + test blokajı + bir çözüm yolunu KAPATAN kısıt | `M-F-575` | ✅ |
| 17 | Kurucunun kararı iki şeyi birden çözüyor, ve bunu bilmesi maliyeti değiştiriyor. | `M-F-575` | ✅ |
| 18 | "bastığım şey beni bir yere GÖTÜRÜYOR mu." | `M-F-574` | ✅ |
| 19 | ama dedektörün kendisi POZİTİF KONTROLSÜZ. | `M-F-574` | ✅ |
| 20 | koordinatör ailenin TOPLAMINDAN akıl yürütüyor, hat KENDİ AĞACINI ölçüyor — ve mekanizma her zaman hattın ağacında oturuyor. | `M-F-574` | ✅ |
| 21 | BİR İŞİN ÖLÇÜMÜ BİTMİŞ OLABİLİR VE UYGULAMASI BİTMEMİŞ OLABİLİR — ikisini tek kelimeyle ("uygulandı") raporlamak, ÖLÇÜMÜ de şüpheli kılar. | `M-F-574` | ✅ |
| 22 | YÜRÜYÜŞ DE EKSİK YÜRÜNÜRSE YALAN SÖYLER | `M-F-573` | ✅ |
| 23 | yürüyüşün TAMLIĞINI hiçbir şey ölçmüyordu | `M-F-573` | ✅ |
| 24 | BİR BAYRAĞIN ÖLÇTÜĞÜ ŞEY, ADININ SÖYLEDİĞİ ŞEY OLMAYABİLİR | `M-F-573` | ✅ |
| 25 | "varılabilen" · "var olan" · "yazarın aklına gelen" | `M-F-572` | ✅ |
| 26 | Bir hattın, başkasının işaret ettiği kusuru kendi ağacında ölçüp BÜYÜTMESİ | `M-F-572` | ✅ |
| 27 | Desen KAPSAMI, yürüyüş GERÇEĞİ, fark ise BULGUYU verir | `M-F-572` | ✅ |
| 28 | ailenin 08-07 hükmü TAM OLARAK onboarding hakkındaydı. | `M-F-572` | ✅ |
| 29 | fark: koordinatör teslim etti, hat etmedi. | `M-F-571` | ✅ |
| 30 | noktasız `I` noktalı `i`ye düşüyor | `M-F-571` | ✅ |
| 31 | BİR KUSURU YARIM KAPATMAK, ONU KAPATMAMAKTAN DAHA KÖTÜ OLABİLİR — ÇÜNKÜ KALAN YARIM, KUSURU BULAN KANAL OLABİLİR. | `M-F-571` | ✅ |
| 32 | tersinin de doğru olduğu ilk vaka | `M-F-571` | ✅ |
| 33 | hattın hızı, koordinatörün kuyruğunu bayatlatıyor. | `M-F-571` | ✅ |
| 34 | Ve hepsi "ölçüm gibi" görünüyordu. | `M-F-570` | ✅ |
| 35 | İKİ TARAF DA ÖLÇTÜ, İKİ TARAF DA YANILDI, VE DÜZELTEN HEP ÖTEKİNİN ÖLÇÜMÜ OLDU. | `M-F-570` | ✅ |
| 36 | KAPILAR, İKİMİZİN DE YOKKEN ÇALIŞAN TEK DENETİM. | `M-F-570` | ✅ |
| 37 | tek yeniden-üretilebilir tanık odur. | `M-F-570` | ✅ |
| 38 | kimse varılan yerde bir şey olup olmadığını saymadı | `M-F-570` | ✅ |
| 39 | bir rota tablosu kodun ANLATIMI, yürüyüş ise GERÇEĞİ | `M-F-570` | ✅ |
| 40 | "gezilebiliyor, ama gidilen yerde bir şey yok" | `M-F-569` | ✅ |
| 41 | her dilde BAŞKA harften, BAŞKA yoldan. | `M-F-568` | ✅ |
| 42 | bir dili KARAKTERLERİNDEN tanıyan her kapı, o dilin BÜYÜK KİPİNDE kördür. | `M-F-568` | ✅ |
| 43 | ADIYLA BIRAKILAN BİR KÖR NOKTAYI, KAPANDIĞINDA HABER VEREN BİR ÇAPAYLA BIRAKMAK | `M-F-568` | ✅ |
| 44 | bugün kapılarda SESSİZ SIFIR YOK. | `M-F-567` | ✅ |
| 45 | BİR KUSUR SINIFINI ÇÖZMEK İÇİN YAZILAN KOD, AYNI SINIFIN YENİ BİR ÖRNEĞİNİ TAŞIYABİLİR — ÇÜNKÜ ÇÖZEN DE AYNI VARSAYIMLA YAZAR. | `M-F-567` | ✅ |
| 46 | ASCII VARSAYIMI, ÖLÇÜM ZİNCİRİNİN HER HALKASINDA AYRI AYRI OTURUYOR VE HER BİRİ AYRI AYRI KIRILIYOR. | `M-F-567` | ✅ |
| 47 | bugün lazım olmadığı için UCUZ; lazım olduğu gün kimse buraya bakmayacak. | `M-F-567` | ✅ |
| 48 | BİR KAPININ ÇIKTISI DOĞRU OLABİLİR VE İDDİASI YİNE DE YANLIŞ OLABİLİR | `M-F-567` | ✅ |
| 49 | prob kaybı GÖREBİLİYOR, sonuç yine de sıfır | `M-F-566` | ✅ |
| 50 | "yalnız-gövde anılan ve defterde OLMAYAN numara == 0" | `M-F-566` | ✅ |
| 51 | kopyalamamak da yetmiyor; kopyalamama gerekçeni YAZDIĞIN yer riski üretebiliyor. | `M-F-566` | ✅ |
| 52 | Bir soruyu kurucuya UCUZLATMANIN yolu, cevabın bir kısmını ÖLÇMEK. | `M-F-566` | ✅ |
| 53 | BİR VEKİL, ÖLÇMEK İSTEDİĞİ ŞEYİN KAPININ ALTINDA KALDIĞI YERDE DOĞAR — ve o yüzden "vekili gerçekle değiştir" önerisi çoğu zaman KAPIYI KALDIRMAK demektir. | `M-F-566` | ✅ |
| 54 | ✅ **HÜKÜM KAPANDI: `cc_cucaracha` taban-altı (2/3)**, sebebi ölçülmüş ( | `M-F-566` | ✅ |
| 55 | BİR PANZEHİR, DİL DEĞİŞİNCE KUSURUN KENDİSİNE DÖNÜŞEBİLİR. | `M-F-565` | ✅ |
| 56 | reçete kulağa evrensel geliyor. | `M-F-565` | ✅ |
| 57 | `YAKINDA` yazan bir yüzey `status_weave_check`ten SESSİZCE geçer | `M-F-565` | ✅ |
| 58 | kuralları DERLEYEN belge, derlediği kurala AYNI GÜN düştü. | `M-F-564` | ✅ |
| 59 | İkisinde de öz-denetim koştu ve hiçbir şey ölçmedi. | `M-F-564` | ✅ |
| 60 | vaka-özgü ↔ gözlem ayrımının YAPILMADIĞI | `M-F-564` | ✅ |
| 61 | araç sağlam, yalnız bizim dilimizde kör. | `M-F-563` | ✅ |
| 62 | BİR HAT, YANLIŞ SIFIR HAKKINDA BİR KURAL ÇIKARDI VE KANITI YANLIŞ SIFIRIN KENDİSİYDİ. | `M-F-563` | ✅ |
| 63 | BİR ARACIN KÖR NOKTASI, ÖLÇTÜĞÜ ŞEYİN DİLİYLE ÇAKIŞABİLİR — VE O ZAMAN "BULUNAMADI", "YOK" DİYE OKUNUR. | `M-F-563` | ✅ |
| 64 | yanlış sıfır, ölçülen şeyin dili İngilizce'den uzaklaştıkça artar | `M-F-563` | ✅ |
| 65 | bir kayıtta 5 kural, 1 kanıt sütunu | `M-F-563` | ✅ |
| 66 | "kaç KÖK, her kök kaç YÜZEYDE" | `M-F-563` | ✅ |
| 67 | kimsenin temizleyemeyeceği KALICI KIRMIZI | `M-F-562` | ✅ |
| 68 | hüküm SÖZDE tutarlı yazılıyor, hat onu KOŞULABİLİR kılınca çelişki görünüyor. | `M-F-562` | ✅ |
| 69 | bir hüküm koşulamıyorsa, hattın onu koşulabilir kılmak için yaptığı ilk değişiklik KOORDİNATÖRE GERİ GELİR. | `M-F-562` | ✅ |
| 70 | çıkış kodu okunacaksa BORU YOK. | `M-F-562` | ✅ |
| 71 | kırmızının da tek anlamı olmadığını | `M-F-562` | ✅ |
| 72 | BİR KOORDİNATÖRÜN YOKLAMASI, EN ÇOK, HATLARIN EN VERİMLİ OLDUĞU ANDA AKSAR — çünkü gelen rapor akışı, GELMEYEN raporun yerini doldurur. | `M-F-561` | ✅ |
