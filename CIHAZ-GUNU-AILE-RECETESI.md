# 📱 CİHAZ GÜNÜ — AİLE REÇETESİ (F5/yayın provası, 2026-08-16)

> **Kaynak:** Gravita (`docs/device-day/RECIPE.md` + `tools/device_day_preflight.py`,
> şeması Ostinato'dan — O-160, `7177c55`) + Gravita'nın kendi yayın-provası turu
> (`G-246`/`G-247`, `b2d9020`→`7d67f10`). Ailede **ilk gerçek `flutter build ipa`**
> koşumu Gravita'daydı ve iki duvara **önceden** çarptı — bu dosya o duvarları
> dört hatta taşır.
> **Bu dosya bir KOD DEĞİL bir REÇETE** — her app kendi `tools/
> device_day_preflight.py`sini Ostinato/Gravita'nın şemasından (yalnız `APP_ID`/
> `TEAM_ID`) kurar, kendi deposuna yazar. **Başka bir hattın deposu buradan
> DEĞİŞTİRİLMEDİ** — yalnız bu paylaşılan belge.

---

## Neden bu dosya var — kopya sayısı dersinin doğrudan uygulaması

`H-57` şunu ölçmüştü: bir aracı KOPYALAYARAK dağıtmak, her kopyayı ayrı bir
bayatlık yüzeyi yapar (17 kopya, 7 farklı bayatlık düzeyi). Cihaz günü reçetesi
de AYNI riski taşıyor — her hat kendi `RECIPE.md`sini bağımsız yazarsa, bir
hattın bulduğu tuzağa öteki dört hat **kendi başına** çarpar. Bu dosya o riski
**önceden** kapatıyor: dört tuzak burada bir kez yazılı, her hat kendi
uygulamasında yalnız KOPYALAR — icat etmez.

---

## §0 — "Eşleşmiş" ≠ "bağlı" (orkestratörün ölçtüğü, Gravita'nın turunda)

`devicectl list devices` bir telefonu `available (paired)` gösterebilir **USB'ye
hiç takılı olmadan** — eşleşme KALICI bir durumdur, canlı bağlantı değil.
Orkestratör bunu doğrudan ölçtü (Gravita'nın "gerçek bağlı cihaz" iddiasını
denetlerken):
```
devicectl        →  "Mustafa Kaan iPhone" · available (PAIRED) · iPhone15,3
system_profiler  →  USB'de iPhone YOK
```
**Kablosuz kurulum kilitli/uykudaki telefonda ya düşer ya asılır.** Cihaz gününe
başlamadan önce **ikinci kaynaktan** doğrula:
```bash
system_profiler SPUSBDataType | grep -i iphone
```
Boş dönerse telefon USB'de DEĞİL — yalnız eşleşmiş. Kablosuz kurulum deneme
YERİNE fiziksel kabloyu kontrol et.

## §0b — TEDARİK PROFİLİ: **4/5 HAZIR** (⚠️ ilk ölçüm YANLIŞTI, düzeltildi 2026-08-16 12:00)

> ### 🔴 ÖNCE BİR DÜZELTME — bu bölüm *"beş hatta da 0"* diyordu ve **YANLIŞTI**
> Orkestratör profilleri **tek** dizinde aradı. **macOS onları İKİ yerde tutuyor** ve asıl olan
> ötekiydi. 🤸 Gravita'nın ön-uçuş betiği **ikisine de** bakıyordu ve düzeltti.
> ```python
> PROFILE_DIRS = [
>     Path.home() / "Library/Developer/Xcode/UserData/Provisioning Profiles",  # ← 15 profil (ASIL)
>     Path.home() / "Library/MobileDevice/Provisioning Profiles",              # ← 1 profil
> ]
> ```
> > ***BİR ARAMA TEK YERE BAKIP "YOK" DİYORSA, ÖNCE KAÇ YER OLDUĞUNU ÖLÇ.*** (`H-68`, dizin ekseni)

### 📊 GERÇEK DURUM — iki dizin birden tarandı
| app | profil | kayıtlı cihaz |
|---|---|---|
| 💃 Choreia | geliştirme, 13 Ağu | **4** |
| 🤸 Gravita | geliştirme 13 Ağu **+ Store 16 Ağu** (bkz. `§0c`) | **4** |
| 🌊 Lissom | geliştirme, 14 Ağu | **4** |
| 🥁 Ostinato | geliştirme 13 Ağu **+ Store 16 Ağu** (bkz. `§0c`) | **4** |
| 🥊 JabLab | 🔴 **yok** | — |

⇒ **4/5 hazır ve kurucunun telefonu dördünün de içinde.** 🥊 **JabLab'ın kendi raporu DOĞRUYDU**;
hatalı olan orkestratörün onu *"beşinde de yok"* diye **genellemesiydi**.

```bash
# DOĞRU ölçüm — İKİ dizin birden:
for d in ~/Library/Developer/Xcode/UserData/Provisioning\ Profiles \
         ~/Library/MobileDevice/Provisioning\ Profiles; do
  for f in "$d"/*.mobileprovision; do
    security cms -D -i "$f" 2>/dev/null | grep -q "<app-id>" && echo "VAR: $f"
  done
done
```

### 📊 VE HESAP TARAFI (ASC API, **salt-okunur**) — asıl tabloyu bu veriyor
| bileşen | durum |
|---|---|
| Bundle ID'ler | ✅ **5/5 kayıtlı** (`T5HZGYBWK8`) |
| Sertifikalar | ✅ 4 kimlik, `Apple Distribution` dâhil |
| **Kurucunun telefonu** | ✅ *"Mustafa Kaan iPhone'u"* · iPhone 14 Pro Max · **23 May 2026'dan beri ENABLED** |
| Tedarik profilleri (**hesapta**) | 🔴 **0** — yerelde **4/5 var** (üstteki tablo) |

⇒ **Yalnız 🥊 JabLab'da profil eksik**, ve profil `-allowProvisioningUpdates`'in **kendiliğinden
yarattığı** şeydir — yeter ki **bundle ID + sertifika + kayıtlı cihaz** olsun. Üçü de var.
🎯 Telefon zaten kayıtlı olduğu için cihaz günü **bir cihaz slotu bile tüketmeyecek**.
📌 *Not: ASC API'de `profiles.total = 0` görünmesi normal — Xcode'un otomatik ürettiği profiller
hesap tarafında ayrı listelenmiyor; **yerel** ölçüm otoritedir.*

```bash
# İlk cihaz derlemesinde profili Xcode'un kendisi yaratır:
xcodebuild -allowProvisioningUpdates ...
```

### 🪤 VE İKİ TUZAK — ikisi de bu ailede daha önce ısırdı
1. ⚠️ ***"İmza geçti" ≠ "kurulur".*** Profilin **`ProvisionedDevices`** listesini **ölç** —
   wildcard bir profil bayat olabilir ve telefonu **içermeyebilir**. `codesign` yine de geçer.
   ```bash
   security cms -D -i <profil>.mobileprovision | plutil -extract ProvisionedDevices xml1 -o - -
   ```
2. 🔴 **Kanıt `--release` olmalı.** Debug paketi cihazda `signal 11` ile düşebilir; *"cihazda
   çöktü"* diye rapor edilen şey çoğu zaman **debug paketinin kendisidir**, ürünün kusuru değil.

### ⚖️ VE PROFİL ÖNCEDEN OLUŞTURULMADI — bilerek
Ön koşullar **ölçüldü**, risk düşük; profil yaratmak Apple hesabında **dışa dönük bir mutasyon**
olurdu. > ***BİR RİSKİ ÖLÇEREK DÜŞÜREBİLİYORSAN, ONU BİR MUTASYONLA ÖNLEMEYE ÇALIŞMA.***

🟡 **Tek ölçülmemiş kalem, adıyla:** Xcode'un bu makinede **hesaba giriş yapmış** olup olmadığı.
Sertifikaların varlığı işaret ediyor ama **kanıt değil** — sertifika, çıkış yapıldıktan sonra da
keychain'de durur. İlk derleme bunu net bir hatayla söyler; düzeltmesi bir dakikadır.

---

## §0c — İKİ profil, YALNIZ biri cihaza kurulabilir: "en yeni" ≠ "doğru" (Gravita ölçtü, 2026-08-16)

§0b'nin ölçtüğü an **hiç profil yokken**di (henüz build yapılmamış). Bir hat
GERÇEK bir yayın provası (§2) koştuktan SONRA farklı bir durum ortaya çıkar:
aynı app-id için ARTIK İKİ profil vardır — bir GELİŞTİRME (`ProvisionedDevices`
dolu) ve bir DAĞITIM/"Store" (`ProvisionedDevices` TASARIM GEREĞİ boş, App
Store profili cihaz listesi istemez).

Ölçüldü (Gravita, `com.yulalab.gravita`, `G-253`):
| Profil | Oluşturma | `ProvisionedDevices` |
|---|---|---|
| `iOS Team Store Provisioning Profile` | 2026-08-16T03:47 (yayın provası turuyla aynı pencerede) | 0 |
| `iOS Team Provisioning Profile` | 2026-08-13T21:58 | 4 (kurucu içinde) |

Ostinato/Gravita şemasındaki `find_<app>_profile()` "aynı app-id'liler
arasında en yeni `CreationDate`" kuralıyla seçim yapıyor — bu YENİ durumda
YANLIŞ profili (Store) seçip cihazı "kayıtlı değil" diye YANLIŞ ALARM
veriyor, GERÇEK durum temizken.

> **BİR PROFİLİN "EN YENİ" OLMASI, ONU CİHAZA KURULUM İÇİN "EN İYİ" YAPMAZ
> — İKİSİ FARKLI EKSENLER.**

**Canlı doğrulandı, varsayımsal DEĞİL:** orkestratör Ostinato'nun kendi
Store profilini de ölçtü — 2026-08-16T03:35:48, `ProvisionedDevices` 0.
Ostinato'nun düzeltilmemiş betiği ŞU AN koşulsa aynı yanlış alarmı üretir.

**Düzeltme:** adayları önce `ProvisionedDevices` DOLU olanlara daralt,
YALNIZ o alt kümede en yeniyi seç; cihaz-kapsamlı profil hiç yoksa bunu
ayrı ve daha kötü bir durum olarak raporla (sessizce "profil yok" ile
karıştırma). Gravita'da uygulandı+doğrulandı (`tools/device_day_
preflight.py`, `G-253`) — bir kez yayın provası koşturmuş HER hat için
aynı koşulda aynı yanlış alarm beklenir; kendi `find_<app>_profile()`ini
kontrol et, yalnız `CreationDate` mi kullanıyor.

---

## §1 — Ön-uçuş betiği: `security find-identity` ÖNCEDEN, tahmin değil

Her hat kendi `tools/device_day_preflight.py`sini kurarken üç şeyi **ölçer,
varsaymaz** (Ostinato/Gravita şeması):
1. `security find-identity -v -p codesigning` — kaç geçerli kimlik var.
   ⚠️ **Bu listede en az İKİ SINIF görünür** — `Apple Development` VE `Apple
   Distribution`/`iPhone Distribution`. İkisinin VARLIĞINI önceden bilmek, §2'nin
   codesign tuzağını anlamanın ön-koşulu (aşağıda).
2. Uygulamanın KENDİ `.mobileprovision` profili — dosya ADINA değil İÇERİĞİNE
   göre bulunur (UUID koşum-bağımlı, profil yenilendikçe değişir).
3. Bağlı cihazın **GERÇEK UDID'si** — `devicectl`in kendi `pairing identifier`ı
   DEĞİL (H-9 dersi, iki ayrı alan): `device info details --device <pairing-id>`
   çıktısındaki `udid:` satırı okunur.

## §2 — Yayın provası: ARŞİVİN imzası ≠ İNDİRİLEN IPA'nın imzası

**Gravita'nın turunda ölçülen, en pahalı olabilecek yanlış-negatif:** `flutter
build ipa` iki katman üretir — ARA ürün `build/ios/archive/Runner.xcarchive` VE
son ürün `build/ios/ipa/<app>.ipa`. **İkisinin imza SINIFI FARKLIDIR:**
```
xcodebuild archive           → Apple DEVELOPMENT sertifikasıyla imzalar (NORMAL)
xcodebuild -exportArchive    → app-store metoduyla DISTRIBUTION'a YENİDEN imzalar
```
**Yalnız arşive bakıp** `codesign -dvvv Runner.xcarchive/.../Runner.app` **okumak
YANLIŞ SONUCA götürür** — `Authority=Apple Development` görürsün ve *"bu IPA
ASC'ye yüklenemez"* diye YANLIŞ bir teşhis koyarsın. **Doğru soru:** yüklenecek
dosya ARŞİV DEĞİL, **`.ipa`nın İÇİNDEKİ** `.app`.
```bash
cd <scratchpad>   # asla /tmp — Gravita bunu bir kez unuttu, kendi bildirdi
unzip -q build/ios/ipa/*.ipa
codesign -dvvv Payload/*.app 2>&1 | grep -i authority
# BEKLENEN: "Apple Distribution: <isim> (<TEAM_ID>)" — Development DEĞİL
```
> ***ARŞİVİN İMZASI BUILD İMZASIDIR, GÖNDERİM İMZASI DEĞİL.*** Yanlış dosyaya
> bakmak, yanlış aracın "yok" demesiyle AYNI sonucu verir (M-F-670'in kardeşi:
> `keytool` eski şemayı görmüyordu, burada doğru dosya bile YANLIŞ AŞAMADA
> okunuyordu).

## §3 — LaunchImage: storyboard'un RENGİ ≠ GÖRSELİN kendisi

İki AYRI varlık, ikisi de düzeltilmeli:
1. `LaunchScreen.storyboard`ın KENDİ `backgroundColor`ı (Ostinato'nun bulduğu,
   ilk bulunan) — yalnız `LaunchImage`ı değiştirmek YETMEZ, storyboard'un
   `<color key="backgroundColor" .../>` alanı AYRI bir XML değeri taşır.
2. ⚠️ **Gravita'nın turunda YENİ bulunan ikinci yarı:** görselin KENDİSİ.
   `Assets.xcassets/LaunchImage.imageset/*.png` genelde Flutter'ın **1×1 piksel
   şablon** dosyalarıdır. `flutter build ipa` bunu KENDİSİ söyler (*"Launch
   image is set to the default placeholder icon"*) ama yalnız `--release`/`ipa`
   turunda — `flutter build ios --simulator --debug` bu uyarıyı VERMEZ. **Kontrol
   ÖNCEDEN yapılabilir, uyarıyı beklemeden:**
```bash
file ios/Runner/Assets.xcassets/LaunchImage.imageset/*.png
# "1 x 1" görürsen şablon HÂLÂ duruyor demektir
```
Renk düzeltmesi görseli düzeltmez, görsel düzeltmesi rengi düzeltmez — bir
"kapanış kanıtı" İKİSİNİ de AYRI AYRI ölçmeli (komşusunu değil, kapatıldığı
iddia edilen şeyin KENDİSİNİ).

## §4 — Yürüyüş tablosu — YAPI paylaşılır, İÇERİK paylaşılmaz

Her hat kendi 10 maddelik "kurucu eli" tablosunu KENDİ ekranlarından türetir
(bkz. Gravita `docs/device-day/RECIPE.md` §3, Ostinato'nunki farklı içerikle
aynı yapıda). Ortak SÜTUN yapısı: *Ekran/eylem · Ne YAPILACAK · "Çalışıyor"
NASIL görünür · Sorun işareti.* **İçerik kopyalanmaz** — her app kendi
onboarding/kütüphane/canlı-seans ekranlarını anlatır.

⭐ **Ortak SON madde önerisi (hepsi için geçerli, kamera-tabanlı beş app da):**
kamera köprüsünün canlılığı (gerçek telefon + gerçek insan gövdesi) bugüne kadar
**yalnız simülatörde** koşuldu ve simülatörde kamera izni genelde OTOMATİK
REDDEDİLİYOR (Gravita'da ölçüldü) — yani GERÇEK kanıt cihaz gününde İLK KEZ
üretilecek. Ostinato'nun kendi çerçevesi: bu bir *"son kontrol"* değil **asıl
soru.**

---

## Kaynak turlar

- Gravita `G-246` (`b2d9020`) — ön-uçuş betiği + reçete, kurucunun gerçek
  UDID'i doğrulandı.
- Gravita `G-247` (`7d67f10`) — ilk gerçek `flutter build ipa`, §2 ve §3'ün
  ikinci yarısı burada bulundu.
- Ostinato `O-160` (`7177c55`) — şemanın kendisi, §3'ün ilk yarısı (storyboard
  rengi).
- Orkestratör ölçümü (2026-08-16) — §0, `system_profiler` karşılaştırması.
