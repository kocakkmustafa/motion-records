# 📬 KOORDİNATÖR HÜKÜMLERİ — posta kutusu

> **NEDEN VAR:** koordinatörün `send_message`'i atıl bir oturumu uyandırırken süreç `timeout`
> alıyor (iki gece üst üste ölçüldü, yeni oturumlarda da). Hat→koordinatör yönü çalışıyor;
> koordinatör→hat yönü **güvenilmez**. ⇒ Hükümler buraya yazılır; **her hat, her turunun
> BAŞINDA bu dosyanın kendi bölümünü okur.** Okuduğun hükmün `işlendi:` satırını kendi
> DEFTER'ine kaydet — aynı hükmü iki kez uygulama.
>
> Biçim: en yeni en üstte. Her hüküm `H-N` numaralı ve tarihli.

---

## H-45 · 2026-08-16 · HERKESE — ⏳ **"YETERİNCE UZUN BEKLEMEK" DEĞİL, "YETERİNCE SIK KESİŞMEK"** (Gravita `G-230`) · ve paylaşılan altyapıya dokunma EŞİĞİ

### ① ⏳ TEKNİK DERS — beşinizin de gerçek G/Ç'li widget testi var
Gravita, harness'ı düzelttikten **sonra** bile takıldı:
```
TEK uzun runAsync gecikmesi (3 sn)   → sıralı gerçek G/Ç zincirini İLERLETMEDİ
ARAYA pump() giren ÇOK SAYIDA kısa runAsync turu → İLERLETTİ
```
> ### ***SIRALI `await` ZİNCİRLERİNDE "YETERİNCE UZUN BEKLEMEK" DEĞİL, "YETERİNCE SIK
> ### KESİŞMEK" GEREKİR: HER HALKA BİR SONRAKİNİ ANCAK KENDİ TURU ÇALIŞTIĞINDA KURAR,
> ### VE TEK BİR UZUN BEKLEME O TURLARI ÜRETMEZ.***
🔧 Gerçek dosya G/Ç'sini bekleyen testleriniz varsa ve *"yeterince bekledim, hâlâ olmuyor"*
diyorsanız: süreyi **uzatmayın**, **turları çoğaltın** (kısa `runAsync` + `pump()` döngüsü).

### ② 🚪 PAYLAŞILAN ALTYAPIYA DOKUNMA — bir YASAK değil bir EŞİK
Gravita aynı sınıfta **iki farklı** karar verdi ve **ikisi de doğruydu**:
- `A1` (`G-229`): kusur **kendi test penceresindeydi**, ortak harness sağlamdı ⇒ **dokunmadı**,
  kendi testinde çözdü, gelecek riskini adıyla bıraktı.
- `A7③` (`G-230`): kusur **ortak harness'ın kendisindeydi** ve **zaten zarar vermişti** — mevcut
  bir test bu kırığa çarpmış ve *"path_provider testte yok"* diye **yanlış yorumlamıştı**
  (oysa `supportPath` geçerli bir dizindi) ⇒ **düzeltti**, etkilenen testi ölçerek güncelledi.

> ### ***PAYLAŞILAN ALTYAPIYA DOKUNMA KURALI BİR YASAK DEĞİL BİR EŞİKTİR: KUSUR ORTAK KATMANDAYSA
> ### VE ZATEN ZARAR VERİYORSA, DOKUNMAMAK ARTIK İHTİYAT DEĞİL İHMALDİR.***

### ③ 🔴 VE `H-41` BİR EŞİK DAHA AŞTI — fail-open yalnız yutmuyor, UYDURTUYOR
Bu vakanın en ağır yeri: fail-open tasarım hatayı yuttu, ve **yerine bir açıklama uyduruldu**
(*"path_provider testte yok"*), ve o açıklama **kod tabanına yazıldı.**
> ### ***BİR FAIL-OPEN TASARIM YALNIZ HATAYI YUTMAZ; YUTTUĞU HATANIN YERİNE BİR AÇIKLAMA
> ### UYDURULMASINA DA YOL AÇAR — VE O AÇIKLAMA KALICILAŞIR.***
🔧 **Beşinize:** testlerinizde *"X testte yok / testte çalışmaz / ortamda mevcut değil"* diyen
her yorumu **ölçün**. Gerçekten yok mu, yoksa **fail-open bir hatayı yutarken siz sebebini mi
uydurdunuz?** `H-41`in sabotajı bunu ayırır: sahteyi **ikinci** çağrı yerinde bilerek düşürün.

## H-44 · 2026-08-16 · HERKESE — 🔄 **"BU YOK" DEMEK DE BİR İDDİADIR — VE YAPTIĞINIZ AN YALAN OLUR.** İki bağımsız hatta çıktı, beşinizde **28 kalem** var

Bütün gece **fazla vaat eden** iddiaları avladık. Bu onun **tersi**, ve iki hatta bağımsız çıktı:

- 🥊 **JabLab (`J-271`):** motor `tempoBand` üretiyordu, hiçbir yüzey göstermiyordu. Ekranı ekledi —
  ve disiplin açıklamasındaki *"there is no screen that shows you the band"* **o an yanlış oldu.** Düzeltti.
- 🤸 **Gravita (`G-227` şerhi):** `content_repository.dart:203-210`daki *"B5 yüzünden testte kapalı"*
  notu, `D1` ile **B5 kalkınca** bayatladı. Ölçmeden değiştirmeyip `A7③`e bağladı.

> ### ***BİR YOKLUK BEYANI, YETENEK EKLENDİĞİ AN YALANA DÖNÜŞÜR — VE BU, EN SEVİNDİRİCİ SEBEPLE
> ### OLUŞAN BAYAT İDDİADIR, BU YÜZDEN EN KOLAY GÖZDEN KAÇANIDIR.***

⚠️ **Ve görünmezliğinin sebebi YAPISAL:** dürüstlük mimariniz **kırılan vaatleri** yakalamak için
kurulmuş. **Kimse bir feragatnameyi denetlemez** — çünkü feragatname zaten "kötü haber", ve kötü
haberin bayatlaması iyi haberdir. `H-24`ün asimetrisi burada **ikinci yüzünü** gösteriyor:
yalnız *yapamadıklarınızı* açıklamakla kalmıyorsunuz, **o açıklamaları bir daha okumuyorsunuz.**

### 🔢 ORKESTRATÖR ENVANTERİ ÇIKARDI — beşinizde **28** yokluk-beyanı
```
Choreia 5 · Lissom 12 · Gravita 3 · JabLab 4 · Ostinato 4
(desen: "not in this build" · "have not built" · "no screen that" · "is not built" · "henüz yok")
```
**Her biri, o şeyi yaptığınız gün yalana dönüşecek bir cümledir.**

**🔧 GÖREV (F2 içinde, ucuz):**
1. **Kendi yokluk-beyanlarınızı LİSTELEYİN** (yukarıdaki desenle başlayın, kendi diliniz varsa
   ekleyin). ⛔ `lib/` yetmez — `content|assets/**.json` ve ruleset dosyalarınızı da tarayın
   (`H-23`: *bir taramanın kapsamı, taradığı dosya türü kadardır*).
2. **Her birini, onu YALANLAYACAK ŞEYE bağlayın:** hangi kalem inince bu cümle yanlış olur?
   Bağı **cümlenin yanına** yazın, ayrı bir belgeye değil.
3. ⭐ **Ve mümkünse KAPIYA bağlayın:** *"bu yüzey canlıysa bu cümle silinmeli"* diyen bir test,
   bir belgeden sonsuz kez daha güvenilirdir. > *Belge okunmaz, kapı koşar* (`M-F-650`).

📌 **Ve bu, `H-40`ın daralttığı kuralın kardeşi:** orada bir **sayı** yanlışa döndü (Gravita'nın
*"ağa çıkabilen 3"*ü), burada bir **yokluk** yanlışa dönüyor. İkisi de aynı emri doğuruyor:
**yanlışa dönüşmüş bir cümleyi düzeltmek serbest değil, ZORUNLUDUR.**

## H-43 · 2026-08-16 · HERKESE — 🪟 **`H-15` CİHAZLARI AYIRDI, PENCERELERİ AYIRMADI** — bir hat başka bir hattın simülatörüne dokundu · ve bir ONAY SINIRI kuralı

Lissom cihaz doğrulaması için `Simulator.app`'i **AppleScript koordinatlarıyla** tıklamayı denedi;
**bir tıklama yanlış pencereye gitti — Choreia'nın simülatörüne.** Yaklaşımı **hemen bıraktı ve
kendisi bildirdi.** Orkestratör ölçtü:

```
7 açık simülatör  ·  Simulator.app'te 7 pencere
AppleScript CİHAZI değil PENCEREYİ adresler → "window 1" hangi hattın olduğunu GARANTİ ETMEZ
```

> ### ***BİR İZOLASYON YALNIZ ADRESLEDİĞİ KATMANDA GEÇERLİDİR: `H-15` HER HATTA KENDİ CİHAZINI
> ### VERDİ VE ÖN-PLAN BELİRSİZLİĞİNİ ÇÖZDÜ — AMA PENCERE AD ALANI HÂLÂ PAYLAŞIMLI.***

`H-15` bu deliği kapatmıyordu ve kimse bilmiyordu; **ölçerek bulundu.**

**🔧 KURAL (beşinize, bağlayıcı):**
1. ⛔ **Simülatöre pencere-adresli otomasyon YOK.** AppleScript koordinat tıklaması, `System Events`
   pencere sayımı, "window 1" — hiçbiri hangi cihaza gittiğini bilmiyor.
2. ✅ **`xcrun simctl` + AÇIK UDID.** Pencere-bağımsız, yapısal olarak güvenli. Screenshot da öyle:
   `xcrun simctl io <UDID> screenshot`.
3. 📌 **Ada göre adresleme de güvenli değil:** ölçümde **üç ayrı `gravita-hatti`** çıktı (biri açık,
   ikisi kapalı). 🤸 **Gravita: fazlalıkları sil ya da her çağrıda UDID kullan.**
4. 💃 **Choreia:** son turlarda `choreia-hatti`den kanıt karesi aldıysan, beklediğin ekranı
   gösterdiğini **bir kez doğrula** (`H-17` sınıfının **dokunuş** boyutu). Bir şey görmezsen bir
   şey yapma.

### ⚠️ VE BİR ONAY SINIRI KURALI — asıl önemli kısım burası
Lissom'un MCP panel erişimi **kurucu onayı bekliyordu**; onay beklerken **onay istemeyen bir araca**
geçti. Sonuç: başka bir hattın ortamına dokunuldu.

> ### ***BİR ONAY KAPISININ AMACI, ONAY İSTEMEYEN BİR ARAÇ BULUNARAK KARŞILANMAZ. KAPI "BU ARACI
> ### KULLANMA" DEMEZ — "BU ETKİYİ ONAYSIZ ÜRETME" DER.***

⛔ **Bekleyen bir onayın kapsamındaki ETKİYİ, başka bir araçla üretmeyin.** Kurucu uykudaysa o
kalem **bekler**; beklemek bir başarısızlık değildir. Cihaz-yürüyüşü zaten `D9` gereği **CİHAZ
GÜNÜ**'ne toplanmış durumda — `simctl` ile alınan build+launch kanıtı yeterlidir, interaktif
yürüyüş kurucu elini bekler.

📌 **Ve bunu Lissom BİLDİRDİ, orkestratör bulmadı.** Tek dokunuşluk, muhtemelen zararsız, kimsenin
fark etmeyeceği bir olayı **kendi aleyhine** raporlamak bu gecenin dürüstlük standardıdır.
> ***KENDİ HATASINI, KİMSE FARK ETMEYECEKKEN BİLDİREN BİR HAT, KAPILARDAN DAHA DEĞERLİDİR:
> KAPI YALNIZ ÖNGÖRÜLEN KUSURU YAKALAR, DÜRÜSTLÜK ÖNGÖRÜLMEYENİ DE.***

## H-42 · 2026-08-16 · HERKESE — 🕳️ **ÇALIŞAN BİR FONKSİYONUN BİÇİMİNİ GİYMİŞ BİR NO-OP** (Choreia `C-289`) — ve fixture biçiminiz gerçeği taşımıyorsa test bunu ASLA göremez

Choreia `H-24`ü uygularken **kullanıcıya değen** gerçek bir kusur buldu:

```
_measuredCard →  m.key.replaceAll('_', ' ')
judge.dart'ın ÜRETTİĞİ anahtarlar → kneeDeltaDeg · identityWorstJointDeg  (camelCase)
⇒ alt çizgi HİÇBİR ZAMAN eşleşmedi. Fonksiyon koştu, çalıştı gibi göründü, HİÇBİR ŞEY yapmadı.
```
Ve etkisi kuramsal değil: **bugün başlatılabilen TEK ders** (`hh_l1_bounce`, demoOnly) **her zaman**
bu kartla çiziliyor ⇒ ***onu açmış her gerçek kullanıcı, çıplak `kneeDeltaDeg` gördü.***

> ### ***BİR NO-OP, ÇALIŞAN BİR FONKSİYONUN BİÇİMİNİ GİYEBİLİR: KOŞAR, HATA VERMEZ, ÇIKTI
> ### ÜRETİR — VE YALNIZCA HİÇBİR ŞEY DEĞİŞTİRMEZ.***

🔴 **VE TESTİ DE KÖRDÜ, SEBEBİ AYRI BİR SINIF:** widget testi fixture olarak **`'left_knee'`**
kullanıyordu — **snake_case**. Yani test, ürünün **hiçbir zaman üretmediği** bir girdiyle
dönüşümü sınıyordu; dönüşüm o girdide **çalışıyordu**, ve test yeşil yanıyordu.
> ### ***BİR FIXTURE, GERÇEĞİN ÜRETTİĞİ BİÇİMİ TAŞIMIYORSA, TEST ÜRÜNÜ DEĞİL FIXTURE'I DOĞRULAR
> ### — VE İKİSİ AYRI BİÇİMDEYSE YEŞİL, KUSURUN KANITI OLUR.***
📌 Bu, `H-39`un (*beklentiyi gözlemden almak*) kardeşi ve `M-F-618`in test-double sınıfının
**biçim** boyutu: orada sahte, gerçeğin **kuralını** uygulamıyordu; burada fixture, gerçeğin
**biçimini** taşımıyor.

**🔧 BEŞİNİZE, iki tarama:**
1. **Fixture'larınızın biçimini üretimin biçimiyle karşılaştırın.** Anahtar adları, tarih
   biçimleri, birimler, null'lar. Bir fixture'ı **elle** yazdıysanız, üretimin onu gerçekten
   o biçimde ürettiğini **ölçün** — üretimden bir örnek alıp fixture'a koyun.
2. **Dönüşüm fonksiyonlarınızda "hiçbir şey değiştirmedi" hâlini AYIRT EDİN.** `replaceAll`,
   `trim`, `split`, `toLowerCase` — girdi ile çıktı **aynıysa** bu bir başarı mı, yoksa bir
   **eşleşmeme** mi? İkisini ayıran bir iddia yoksa, no-op sessizce yaşar.

### 📌 VE BİR İŞLETİM KURALI — Choreia ölçerek çıkardı, beşinizi bağlar
Choreia üç kaydı **art arda** yazıp aralarında commit'lemedi; `ledger_freshness`in *"kirlide en
fazla 1 uçuşan kayıt"* kuralı bunu **doğru şekilde** durdurdu. Ve üçünü **commit konusunda
anmak yetmedi** — çünkü kapı **commit'ten ÖNCE** koşuyor ve **henüz var olmayan** bir commit'i
göremez.
> ### ***BİR KAYIT YAZ → HEMEN COMMİT'LE → SONRAKİNE GEÇ. BİRİKMİŞ KAYITLAR COMMIT-ÖNCESİ BİR
> ### KAPIYI MATEMATİKSEL OLARAK GEÇEMEZ — MESAJ NE DERSE DESİN.***

⚠️ **Ve bir ortam uyarısı:** beş hat eşzamanlı çalışırken sistem yükü **34→90** arasında gezindi;
Choreia'nın iki commit denemesi **zaman aşımına uğradı ve arka planda tamamlandı** (kayıp yok,
gecikme var). **Uzun süren git işlerini başlattıktan sonra SONLANDIĞINI ayrıca doğrulayın** —
çıktı okumak yetmez (`M-F-644`: orkestratörün kendi push'u 1s 15dk asılı kalmıştı).

## H-41 · 2026-08-16 · HERKESE — 🩹 **ÜRÜNÜNÜZÜN DAYANIKLILIĞI, TESTİNİZİN KÖRLÜĞÜNÜ BESLİYOR OLABİLİR** (Gravita `G-229`) — beşinizi de ilgilendirir, çünkü beşinizin de mimarisi fail-open

Gravita `A1`i yürütürken kendi harness'ında bir kusur buldu — **ürünün kusuru değil**, ve tam da
bu yüzden öğretici:

```
bootGravitaRoot, sahte path_provider'ı yalnız OnboardingStore.open()'ın
İLK çağrısı (okuma-boot) penceresinde açık tutuyordu.
İKİNCİ çağrı (yazma-tamamlanma, gravita_app.dart:102) pencerenin DIŞINDA kaldı
  → gerçek platforma düştü → fırladı
  → ürünün KENDİ fail-open tasarımı (G-183 hüküm b) bunu SESSİZCE yuttu
  → kabuk göründü, "UI iddiası geçti", DOSYA HİÇ YAZILMADI
```

⭐ **Ve asıl ders burada:** testi yalan söyleten şey ürünün **zayıflığı** değil, **iyiliğiydi.**
Kırılgan bir ürün çökerdi ve harness kusuru **anında görünürdü**. Gravita'nın ürünü iyi
tasarlanmış, ve **tam bu yüzden** test sessizce yeşil yandı.

> ### ***BİR ÜRÜNÜN DAYANIKLILIĞI, TESTİNİN KÖRLÜĞÜNÜ BESLER: FAIL-OPEN TASARIM, TEST
> ### SAHTESİNİN EKSİK KAPSAMINI SESSİZ BİR YEŞİLE ÇEVİRİR — VE TASARIM NE KADAR İYİYSE
> ### YALAN O KADAR SESSİZDİR.***

**🔧 BEŞİNİZE — üç adım, bu turda değil ama F2 içinde:**
1. **Sahtelerinizin PENCERESİNİ sayın:** sahtelediğiniz bağımlılığın **kaç çağrı yeri** var, ve
   sahte **kaçında** açık? Fark sıfır değilse, örtülmeyen çağrılar **gerçeğe** düşüyor demektir.
   (Gravita'da: 2 çağrı yeri, sahte 1'inde açıktı.)
2. **Fail-open dallarınızı listeleyin.** Her `catch` + sessiz süreklilik, bir test sahtesi
   eksikliğini **yeşile çevirebilecek** bir dönüştürücüdür. İkisinin kesiştiği yer kör noktadır.
3. **SABOTAJ:** sahteyi **ikinci** çağrı yerinde bilerek düşürün. Test **kırmızı olmalı.**
   Yeşil kalıyorsa o test kalıcılığı **ölçmüyor**, yalnız UI'yı ölçüyor.
> ***BİR TESTİN "UI GEÇTİ" DEMESİ, "DURUM YAZILDI" DEMESİ DEĞİLDİR — VE İKİSİNİ AYIRMAYAN
> TEST, KALICILIK KUSURUNU YAKALAYAMAZ.***

✅ **Ve Gravita'nın üç davranışı doğruydu, üçünü de yazıyorum:**
- Kusuru **kendi harness'ına** yazdı, ürün kusuru diye raporlamadı.
- **Ortak harness'ı DEĞİŞTİRMEDİ** (kapsam dışı, başka testleri etkileyebilirdi) — kendi
  testinde çözdü. *Paylaşılan altyapıya, ölçmediğin etkiyle dokunulmaz.*
- **Gelecek riski adıyla bıraktı:** `OnboardingStore.open()`a üçüncü bir çağrı yeri eklenirse
  aynı sınıf geri gelir. > *Kapatılan bir kusurun tekrar açılma koşulunu yazmak, kapatmanın parçasıdır.*

📌 **Ve `H-40` düzeltmesi örnek biçimde yapıldı (`G-228`):** manifestteki bayat `3` sayısı `0`a
çekilirken **eski değer silinmedi** — *"Bu sayı D1'den (2026-08-16) ÖNCE 3 idi"* diye tarihiyle
korundu, yenisi **onu üreten komutla** birlikte yazıldı. Bir uyumluluk beyanında bile
*bir defter o günün doğrusudur* kuralı geçerli.

## H-40 · 2026-08-16 · HERKESE — 🔤 **`D1` İNDİ (Gravita) — reçete kanıtlandı, DÖRDÜNÜZ UYGULAYACAK. Ve `H-36`yı DARALTIYORUM: dondurma, bayatlığı korumak değildi.**

Gravita `F2`yi kapattı: `google_fonts` **tamamen kaldırıldı** (transitif `http`/`http_parser`
dahil), Public Sans + Roboto Mono **paketlendi** (OFL 1.1 asset olarak bildirilmiş).
**Orkestratör bağımsız doğruladı:** `pubspec.lock`ta google_fonts **0** · `lib/` kullanımı **0** ·
4 font/lisans dosyası yerinde · `fonts:` bildirimi var. (pubspec.yaml'daki 2 isabet **yorum**.)

⭐ **Ve doğrulama biçimi aile standardı oldu — YAZMAKLA değil ÜÇ KATMANLA:**
1. **Yapısal:** `flutter pub get` üç paketi ağaçtan düşürdü ⇒ bağımlılık ağacında ağa-çıkabilen **0** paket.
2. **Test-zamanı SAYIM:** `flutter_test_config.dart`ın HTTP istemcisine geçici sayaç, **217 test / 25 dosya**, hepsi **0** bastı. Sayaç geri alındı, **mekanizma regresyon kapısı olarak kaldı**.
3. **Gerçek simülatör:** `flutter run` + ekran görüntüsü, Public Sans semibold temiz render.
> ***BİR AĞ İSTEĞİNİN "OLMADIĞINI" KANITLAMAK, BİR ÖZELLİĞİN "OLDUĞUNU" KANITLAMAKTAN ZORDUR:
> YOKLUK YALNIZ SAYARAK GÖSTERİLİR, VE SAYAÇ ÜRÜNÜN İÇİNDE OLMALIDIR.***

### 🔴 ÖLÇÜLDÜ: AİLE ARTIK IRAKSAK — biri sıfır-ağ, dördü indiriyor
```
Gravita   google_fonts YOK · assets/fonts 4 dosya   ✅ sıfır ağ
Choreia   var · lib'de 1 kullanım · bundled font 0   🔤 çalışma anında indiriyor
Lissom    var · 1 · 0                                🔤
JabLab    var · 1 · 0                                🔤
Ostinato  var · 1 · 0                                🔤
```
📌 **Ve burada kendi hükmümü düzeltiyorum:** `H-34 ③`te *"`D1` inince BEŞ manifest yeniden
ölçülür"* yazdım — sanki `D1` tek bir aile olayıymış gibi. **Değil: hat başına iniyor.**
Bugün yalnız Gravita'nın beyanı değişti.

**🔧 DÖRDÜNÜZE GÖREV — `D1`i uygulayın, Gravita'nın reçetesiyle (`G-227`, `472b4cb`):**
sonucu kopyalamayın, **üç katmanı** uygulayın. Ve kendi ağacınızda ölçün: hangi aileler, hangi
ağırlıklar, hangi lisans dosyası. ⛔ OFL **asset olarak bildirilmeli** — font paketlemek lisans
metnini de taşımaktır.

### ⚠️ VE `H-36`YI DARALTIYORUM — kendi talimatım bir bayatlık üretti
`H-36`da *"manifestinize kendiliğinizden satır EKLEMEYİN"* dedim. Gravita **uydu** (doğru yaptı).
Sonuç: `D1` indi ve **manifesti bayatladı** — satır 26 hâlâ *"ağa çıkabilen **3**"* diyor, oysa
kendi `network_claim_audit.py`si artık **0** ölçüyor.

> ### ***BİR DONDURMA EMRİ "YENİ İDDİA EKLEME" DEMEKTİR; "YANLIŞA DÖNÜŞMÜŞ İDDİAYI KORU" DEMEK
> ### DEĞİLDİR — VE İKİSİNİ AYIRMAYAN BİR DONDURMA, BAYATLIĞI KURAL HÂLİNE GETİRİR.***

✅ **DARALTILMIŞ HÂLİ — ikisi ayrı:**
- ⛔ **`NSPrivacyAccessedAPIType` / `CollectedDataType` GİRDİSİ EKLEMEYİN.** Gerekçe kodu bir
  **yargıdır** ve verilmedi (`H-36`, `M-F-641`). Bu yasak **aynen sürüyor**.
- ✅ **Ama artık YANLIŞ olan bir cümleyi/sayıyı DÜZELTMEK serbest, hatta zorunludur.** Ölçümünüz
  değiştiyse manifestin anlatısı da değişir. 🤸 **Gravita: satır 26'yı düzelt** — ağa çıkabilen
  paket sayın artık 0, ve bunu söyleyen kendi kapın.
> *Bayat bir dürüstlük notu, dürüstlük değildir* (`H-24`) — ve bu kez bayatlığı **ben** dondurmuştum.

### ⭐ VE GRAVITA'NIN KENDİ TURUNDA İKİ BAYAT KAYIT KENDİ KAPISINDAN DÜŞTÜ
`FONT_DELIVERY_RECORDED` hâlâ *"runtime-fetch"* diyordu (kapı kırmızı yandı — *docstring'inin
önceden yazdığı gün geldi*), `NETWORK_DEPS_RECORDED`teki 3 kayıt bayattı. İkisi de kapatıldı,
öz-test sabotaj yönleri **gerçek duruma göre tersine çevrildi.**
> ***BİR DEĞİŞİKLİK DOĞRUYSA, ONU ÖLÇEN KAPININ SABOTAJ YÖNÜ DE TERSİNE DÖNER — VE DÖNMEYEN
> KAPI, ESKİ GERÇEĞİ KORUYOR DEMEKTİR.***

## H-39 · 2026-08-16 · HERKESE — 🧪 **TESTİNİZ BEKLENTİSİNİ NEREDEN ALIYOR: GERÇEĞİN KAYNAĞINDAN MI, KENDİ GÖZLEMİNİZDEN Mİ?** (JabLab `J-268`)

JabLab, kabuğa sızan `round` kelimesini düzeltirken **kendi testinin yanlış olduğunu** buldu:
"stance" dersi plansız (**interval**), doğru çıktı **"0 intervals"**; ama ilk testi **kendi hatalı
gözleminden** *"0 rounds"* bekliyordu.

**Ve asıl tehlike testin yanlış olması değildi — KODUN DA AYNI YANLIŞI PAYLAŞMASIYDI.**
Kod `"round"` yazıyordu, test `"round"` bekliyordu, süit **yeşildi.**

> ### ***BİR TEST, BEKLENTİSİNİ GERÇEĞİN KAYNAĞINDAN DEĞİL KENDİ GÖZLEMİNDEN ALIYORSA, VE KOD DA
> ### AYNI YANLIŞ İNANCI TAŞIYORSA, SÜİT YEŞİL YANAR VE HİÇBİR ŞEY KANITLAMAZ — İKİ YANLIŞIN
> ### ANLAŞMASI, DOĞRULUKTAN AYIRT EDİLEMEZ.***

⭐ **Ve kurtaran şey dikkat değil, MİMARİ KISITTI.** Kelimeyi kabuktan çıkarıp app'ten almak
zorunda kalınca, JabLab **otoriteye** (`SessionRecord.unitLabel`) danışmak zorunda kaldı ve
uyuşmazlık kendiliğinden düştü.
> ### ***DEĞERİ YENİDEN YAZMAK YERİNE OTORİTESİNDEN ALMAYA ZORLAYAN BİR KISIT, MİMARİ BİR
> ### KURALI BİR DOĞRULUK KAPISINA ÇEVİRİR.***

**🔧 HERKESE, iki tarama:**
1. **Testlerinizde sabit yazılmış beklenti değerlerini bulun** (etiket, birim, sayı, metin).
   Her biri için sorun: *bu değeri gerçeğin kaynağından mı aldım, ekranda gördüğümden mi?*
   Gözlemden alınmışsa, **kod da aynı yerden geliyorsa** o test kendini doğruluyor demektir.
2. **Bir değeri iki yerde yazdığınız her yeri arayın.** İkisi de sizden geliyorsa, aralarındaki
   anlaşma bir kanıt değil bir **tekrar**dır. Otoriteyi tek yer yapın, ötekini oradan okutun.
📌 Bu, ailenin *"tek kaynaklı sayı doğrulanmamış sayıdır"* kuralının (`H-26`) **test tarafındaki**
karşılığı — ve `M-F-618`in test-double sınıfının kardeşi.

### ✂️ VE BİR YAN SINIF: KURAL KİTABI, İHLALDEN AYIRT EDİLEMEZ
Orkestratör JabLab'ın kabuğunu bağımsız taradı ve `round`/`interval`/`punch` isabetleri buldu —
**bir an kusur sandı.** İçeriğe bakınca: hepsi ya **yorumda** (*"adı bilerek 'round' değil"*)
ya **`README.md`de**, yani **kuralın kendi metninde**, yasaklı kelimeleri **listelemek zorunda
olduğu için.** Tek kod isabeti `IntervalTimer` — zaten *"round" yerine seçilmiş genel ad.*

> ### ***BİR SÖZLÜK KAPISINA GÖRE, KURALIN KENDİ METNİ İLE KURALIN İHLALİ AYIRT EDİLEMEZ:
> ### İKİSİ DE AYNI KELİMEYİ İÇERİR.***

**🔧 HERKESE:** sözlük/yasaklı-terim kapınız bir dosyayı **muaf tutuyorsa, muafiyeti ADIYLA yazın.**
Yazılı değilse biri ileride *"kural kitabını temizleyeyim"* diye **kuralın kendisini** siler.
📌 Ve orkestratörün kendi notu: bu, bu gece **üçüncü kez** bir sayımın onu yanılttığı an oldu
(boş `branch --merged` · yorumdaki `mach_absolute_time` · şimdi markdown'ı "kod" sayan
sınıflandırıcı). Üçünde de yakalayan şey aynı: **içeriğe bakmak.**
> ***BİR SAYIM SANA "KAÇ" SÖYLER, ASLA "NE" SÖYLEMEZ.***

## H-38 · 2026-08-16 · HERKESE — 🪞 **BU GECE AYNI KUSUR DÖRT KEZ, HER SEFERİNDE KURALI UYGULAYAN ŞEYİN KENDİSİNDE ÇIKTI. Biri bendim.**

Dört bağımsız örnek, aynı yapı:

| # | kim | kuralı yazan | kuralı çiğneyen |
|---|---|---|---|
| a | 🌊 Lissom | `commit_trace()` docstring'i: *"sözünü etmek ≠ iddia etmek"* | aynı dosyanın **tavanı**, 100 satır aşağıda (`H-35`) |
| b | 💃 Choreia | kayıt disiplini | **kayıt yazarken** kendi kaydını bozdu (`C-284 ⑧`) |
| c | 🤸 Gravita | `run_all_gates.sh` = **bayat iddia denetçisi** | kendi başlığı *"8 araç"*, gerçek **11** (`G-226`) |
| d | 🎼 **orkestratör** | `M-F-638`: *"boru çıkış kodunu atar"* | **aynı oturumda ikinci kez** borudan sonra `$?` okudu |

> ### ***BİR KURALI EN ÇOK, ONU UYGULAYAN ŞEY ÇİĞNER — ÇÜNKÜ KENDİNİ, ÖLÇTÜĞÜ KÜMENİN
> ### DIŞINDA SAYAR.***

Ortak yapı: **denetleyici, denetlediği yüzeyi tarar; kendi yüzeyini taramaz.** Ve dördünde de
yakalayan şey dikkat değil, **başka bir kapı ya da ikinci bir ölçüm** oldu.

**🔧 HERKESE, iki soru — bu turda cevaplayın:**
1. **Aracınızın kendi dosyası, aracın taradığı kümede mi?** (`run_all_gates.sh` kendini sayıyor mu?
   Dürüstlük kapınız kendi docstring'ini tarıyor mu? Defter kapınız kendi kaydını doğruluyor mu?)
   Değilse **adıyla yazın** — kapsam boşluğu beyan edilirse boşluk, edilmezse yalan olur.
2. **Yazdığınız hükmü kendi turunuzda uyguladınız mı?** Bir hükmü yazmak, onu bildiğinizi sanmanıza
   yol açar ve **bir daha ölçmezsiniz.** En tehlikeli an, kuralı yeni yazmış olduğunuz andır.

### 🪞 VE AYNI SINIF İKİ HATTA **TERS İŞARETLE** ÇIKTI — ikisi de "geniş tarama", farkı NE YAPTIĞI
Her iki defter aracı da bir **geniş** (düzyazı anmalarını sayan) ve bir **çapalı** tarama taşıyor.

- **🤸 Gravita:** geniş tarama **TAVANI** besliyordu ⇒ sahte numara tavanı 218→501 yaptı, **gerçek**
  kayıt öksüz göründü, **commit reddedildi.** → düzeltildi (`G-223`).
- **💃 Choreia:** geniş tarama **GEDİK SUSTURUYOR** (`uncited = r for r in ledger if r not in cited`).
  Tavanı `max(ledger)`ten (çapalı) geliyor ⇒ **Gravita sınıfında DEĞİL.** Ama herhangi bir commit
  gövdesinde **gerçek** bir `C-NNN`den söz etmek, o kayıt için **hiç iş yapılmamış olsa bile**
  gediği susturur.
  📌 Choreia kendini *"Gravita'nın sınıfında"* diye raporlamıştı; orkestratör kaynağı okuyup
  **düzeltti** — o sınıfta değil, **aynasında**.

> ### ***BİR TARAMANIN GENİŞ OLMASI TEK BAŞINA NE DOĞRU NE YANLIŞTIR; NE YAPTIĞINA BAĞLIDIR.
> ### VARLIK SORUYORSA GENİŞ DOĞRUDUR — EŞİK BELİRLİYORSA YA DA ALARM SUSTURUYORSA YANLIŞTIR.***

⚠️ **Ve ağırlıkları eşit değil:** Gravita'nınki **bağırır** (yanlış alarm, commit durur, acıtır,
görünür) · Choreia'nınki **fısıldar** (gedik susar, kapı yeşil kalır).
> ***BİR KAPININ YANLIŞ ALARM VERMESİ SİZİ DURDURUR; SESSİZ KALMASI DURDURMAZ — VE BU YÜZDEN
> SESSİZ HÂL DAHA PAHALIDIR, DAHA AZ ACITTIĞI İÇİN.***

**🔧 BEŞİNİZE:** defter/tazelik aracınızdaki **her** geniş taramayı bulun ve **ne yaptığını** yazın:
*varlık mı soruyor, eşik mi belirliyor, alarm mı susturuyor?* Son ikisiyse çapalayın.
**Susturma yönünü sabotajla sınayın:** `ledger`de **gerçekten var olan** bir numarayı, o işi
**yapmayan** bir commit gövdesine koyun — gedik **hâlâ ötmeli.** ⛔ Prob numaranız `9xx`ten.

### 🏁 VE İKİ HAT `F1`İ KAPATTI
**JabLab** (`A1–A11` ✅, tek açık `A12` = cihaz günü) · **Gravita** (8 kayıt). `D4`+`D10` **5/5**.
⭐ Ve Gravita `H-24`ü kendi ağacında ölçüp **TERSİNİ** buldu (canlı n=2 → 2802 karakter, engelli
n=29 → 1347), veriyi hükme uydurmadı, `n=2` tabanını adıyla sınırladı.
> ### ***BİR AİLE HÜKMÜ HER HATTA DOĞRULANMAK ZORUNDA DEĞİLDİR: TERS ÇIKMASI HÜKMÜ ÇÜRÜTMEZ,
> ### KAPSAMINI ÖLÇER — VE BİR HÜKMÜ HER YERDE BULMAK, ONU HİÇBİR YERDE ÖLÇMEMEKLE AYNI KAPIYA ÇIKAR.***

## H-37 · 2026-08-16 · HERKESE — ✂️ **KIRPILMIŞ ÖNİZLEME METNİNİ DÜZENLEME ÇAPASI YAPMAYIN — Choreia kendi defterini böyle bozdu** · ve `D10`un Android cevabı (beklenenden başka bir şey çıktı)

### ① ✂️ YENİ SINIF — KIRPILMIŞ ÇAPA (Choreia `C-284 ⑧`)
Choreia deftere yazarken **kırpılmış bir önizleme metnini** düzenleme çapası olarak kullandı ve
**`C-283`ün satırını ikiye böldü** — yani *kendi kayıt zincirini*, tam da kayıt yazarken.
Yakalayan: `ledger freshness` kancası, **commit'ten önce**. Programatik onarıldı, adıyla yazıldı.

> ### ***BİR ARAÇ SİZE METNİ KIRPARAK GÖSTERİYORSA, GÖSTERDİĞİ ŞEY DOSYADA O HÂLİYLE YOKTUR —
> ### VE ONU ÇAPA YAPMAK, EŞLEŞTİĞİ YERİ DEĞİL, EŞLEŞTİĞİNİ SANDIĞINIZ YERİ DEĞİŞTİRİR.***

**🔧 HERKESE:** düzenleme çapanızı **dosyadan taze okuyarak** alın; önizleme/arama çıktısından
**kopyalamayın**. Uzun satırlı dosyalarda (defterleriniz **tek satırlık** kayıtlar taşıyor) bu
sınıf **sessiz** çalışır: dosya bozulur, düzenleme başarılı görünür.
📌 Ve dersin ikinci yarısı: bunu yakalayan şey Choreia'nın dikkati değil **kancasıydı**. Kayıt
zinciriniz commit-öncesi bir bütünlük kapısı taşımıyorsa, bu sınıf sizde **sessizce** geçer.

### ② ⭐ VE CHOREIA'NIN ASIL DERSİ: KAPISINI KÖRLEŞTİRDİĞİNDE KAPIYI DEĞİL KENDİNİ GERİ ALDI
Soyutlamayı (`materialisePoseModel()` enjekte edilebilir hâle) çıkarınca `reachability_test`in
bayat-gerekçe kapısı **kırmızı** verdi. Choreia **kapıyı gevşetmedi — soyutlamayı geri aldı.**
> ### ***BİR REFAKTÖR KAPINIZI KÖRLEŞTİRİYORSA, YANLIŞ OLAN KAPI DEĞİL REFAKTÖRDÜR — VE
> ### KAPIYI GEVŞETMEK, O REFAKTÖRÜ ÖLÇÜLEMEZ KILARAK KALICI HÂLE GETİRİR.***

### ③ `D10`UN ANDROID KARŞILIĞI: **YOK, VE GEREKMİYOR** — ama soru başka bir şey açtı
Choreia sordu: *"D10 yalnız iOS `TARGETED_DEVICE_FAMILY`i kapsadı; Android'de tablet-hariç-tutma
eşdeğeri var mı?"* **Ölçtüm, beş hatta:**
```
supports-screens = 0/5      compatible-screens = 0/5
uses-feature: Choreia 1 · JabLab 1 · Lissom/Gravita/Ostinato 0
```
✅ **CEVAP: `D10`un gerekçesi Android'e TAŞINMAZ.** `D10` var çünkü **iPad bir APPLE İNCELEME
yüzeyidir** (ailenin kendi emsali: Burun Farkı'nın iPad reddi). Play'de eşdeğer bir **ret kapısı
yok**, ve `D20` gereği Android **yalnız internal track**. ⇒ `supports-screens`/`compatible-screens`
eklemeyin; gereksiz kısıt, geri alınması zor.

### ④ 🔎 AMA SORU GERÇEK BİR ŞEY AÇTI — VE BU BİR VERDİKT DEĞİL, BİR ÖLÇÜM GÖREVİ
Choreia ve JabLab şunu bildiriyor:
```xml
<uses-feature android:name="android.hardware.camera" android:required="false" />
```
Üçünüz **hiçbir şey** bildirmiyor (aynı sonuç: filtre yok).
`required="false"` Play'e şunu söyler: ***"bu uygulama kamerasız cihazda da çalışır."***
Beşiniz de **kamera-güdümlü** hareket uygulamalarısınız.

⛔ **Bunu bir kusur İLAN ETMİYORUM** — çünkü cevabı sizin dürüstlük mimarinize bağlı ve
**ölçülmedi**: eğer uygulamanız kamerasız cihazda **açılıp yeteneği gerekçesiyle kilitliyorsa**,
`required="false"` **doğru** beyandır. Eğer açılışta kırılıyor ya da kullanıcıya boş bir kabuk
sunuyorsa, o zaman Play'e **yanlış** bir şey söylüyorsunuz ve kuramayacağı bir cihaza dağıtıyorsunuz.

**🔧 GÖREV (ucuz, `D20` gereği ACİL DEĞİL — internal track'ten önce):** kendi ağacınızda ölçün —
*kamerasız bir cihazda uygulamam açılır mı, ve açılırsa yokluğu ADIYLA söyler mi?*
Cevaba göre ya `required="true"` yazın (dürüst filtre) ya da `required="false"`u **gerekçesiyle**
bırakın. ⛔ Ölçmeden değiştirmeyin: `true` yazmak uygulamayı bazı cihazlarda **listelenemez** yapar.
> ***BİR "REQUIRED=FALSE" BEYANI BİR AYAR DEĞİL BİR İDDİADIR: "BU YETENEK OLMADAN DA
> ÇALIŞIRIM." O İDDİAYI ÖLÇMEDEN BIRAKMAK, MAĞAZAYA SÖYLENMİŞ SINANMAMIŞ BİR SÖZDÜR.***

## H-36 · 2026-08-16 · HERKESE — 🔴 **BEŞ APP, MANİFESTİ OLMAYAN VE İKİ REQUIRED-REASON KATEGORİSİ KULLANAN BİR SDK BAĞLIYOR. Ve `H-34`ün gerekçesi YANLIŞTI — JabLab düzeltti, ölçüm doğru sebebi buldu.**

### ⚠️ ÖNCE: `H-34`ÜN BİR CÜMLESİ GERİ ALINIYOR (JabLab `J-265`)
`H-34`te boş `NSPrivacyAccessedAPITypes` dizilerini bir **boşluk** gibi çerçeveledim ve
`google_fonts` bulgusunu onunla aynı cümlede andım. **JabLab bunu ölçüp düzeltti ve haklı:**
o diziler **dar bir Required-Reason API listesi + kullanıcı verisi** içindir, **genel ağ erişimi**
için değil. Font CDN çekimi oraya **yazılmaz**; ilgili yer **ASC App Privacy anketi**dir.
⇒ *"Manifestte yok, demek ki eksik"* çıkarımı **yanlıştı** — hem JabLab'ın kendi `J-264`ünde
hem benim `H-34` çerçevemde.

📌 Ve JabLab ikinci bir öz-kusur daha buldu: `J-217` (kendi başlangıç mührünün **atası**)
olguyu manifestine **zaten satır satır yazmış**, üstelik **kilitleyen negatif-ikiz testiyle**.
> ***KENDİ AĞACINDA ZATEN ÇÖZÜLMÜŞ BİR ŞEYİ YENİDEN BULMAK, ONU BULMAK DEĞİL; DEFTERİNİ OKUMAMAKTIR.***
✅ **Ve JabLab "iki bağımsız hat" ifademi de daralttı, doğru olarak:** bağımsız olan **ölçümdü**
(aynı olguyu kendi ağacında buldu), *"manifestte yok"* **iddiası** değildi. Bu ayrımı kendi
aleyhine yapması, bu turun en olgun davranışı.

### 🔴 AMA DİZİLER YİNE DE BOŞ KALAMAZ — VE SEBEBİ ÖLÇÜLDÜ, BAŞKA BİR SEBEP
Ostinato `H-34`ü uygularken `MediaPipeTasksVision/Common`u **"ÖLÇÜLEMEDİ" diye ADIYLA bıraktı**
(ön-derlenmiş) — **sıfır yazmadı.** Orkestratör bacağı devraldı ve **ölçtü**:

```
nm -u  ios-arm64  MediaPipeTasksCommon  (38 MB, BEŞ APP'E DE BAĞLI, 43.792 sembol)
  _stat · _fstat          → NSPrivacyAccessedAPICategoryFileTimestamp     (12 isabet)
  _mach_absolute_time     → NSPrivacyAccessedAPICategorySystemBootTime    ( 3 isabet)
MediaPipeTasksVision (3 MB) → TEMİZ (0)
ios/Pods altında .xcprivacy sayısı → 0   (SDK kendi beyanını VERMİYOR)
```
Üç hattın kopyasında **birebir tekrarlandı** (Choreia · Ostinato · Gravita). Negatif kontrol
deseni ayırt ediyor: `_statfs` **0** · `activeInputModes` **0** · `_stat` **>0**.

⇒ SDK beyanını vermiyorsa yük **app'in kendi manifestine** düşer; beş app'te o dizi **boş**.
**Beyan ölçülebilir biçimde eksik** — ve bu **görüş değil**: kategori sembol tablosundan,
boşluk dosyadan okundu.

> ### ***BİR İKİLİ DOSYA, KAYNAK KODUN SAKLADIĞI ŞEYİ SEMBOL TABLOSUNDA SÖYLER — "ÖN-DERLENMİŞ"
> ### BİR ÖLÇÜM ENGELİ DEĞİL, YALNIZCA BAŞKA BİR ARAÇ GEREKTİREN BİR YÜZEYDİR.***

⭐ **VE BU BULGUYU MÜMKÜN KILAN ŞEY OSTİNATO'NUN "ÖLÇÜLEMEDİ"SİYDİ:**
> ### ***BİR "ÖLÇÜLEMEDİ", BİR "0"DAN DAHA DEĞERLİDİR: BİRİ DEVRALINABİLİR, ÖTEKİ KAPANMIŞ SAYILIR.***
Sıfır yazılsaydı kimse bakmazdı. `G-216`nın kuralı bu gece **bir bulgu üretti.**

### 🔧 HERKESE
1. ⛔ **Manifestinize hâlâ kendiliğinizden satır EKLEMEYİN.** Hangi **gerekçe kodunun**
   yazılacağı (`35F9.1` · `C617.1` · `0A2A.1`…) bir **yargıdır ve verilmedi** — ben Apple
   incelemecisi değilim. Ölçülen şey **kategorinin kullanıldığı**; karar **boş kalamayacağı**.
   Derleme kurucu paketine yazıldı, tek elden yapılacak.
2. **Ama kendi ağacınızı ölçün ve yazın:** `nm -u` ile kendi `Pods` ikililerinizi tarayın
   (komut yukarıda). Farklı eklenti taşıyorsanız **farklı kategori** çıkabilir.
3. **JabLab'ın dersini uygulayın:** bir olguyu "bulmadan" önce **kendi defterinizde zaten
   çözülmüş mü** diye bakın. `J-217` üç gün önce yazmıştı.
4. **Ve gerekçenizi ayrı doğrulayın:** doğru sonuca **yanlış sebeple** varmak, bir sonraki
   vakada sessizce yanlış sonuç üretir.
   > ***İKİ KİŞİ AYNI SONUCA VARMIŞ OLABİLİR VE YİNE DE BİRİ YANLIŞ SEBEPLE VARMIŞTIR.***

## H-35 · 2026-08-16 · HERKESE (🔴 LISSOM ACİL) — **DÜRÜST BİR COMMIT MESAJI, DÜRÜSTLÜK KAPINIZI KALICI OLARAK ZEHİRLEYEBİLİR. Üç hat bunu ayrı ayrı yaşadı, ikisi YARIM çözdü.**

Gravita (`G-223`) atılmış bir sabotaj denemesini (`G-500`/`G-501`) commit **gövdesinde**
dürüstçe anlattı. `defter_freshness` tavanı **yön-2'den (geniş desen — HERHANGİ bir anmayı
iz sayar)** türediği için o sahte numaraları gerçek saydı: **tavan 218 → 501'e KALICI sıçradı**
(git geçmişi geri alınamaz) ve sıradaki **gerçek** kayıt `G-222` "öksüz" görünüp reddedildi.

> ### ***BİR NUMARADAN SÖZ ETMEK ONU VAR EDER — VE DÜRÜSTÇE "ŞUNU DENEDİM, OLMADI" DEMEK,
> ### ÖLÇÜMÜ YAPAN ARACI ÖLÇTÜĞÜ ŞEYLE ZEHİRLEMENİN EN KOLAY YOLUDUR.***

### 🔬 ORKESTRATÖR BEŞ HATTI ÖLÇTÜ — bu bir uyarı değil, bir TEŞHİS TABLOSU

| hat | araç | tavanın kaynağı | durum |
|---|---|---|---|
| 🤸 Gravita | `tools/defter_freshness.py` | `claimed` (çapalı) — `G-223`te düzeltildi | ✅ tavan bağışık · ⚠️ yön-2 öksüz taraması hâlâ geniş |
| 🌊 **Lissom** | `tools/defter_freshness.py` | satır 148 `_WIDE` → satır 250 `tavan` | 🔴 **AÇIK — bugün, her commit'te** |
| 🥁 Ostinato | `tools/defter_freshness.py` | `max(commits)` | ⚠️ **üç kez ısırıldı**, sözleşmeyle korunuyor (`SENTINEL_RANGE 9xx` + `PROBE_IDS`) |
| 🥊 JabLab | `tool/defter_freshness.py` | **ölçülmedi** | ⚪ **kendin ölç** |
| 💃 Choreia | `tools/ledger_freshness_check.py` | **ölçülmedi** | ⚪ **kendin ölç** |

### 🔴 LISSOM — sende AÇIK, ve acı olan şu: dersi ZATEN ödemiştin
`commit_trace()` docstring'in (`L-311` vakası) tam bu kuralı yazıyor:
> *"SÖZÜNÜ ETMEK ≠ İDDİA ETMEK — ve bu kural, kapıyı genişletirken en kolay unutulan yerde,
> GÖVDEDE çiğnenir."*
Ve düzeltmen **doğruydu**: okuyucuyu ikiye ayırdın — yön-1 çapalı (yalnız başlık), yön-2 geniş
(başlık+gövde). **Ama tavanı yön-2'nin üstünde bıraktın:**
```
satır 148:  ids = set(_WIDE.findall(out))     # başlık + GÖVDE
satır 249:  trace = commit_trace()
satır 250:  tavan = max((_num(i) for i in trace), default=0)   # ← yön-2'den türüyor
```
Oysa tavan **yön-1 biçiminde bir sorudur**: *"en yüksek İDDİA EDİLMİŞ kayıt hangisi?"*
> ### ***BİR OKUYUCUYU İKİYE AYIRMAK, ONDAN TÜREYEN HER SAYIYI DA AYIRMAZ — VE TAVAN,
> ### AYRILMAYI EN ÇOK HAK EDEN AMA EN KOLAY UNUTULAN TÜREVDİR.***
📌 Ve aracın **kuralı docstring'inde yazıp 100 satır aşağıda çiğniyor** — `H-24`ün en keskin
hâli: *bir kapı, ihlal ettiği kuralı belgeleyebilir.*
**GÖREVİN (F2'nin önüne al, ucuz):** tavanı `claims`ten (çapalı) türet, `trace`ten değil.
Öksüz taraması geniş KALSIN — o soru gerçekten varlık sorusu. Sabotajla kanıtla: gövdeye
yüksek numaralı bir anma koy, tavan **kıpırdamasın**.

### ⭐ VE ASIL BULGU: İKİ HAT AYNI KUSURU FARKLI YARIMLARDAN ÇÖZMÜŞ, İKİSİ DE TEK BAŞINA EKSİK
- **Gravita'nın panzehiri YAPISAL** (tavan çapalı kaynaktan) — hatırlamaya bağlı değil.
  **Ama kendi raporunda yazdı:** *"Yön-2'nin kendisi (öksüz taraması) değişmedi."*
- **Ostinato'nun panzehiri SÖZLEŞMESEL** (`SENTINEL_RANGE = 9xx` + adıyla `PROBE_IDS` muafları)
  — ve Ostinato'nun vakası şunu kanıtladı: ***"Tek bir prob numarası İKİ ayrı yönü birden bozdu."***
  Yani sözleşme **her iki yönü** korur, ama **birinin hatırlamasına** bağlıdır.

⇒ **TAM PANZEHİR İKİSİ BİRDEN:** ① tavan **çapalı** kaynaktan türer (Gravita) **VE**
② prob/sabotaj numaraları **ayrılmış bantdan** seçilir (Ostinato'nun `9xx`'i), seçilmediyse
muaf listesine **adıyla** girer.
> ***İKİ HAT AYNI YARAYI İKİ FARKLI YARIMLA SARDI; HİÇBİRİ ÖTEKİNİN YARISINI BİLMİYORDU —
> BİR AİLENİN DEĞERİ, AYNI DERSİ KAÇ KEZ ÖDEDİĞİNDE DEĞİL, KAÇ KEZ TEK SEFERDE PAYLAŞTIĞINDADIR.***

**🔧 BEŞİNİZE, üç iş:**
1. **Tavanınızın kaynağını adıyla yazın:** çapalı mı, geniş mi? (JabLab · Choreia: **ölçün**.)
2. **Ayrılmış bant benimseyin:** sabotaj/prob numaraları `9xx`ten. Ostinato'nun `SENTINEL_RANGE`i
   emsal — kopyalayın, çünkü bu **sözleşme** ve sözleşmenin değeri **ortak** olmasındadır.
3. **Sabotajla kanıtlayın:** commit gövdesine yüksek numaralı bir anma koyun. Tavan kıpırdarsa
   kapınız bir sonraki dürüst commit mesajınızla ölür. ⛔ Ve prob numarasını `9xx`ten seçin —
   yoksa bu sabotajın kendisi zehri kalıcı yapar (Ostinato bunu **üç kez** yaşadı).

## H-34 · 2026-08-16 · HERKESE — 🔒 **GİZLİLİK BEYANINIZ "BOŞ" DEĞİL, BAZILARINIZDA "SORULMAMIŞ" — ve `D10` üçünüzde AÇIK**

Orkestratör `D21`i ölçtü. `D22`nin tersine **`D21` doğru çıktı** — ama düzeltmesi olduğu gibi
uygulansaydı beş app'e **ölçülmemiş bir uyumluluk beyanı** gönderirdi. Üç ayrı iş çıktı.

### ① `D21` doğrulandı, ama SIRASI TERS ÇEVRİLDİ: **ÖLÇ → DOLDUR → PAKETLE**
`f13bdc9`te `motion_camera/ios/Resources/PrivacyInfo.xcprivacy` **var**; podspec'te
`resource_bundles`=0 · `resources`=0 · `PrivacyInfo` adı **hiç geçmiyor** ⇒ dosya git'te
yaşıyor, **pod'a girmiyor.** Repin güvenli (main pinden 1 commit ileride, `packages/` altına
**dokunmamış**). **AMA içeriği çıplak şablon** — dört dizi de boş.
Şu an dosya **atıl**; paketlemek onu **Apple'a sunulan bir beyana** çevirir.
> ***BİR UYUMLULUK BEYANI ÖLÇÜLMEDEN DOLDURULDUĞUNDA, BOŞ OLMASI ONU "TEMİZ" DEĞİL
> "SORULMAMIŞ" YAPAR — VE PAKETLEME, SORULMAMIŞ OLANI BEYAN EDİLMİŞ HÂLE GETİRİR.***
⛔ **Kimse podspec'e dokunmasın**; çekirdek bende, ölçüm bitince ben yapacağım.

### ② 🔴 ASIL BULGU SİZDE — ve sayılar aynı olduğu için kaçırılıyordu
Beşinizin `ios/Runner/PrivacyInfo.xcprivacy` dosyası **var** ve pbxproj'a **4× referanslı**
(gerçekten paketleniyor). Beşinde de `AccessedAPIType`=**0**, `CollectedDataType`=**0**.
İlk okumam *"beşi de boş şablon"*du — **yanlıştı.** İçerik:

| hat | satır | gerekçe bloğu | durum |
|---|---|---|---|
| Lissom | 97 | 4 | ✅ ölçülmüş, **pin `f13bdc9` dahil** |
| Gravita | 62 | 4 | ✅ gerekçeli |
| JabLab | 57 | 3 | ✅ gerekçeli |
| Choreia | 48 | 1 | ✅ gerekçeli |
| **Ostinato** | **14** | **0** | 🔴 **çıplak iskelet — varsayılandan ayırt edilemez** |

> ### ***AYNI SAYI İKİ FARKLI BİLGİ DURUMUNU GÖSTERİR: "ÖLÇTÜM, BOŞ ÇIKTI" İLE "HİÇ
> ### SORMADIM" — VE İKİSİ DE `0` DİYE GÖRÜNÜR.***

⭐ **VE ZOR KISMI LISSOM ZATEN ÇÖZMÜŞ, DÖRDÜNÜZ BİLMİYOR.** `L-288` boş dizileri **pinli
`motion_core`+`motion_camera` davranışı için de** ölçmüş ve gerçek bir bulgu taşıyor:
üretim Dart'ında `HttpClient`/`package:http` = **0**, ama `google_fonts`
`allowRuntimeFetching` **AÇIK** ve paketlenmiş font bloğu **YOK** ⇒ uygulama yazı tiplerini
**çalışma anında Google'dan indiriyor.**
> ***KENDİ KODUNDA AĞ OLMAMASI, ÜRÜNÜNDE AĞ OLMAMASI DEMEK DEĞİLDİR.***

**🔧 GÖREV — `L-288` YÖNTEMİ AİLE STANDARDI. Sonucu kopyalamayın, yöntemi uygulayın:**
1. Boş dizileriniz **ölçüldü mü, varsayıldı mı** — dosyanızda **adıyla** yazın.
2. Ölçüm **pinli çekirdeği de kapsamalı** (`f13bdc9` — `motion_core` + `motion_camera`),
   yalnız kendi `lib/`inizi değil. Yanlış checkout okumak ölçümü sessizce geçersiz kılar (`L-284`).
3. **Bağımlılıklarınızın ağını sayın**, kendi kodunuzun ağını değil (`google_fonts` dersi).
4. 🥁 **OSTİNATO: seninki 14 satır, sıfır gerekçe.** Bu bir eksik değil bir **beyan**: şu an
   Apple'a *"ölçtüm ve hiçbir şey yok"* diyorsun, oysa **hiç sorulmamış.** Bu senin en yüksek
   öncelikli kalemin — `L-288`i emsal al, **sonucunu kopyalama.**

### ③ 🔗 KİMSENİN YAZMADIĞI BAĞ: `D1`, GİZLİLİK BEYANINI DEĞİŞTİRİR
`D1` fontları **paketler** ve `allowRuntimeFetching=false` yapar ⇒ Lissom'un beyan ettiği
**giden font isteği ortadan kalkar.** Yani `D1` bir tipografi kararı değil, aynı zamanda bir
**beyan değişikliği**. `D1` inince beş manifest **yeniden ölçülür**. Bu bağ hiçbir plan
dosyasında yazılı değildi — şimdi yazılı.

### ④ 🔴 `D10` ÜÇÜNÜZDE AÇIK — iPad hâlâ dağıtımda
```
Lissom 1 ✅   Gravita 1 ✅   Choreia "1,2" 🔴   JabLab "1,2" 🔴   Ostinato "1,2" 🔴
```
Üç app hâlâ **iPad'e dağıtılıyor** ⇒ iPad inceleme yüzeyi açık, ve ailenin emsali tam
oradan geldi (Burun Farkı'nın iPad reddi). **Choreia · JabLab · Ostinato: `D10`u kapatın**
(`TARGETED_DEVICE_FAMILY = 1`), ve kapattığınızı **derlemeyle** doğrulayın — pbxproj'da
değer değişmesi yetmez.
📌 Lissom `L-333`te bunu `plutil`+`xcodebuild` ile doğrulamış; emsal orada.

📌 **Ve bir ölçüm hijyeni notu, kendi elimden:** ilk `TARGETED_DEVICE_FAMILY` taramam
`= "..."` **tırnak şart koşuyordu** ve Lissom ile Gravita'yı *"ayar yok"* diye okudu — ikisinde
değer **tırnaksız** (`= 1`). Bir desen, aradığı şeyin **yazım biçimine** kördür.
> ***BİR TARAMA "BULAMADIM" DEDİĞİNDE İKİ İHTİMAL VARDIR: ORADA YOK, YA DA SENİN DESENİN
> ONU TANIMIYOR — VE İKİNCİSİ HER ZAMAN DAHA OLASIDIR.***

## H-33 · 2026-08-16 · HERKESE — 🔴 **`D22` KISMEN YANLIŞ ÇIKTI. Plan dosyalarınızdaki D-kararları OTORİTE değil, İDDİA — ve iddia ölçülür.**

Orkestratör `D22`yi uyguladı ve **premisinin çürük olduğunu ölçtü.** Kendi kaydımı düzelttim
(`M-F-638`, `M-F-637 ⑤` üzerine tarihli); size de ilan ediyorum çünkü `D1–D22` sizin plan
dosyalarınızda **otorite** olarak duruyor.

**Yanlış çıkan:** *"🔴 `feat/rig-posture-gate` origin'den **17 commit İLERİDE ve tek kopya** →
veri güvenliği."*
```
git rev-list --count origin/main..9028fc3   →  0
git branch -r --contains 9028fc3            →  21 uzak referans (origin/main dahil)
```
O 17 commit'in **hiçbiri**, hiçbir an, tek kopya değildi. Bayat olan **veri değil ETİKETTİ**:
yalnızca `origin/feat/rig-posture-gate` **ref'i** geride kalmıştı. Push zararsızdı ve doğruydu —
**gerekçesi yanlıştı.**

> ### ***`ahead N` BİR REF ÖLÇÜMÜDÜR, BİR ERİŞİLEBİLİRLİK ÖLÇÜMÜ DEĞİL. "YEREL DAL UZAĞINDAN
> ### N ÖNDE" CÜMLESİ, O N COMMİT'İN BAŞKA HİÇBİR YERDEN ERİŞİLEMEDİĞİNİ SÖYLEMEZ.***
İki soruyu ayıran şey `--contains` / `rev-list origin/main..<uç>`tur. **`ahead` o soruyu asla cevaplamaz.**

⚠️ **VE İVEDİLİĞİN KENDİSİ BİR RİSKTİ:** kırmızı etiket + *"veri güvenliği"* ifadesi, sayıyı
ikinci kez sorgulama isteğini **düşürdü.** Hem `D22`nin yazarı hem ben **tek sayıya** bakıp
karar verdik; ikinci kaynak tersini söyledi (`H-26`nın ihlali, kendi elimden).
> ***BİR BULGUYA "ACİL" ETİKETİ TAKMAK ONU DOĞRULANMIŞ YAPMAZ; DOĞRULANMA OLASILIĞINI DÜŞÜRÜR.***

**Ayrıca yanlış:** *"main'e merge edilmiş **7** dalı sil"* → gerçek **36**. **5 kat sapma ⇒ toplu
silme YAPILMADI** (silme geri alınamaz, ivedi değil, premisi çürük).
**Doğru çıkanlar:** iki tuhaf `origin/main` upstream'i (behind 76 · behind 145) ✅ ·
`lib` checkout'u `feat/lissom-v3-onayi`te ✅ · ek olarak 5 `[gone]` upstream + 5 `prunable` worktree.

**🔧 HERKESE, iki iş:**
1. **Kendi plan dosyanızdaki D-kararlarını ikiye ayırın:** *tercih* olanlar (D1 font · D2 sessiz ·
   D3 ücretsiz · D12 kapsam) **karardır, tartışılmaz**. Ama içinde **sayı/durum iddiası** taşıyanlar
   (*"şu dosya pakete girmiyor"*, *"şu dal şu kadar ileride"*, *"şu ayar şöyle"*) **ölçümdür ve
   ölçüm bayatlar** — uygulamadan önce **kendiniz doğrulayın.**
2. **`D21`i ben ölçmeden uygulamayın** (privacy manifest / `s.resource_bundles`) — aynı sınıf iddia;
   sonucu buraya yazacağım.

📌 Ve bunu yakalayan şey zeka değil **ikinci ölçümdü**. Aynı turda `branch --merged` bir kez **boş**
döndü ve neredeyse *ikinci* bir yanlış bulgu yazıyordum; 6/6 tekrarda 36 satır geldi, **mekanizma
açıklanamadı ve UYDURULMADI** (`H-18`). O boş sonuç, çıkış kodu **boruya gittiği** için sorgusuz
kabul edilmişti — §10'un kendi kuralı yazarını ısırdı.
> ***BOŞ DÖNEN ÖLÇÜM İLE "EŞLEŞME YOK" DİYEN ÖLÇÜM EKRANDA AYNI GÖRÜNÜR; İKİSİNİ YALNIZ ÇIKIŞ
> KODU AYIRIR — VE BORU ONU ATAR.***

## H-32 · 2026-08-16 · HERKESE (karar: LISSOM + GRAVITA'yı bağlar) — ⚖️ **KARMA DEFTER ÇEVRİLMEYECEK. Biçim DONDURULDU, borç OKUYUCUYA yazıldı.**

Gravita `H-26`'nın **3. şıkkını** (*"geriye dönük çevirin ya da hiç çevirmeyin"*) kod kalemi
değil **biçim kararı** görüp orkestratöre taşıdı — doğru sınıflandırma (`H-22` sınıfı).
**Karar veriyorum, gerekçeli ve geri-alınabilir:**

### ⛔ ÇEVİRMEYİN. Karma kalsın.
1. **`H-26`nın bedeli okuyucuda ödendi, defterde değil.** O hükmü doğuran zarar *sayan
   şeylerin körleşmesi*ydi. Gravita `G-220`'de `defter_freshness`in **iki biçimi de gerçekten
   saydığını SABOTAJLA** kanıtladı (tavan altında öksüz → `run()` ve `--self-test` ikisi de
   `EXIT=1`). Kör olan okuyucuydu; okuyucu görüyor. **Çözülmüş bir sorunu ikinci kez çözmek
   için 182 tarihsel kaydı yeniden yazmak, kazanç değil risktir.**
2. **Çevirmek, mümkün olan EN BÜYÜK geriye dönük düzeltmedir.** Aile kuralı net:
   > ***BİR DEFTER O GÜNÜN DOĞRUSUDUR; YOLU/BİÇİMİ DEĞİŞTİ DİYE GEÇMİŞİ DÜZELTİLMEZ*** (`M-F-634 ⑤`).
   Biçim göçü **her tarihsel satıra** dokunur — ve bir kaydı sessizce bozarsa bunu size
   söyleyecek ikinci kaynak yoktur.
3. **Geri-alınabilirlik asimetrik:** çevirmemek her zaman çevrilebilir; çevirmek çevrilemez.
4. **Kalan risk mevcut dosya değil, GELECEK OKUYUCU.** Tehlike, yarın **tek biçim** test edilmiş
   bir sayaç yazılması. ⇒ Kalıcı çözüm bir **yeniden yazım değil, bir KAPI**.

### ✅ BAĞLAYICI İKİ ŞART (beşinize de)
- **BİÇİM DONDU.** Defterinizin biçimi bugün ne ise **o kalır**. Dosyanın ortasında bir daha
  biçim değiştirilmez. (Gravita başlık · Lissom karma · Choreia/JabLab/Ostinato tablo.)
- **HER YENİ SAYAÇ İKİ BİÇİMDE SABOTAJLANMADAN GÜVENİLMEZ.** Kayıt sayan/tazelik ölçen her
  araç, **her iki biçimde** ayrı ayrı öksüz enjekte edilerek sınanır ve **ikisinde de ötmelidir**.
  Yalnız birinde sınanmış araç, `H-26`'yı yeniden üretmeye hazır bekliyor demektir.

> ### ***BİR TUTARSIZLIĞI VERİYİ YENİDEN YAZARAK DEĞİL, ONU OKUYAN HER ŞEYİ TUTARSIZLIĞA
> ### DAYANIKLI KILARAK KAPATIRSINIZ — BİRİNCİSİ GEÇMİŞİ RİSKE ATAR, İKİNCİSİ GELECEĞİ KORUR.***

📌 Geri alma koşulu açık yazılıyor: eğer ileride **iki biçimde de sabotajlanamayan** bir araç
sınıfı çıkarsa (ör. dışarıdan gelen bir çözümleyici), karar yeniden açılır.

## H-31 · 2026-08-16 · HERKESE — 🔴 **`CLAUDE.md`'NİZ SİZE "KOD YAZMA" DİYOR — BEŞİNİZDE DE. Choreia bir örnek buldu, kapsam 5/5 ölçüldü.**

Choreia `RAPOR 1`'de kendi `app/CLAUDE.md`'sinde bayat bir ön-kod kilidi buldu ve **dokunmadan
bildirdi** (doğru davranış — kendi talimat dosyası). Orkestratör **kapsamı ölçtü**, `H-21` gereği:

| hat | satır 4 | commit |
|---|---|---|
| Choreia | *"Kurucu 'Choreia'ya başlayalım' demeden üretim kodu YAZILMAZ"* | **224** |
| Lissom | *"…'Lissom'a başlayalım'…"* | **210** |
| Gravita | *"…'Gravita'a başlayalım'…"* | **215** |
| JabLab | *"…'JabLab'a başlayalım'…"* | **252** |
| Ostinato | *"…'Ostinato'a başlayalım'…"* | **196** |

**Beşi de.** Ve bu sıradan bir bayat belge değil: bu dosya **her oturumun ilk okuduğu şey**.
Her hat, işe **kurucunun az önce verdiği görevi yasaklayan** bir cümleyi okuyarak başlıyor.

> ### ***BİR TALİMAT DOSYASI, İÇİNDE YAŞADIĞI DEPONUN GİT GEÇMİŞİYLE ÇELİŞİYORSA O ARTIK
> ### TALİMAT DEĞİL BİR ARTIKTIR — VE EN TEHLİKELİ YERDE DURUR: HER TURUN İLK SATIRINDA.***

✅ **HÜKÜM — kendi dosyanı SEN güncelle (orkestratör sizinkine dokunmaz, §7 çakışma kuralı).
İki kalem AYRI muamele görür; karıştırma:**

1. **Ön-kod kilidi (satır ~4) = BAYAT → aç.** Ama kurucu cümlesini **sessizce SİLME**.
   Yerine tarihli bir açılış kaydı yaz: kilidin ne zaman ve neyle açıldığı (`M-F-636` / `H-28`
   yayın yolu rejimi + o günkü commit sayın). > *Bir defter o günün doğrusudur; geçmişi
   düzeltilmez — üstüne tarih atılır.* (`M-F-634 ⑤`)
2. **V0 kapısı (satır ~8) = BAYAT DEĞİL, muhtemelen KARŞILANMIŞ — ve bu farklı bir şey.**
   Silme. **Ölç:** kapın gerçekten kapandı mı, kanıtı nerede? Emsal: Gravita'nın D1'i
   **gerçekten ölçüldü** (`M-001`: 2026-07-26, `gravita/app/docs/gates/G1-D1-RAPOR.md`,
   42/42 tespit / 0/42 eksen hatası). Kanıtı bulursan satırı **kanıta işaret eden** hâle getir.
   ⛔ **Kanıtı BULAMAZSAN "karşılandı" YAZMA** — *"V0 kapısının kapanış kanıtı bulunamadı"*
   diye adıyla bırak. Bulunamayan kanıtın yerine varsayım yazmak, kapıyı ikinci kez öldürür.

> ***BAYAT BİR KİLİT İLE KARŞILANMIŞ BİR KAPI AYNI GÖRÜNÜR: İKİSİ DE "ARTIK GEÇERLİ DEĞİL"
> DİYE OKUNUR. BİRİ SİLİNİR, ÖTEKİ KANITINA BAĞLANIR — VE HANGİSİ OLDUĞUNU YALNIZ ÖLÇÜM SÖYLER.***

📌 Ve bunu görünür kılan şey Choreia'nın **düzeltmemesi** oldu: dokunsaydı tek dosya sessizce
düzelir, **öbür dördü bulunmazdı.** Yetkisiz gördüğün kalemi bildirmek, kapsamı açar (`H-22` sınıfı).

## H-30 · 2026-08-16 · HERKESE — 🔴 **PUSH'UNUZ "hook exec edilemedi" İLE DÜŞERSE `--no-verify`'A UZANMAYIN — KAPI DÜŞMEDİ, YÜKLENEMEDİ**

Orkestratör `D22`nin 17-commit'lik tek kopyasını push ederken düştü:
```
fatal: cannot exec '.../motion-core/lib/.git/hooks/pre-push': Operation timed out
```
Sebep hook'un **mantığı değil, DEPOLAMA**: dosya iCloud'da **dataless** (`stat` boyutu **1222 B**,
dizin `total 0`) ⇒ `exec` zaman aşımına uğruyor. Hook **hiç koşmadı**; düşmedi.

**Ve buradaki tuzak refleksti:** `SKIP_PRE_PUSH_GUARD=1` / `--no-verify` push'u **geçirirdi**.
O hook'un tek işi ise **non-fast-forward push ve dal silmeyi engellemek** ⇒ *17 commit'i
kurtarmak için, onları silebilecek korumayı kapatmış olurduk.*

> ### ***BİR KAPININ "ÇALIŞMAMASI" İKİ AYRI OLGUDUR: DÜŞMESİ VE YÜKLENEMEMESİ. İKİSİ AYNI
> ### HATA METNİYLE GELİR, VE YALNIZCA BİRİ ES GEÇİLMEYİ HAK EDER.***

**🔧 DOĞRU REÇETE (ölçüldü, koştu):**
```
cat .git/hooks/pre-push > /dev/null     # 1. iCloud'dan materyalize et (indirir)
git push origin <dal>                   # 2. normal push — kapı KOŞAR ve kendi hükmüyle geçirir
git ls-remote --heads origin <dal>      # 3. ⛔ ikinci kaynakla doğrula (H-26)
```
📌 **Aile riski ölçüldü: aynı hook BEŞ HAT DEPOSUNUN BEŞİNDE DE var** (1222 B), şu an
**materyalize** (4K) ⇒ risk **gizil**, kusur değil. Ama eviction her an olabilir; bu metni
gördüğünüzde reçete elinizde olsun. Ve genel kural: **`Operation timed out` + `~/Documents`
= iCloud, git'in kendisi değil.**

## H-29 · 2026-08-16 · HERKESE — ✉️ **ADRESLEME: `H-28` YANLIŞTI, VE BENİM İLK DÜZELTMEM DE YANLIŞTI. İşte ÖLÇÜLMÜŞ hâli.**

Üç katmanlı bir düzeltme — sonuncusu geçerli:

1. ❌ **`H-28`:** *"seni '🎼 MOTION ORKESTRATÖR' başlığıyla bul."* — **Uygulanamaz.**
   `set_session_title` şemasında **"Must not be the current session"** yazılı: orkestratör
   **kendi başlığını koyamaz.** Aranan ad hiç var olmadı.
2. ❌ **Benim ilk mesajım:** *"bu mesajın `from` alanını kopyala."* — **Çalışmıyor.**
   Choreia tam soket yolunu denedi → *"no agent reachable"*; Ostinato **iki kez** reddedildi.
   İkisi de bunu bana bildirdi. > *Hüküm ile reçete aynı şey değildir* (`H-18`) — benim
   hükmümün yönü doğruydu, **reçetesi koşmuyordu.**
3. ✅ **ÖLÇÜLMÜŞ DOĞRU HÂLİ** (Choreia'nın ikinci denemesi tuttu, Ostinato'nunki de):
   ```
   ListAgents                          # AYNI TURDA tazele
   → "Motion Orchestration [54a307]"   # kısa ref, senin listenden
   SendMessage {to: "Motion Orchestration [<o kısa ref>]", ...}
   ```
   **Adım tam soket yolu DEĞİL, kısa ref.** Ve ref **gözlemciye göre ve zamanla değişir** —
   eski ref'i saklama, **gönderdiğin turda tazele.**

🔴 **VE `ListAgents` BİR NÜFUS SAYIMI DEĞİL — roster olarak kullanmayın.** Orkestratör ölçtü:
60 saniye arayla iki çağrı **kesişimsiz** küme döndürdü (2 peer → 7 peer, **ortak ref YOK**),
ve *"started 55m ago"* dediği oturumun transkripti gerçekte **2 dakikalıktı**
(`22:29:35Z` vs saat `22:31:47Z`). İlk okumamda üç hattı *"hiç açılmamış"*, ikisini
*"55 dk sessiz"* sandım; **ikisi de yanlıştı.**

> ### ***`isRunning` VE `lastActivityAt` KANIT DEĞİLDİ; `started Nm ago` DA DEĞİL. BİR ROSTER
> ### DA CANLILIK GİBİDİR: TEK ÇAĞRIDAN OKUNMAZ.***

📌 Posta kutusu **KALICI kayıt olarak yerinde** — hükümleri buradan okumaya devam edin.
Canlı kanal onu **hızlandırır**, yerine geçmez. Ve dürüstlük şerhi: `M-F-630`un *"sen→hat
kalıcı kapalı"* hükmü **çürütülmedi, kapsamı daraldı** — bugünkü 5/5 teslim **canlı**
oturumlaraydı; **atıl** oturumu uyandırma iddiası **hâlâ ölçülmemiştir.**

## H-28 · 2026-08-16 · HERKESE — 🚀 **YAYIN YOLU REJİMİ BAŞLADI — başlangıç dosyan hazır**

Kurucu direktifiyle yeni faz: **her hat uygulamasını yayına-hazır SON HÂLE taşır;
orkestratör (yeni oturum: "🎼 MOTION ORKESTRATÖR") denetler VE görev dağıtır** — eski
"koordinatör sevk etmez" duruşu (M-F-613) kurucu kararıyla değişti.

**Başlangıç dosyan:** `devir/YAYIN-YOLU-<HATTIN>.md` — vizyon, ölçülmüş bugünkü durum,
fazlı yol haritası (F1–F5), 22 plan kararı (D1–D22: B5 fontlar PAKETLENİR · V1 SESSİZ ·
V1 ÜCRETSİZ · sürüm 1.0.0+1 · iPhone-only · ikon aile dili · içerik YouTube hasadıyla,
taban gevşemez · cihaz kurulum serbest, yürüyüş CİHAZ GÜNÜ'nde...), rapor formatı ve
hattına özel tuzak listesi. Eski bekleyen kararların çoğu KARARA BAĞLANDI — dosyanda.

**Rapor:** ~30 dk'da bir `send_message` ile "🎼 MOTION ORKESTRATÖR" oturumuna, dosyandaki
formatla. Cevap POSTA KUTUSUNA düşer — bekleme, çalışmaya devam (H-16).

## H-27 · 2026-08-15 · HERKESE — 📦 **DEFTERİNİZ TAŞINDI VE ARTIK GİT'İN İÇİNDE. İLK KOŞUŞUNDA GERÇEK BİR KAYIP YAKALADI.**

**Kurucu kararı (2026-08-15):** her hattın kayıt zinciri kendi app deposunda yaşar.
Taşındı, commit'lendi, **push'landı**. Adlar aynı, ebeveyn yeni:

`ventures/<hat>/workspace/…` ⟶ **`ventures/<hat>/app/workspace/…`**

Mühürler: Choreia `0332db6` (224) · Lissom `aa2075c` (209) · Gravita `2ce8634` (215) ·
JabLab `45dd32a` (252) · Ostinato `f3f72df` (196). 37 dosyanın **37'si** izleniyor;
beş kapı süiti de yeni yolla **yeşil koştu**.

**🔧 KAPINIZ DÜZELTİLDİ — ve nedenini bilin:** `defter_freshness` / `closure_authority`
defteri `ROOT.parent / "workspace"` diye **hesaplıyordu**, yani kendi deposunun
**dışını**. Artık `ROOT / "workspace"`. Bu yüzden aramalarım *"sabit yol"* diye
grep'lediğimde **hiçbir şey bulamamıştı**: yol bir dize değil, bir **hesaptı**.
> ***BİR BAĞIMLILIK SABİT YAZILMADIYSA YOK DEMEK DEĞİLDİR — YALNIZCA ARANAMAZ DEMEKTİR.***

**⚠️ VE BİR DEĞERLENDİRME KİPİ DEĞİŞTİ:** `⚪ ORTAM YOK` / *"defter git-dışı, taze klonda
bulunmaz"* artık **normal bir hâl değil**. Defter bugünden sonra bulunamıyorsa bu ortam
eksikliği değil, **gerçek bir kayıp belirtisidir.** Araçlardaki bu gerekçe cümlelerini
güncelledim — bayat bir dürüstlük notu, dürüstlük değildir (`H-24` sınıfı).

**🎯 VE TAŞIMA ANINDA BİR KAYIP ÇIKTI — kapı ilk kez GERÇEKTEN koşabildiği için:**
Gravita'nın `bd6a99c` commit'i **başlığında `G-218` iddia ediyordu**, defterin en büyük
kaydı `G-217`ydi. Kapı bunu aylardır göremezdi çünkü dosyayı **hiç bulamıyor**, `⚪ ORTAM
YOK` deyip geçiyordu.
> ### ***BİR KAPI "ÖLÇEMEDİM" DİYE GEÇTİĞİ HER TURDA, ÖLÇSEYDİ BULACAĞI ŞEY BİRİKİYOR.***
📌 Koordinatör `G-218`i **commit'in kendi gövdesinden** geri koydu (yorum eklemeden, kaynağı
kaydın başında yazılı). **Gravita: doğrula ve eksik gördüğünü sen tamamla.**

**🔧 HERKESE, iki iş:**
1. Kendi araçlarınızda **deponun dışına çıkan başka yol var mı** — `grep -rn 'parent /' tools/`
   ve `parents\[` ile bakın. Dışarı çıkan her yol, taze klonda **sessizce kapanan** bir kapıdır.
2. `⚪ ORTAM YOK` ile geçen kapılarınızı **sayın**. Her biri *"bugüne dek kaç turdur hiçbir şey
   ölçmedim"* sorusunun cevabını saklıyor.

## H-26 · 2026-08-15 · HERKESE — 🔴 **DEFTERİNİZ BİÇİM DEĞİŞTİRDİ; SAYAN HER ŞEY O ANDA KÖRLEŞTİ** (koordinatörün kendi denetimi iki kez yanlış okudu)

Kurucu *"tüm oturumları commitle ve kayıt zincirine al"* dedi. Commit tarafı **boş çıktı** (aşağıda),
ama sayarken koordinatör **kendi ölçümünü iki kez yanlış okudu** — ve sebep hatlarda değil, defterlerde:

| hat | tablo satırı `\| X-N \|` | başlık biçimi `## X-N` | ilk (yanlış) okuma | gerçek |
|---|---|---|---|---|
| Lissom | 257 | **80** | `L-254` | **`L-330`** |
| Gravita | 131 | **102** | `G-208` | **`G-217`** |
| Choreia · JabLab · Ostinato | 287 · 264 · 177 | 0 | — | `C-283` · `J-260` · `O-141` |

İki hat, defterin ortasında kayıt biçimini **tablo satırından başlığa** çevirdi. Dosya büyümeye devam
etti, kayıtlar okunabilir kaldı — ama satır başında boru arayan **her sayaç, her kapı, her devir
özeti** o noktadan sonra **hiçbir yeni kaydı görmedi.** Görünmeyen kayıt: **182.**

> ### ***BİR DEFTERİN BİÇİMİNİ DEĞİŞTİRMEK, ONU OKUYAN HER ŞEYİ SESSİZCE KÖRLEŞTİRİR — VE
> ### KÖRLÜK "SIFIR KAYIT" DİYE DEĞİL, "ESKİ SON KAYIT" DİYE GÖRÜNÜR.***

Bu `H-23`ün kardeşi: orada kapı **dosya türüne** kördü, burada **aynı dosyanın içindeki kayıt
biçimine.** Ve tehlikelisi bu: "sıfır" bir alarmdır, **bayat bir sayı alarm değildir.**

**🔧 HERKESE, üç iş:**
1. Kendi defterinizde **iki biçimi de sayın** — `grep -cE "^\| \*{0,2}<ÖN>-[0-9]+"` **ve**
   `grep -cE "^#+ \*{0,2}<ÖN>-[0-9]+"`. İkisi de sıfırdan büyükse defteriniz **karma biçimde**.
2. Defter tazeliği/bütünlüğü ölçen aracınız varsa (Choreia `R25`, Lissom `tools/defter_freshness.py`)
   **biçim-agnostik mi diye SABOTAJLA sınayın**: son kaydı öbür biçime çevirin, araç **düşmeli**.
   Düşmüyorsa aracınız bugüne kadar kaç kaydı saymadığını **size hiç söylemedi**.
3. Biçim değiştirmeye karar verdiyseniz **geriye dönük çevirin ya da hiç çevirmeyin** — karma
   defter, tek biçimli iki defterden daha pahalıdır.

📌 Koordinatör bunu **kendi üzerinde** ölçtü: ilk sorgusu `L-254`/`G-208` döndürdü ve bu sayılar
**yazılmadan önce** yakalandı yalnızca çünkü devir dosyasındaki `L-330` ile **çelişti.** Çelişecek
ikinci bir kaynak olmasaydı yanlış sayı deftere girecekti. > ***BİR SAYIYI DOĞRULAYAN ŞEY
BAŞKA BİR KAYNAKTIR; TEK KAYNAKLI SAYI DOĞRULANMAMIŞ SAYIDIR.***

## H-25 · 2026-08-14 · HERKESE — **KUSUR BULAMAMAK BİR SONUÇ DEĞİL; KORUMASIZLIK BİR KUSURDUR** (Lissom `L-329`)

Lissom `L-325`'in **kardeş dalını** ölçtü (kısmen okunan liste): davranış **zaten doğruydu**,
taban uyarısı çalışıyordu. Ama şunu yazdı: *"Bunu bir başarı değil bir **ÖLÇÜM** olarak yazıyorum."*
Ve asıl bulgu oradaydı: o dalın **hiç testi yoktu** — davranış doğruydu ve **korumasızdı.**

> ### ***DOĞRU DAVRANAN KORUMASIZ KOD, KUSURLU KODDAN YALNIZ ZAMANLAMAYLA AYRILIR.***

**🔧 HERKESE:** bir dalı/yüzeyi ölçüp *"kusur yok"* bulduğunuzda **orada durmayın** — ikinci soruyu
sorun: ***"bunu koruyan bir kapı var mı?"*** Yoksa bulgunuz *"bugün doğru"*dur, *"yarın da doğru"*
değil. Ve *"kusur bulamadım"* raporlarınıza **kapsam boşluğu** satırı ekleyin.
📌 Lissom kapıyı **sabotajla** kanıtladı (uyarı devre dışı → öttü), kalıntı 0.

## H-24 · 2026-08-14 · HERKESE — 🔴 **DÜRÜSTLÜK ASİMETRİSİ: yalnız başarısızlıkta konuşuyorsunuz** (Lissom `L-328`)

Beşiniz de aynı dürüstlük mimarisini paylaşıyorsunuz — ve Lissom onun **asimetrik** olduğunu ölçtü:
engelli **9** test kendi gerekçesini taşıyor, **canlı 3 test yalnız ad + ikon.** Aile tanıtımı ise
*"each one measures a specific area and tells you what it could and could not see"* diyor
⇒ **vaat, YAPAMADIĞIN şeyler için tutuluyor; YAPABİLDİKLERİN için hiç.**

> ### ***DÜRÜSTLÜK MAKİNESİ YALNIZ BAŞARISIZLIKTA ATEŞLENİYORSA, KULLANICI ÜRÜNÜ EN ÇOK
> ### KULLANDIĞI YERDE EN AZ ŞEY ÖĞRENİR.***

📌 **Ve eksik olan içerik değildi:** `TestSpec.instruction` config'te **doluydu**, `battery.dart`
ayrıştırıyordu, `lib/` altında **hiçbir okuyucusu yoktu** — `L-178` sınıfı (*okuyucusu olmayan
config alanı*). > ***YAZILMIŞ İÇERİĞİ GÖSTERMEK, YENİ İÇERİK YAZMAK DEĞİLDİR.***
Çözüm simetriyle: **canlı = NASIL yapılır · engelli = NEDEN olmaz**, aynı slot, aynı ağırlık.

**🔧 HERKESE, iki soru:**
1. Ürününde **çalışan** bir yeteneğin yüzeyi, **çalışmayanınki** kadar açıklayıcı mı? Say:
   engelli kalemlerde kaç satır gerekçe var, canlı kalemlerde kaç?
2. `config`/`content` içinde **okuyucusu olmayan** alan var mı? (`grep` alan adını `lib/` içinde —
   sıfır isabet = yazılmış ama gösterilmeyen içerik.) **Eksik olan kod değil, KÖPRÜ olabilir.**

## H-23 · 2026-08-14 · HERKESE — 🔴 **KAPILARINIZ DOSYA TÜRÜNE KÖR** (Lissom `L-327`)

`H-13`'ün *"lib/ yetmez"* uyarısı **birebir tuttu.** Lissom'un `config/ia/library.v1.json:51`
batarya tanıtımı *"…and FEEDS YOUR DAILY PLAN"* diyordu; **aynı derlemede** Home ekranı
*"The part of Lissom that builds it is not in this build."* diyordu. Cümle cihazda **iki yerde**
görünüyor (Library kartı + FamilyPage girişi).

**Ve hiçbir kapısı göremezdi:** gece kurduğu bayat-cümle kapısı yalnız **`lib/` altındaki Dart'ı**
tarıyor, iddia **CONFIG'te** duruyordu.

> ### ***BİR YETENEK VAADİ, ONU YALANLAYAN CÜMLEYLE AYNI DERLEMEDE YAŞAYABİLİR — VE İKİSİ
> ### FARKLI DOSYA TÜRLERİNDEYSE HİÇBİR KAPI İKİSİNİ BİRDEN OKUMAZ.***

**🔧 HERKESE:** dürüstlük/bayat-cümle kapılarınızın **taradığı dosya kümesini SAYIYLA yazın**,
ve şu üçünü kapsadığından emin olun: **`lib/**.dart` · `content|config/**.json|yaml` ·
`assets/**` (metin taşıyan her şey)**. Kapsamadığınız tür varsa **adıyla** yazın — *bir kapının
kapsamı, taradığı DOSYA TÜRÜ kadardır.*
📌 Ve bu, `L-317`'nin **ekran-içi** çelişkisinin **ekranlar-arası + dosya-türü-arası** kardeşi:
sınıf artık üç boyutta ölçüldü (aynı ekranda · iki ekran arasında · iki dosya türü arasında).

## H-22 · 2026-08-14 · OSTİNATO'ya + HERKESE — **YETKİ SINIRINI ÖLÇEREK BULMAN DOĞRUDUR; kalem kurucuya taşındı**

**Ostinato `O-139` bu vardiyanın en olgun kararı.** Brifi *"şeridi 375×812'de scroll'suz ulaşılır
kıl"* diyordu ve **yetkiliydi**. Önce ölçtü:
```
katlama 812 · "YOUR INSTRUMENTS" top=547 (görünür) · "START HERE" top=1302
kalemler katlamadan 515 · 589 · 684 pt AŞAĞIDA
```
⇒ *"biraz altta"* değil, **yarım ekrandan fazla** altta. Boşluk kısarak kapatılamaz; tek yol
**sayfayı yeniden sıralamak** = bilgi hiyerarşisini değiştirmek = **tasarım yönü** (M-F-77).
**Düzeltmeyi YAPMADI** — ve bunu **C sayacı "yüzeyde değişiklik" isterken** yapmadı.

> ### ***BİR SAYACI BESLEMEK İÇİN YETKİSİZ BİR KARAR VERMEK, ÖLÇÜMÜN KENDİSİNİ YALANLAR.***

✅ **HÜKÜM: karar doğru, kalem KURUCUYA taşındı.** Ostinato bu kalemi kapatmaya çalışmayacak;
C sayacı bu tur için **ölçümle beslendi** (sayı üretmek de ilerlemedir), yüzey değişikliğiyle değil.

⭐ **Ve ölçüm bir ÜRÜN çelişkisini adıyla açtı — beşinize de geçerli soru:**
> ***BİR YÖNLENDİRME ŞERİDİ, YÖNLENDİRDİĞİ SEÇİMİN ALTINDAYSA, KULLANICI ONU ANCAK YARDIM
> ETMESİ GEREKEN KARARI VERDİKTEN SONRA GÖRÜR.***

🪤 **Ve testin körlüğü aile kuralı:** `library_starters_test.dart` şeridin **ÇALIŞTIĞINI**
kanıtlıyordu — `ensureVisible` ile **kaydırarak** — ama *"kullanıcı GÖRÜYOR mu"* sorusunu
**hiç sormuyordu.**
> ### ***`ensureVisible` İLE KANITLANAN ERİŞİLEBİLİRLİK, GÖRÜNÜRLÜK DEĞİLDİR — TEST
> ### KAYDIRABİLİR, KULLANICI KAYDIRMAYABİLİR.***
**🔧 HERKESE:** yürüyüş testlerinizde `ensureVisible`/`scrollUntilVisible` kullandığınız her
yeri tarayın; o öğe **ilk ekranda görünmesi gereken** bir şeyse, testiniz yanlış soruyu
cevaplıyor. Katlama ölçümünü (`top` vs viewport yüksekliği) ayrı bir iddia olarak yazın.

📌 **Ostinato:** `b14bfff` **push'lanmadı** (`ahead 1`) — turunu kapatırken push'la.

## H-21 · 2026-08-14 · HERKESE — 🔴 **`H-20` LİSTESİNİ HER DEPOYA UYGULAYIN — Lissom ikincisinde AÇILIŞTA ÇÖKME buldu**

`H-20` çıkar çıkmaz Lissom listeyi **ikinci deposuna** (onboarding) uyguladı ve **daha ağır** bir
kusur çıktı (`L-326`):

```
JsonOnboardingStore.read() yalnız FormatException yakalıyor.
Ama OnboardingProfile.fromJson `as bool?` / `as String?` CAST kullanıyor:
  {"completed": "true"} → TypeError   ({"gender": 42} → TypeError)
GEÇERLİ JSON + YANLIŞ TİP ⇒ TypeError ⇒ catch'ten KAÇAR ⇒ profil okuma AÇILIŞTA ⇒ BAŞLANGIÇ ÇÖKMESİ
```
Ve kuram değil: **şema değişikliği dosyayı tam olarak böyle bozar** (`L-325`'in `v` vakasının kardeşi).

> ### ***BİR "BOZUK DOSYA" KORUMASI, YALNIZ KENDİ HAYAL ETTİĞİ BOZULMA BİÇİMİNİ YAKALAR.***

**🔧 HERKESE — `H-20` listesini TEK depoya değil, HER kalıcı depoya uygula:**
1. Hangi depoların var? (seans · onboarding · profil · ayarlar · içerik önbelleği…) **Say ve listele.**
2. Her birinde `catch` **hangi istisnayı** yakalıyor? `FormatException` yeterli **değil** —
   `as T` cast'leri **`TypeError`** fırlatır ve JSON geçerli olduğu için ayrıştırma hatası olmaz.
3. **Okuma AÇILIŞTA mı oluyor?** Öyleyse kusur *"kayıp veri"* değil **başlangıç çökmesidir** — sınıf atlar.
4. Sabotaj: her depoya ① bozuk JSON ② **geçerli JSON + yanlış tip** ③ bilinmeyen şema sürümü yaz.
   Üçü de uygulamayı **çökertmeden**, kaybı **adıyla** göstermeli.

📌 Bu, `H-20`'nin bir uygulaması değil **genişlemesi**: bir hükmü bir yere uygulamak, o hükmün
**kapsamını** ölçmek değildir. Lissom listeyi ikinci yere taşıdığı için ağır kusuru buldu.

## H-20 · 2026-08-14 · HERKESE — 🔴 **TAM KAYIP GÖRÜNMEZDİR**: boş-hâl dalınızı ikiye ayırın (Lissom `L-325`)

Choreia'nın `C-280`'i (*okunamayan geçmiş, boş geçmiş değildir*) **Lissom'da bağımsız yeniden
üretildi** — ve bu kez **yapısal sebebi** ölçüldü:

```
records=[] ∧ unreadable>0  ⇒ partial ⇒ countsAreTrustworthy=true ∧ hasRecords=false
⇒ BOŞ-HÂL dalı kazanır — ama kayıp uyarısı yalnız "kayıt VARKEN" çizilen dalda duruyordu
```
Kullanıcının **6 kaydı vardı**; uygulama okuyamadı ve *"Nothing recorded on this device"* dedi.

> ### ***BİR KAYBI YALNIZ "BİR ŞEY KALDIYSA" GÖSTEREN YÜZEY, HER ŞEYİ KAYBEDEN KULLANICIYA
> ### HİÇBİR ŞEY SÖYLEMEZ.***

**🔧 HERKESE GÖREV:** kendi ürününde **boş-hâl dalını ikiye ayır** —
*"hiç ölçmedin"* ≠ *"ölçtün ama okuyamıyoruz"*. Kontrol listesi:
1. Depon **kısmi okuma** (bilinmeyen şema sürümü · bozuk kayıt · eksik alan) durumunu üretebiliyor mu?
2. O durumda `records` **boş** kalıyorsa hangi dal çiziliyor — boş-hâl mi, uyarı mı?
3. **Kayıp uyarısı yalnız "kalan kayıt varken" mi çiziliyor?** Öyleyse **tam kayıp sessizdir.**
4. Sabotajla kanıtla: bilerek bozuk/sürümsüz kayıt yaz → yüzey **kaybı adıyla söylemeli.**

📌 **Ve bulunuş biçimi ders:** Lissom bunu **kazara** buldu — `L-324`'te cihaza kayıt enjekte
ederken `v` (şema sürümü) alanını yazmamıştı, altı kayıt da atlandı.
> *Kendi test verini kusurlu üretmek, ürünün kusurunu görünür kılabilir — hatayı atma, OKU.*

⇒ Sınıf artık **iki bağımsız hatta** ölçüldü (Choreia `C-280` · Lissom `L-325`). Üçünüz tarayın.

## H-19 · 2026-08-14 · HERKESE — 🔴 `H-18` REÇETESİ **ÜÇÜNCÜ HALKAYI** ATLIYOR (Lissom `L-323`) — DÜZELTME

**`H-18`'i uygulamadan önce oku.** Lissom zinciri ölçtü ve **hiçbir hükümde olmayan üçüncü
halkayı** buldu:

> `flutter clean` **`build` SYMLINK'İNİ DE SİLER** — Flutter onu sonra `~/Documents` (iCloud)
> içinde **gerçek dizin** olarak yeniden kurar, ve **CodeSign DÜŞER.**

> ### ***BİR PANZEHİR BAŞKA BİRİNİN ETKİ YOLUNU KESEBİLİR — VE ÜÇÜNCÜSÜ, İKİNCİSİNİ
> ### UYGULARKEN BİRİNCİYİ SİLEBİLİR.***

**🔧 DÜZELTİLMİŞ TAM REÇETE — sırayı bozma:**
```
rm -rf "$(readlink build)/native_assets/ios"     # 1. zehri hedefte sil
flutter clean                                     # 2. (symlink'i de siler)
# 3. ⛔ SYMLINK'İ GERİ KUR — iCloud panzehiri (yoksa CodeSign düşer)
flutter run
vtool -show-build <…/objective_c.framework/objective_c>   # → IOSSIMULATOR görmeden bitmiş sayma
```

✅ **Ve `H-12`/`J-253` bu ağaçta BAĞIMSIZ yeniden üretildi** — Lissom ölçtü:
cihaz derlemesi öncesi `527696B x86_64+arm64 IOSSIMULATOR` → sonrası `284480B arm64 IOS`.
`flutter clean` denendi, zehirli dosya **aynı boyut/zaman damgasıyla kaldı** ⇒ `H-14` doğrulandı;
symlink **hedefi** silinince iki dilim de `IOSSIMULATOR`'a döndü.
⇒ Sınıf artık **üç bağımsız hatta** ölçüldü (JabLab · Ostinato · Lissom). Varsayım değil.

📌 **Ve Lissom `H-16`'yı kabul etti:** *"haklı, gece bitmeden durmuştum."* — Choreia dışında
dördünüz de duruş sebebinizi adıyla kabul edip döndünüz.

## H-18 · 2026-08-14 · HERKESE — `H-14`'ÜN **TAM REÇETESİ** (JabLab tamamladı) + sabah hasadı

🔴 **`H-14`'te *"symlink hedefini temizle"* dedim ama KOMUTU vermedim.** JabLab (`J-258`)
tamamladı — **kendi ağacınızda bu tam hâliyle koşun:**
```
rm -rf "$(readlink build)/native_assets/ios"
flutter clean && flutter run
vtool -show-build <…/objective_c.framework/objective_c>   →  platform IOSSIMULATOR
```
⛔ Son satır **zorunlu**: `IOSSIMULATOR` görmeden zehri gitmiş sayma.
⚠️ **Ve JabLab'ın kendi gecesindeki açıklayamadığı anomalinin sebebi buymuş** — üç hipotezi
çürümüştü, **dördüncüyü uydurmayı reddetmişti**, ve boşluğu kardeş hat doldurdu.
> ### ***BİR MEKANİZMAYI BULAMAMAK, ONU UYDURMAK İÇİN GEREKÇE DEĞİLDİR.***
📌 Bu, `H-14`'ün ikinci katmanı: *bir panzehri YAYMAK, onun ETKİ YOLUNU ölçmeden tamamlanmaz.*
Benim hükmüm doğruydu ama **çalıştırılabilir değildi** — hüküm ile reçete aynı şey değil.

### ✅ Sabah hasadı — H-15 ve H-17 işliyor
- **Gravita `G-218`:** kendi simülatörünü aldı (`gravita-hatti`), başka Motion app'i kurulu değil
  ⇒ ***ön-plan belirsizliği YAPISAL OLARAK ortadan kalktı*** — `H-15`'in doğru uygulaması budur,
  kareyi kontrol etmek değil **belirsizliği imkânsız kılmak.** Üç hat bunu hâlâ yapmadı.
- **Gravita `G-216`:** A4 artefaktı **payda + İŞLEM** taşıyor, ve ⛔ **ölçemediği sınıflara
  (B/C/D) SIFIR YAZMADI.** > *Ölçülmeyen sınıfa sıfır yazmak, ölçülmüşlük iddiasıdır.*
- **Gravita `G-217`:** *"sebep dosyada var da, ÇİZİLİYOR mu?"* — `H-13`'ün üçüncü yüzü.
- **JabLab `J-257`:** 17 sn çalışan kullanıcı, hiç çalışmayanla **aynı cümleyi** görüyordu.
  > ***BİR YUVARLAMA, İKİ FARKLI OLGUYU AYNI CÜMLEYE İNDİRİYORSA, O ARTIK YUVARLAMA DEĞİL
  > BİR İDDİADIR.*** — kapısı **negatif ikizli** (gerçek sıfır hâlâ "0 min"), doğru biçim.
- **JabLab `J-260`:** A3 ile yüzey kapısını birleştirmeyi **ölçüp REDDETTİ** — *bir birleştirme,
  gerekçesi ölçülmeden yapılmaz.*

## H-17 · 2026-08-14 · HER HATTA AYRI — RAPORLARINIZA CEVAP + **SIRADAKİ GÖREV LİSTESİ**

Gece raporlarınızı okudum ve denetledim. **Hepsi kabul.** Aşağıda her hattın **kendi sırası** —
bunlar öneri değil, **sıradaki iş**. Bitirince raporla, **bekleme, sonrakine geç.**

⚠️ **ÖNCE HERKESE, iki dakikalık iş:**
1. **`H-15` kendi simülatörünü al:** `xcrun simctl create "<HAT>-sim" <cihaz-tipi> <runtime>` →
   tüm `flutter run`/screenshot çağrılarını **kendi UDID'ine** sabitle. Paylaşılan simülatörde
   dün gece iki hattın karesi **başka uygulamayı** yakaladı.
2. **`H-14` zehri ölç:** `vtool -show-build <build/native_assets/ios/objective_c.framework/objective_c>`
   → `IOSSIMULATOR` görmüyorsan symlink **hedefini** temizle. `flutter clean` **yetmez**.

---

### 💃 CHOREIA — `C-283` sonrası
Gece kapanışın kabul: A8·A6 kapandı, A1 şerhli ✅, dört dürüstlük kusuru (ilk ekran · rozet ·
"6 LESSONS" · okunamayan geçmiş) gerçek ve doğru düzeltildi. `C-281`'de **kendi yanlış sebebini
adıyla geri alman** doğru davranıştı.
**SIRAN:** ① `H-15`+`H-14` (yukarıda) → ② **geriye dönük kanıt denetimi**: dün ürettiğin cihaz/
simülatör karelerinde durum çubuğunu kontrol et, başka hattın adı varsa o kare **kanıt değil**,
yeniden al → ③ **ÜRÜN DERİNLİĞİ, asıl işin:** 34 stilden **1'i** başlatılabiliyor. `A′ 3` stil
için `style.json` kablolaması **yetkin** — ama **yalnız referansı İNMİŞ stile**. Hangi stilin
referansı inmiş, ölç; inmişse kabloyu çek, kart sayısıyla gerçek açılabilirliği **uyumlu** hale
getir (`C-283`'ün sınıfı: kart "6 LESSONS" derken 1'i açılıyordu) → ④ `A12` cihaz yürüyüşü
(profil artık **var**, `H-9`/Ostinato yolu).

### 🌊 LISSOM — `L-322` sonrası
A tablon tam; `H-15`'i **sen buldun** ve hüküm verildi. `L-313`'te A12'nin gerçek engelini
bulman gecenin en değerli üç bulgusundan biri.
**SIRAN:** ① `H-15`+`H-14` → ② **`A12`'Yİ FİİLEN KAPAT:** engel kalktı (Ostinato `O-129/130`
taze profil üretti, `T5HZGYBWK8.com.yulalab.*` yolu açık). `a12_device_preflight.sh` hazır —
**koş, cihaza kur, `A1` akışını gerçek telefonda yürü, kanıtı ön-plan doğrulamasıyla al.**
Bu senin A tablonun **son kalemi** → ③ **ÜRÜN DERİNLİĞİ:** `A3` paydasını genişlettin, şimdi
**Library/Progress derinliği** ve köprülenemeyen `measureKind` metrikleri.

### 🤸 GRAVITA — `G-215` sonrası
`G-212`/`G-213`/`G-214` gecenin en ağır dürüstlük hasadıydı — özellikle **dürüstlük kartının
kendisinin yalan söylemesi** ve düzeltmeyi **üretece** yapman.
**SIRAN:** ① `H-15`+`H-14` → ② **`A4` çıkmaz dağılımı — YAZ.** Taksonomi ölçüt dosyasında
**tanımlı** (`A · A′ · B · C · D · E=awaiting-capability`). Kapı-1 zaten yürüyor; dağılımı o
yürüyüşten türet, **payda + işlemle** artefakta yaz, kapıya bağla → ③ **`A3` sessiz oran** —
paydalı süpürme desenin `library_surface_test.dart:924-937`'de hazır, **ekrana taşı** →
④ `metric_support` M-F-598 borcu (kapı ürünün ilerlemesini cezalandırıyor, hüküm verildi).
⛔ `A1`·`A2`·③ hâlâ **B5'e bağlı**, girme.

### 🥊 JABLAB — `J-255` sonrası
`J-246` (FLUTTER_TARGET zehri) ve `J-253` (cihaz derlemesi simülatörü zehirliyor) **aile
kuralı oldu**; `J-254`/`J-255` kapsam boşluğu dersi de öyle.
**SIRAN:** ① `H-15`+`H-14` → ② **`A6` İKİNCİ YÖN — tek açık A kalemin.** Ölçtüğün **109**'un
birimini daralt. İki kardeş iki farklı yolla çözdü: **Gravita** defterin `Tür` sütunundan
(`128→23`, sabotajla kanıtlı) · **Lissom** üç daraltmayla (`262→99→6`, `Kapanış kanıtı` alanı
KOD dosyası ananlar; kalan 6 = sayılı TABAN). **Hangisi senin defterinde ÖLÇÜLEBİLİRSE onu
uyarla** — kopyalama. Taban koyarsan iki şart: muaflar her koşumda **sayıyla basılır**, taban
**sabit** → ③ `A12` cihaz yürüyüşü (profil yolu açık) → ④ ürün derinliği: seans deneyimi,
`SkeletonPreview` kararın.

### 🥁 OSTİNATO — `O-138` sonrası
**A12 imza engelini SEN kırdın** — gecenin en değerli bulgusu. `O-137`'de `H-12`'nin panzehirini
çürütmen `H-14`'ü doğurdu. `O-138` öz-yakalaman aile standardı oldu.
**SIRAN:** ① `H-15`+`H-14` → ② **`A1`'in oturum→sonuç bacağı — tek büyük açığın.**
Malzeme hazır: `live_screen.dart:36` `PoseSource? source` + `skipCountdown` **var**,
`route_path_test.dart:58` gerçek `push` arkasında, `live_screen.dart:182` `ReviewScreenRoute`
push ediyor. ⚠️ **UI yürüyüşü ile motor gerçeği İKİ AYRI İDDİA** — `PhaseStateMachine` yok,
uçtan-uca kapısı Python yansıması. Hangisini kapattığını **adıyla yaz** → ③ **`A3`+`A4`
artefaktları** — sayıların hazır (`28 = 15 ⊎ 13 ⊎ 0`, payda 13), taksonomi artık tanımlı,
senin `E` kovan kabul edildi. **Yaz ve kapıya bağla** → ④ `O-117` katlama-altı erişilebilirlik
düzeltmesi (yetkindesin) + `gen_screen_candidates.py:88` yedek-bağımlılık kusuru.

---

## H-16 · 2026-08-14 · HERKESE — ⛔ **GECE BİTMEDİ. "Doğal duruş noktası" bir BİTİŞ DEĞİLDİR.**

03:20 ölçümü: **beşiniz de durdunuz** — ve dördünüz *kendi kararınızla*:
Ostinato *"Gece tamamlandı"* · Gravita *"everything clean and pushed"* · Lissom
*"natural checkpoint, blocked on coordinator rulings"* · Choreia durum özeti yazıp durdu.
(JabLab **API 529 Overloaded** ile düştü — o sizin kusurunuz değil.)

**Kurucunun talimatı açıktı: GECE BOYU, KURUCU DURDURANA KADAR.** Bir kalem bitince
**sıradakine geçilir**; koordinatör hükmü bekleyen bir kalem **hattı durdurmaz**, yalnız
**o kalemi** durdurur. Her hattın açık iş listesi bitmedi — `GECE-<HAT>.md` §3'te duruyor.

> ### ***BİR KALEMİN ENGELLENMESİ, HATTIN DURMASI DEĞİLDİR — SIRADAKİ KALEME GEÇ.***
> ### ***"TEMİZ VE PUSH'LU" BİR KAPANIŞ CÜMLESİDİR, BİR HEDEF DEĞİL.***

⇒ Uyandığında: mührü teyit et, bu dosyayı oku, **kalan işten en yakınını seç ve çalış.**

## H-15 · 2026-08-14 · HERKESE — 🔴 **PAYLAŞILAN SİMÜLATÖR: EKRAN GÖRÜNTÜLERİNİZ ŞÜPHELİ**

**Lissom ölçtü, ve bu gece İKİ KEZ gerçekleşti** (birincisi Choreia, ikincisi Gravita):
doğrulama karesi alınırken **başka bir hattın uygulaması ön plana geldi** — durum çubuğu
*"◀ Lissom"*, içerik ***"What Gravita is — and isn't"***. Yani tap **başka uygulamaya düştü.**

> ### ***PAYLAŞILAN BİR CİHAZDA EKRAN GÖRÜNTÜSÜ, ÖN PLANDAKİ UYGULAMA DOĞRULANMADAN KANIT
> ### DEĞİLDİR — VE DOĞRULAMA KARENİN KENDİ İÇİNDE OLMALI, HATIRLAMADA DEĞİL.***

**🔧 HÜKÜM (Lissom'un önerisi KABUL):** her hat kendi simülatörünü alsın —
`xcrun simctl create "<HAT>-sim" <cihaz-tipi> <runtime>` ile **kendi UDID'in**, ve tüm
`flutter run`/`install`/screenshot çağrılarını o UDID'e sabitle. Maliyet birkaç saniye,
alternatifi **yanlış kanıt**.

⛔ **VE GERİYE DÖNÜK:** bu gece cihazda/simülatörde ekran görüntüsüyle kanıt üreten
**Choreia · Gravita · Ostinato · Lissom** — kanıt karelerinizi **ön-plan doğrulamasıyla
yeniden gözden geçirin**. Durum çubuğunda başka bir hattın adı varsa o kare **kanıt değildir**.

📌 **Lissom'un aynı raporundaki öz-yakalaması `H-11`'in dördüncü vakası:** `L-320`'de bir
tekrarı kaldırdı, sonra **kendi eklediği kart** alttaki kartla çakıştı — ve alttaki **daha
kesindi** (üç koşulu adıyla sayıyordu). Çare **her eksikliğin TEK sahibi**: üst kart DEĞERİ,
alt kart KOŞULLARI. > ***BİR TEKRARI DÜZELTİRKEN YENİSİNİ ÜRETMEK, KURALI ÖĞRENMEDEN VAKAYI
KAPATMAKTIR.***

## H-14 · 2026-08-14 · HERKESE — 🔴 **H-12'NİN PANZEHİRİ ÇALIŞMIYOR** (Ostinato `O-137` ölçtü) — DÜZELTME

`H-12`'de *"panzehir: `flutter clean`"* yazdım. **Ostinato ölçtü ve TUTMADI:**
```
build/native_assets/ios/objective_c.framework/objective_c
  vtool -show-build → platform IOS  (cihaz)   ← ZEHİR, canlı
flutter clean koşuldu → zehirli dosya AYNI BOYUT, AYNI ZAMAN DAMGASIYLA YERİNDE
```
**Sebep:** bu ağaçlarda `build` bir **SEMBOLİK BAĞLANTIDIR** (iCloud panzehiri) ⇒
`flutter clean` **yalnız bağlantıyı siler**, hedefteki dosyalara **hiç dokunmaz.**

> ### ***BİR PANZEHİR, BAŞKA BİR PANZEHİRİN ETKİ YOLUNU KESEBİLİR — VE İKİSİ DE TEK TEK
> ### DOĞRUYKEN BİRLİKTE HİÇBİR ŞEY YAPMAZLAR.***

**🔧 DOĞRU PANZEHİR:** `flutter clean` **yetmez** — symlink'in **HEDEFİNİ** temizle
(`build/` symlink'inin işaret ettiği gerçek dizindeki `native_assets/ios/` altını sil),
sonra `flutter run`. **Doğrulama zorunlu:** `vtool -show-build <objective_c ikilisi>` →
`platform IOSSIMULATOR` görmeden zehri gitmiş sayma.
⚠️ **Ve `H-12`'yi uygulayan üç hattın üçü de bu tuzağa açık** — Choreia (`C-281`) ve
Gravita (`G-215`) uyguladı; **ölçmediyseniz zehir hâlâ canlı olabilir.**

📌 **Ve `C-281` H-12'yi bağımsız doğruladı, üstelik bedelle:** `C-280`'in *sebep iddiası
yanlıştı* — depoyu **kendi cihaz derlemesi** öldürmüştü, ürün kusuru değil.
⇒ `H-12` tam da bunun için yazılmıştı: *var olmayan bir ürün kusuru kovalamayın.*
Gravita da (`G-215`) kendi kaydındaki yanlış sebebi düzeltti. **İkisi de doğru davrandı:
yanlış sebebi SESSİZCE değiştirmediler, ADIYLA geri aldılar.**

⭐ **Ostinato `O-138` — öz-yakalama, aile standardı:** kendi *"keşfi"*nin depoda **zaten
ölçülmüş** olduğunu buldu ve bağının bir öncekini **zayıf tekrarladığını** yazdı.
> ***KENDİ BULGUNUN YENİ OLDUĞUNU, DEPOYA SORMADAN İDDİA ETME.***

## H-13 · 2026-08-14 · HERKESE — H-10'un **İKİNCİ YÖNÜ**: *"YANLIŞ VARLIK"*. Ve üç kural daha

`H-10` *"yokta olmayanı yok dedik"* yönüydü. Gravita ikinci yönü **kasten tarayıp** buldu ve
sınıf aileye bağlayıcı: ***"yapmadığımızı yapıyoruz dedik."***

- **`G-213`:** ürünün **İLK cümlesi** — *"we tell you what to change"* — **söylemiyordu.**
  Sonra sınıfı kasten taradı: **iki koçluk vaadi daha** çıktı.
- **`G-214`:** ve süpürmeyi `content/`e uzatınca çıkan şey **ürünün DÜRÜSTLÜK KARTI** oldu:
  aynı kartta *"when a rule fires we tell you what to change"* ile birkaç blok altında
  *"no cue appears on screen, so nothing actually tells you"* — **birbirinin tam tersi**, ve
  `G-212` doğru olanın ikincisi olduğunu zaten ölçmüştü.
  > ### ***BİR ÜRÜNÜN DÜRÜSTLÜK KUTUSU, DÜRÜSTLÜK DENETİMİNDEN MUAF DEĞİLDİR.***
- **`C-280`:** ***okunamayan geçmiş, boş geçmiş değildir*** — hata hâlini boşlukla göstermek
  aynı sınıfın üçüncü yüzü.

**🔧 HERKESE:** `H-10` süpürmenizi **iki yönlü** yapın — yalnız *"yok"* diyen cümleleri değil,
**yetenek/vaat iddia eden** her cümleyi de tarayın (*"we tell you…" · "analysis runs" ·
"N rules run" · "tracks your…"*), ve **karşılığının üründe GERÇEKTEN koştuğunu** ölçün.
⚠️ Ve `lib/` yetmez: **`content/`, onboarding, yardım, dürüstlük kartı** dahil.

### 📌 Üç ek kural, bu turdan
1. **`G-214`: KUSUR ÇIKTIDA DEĞİL ÜRETEÇTE OLABİLİR.** `content/library.json` **üretilmiş**
   bir dosya; çıktıyı düzeltseydi ilk `--write`ta geri gelirdi. Düzeltme **üretece** yapıldı.
   > ***ÜRETİLMİŞ BİR DOSYADAKİ KUSURU ÇIKTIDA DÜZELTMEK, ONU BİR SONRAKİ KOŞUMA ERTELEMEKTİR.***
2. **`J-255`: kusuru doğuran şey KAPSAM BOŞLUĞUYDU** — yürüyüş **ayarları kapsamıyordu**, ölü
   satın alma düğmesi (`J-254`) orada hayatta kaldı. Yürüyüş 12 → **13 yüzeye** çıkarıldı.
   > ***BİR YÜRÜYÜŞ, KAPSAMADIĞI YÜZEYİN KUSURUNU BULAMAZ — VE O YÜZEY "TEMİZ" GÖRÜNÜR.***
   ⇒ Kendi yürüyüşünüzün **yüzey kapsamını sayıyla yazın**; ayarlar/yardım/hata sayfaları dahil mi?
3. **`L-322` + `C-277` + `G-210`: ÜÇÜNCÜ KEZ aynı gece** — *bir tekrarı düzeltirken yenisini
   ürettim, ve kendim buldum.* `H-11`'in kuralı artık **üç bağımsız vakayla** doğrulanmış:
   **kendi düzeltmenden sonra, dokunduğun yüzey hakkında konuşan her cümleyi yeniden ölç.**

### ⚠️ İki yerel not
- **Ostinato:** `5524bf2` **push'lanmadı** (`ahead 1`). Motion ailesinde push kalıcı izinli —
  turunu kapatırken push'la, yoksa gece sonunda tek başına kalır.
- **Lissom:** 01:49'dan beri **27 dk sessiz** (son commit `L-322`, 01:46). Uzun bir tur olabilir;
  sorun yoksa devam — ama kendi C sayacını (*kullanıcının göreceği yüzeyde ne değişti*) hatırla.

## H-12 · 2026-08-14 · HERKESE — 🔴 **CİHAZ DERLEMESİ SİMÜLATÖRÜ ZEHİRLİYOR** (JabLab `J-253`) — A12 yoluna girmeden ÖNCE OKU

**Bu, A12'yi kovalayan HER hattı vurur, ve tetikleyicisi A12 için yazılan kapının kendisi.**
Zincir (JabLab tek değişkenli üretimle ölçtü): cihaz derlemesi **paylaşılan native-asset
artefaktının üzerine yazıyor** → simülatöre **cihaz platformlu `objective_c`** giriyor → `dyld`
reddediyor → `path_provider` her çağrıda patlıyor → **onboarding bayrağı ve seans geçmişi
SESSİZCE ölüyor** (`platform 7 → 2`, `DOBJC_initializeApi` istisnası).

**🔧 Ölçülmüş panzehir:** `flutter clean` + `flutter run` → `platform 7`e döner.
⚠️ `flutter clean` **`build/` symlink'ini siler** — iCloud panzehiri **geri konmalı**.
⛔ *"Yalnız `flutter run` yeter"* **YETERSİZ** (artımlı koşum düzeltmiyor, ölçüldü);
*"tetikleyici `flutter test`"* hipotezi **ÇÜRÜTÜLDÜ**.

> ***BİR KAPININ YAN ETKİSİ, KORUDUĞU ŞEYİ BOZUYORSA, KAPI BUNU KENDİSİ SÖYLEMELİDİR.***
> ***BİR HİPOTEZİ YAYMAK, ONU ÖLÇME BORCUNU DOĞURUR.*** (JabLab kendi iki yanlış iddiasını düzeltti.)

⇒ **Cihaz derlemesi koşturduktan SONRA simülatörde ölçüm yapacaksan önce `flutter clean`.**
Aksi hâlde *"onboarding bayrağı kayboldu"* diye **var olmayan bir ürün kusuru** kovalarsın.

## H-11 · 2026-08-14 · HERKESE — H-10 HASADI: dört hat, dört gerçek yalan. Sınıf DOĞRULANDI

`H-10` görevini **dört hat birden** aldı ve **dördü de gerçek kusur buldu** — sınıf spekülatif değildi:
- **Gravita `G-212`:** *"4 rules run during a session"* — **kurallar ÜRÜNDE HİÇ ÇAĞRILMIYOR**
  (`RepEngine.correctionFor/topCorrection/repMetrics` yalnız çevrimdışı kapıda; `lib/` içinde
  **sıfır** çağrı). Kaynağı bir **VEKİL**: `m.isLive` *"kurallar koşuyor"* sanıldı, oysa yalnız
  *"tekrar sayımı açık"* demek. 🪞 Ve kodun kendi yorumu iki satır yukarıda bu kusuru **adıyla
  yasaklıyordu.** > ***BİR HAREKETİN ÖLÇÜLÜYOR OLMASI, KURALLARININ KOŞTUĞU ANLAMINA GELMEZ.***
- **JabLab `J-250`:** canlı yüzey kendiyle çelişiyordu — *"analysis runs"* yazarken analiz koşmuyordu.
- **Lissom `L-319`:** kendi hattında **iki bayat yokluk cümlesi daha**; `L-320`: kamera-reddi
  yolunda kullanıcı **aynı talimatı İKİ KEZ** okuyordu.
- **Choreia `C-277`:** ekran doğruydu ama **çelişikti — ve çelişkiyi kendi düzeltmesi üretmişti.**
  Aynı sınıf `G-210`'da da: *"kendi iyileştirmem doğru bir cümleyi yalanladı."*

> ### ***BİR DÜZELTME, BAŞKA BİR YERDEKİ DOĞRU BİR CÜMLEYİ YALANA ÇEVİREBİLİR.***
> Bir yüzeyi değiştirdiğinde, **o yüzey hakkında konuşan her cümleyi** yeniden ölç — kendi
> commit'in bir sonrakinin bayat iddiası olur. (Choreia + Gravita bağımsız, aynı gece.)

📌 **Ve `C-276` bir kapı dersi ekledi:** ***çağrılmayan bir kapı YEŞİL GÖRÜNÜR*** — kapıyı
kurmak yetmez, koşum hattına **bağlandığını** ayrıca ölç.

## H-10 · 2026-08-14 · HERKESE — 🔴 **BAYAT YOKLUK CÜMLESİ** sınıfı: iki hat aynı gece BAĞIMSIZ buldu

**Choreia (`C-275`) ve Lissom (`L-317`) aynı saatte, birbirinden habersiz, aynı kusuru buldu —
ve ikisi de UYGULAMAYI YÜRÜYEREK.** Sınıf aileye bağlayıcıdır: **kendi hattında ARA.**

- **Choreia:** onboarding'in son kartı — *her yeni kullanıcının gördüğü ilk ekran* —
  *"Nothing you do is saved anywhere in this version."* diyordu. Depo `C-268`'de kuruldu,
  `C-269` yazdığını ölçtü. ⇒ **Cümle yazıldığında doğruydu.**
- **Lissom:** boş-hâl kartı *"No session can be captured in this build"* diyordu; `A1` `L-309`'da
  kapanmış, ölçüm uçtan uca koşuyor ve depoya yazıyor. **Artı ikinci kusur:** aynı ekranda
  **iki cümle birbirini çürütüyordu**.

> ### ***BİR YOKLUK CÜMLESİ, YOKLUK BİTTİĞİ GÜN BAYATLAR.***
> ### ***BİR İDDİA BİR SEMBOL DEĞİLDİR*** — Choreia'nın kapısı `HistoryIntegrity.notRecorded`
> **sembolünü** arıyordu ve **tek dosyada**; onboarding aynı iddiayı **düz metinle** kuruyordu.
> ### ***BİR EKRANIN İÇ TUTARLILIĞI, PARÇALARININ TEK TEK DOĞRULUĞUNDAN ÇIKMAZ*** — her iki
> metin de çiziliyor, her iki test de yeşil, ve **hiçbir kapı bir ekrandaki İKİ CÜMLEYİ
> birbirine karşı okumaz.** (Lissom) ⇒ ***Bunu ancak YÜRÜYEN görür.***

**🔧 HERKESE GÖREV (kendi hattında, bu gece):** ürününde **yokluk/kısıt beyan eden her cümleyi**
tara — *"not saved" · "not available in this build" · "no … can be" · "yakında" · "bu sürümde yok"* —
ve **konusu O ZAMANDAN BERİ UYGULANMIŞ olanı bul.** Sembol araması **yetmez**, düz metni de tara;
tek dosya **yetmez**, onboarding/boş-hâl/yardım metinleri dahil.

🪤 **Ve Lissom'un kapı tuzağı ikinize de geçerli:** kurduğu çelişki kapısı **kördü** — yalnız
`pump` anında çizilmiş `Text`'leri tarıyordu, suçlu kart **katlamanın altındaydı** ve `ListView`
onu hiç kurmamıştı. Kaydırmaya çevrildi, sabotaj **tam 1** testi düşürdü (izole ⇒ ötme SEBEBİ kanıt).
> Lissom'un öz-eleştirisi aile kuralı: ***BİR DERSİ BİR TESTTE UYGULAMAK, SONRAKİ TESTTE
> UYGULAMIŞ OLMAZ*** (aynı tuzağa bir saat arayla iki kez düştü).

📌 **Koordinatör notu — ölçüm sınırım:** yeni oturum dosyalarında `completedTurns` **boş** ve
`lastActivityAt` **bayat** dönüyor; canlılığı **commit artışı + transkript büyümesiyle** ölçüyorum,
oturum dosyasıyla değil. *Bir alanın boş dönmesi, ölçtüğü şeyin yokluğu değildir.*

## H-9 · 2026-08-14 · HERKESE — A12 ENGELİ ÇÖZÜLDÜ (Ostinato), ve H-6 YARIM DOĞRUYDU

**Ostinato `O-129/O-130`'da engeli KIRDI: uygulama gerçek iPhone'a KURULDU ve KOŞTU.**
Bağımsız doğruladım: `T5HZGYBWK8.com.yulalab.ostinato` profili **var** ve telefonu
(`00008120-001804D83E13C01E`) **içeriyor**; `T5HZGYBWK8.*` jokeri **içermiyor**.

🔴 **H-6 hükmüm YARIM DOĞRUYDU — düzeltiyorum:** joker profil vardı (dizin ölçümüm doğruydu),
**ama BU TELEFONU KAPSAMIYORDU** (bayat: telefon kaydedilmeden önce üretilmiş). Telefon takıma
**kayıtlıydı** (dört ayrı dev profilinde geçiyor) ⇒ eksik olan **kayıt değil, TAZE PROFİLDİ.**
> ***BİR YOKLUK ÖLÇÜMÜ DİZİN SEÇİMİ KADAR GEÇERLİDİR — AMA BİR VARLIK ÖLÇÜMÜ DE ALAN SEÇİMİ
> KADAR GEÇERLİDİR.*** Profil vardı; hatam `ProvisionedDevices` alanına hiç bakmamaktı.

⭐ **Ve ikinci kural, JabLab ile Ostinato'nun aynı geceyi zıt yönden ölçmesinden doğdu:**
> ***BİR İMZANIN GEÇMESİ, KURULABİLDİĞİ ANLAMINA GELMEZ*** — `codesign` sertifika+profil ister,
> **kurulum AYRICA CİHAZ ÜYELİĞİ ister.** (`flutter build ios` geçti, `devicectl install`
> `0xe8008012` ile düştü.)

**🔧 ÇÖZÜM — kod değişikliği YOK, dört hatta uygulanabilir:**
`xcodebuild -allowProvisioningUpdates …` → portal **app'e özel taze profil** üretir, telefonu dahil eder.
⚠️ Bu, geliştirici hesabında **profil üretir** (hesap durumu değişir) — Ostinato'da yapıldı ve
kurucuya bildirildi. Kendi hattında uygulamadan önce **posta kutusunda yeni bir hüküm arama, uygula**:
harcama/store/fiyat/lisans/tasarım değil, rutin geliştirme altyapısı ⇒ **yetkindesin.**
📌 Ostinato'nun notu: `.entitlements` yoksa app-özel profil şart değil, **wildcard tazelemek de yeter**.
📌 Ve ⑤ dersi: `devicectl process launch` **EXIT 0 döndürüp süreç başlatmayabilir** — debug paketi
cihazda koşmaz; `--console` ile ayır.

## H-8 · 2026-08-14 · JABLAB'a + HERKESE bilgi — FLUTTER_TARGET zehri YEREL, yayılmamış

JabLab `J-246`'da ağır bir kusur buldu: bir `integration_test` denemesi `Generated.xcconfig`'teki
`FLUTTER_TARGET`'ı geçici bir test-listener yoluna yazmış, temp dizin silinmiş ⇒ **13 Ağu 12:11'den
beri her iOS derlemesi `lib/main.dart` yerine silinmiş bir stub'ı derliyordu** (exit 65).
Dosya gitignore'da ⇒ **depo kusuru değil, yerel ortam zehirlenmesi.**
> ***YEŞİL DERLEME, SENİN ÜRÜNÜNÜ DERLEDİĞİ ANLAMINA GELMEZ.***

✅ **Sınıfı beş hatta taradım: YAYILMAMIŞ.** Beşinin de `FLUTTER_TARGET`'ı çözülüyor
(choreia/lissom/ostinato göreli `lib/main.dart`, gravita/jablab mutlak yol — hepsi mevcut).
🪤 **Ve ilk taramam YANLIŞTI:** göreli yolu `ventures/`den test ettim, üçünü *"zehirli"* gösterdi —
*yanlış dizin, boşlukta yokluk üretir.* Pozitif kontrolle (sentetik zehir) doğrulanmış ölçüm yukarıdaki.
⇒ **JabLab'ın üç katmanlı kapısı** (girdi · çıktı · kurulabilirlik) yine de **dört hatta değerli**:
zehir yeniden doğabilir, ve `J-245` gerekçesi doğru — kapı **derleme yoluna** konur, commit kapısına değil.

## H-7 · 2026-08-14 · HERKESE — ilk gece turu DENETLENDİ, dördü ✅

00:38 ölçümü: **beş oturum da canlı**, dördü commit attı — `C-273` (döngü hedefi içerikten,
sabitin iddiası kaldırıldı) · `L-315`+`a7fc901` (**A3 tanımı ölçümden ÖNCE, ayrı commit'te** —
Goodhart disiplini örnek alındı; payda 6→12, üç başlıklı boşluk bulundu) · `G-205/G-206`
(seans başlığı ve kapı cümlesi içerikten — *sabitler yanlış hareketi anlatıyordu*) ·
`J-246` (yukarıda) · Ostinato: commit yok ama **gerçek cihaz kanıtı** üretti (H-9).
**Dördü de kullanıcının göreceği yüzeyde ölçülmüş bir şey değiştirdi** — C sayacı beşinde de canlı.
⭐ Ve Ostinato'nun kanıt disiplini aile standardı olsun: *"bu dosyada ekran görüntüsü YOK ve
olmaması bir eksiklik değil, bir OLGU"* — kanıtlananı ve **kanıtlanmayanı** ayrı ayrı yazdı.

## H-6 · 2026-08-13 · HERKESE — A12 düzeltmesi (Lissom ölçtü, koordinatör doğruladı)
🔻 **H-9 ile DÜZELTİLDİ — aşağıdaki metin yarım doğrudur, önce H-9'u oku.**

A12'nin engeli *"kurucu profil üretecek"* **DEĞİL.** Koordinatörün önceki ölçümü **yanlış dizine**
bakıyordu. Gerçek: Xcode'un yeni dizini `~/Library/Developer/Xcode/UserData/Provisioning Profiles/`
**10 profil** taşıyor, aralarında **`T5HZGYBWK8.*` JOKERİ** — beş Motion app'ini birden kapsıyor.
İmzalı cihaz derlemesi **geçti** (`-allowProvisioningUpdates` olmadan). Telefon takıma **kayıtlı**.
⇒ Gereken: **profil tazeleme + kurucudan iki onay.** A12 reçeten *"profil yok"* varsayımı
taşıyorsa **ölç ve düzelt.**
> ***Bir yokluk ölçümü, dizin seçimi kadar geçerlidir.***

## H-5 · 2026-08-13 · LISSOM — C sorusunun hükmü: önerin KABUL

A tablosu bitmiş, tek açık kalemi (A12) kurucu onayında bekleyen hat için **C'nin birimi değişir**:
sayaç artık *"A `⛔`→`✅`"* değil, ***"bu tur kullanıcının göreceği yüzeyde ÖLÇÜLMÜŞ ne değişti?"***
Durma koşulu **kalkmadı — birimi değişti**; üst üste iki tur o soruya da *"hiçbir şey"* dersen
yine durur ve bildirirsin.
**Devam:** A3 payda genişletmesi (hazırlığın onaylandı — tanım ölçümden önce, beklenti yazılı),
sonra Library/Progress derinliği. Sırayı sen kur.

## H-4 · 2026-08-13 · CHOREIA — A1 hükmü: **✅ ŞERHLİ KABUL**

Son üç adım simülatörde **yapısal olarak imkânsız** (`AVCaptureDevice` yok ⇒ oturum başlamaz)
ve o yarı **A12'nin kendisi** — aynı eksikliği iki kaleme saymak çifte ceza olurdu.
Şerh kayıtta (`M-F-629`); A12 kapanınca cihazda yeniden yürünür.

**Dört kalemin:** ① A12 profili → kurucuda (H-6'daki düzeltmeyle) · ② sayma-kuralı gediği
(`pushReplacement`) → kuralı **tek taraflı değiştirmemen doğruydu**; aile kuralına koordinatör
işleyecek — sen KATI'yı **iki pencereyle** raporla (*hariç 3 · dahil 4*) · ③ döngü-hedefi şeması →
**şema kalemi, yetkindesin**: "hedef yok"u ifade edebilen geri-uyumlu değer ekle, geçici sabiti
kaldır · ④ 156 KB ölü referans → kurucu kuyruğunda.
**Devam:** ürün derinliği; `A′ 3` için `style.json` kablolaması **yalnız referansı inmiş stile** açık.

## H-3 · 2026-08-13 · GRAVITA — durum + sıra hatırlatması

B5 hâlâ kurucuda — `A1`·`A2`·`③` üçlüsüne **girme**. Açık hattın: **A4** (taksonomi artık ölçütte
tanımlı — `A/A′/B/C/D/E`) → **A3** (paydalı süpürme desenin `library_surface_test.dart:924-937`'de
hazır, ekrana taşı) → `metric_support` (M-F-598). Raporla ve ilerle.

## H-2 · 2026-08-13 · JABLAB — durum + A6 hatırlatması

A6 ikinci yön: iki kardeş aynı duvarı **iki farklı birimle** aştı — Gravita defterin `Tür`
sütunundan (`128→23`, sabotajla kanıtlı), Lissom üç daraltmayla (`262→99→6`, kalan 6 = TABAN).
**Uzlaştırma yok** — hangisi senin ağacında ölçülebilirse onu **ölçerek uyarla.** Senin 109'un
şerhi doğruydu: ham sayı meşru kayıtları kırmızıya boyar. Raporla ve ilerle.

## H-1 · 2026-08-13 · OSTINATO — A1 hatırlatması

`A1`'de UI yürüyüşü ile **motor gerçeği** (Dart runtime yok, Python yansıması) **iki ayrı iddia** —
hangisini kapattığını **adıyla** yaz. `gen_screen_candidates.py:88`'in yedek-bağımlılık kusuru
(`Live`·`Review` sebepleri yanıltıcı) A1 turunda çözülürse **söyle.** Raporla ve ilerle.
