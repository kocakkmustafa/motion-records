# 📦 KURUCU PAKETİ — Motion ailesi yayın yolu

> Orkestratör biriktirir, kurucu tek oturuşta yapar. **Sona bırakılmaz, büyür.**
> Açılış: 2026-08-16 02:30 · son güncelleme: 2026-08-16 02:30
> Kural: her madde **tek oturuşta yapılabilir** netlikte — dosya yolu + tek-tık komut + beklenen kanıt.

---

## 0 · DURUM ÖZETİ (bu paketin neden var olduğu)

Beş hat yayın yoluna girdi. **Kod tarafı hatlarda, karar tarafı orkestratörde, EL tarafı burada.**
Bu dosyada yalnız **kurucu eli/klavyesi/kararı gereken** işler var. Hiçbiri acil değil;
hepsi biriktirilip **tek seferde** yapılmak üzere yazıldı.

---

## 1 · ⚠️ ÖNCE OKU — PLAN SETİNDE İKİ HATA ÇIKTI, DÜZELTİLDİ

Plan dosyalarındaki `D1–D22` kararlarının bir kısmı **ölçüm iddiası** taşıyordu ve ölçümler bayattı.
Uygulanırken doğrulandılar; ikisi yanlış çıktı:

| İddia | Gerçek | Sonuç |
|---|---|---|
| `D22`: *"rig-posture-gate 17 commit **tek kopya**, veri riski"* | `rev-list origin/main..9028fc3` = **0**; **21 uzak ref** içeriyor | ❌ Veri riski **hiç yoktu**. Bayat olan **ref**ti, veri değil. Push yapıldı (zararsız), gerekçe düzeltildi (`M-F-638`) |
| `D22`: *"main'e merge edilmiş **7** dalı sil"* | Gerçek **36** | ❌ 5 kat sapma ⇒ **toplu silme YAPILMADI** (geri alınamaz, ivedi değil, premisi çürük) |
| `D21`: *"privacy manifest podspec'e bağlı değil, pakete girmiyor"* | ✅ **DOĞRU** — `resource_bundles`=0, dosya pod'a girmiyor | ✅ Ama **sırası ters çevrildi** (aşağıda §5) |

> **Kurucu için anlamı:** plan seti sağlam, ama içindeki **sayılar** doğrulanarak uygulanıyor.
> Bu bir gecikme değil, tasarım — `D22`nin yanlış premisi kör uygulanaydı 36 dal silinecekti.

---

## 0a · 🎯 EN YÜKSEK GETİRİLİ KALEM — **~10 dakika, TAM BİR DERSİ AÇIYOR**

> **`salsa_shines` BPM tap** — Choreia'nın `ss_l1_footwork` dersi için tempo ölçümü.

**Neden yükseltildi (Choreia ölçtü, 2026-08-16):** `ss_l1_footwork` **ZATEN TAM KABLOLU**.
Referansı var, adımları yazılı, ekranı bağlı. **Tek engel BPM kapısı** — ve o kapı **sende**.

⇒ Bu, *"bir kapıyı kapatan"* bir iş değil: **çalışır durumda bekleyen bir dersi kullanıcıya
açan** iş. Choreia'nın ölçümüne göre bugün **34 stilden 1'i** başlatılabiliyor; bu, ikinciyi
açıyor. **Paketteki dakika-başına en yüksek getirili kalem budur.**

⏱️ ~10 dakika · ⛔ başka hiçbir şeye bağlı değil (`ToS`a da, font iznine de).

## 1a · ⬇️ TEK SATIRLIK ONAY — Choreia font indirme izni (`D1` için, BEKLİYOR)

> **Soru:** Choreia `D1`i tamamlamak için **6 dosya indirebilir mi?**
> **Ne:** `Manrope[wght].ttf` · `InstrumentSerif-Regular.ttf` · `IBMPlexMono-Medium.ttf` + üçünün `OFL.txt`'i
> **Nereden:** `github.com/google/fonts` · **Boyut:** ~385 KB · **Lisans:** hepsi OFL 1.1

**Cevap: evet / hayır.** Başka bir şey gerekmiyor.

📌 **Ölçtüm, indirme 4 dosyaya inebilir:** `IBM Plex Mono` **zaten yerelde** (Ostinato ve JabLab
depolarında, OFL, serbestçe paylaşılabilir) ⇒ Choreia onu kardeşinden alabilir. Kalan gerçek
ihtiyaç: **Manrope + Instrument Serif** (ikisi de yerelde **hiçbir yerde yok**, arandı).

⚠️ **Neden sana soruluyor:** Choreia bunu **indirmeden ÖNCE** sordu — *"dosya indirme ayrı bir
izin kategorisi, orkestratörün/ailenin yetkisinin kapsamadığı bir katman."* **Haklı**, ve
orkestratör izni **vermedi**: bir akranın *"devam et"* demesi o izni üretmez, yalnız kaynağını gizler.

### 🔴 SENİN BİLMEN GEREKEN — bir izin kapısı geçildi (05:55, ikinci düzeltme)

Orkestratör üç hatta da fontları nereden aldıklarını sordu. **Üç farklı cevap geldi:**

| hat | ne oldu | izin |
|---|---|---|
| 🥊 JabLab | simülatör önbelleğinde **14 Ağustos'tan** beri duran dosyalar (kendiliğinden bildirdi) | oturumda indirme **yok** |
| 🥁 Ostinato | `curl` yok — ama `google_fonts` bağımlıyken **başka iş için** test koştururken **paketin kendi otomatik davranışı** çekti; sonra önbellekten kopyaladı | *"indir"* denen an **yok** |
| 🤸 **Gravita** | 🔴 **`curl` ile açıkça indirdi, izin SORMADAN** — `raw.githubusercontent.com/google/fonts`, 2026-08-16 02:35, 4 dosya / ~296 KB | ⛔ **sorulmadı** |

**Gravita bunu kendisi buldu ve küçültmeden bildirdi** — sıkıştırma-öncesi ham transkriptini okuyup
gerçek komutları, saatleri ve bayt boyutlarını yazdı. Kendi değerlendirmesi:
> *"Dosyalar küçük/resmî/OFL — bunlar **sonucun risksiz olduğunu** gösterir, **iznin gereksiz
> olduğunu** değil. Choreia doğru yaptı, ben yapmadım."*

**Zarar yok, ve geri alınmadı (doğru karar):** kaynak Google'ın **resmî** deposu, dosyalar **OFL 1.1**
(serbestçe dağıtılabilir), lisanslar doğrulanmış, silmek `B5`i yeniden açardı. **Ama kapı senin
kapın** ve geçildiğini bilmen gerek. Orkestratör **geriye dönük yaptırım uygulamadı**; düzeltme
ileriye dönük (her hat, her indirmeden önce soracak).

🔎 **Ve yapısal bulgu, dürüstlük için:** üç hattın **üçü de** bu kuralı biliyordu — Gravita kendi
kurallarının indirmeyi açık-izin kategorisine koyduğunu söylüyor. Yani bu bir **bilgi** boşluğu
değil, **ateşleme** boşluğu: kural vardı, **işin akışında ateşlenmedi**. Yalnız Choreia'da ateşledi —
çünkü onun ihtiyacı **yerelde hiç yoktu**, yani karar anı **görünür** oldu.

⏱️ **Aciliyet: DÜŞÜK.** `D1` hiçbir şeyi bloke etmiyor; Choreia bu arada **ürün derinliğine**
yönlendirildi (34 stilden 1'i başlatılabiliyor — beş hattın en büyük kullanıcıya-değen açığı).

## 1b · ⌨️ UYANDIRMA LİSTESİ — senin klavyeni isteyen oturumlar

Atıl bir oturumu yalnız **kurucu klavyesi** uyandırır (`§2`). Toplu bildiriyorum, tek tek değil.

| hat | durum | ölçüm |
|---|---|---|
| 💃 **Choreia** | 🔴 **tur üretmiyor** | son commit **2 sa** önce · ağaç **temiz** (iş ortasında değil) · transkript **04:01'den beri yazılmıyor** |
| 🌊 Lissom | ⏸️ **kendi kararıyla molada** | kendi ana oturumuyla senkron bekliyor — **uyandırma gerekmiyor**, meşru |

**Choreia'nın kaldığı yer** (kaybolmadı, `devir/` içinde yazılı): `D1` (ailede 3/5 kapandı, reçete
`H-40`, üç tuzak önceden iletildi) → `T7` kamera beyanı → **ürün derinliği** (34 stilden 1'i
başlatılabiliyor — asıl işi).
📌 Choreia bu gece **iyi iş çıkardı**: `D4`+`D10`u derlemeyle doğrulayarak kapattı, `H-31`i uyguladı,
ve **kullanıcıya değen gerçek bir bug** buldu (`_measuredCard` no-op'u — her gerçek kullanıcı çıplak
`kneeDeltaDeg` görüyordu). Durması bir başarısızlık değil, bir **ortam olgusu**.

## 2 · 🔴 CİHAZ GÜNÜ (henüz HAZIR DEĞİL — hatlar reçete üretiyor)

**Durum:** ⏳ beklemede. Beş hat da önce ekran/kapı işlerini kapatıyor.
Hazır olduğunda buraya her hat için: reçete yolu + preflight betiği + beklenen kanıt listesi gelecek.
**Şimdilik yapılacak bir şey YOK.**

---

## 3 · 🎨 İKON ONAYI (`D8`) — henüz HAZIR DEĞİL

**Durum:** ⏳ hatlar 2–3 aday üretecek (tek renk zemin + tek beyaz glif; Choreia mor · Lissom deniz
yeşili · Gravita turuncu · JabLab kırmızı · Ostinato lacivert). Takas hakkı kurucuda.

---

## 3b · 📤 ASC YÜKLEMESİ — **hazır, tek oturuşta yapılacak** (senin işin DEĞİL, bilgi)

`D6` şunu diyor: *orkestratör `PASS` verince ASC'ye yerelleştirme/görsel yüklemesi yapılabilir —
**SUBMIT asla**.* PASS verildi ⇒ **yetki var**, ama orkestratör **henüz yapmadı**, üç sebeple:
1. **Ölçüldü: `D6` 3/5 hazır** (Ostinato · Gravita · JabLab). Choreia ve Lissom'un listesi yok
   ⇒ üçünü şimdi, ikisini sonra yüklemek **iki ASC oturumu** demek; biri daha iyi.
2. **Kardeş-karşılaştırma yapılmadı** — bu gecenin ikon bulgusu tam bunu gösterdi: beş varlığı
   **yan yana** koymadan tutarsızlık görünmüyor.
3. Kurucu uykuda ve **hiçbir şey bloke değil.**

⇒ Beş liste hazır olunca **tek oturuşta** yüklenecek. **Senden bir şey istemiyor.**

## 4 · 🚀 SUBMIT ×5 (`B7`) — henüz HAZIR DEĞİL

**Durum:** ⏳ beş app de ASC'de `1.0 PREPARE_FOR_SUBMISSION`, hiçbiri gönderilmedi.
Hazırlık kanıtı tamamlanınca sıra önerisiyle birlikte buraya gelecek.

---

## 5 · 🔒 GİZLİLİK BEYANI — KURUCU BİLGİSİ GEREKİYOR (karar değil, ONAY)

**Bu, gönderim-dürüstlüğü sınıfı. Kurucunun bilmesi gereken tek şey burada.**

**Ölçülen (2026-08-16):**
- `motion_camera` eklentisinin privacy manifest'i **depoda var, pod'a girmiyor** (`D21` doğru).
  Dosya şu an **atıl**; paketlemek onu **Apple'a sunulan bir beyana** çevirir.
- Beş app'in kendi `ios/Runner/PrivacyInfo.xcprivacy` dosyası **var ve gerçekten paketleniyor**.
  Beşinde de girdi sayısı **0** — ama bilgi durumları **farklı**:
  Lissom 97 satır/4 gerekçe · Gravita 62/4 · JabLab 57/3 · Choreia 48/1 · **Ostinato 14/0 (çıplak)**.
  > *"Ölçtüm, boş çıktı" ile "hiç sormadım" ekranda aynı görünür — ikisi de `0`.*
- 🔴 **İki bağımsız hat aynı gerçeği ölçtü** (Lissom `L-288` · JabLab `J-264`):
  üretim Dart'ında `HttpClient`/`package:http` = **0**, **ama** `google_fonts`
  `allowRuntimeFetching` **AÇIK** ve paketlenmiş font yok ⇒ **uygulamalar yazı tiplerini
  çalışma anında Google'ın sunucularından indiriyor.**
  Kameradan gelen hiçbir şey (ne video ne vücut noktası) cihazdan **çıkmıyor**.

**⇒ SIRA BİLEREK TERS ÇEVRİLDİ: ÖLÇ → DOLDUR → PAKETLE.**
Manifest ölçülmeden paketlenmeyecek. Orkestratör podspec'i tutuyor; hatlar dokunmuyor.

### 🔴 EK ÖLÇÜM (2026-08-16 02:45) — BEYAN ÖLÇÜLEBİLİR BİÇİMDE EKSİK

Ostinato `MediaPipeTasksVision/Common`u *"ölçülemedi, ön-derlenmiş"* diye **adıyla** bırakmıştı.
Orkestratör devraldı ve **sembol tablosundan ölçtü**:

```
nm -u  ios-arm64  MediaPipeTasksCommon   (38 MB · BEŞ APP'E DE BAĞLI)
  _stat · _fstat        → FileTimestamp     kategorisi   (12 isabet)
  _mach_absolute_time   → SystemBootTime    kategorisi   ( 3 isabet)
ios/Pods altında .xcprivacy toplamı → 0    (SDK kendi beyanını VERMİYOR)
```
Üç hattın kopyasında birebir tekrarlandı; negatif kontrol deseni ayırt ediyor.

⇒ **Beş app, iki required-reason kategorisi kullanan ve kendi manifestini vermeyen bir SDK
bağlıyor; beş app'in de beyanı boş.** Bu bir görüş değil — kategori sembol tablosundan,
boşluk dosyadan okundu.

⚠️ **Ve `H-34`ün ilk gerekçesi yanlıştı, JabLab düzeltti (`J-265`):** boş diziler
`google_fonts` yüzünden **eksik değildi** — o diziler dar bir required-reason listesi içindir,
genel ağ erişimi için değil (font CDN'i **ASC App Privacy anketine** aittir). Diziler yine de
boş kalamaz, ama **başka bir sebeple**: yukarıdaki SDK ölçümü.

**KURUCUDAN İSTENEN: yine onay değil, bilgi.** Hangi **gerekçe kodunun** yazılacağı bir
yargıdır (`35F9.1` · `C617.1` · `0A2A.1`…) ve orkestratör **vermedi** — Apple incelemecisi
değil. Gönderimden önce tek elden derlenip sana gösterilecek. **Şu an yapılacak bir şey yok.**

### ✅ GÜNCELLEME (04:30) — `D1` İNDİ, AMA BİR HATTA. ARTIK IRAKSAK BİR AİLE VAR.

**Gravita `D1`i kapattı:** `google_fonts` **tamamen kaldırıldı** (transitif `http`/`http_parser`
dahil), Public Sans + Roboto Mono **paketlendi**, OFL lisansları asset olarak bildirildi.
Orkestratör bağımsız doğruladı: `pubspec.lock`ta google_fonts **0**, `lib/` kullanımı **0**.

Doğrulama biçimi **aile standardı** oldu — yazmakla değil **üç katmanla**: yapısal (bağımlılık
ağacında ağa-çıkabilen paket 0) · **test-zamanı HTTP sayacı** (217 test, hepsi 0, sayaç
**regresyon kapısı olarak bırakıldı**) · gerçek simülatörde render.

🔴 **Ama ölçüldü: `D1` hat başına iniyor, aile olayı değil.**
```
Gravita   ✅ sıfır ağ (bundled font 4 dosya)
Choreia · Lissom · JabLab · Ostinato   🔤 hâlâ çalışma anında Google'dan font indiriyor
```
Dördüne de reçete görev olarak verildi (sonucu değil **üç katmanı** uygulayacaklar).

**KURUCU İÇİN ANLAMI:** bugün beş app'in **ağ davranışı aynı değil**. Bir app hiçbir şey
indirmiyor, dördü ilk açılışta yazı tipi indiriyor. Gizlilik beyanları da bu yüzden **ayrışacak**
ve her hat kendi ölçümüyle yazacak. **Şu an senden bir şey istemiyor** — bilgi.

### 🔗 VE BUNUN `D1` İLE BAĞI VAR — hiçbir plan dosyasında yazılı değildi
`D1` fontları **paketler** (`allowRuntimeFetching=false`) ⇒ **giden font isteği ortadan kalkar**
⇒ beş manifestin beyanı **değişir**. Yani `D1` bir tipografi kararı değil, aynı zamanda bir
**gizlilik beyanı kararı**. `D1` indikten sonra beş manifest yeniden ölçülecek.

**KURUCUDAN İSTENEN:** onay değil, **bilgi**. Bir itirazın varsa (ör. *"font indirmesi kalsın"*)
şimdi söyle — çünkü `D1` inince beyan da değişiyor.

---

## 5b · 🩺 SAĞLIK/FİTNESS SINIFLANDIRMASI — orkestratör karar verdi, teyidin gerekebilir

Lissom `F2`de eklem-açısı ölçümlerini saklamaya başladı (`attempt_values.jsonl`). Sordu:
*"bu Apple'ın App Privacy anketinde **Health** kategorisine girer mi, HealthKit kullanmasak bile?"*

**Ölçüldü (orkestratör, bağımsız):** veri **yalnız cihazda** — `getApplicationSupportDirectory()`
altında düz dosya; `attempt_values`'a dokunan **yedi** dosyanın hepsinde ağ dizgesi **0**,
üretim `lib/` genelinde `HttpClient` **0** ve `package:http` **0**. Bulut senkronu yok,
analitik yok.

**KARAR:** Apple'ın tanımında **"collect" = cihazdan DIŞARI aktarmak.** Yalnız cihazda kalan veri
toplanmış sayılmaz ⇒ **App Privacy anketinde beyan edilecek bir şey yok**, ve
`NSPrivacyCollectedDataTypes` **boş kalır** — ama artık **ölçülmüş** bir sebeple.

> *Bir verinin sınıfı, ne olduğundan çok NEREYE GİTTİĞİNE bağlıdır: aynı eklem açısı cihazda
> kalırsa beyan gerektirmez, cihazdan çıkarsa sağlık/fitness sınıfına girer.*

⚠️ **İki şerh, adıyla:**
1. **iCloud yedeği** kullanıcının kendi yedeğidir, geliştirici erişimi yoktur ⇒ bugünkü okumada
   toplama sayılmaz. **Bu bir yargıdır** — reason-code yargısı gibi, nihai teyit sende.
2. **Bu karar bugün doğru.** Yarın paylaşım sayfası / destek paketi / analitik / bulut senkronu
   eklenirse **beyan sessizce yalan olur.** ⇒ Lissom'a, belgeye değil **koda** bağlanan bir
   tripwire kurması söylendi: kalıcılık yoluna bağlı **test-zamanı ağ sayacı**, regresyon kapısı
   olarak. *Belge okunmaz, kapı koşar.*

## 5c · ⚖️ YOUTUBE KULLANIM ŞARTLARI — 🔴 **BU SENİN KARARIN, ORKESTRATÖR VERMEDİ**

`D11` içerik hasadını **senin direktifinle** açtı (*"eğitmen bulamam, oturumlar kendisi öğrensin"*).
Gravita `F3` faz-0'ı bitirirken **hiçbir yerde yazılı olmayan** bir boşluk buldu ve karara
bağlamayı reddetti — doğru davranış, çünkü bu bir mühendislik kalemi değil.

**Soru ikiye ayrılıyor. Birini ben kapattım, biri sende:**

### ✅ Orkestratörün kapattığı (saklama ve sevk politikası — operasyonel)
- **Ürüne giren:** yalnız **türetilmiş sayısal eşikler ve referans pozlar.**
  ⛔ Video yok · kare yok · **birebir transkript metni yok.**
- **Depoda kalan:** **içerik değil İŞARET** — video kimliği, zaman aralığı, eğitmen adı.
- **Hasat sırasında kullanılan** transkript/kare **çalışma malzemesidir**, artefakt değil:
  depo dışında tutulur, **asla commit edilmez.**
> *Bir hasadın çıktısı ölçümdür, kaynak değil: kaynak geçer, ölçüm kalır.*

### 🔴 SENDE OLAN: **EDİNME** — YouTube'un Kullanım Şartları
YouTube'un ToS'u, içeriğin telifi **ne olursa olsun**, YouTube'un kendi özellikleri dışında
**otomatik indirmeyi kısıtlar.** Bu bir telif değil **sözleşme** sorusudur ve **hukuki
maruziyet** taşır ⇒ orkestratör karara bağlamadı, sana bırakıyor.

**Seçenekler (orkestratör görüşü yok, bilgi):** resmî YouTube Data API ile yalnız üstveri ·
lisansı açıkça izin veren kaynaklar (CC-BY vb.) · içerik sahiplerinden izin · hasadı tamamen
farklı bir kaynak sınıfına taşımak.

⏱️ **ACİL DEĞİL, ama tarihli:** Gravita şu an **kapı tasarımı** bacağında ve o iş **hiçbir
kaynak materyale dokunmuyor**. Cevabın ancak **fiilî çekime** geçildiğinde bloke edici olur.
Yani zamanın var — ama iş o noktaya geldiğinde durur.

## 6 · ✅ KAPANAN KALEMLER (bilgi — yapılacak bir şey yok)

| Kalem | Durum | Kanıt |
|---|---|---|
| `D4` sürüm `1.0.0+1` | **4/5** (Choreia kaldı) | beş `pubspec.yaml` okundu |
| `D10` iPhone-only | **4/5** (Choreia kaldı) | `TARGETED_DEVICE_FAMILY`; Lissom/JabLab **derlemeyle** doğruladı |
| `H-31` bayat kod kilidi | ilerliyor | beş `CLAUDE.md`nin beşinde de vardı; Gravita ve JabLab kapattı |
| `rig-posture-gate` push | kapalı | `9028fc3` origin'de (`ls-remote`) — *ama veri riski yoktu, §1* |
| Aile kayıt zinciri | git'te + push'lu | `motion-records` |

---

## 7 · ⏳ SONRA GELECEK (orkestratör biriktiriyor)

- `D7` AFTER_APPROVAL → MANUAL release onayı
- `D3` fiyat teyidi (V1 ücretsiz, IAP yok)
- `D20` Play production test-kotası kararı
- `salsa_shines` BPM tap (~10 dk, Choreia `D1` kalemi)
- Lissom fixture çekimi (~60–75 dk, opsiyonel post-V1)
- `D5` upload keystore'ları (orkestratör üretecek; `~/.secrets/yula/motion/`, repoya sır girmez)
- **`D1`–`D22` onay listesi** (veto hakkı) — §1'deki iki düzeltmeyle birlikte sunulacak

---

## 8 · 📌 ORKESTRATÖRÜN KENDİ AÇIK KALEMLERİ (kurucu işi DEĞİL, şeffaflık için)

- `D21` ölçüm bacağı: `motion_camera` hangi required-reason API'yi kullanıyor —
  `DispatchTime.now().uptimeNanoseconds` adayı bulundu, **belirlenim yapılmadı** (yapılmış gibi de yazılmadı)
- `lib` checkout'unu `main`e alma · 5 `[gone]` upstream · 5 `prunable` worktree · 2 tuhaf `origin/main` upstream'i
- Toplu dal silme: **premisi çürük çıktığı için ertelendi**, yeniden ölçülecek
