# 💃 CHOREIA — AJAN DEVRİ (ölçüm ajanı → oturum), 2026-08-13 00:5x

> **Bu not bir MÜHÜRDÜR.** Ajan turu kapandı; üretim oturumun. Aşağıdaki her
> sayı **çalıştırılarak** ölçüldü — beyan yok. Ölçemediklerim §6'da **adıyla**.

## 0. MÜHÜR — kapanışta ölçüldü, açılışta değil

| ne | değer | nasıl |
|---|---|---|
| HEAD | **`0885ff2`** | `git rev-parse --short HEAD` |
| `HEAD == @{u}` | **EVET** (push edildi) | `c54c957..0885ff2  main -> main` |
| ağaç | **0 satır kirli** | `git status --porcelain \| wc -l` — **iki derlemeden SONRA** ölçüldü |
| kapılar | **20 koşucu, exit 0**, 0 ⚪ | `bash tool/gates.sh`, borusuz |
| testler | **237 (flutter) + 36 (engine) = 273** · analyze temiz | gates çıktısı |
| DEFTER | son kayıt **`C-266`** (242→243 kayıt) | `workspace/DEFTER.md` |

⚠️ **Tur açılışında ağaç temizdi ve kapanışta 5 kirliydi** — `flutter build ios`
`pod install` çalıştırır ve `ios/Podfile.lock` + `project.pbxproj` yazar.
***Kapanış sinyalleri kapanışta ölçülür.*** Beşi de commit edildi (§2).

---

## 1. A8 — **KAPANDI ✅**, ve tam olarak nereye kadar

**Ölçüt neyi istiyordu:** *"Gizlilik manifesti **PAKETTE** (yalnız depoda değil)
— paket içinden çıkarılıp doğrulanmış."* ⇒ dosyayı eklemek **yetmez**.

### Ne çalışıyor (çalıştırılabilir kanıtla)

| dosya | ne | kanıt |
|---|---|---|
| `ios/Runner/PrivacyInfo.xcprivacy` | manifestin kendisi, 4 anahtar | md5 `6cc187d9a13e5fa10207374166f8e8ad` |
| `ios/Runner.xcodeproj/project.pbxproj` | **4/4 çapa** — satır **20** (`PBXBuildFile`) · **68** (`PBXFileReference`) · **164** (Runner grubu çocuğu) · **270** (`Resources` fazı) | `git diff` ile dördü de görülür |
| `tools/privacy_manifest_check.py` | iki yönlü kapı, **öz-test 8/8** | `python3 tools/privacy_manifest_check.py` → exit 0 |
| `tool/gates.sh` satır **58-63** | kapı bağlı, **19 → 20 koşucu** | `grep -c '^── '` → 20 |

**PAKET KANITI — ölçütün istediği hâli, üretildi:**
```
flutter build ios --release --no-codesign   → exit 0, 29 s, Runner.app 45,3 MB
find Runner.app -name '*.xcprivacy'         → 3 manifest:
      Runner.app/PrivacyInfo.xcprivacy                      ← BENİMKİ
      Runner.app/permission_handler_apple_privacy.bundle/…
      Runner.app/Frameworks/Flutter.framework/…
plutil -p Runner.app/PrivacyInfo.xcprivacy  → NSPrivacyTracking => false, dört anahtar yerinde
```
Artefakt: `~/choreia_buildout/ios/iphoneos/Runner.app` (`build/` iCloud dışına
symlink — bilinen tuzak zaten çözülmüş).

**KAPININ İKİ YÖNÜ** (`privacy_manifest_check.py`):
① Xcode projesine 4/4 bağlı mı — *bağlı değilse dosya depoda durur, **pakete
girmez**, mağaza yine reddeder.* ② `NSPrivacyAccessedAPITypes` **boş**, ve
boşluk **da bir iddiadır**: Runner'ın kendi kaynakları gerekçeli-API çağırıp
manifest beyan etmiyorsa **kırmızı**.
⚠️ **Asimetri kasıtlı:** eksik-beyan **bloklar**, fazla-beyan **adıyla yazılır**
— tarayıcı yalnız ObjC/Swift görür, **Dart tarafı ona görünmez**.
⚠️ **Vakum:** taranacak kaynak hiç yoksa kapı öter.

**SABOTAJ (yeşil tek başına sayılmadı):** öz-test 8/8, içinde **iki pozitif
kontrol** — sağlam hâl yeşil, **ve beyan edilmiş `UserDefaults` yeşil**
(*ikincisi olmasa kapı bir denetim değil bir **yasak** olurdu*).
**Gerçek depoda da:** manifest kenara alındı → **exit 1** → geri kondu,
**md5 birebir aynı**.

### Ne çalışmıyor / A8'in kapsamadığı
- **Android ekseni kapatılmadı, KASITLI.** Ölçütün A8 kanıtı iOS-özel
  (`.xcprivacy`); Android karşılığı **Play Data Safety beyanı** ve o **B
  tablosu** işidir. Koordinatör hükmü: *adıyla B'ye bırak, kendin çözme.*
- Manifest **imzalanmış** bir IPA'dan değil, **imzasız `Runner.app`**tan
  çıkarıldı. İçerik aynı; imza zinciri ayrı iş (B1 keystore/sertifika).

---

## 2. Commit kararı — **(a) COMMIT EDİLDİ**, sessizce geri alınmadı

`0885ff2`, **5 dosya, 381 ekleme**. Beşi de ya benim ya ölçümün **zorunlu**
sonucu; **yabancı/untracked dosya commit edilmedi** (`flutter_01.log` ·
`flutter_02.log` — ikisi de **Flutter çökme raporu**, `.gitignore`'da `*.log`,
**dokunulmadı**).

| dosya | niye commit edildi |
|---|---|
| `PrivacyInfo.xcprivacy` · `privacy_manifest_check.py` · `gates.sh` | A8'in kendisi, tamamlanmış |
| `ios/Podfile.lock` · `project.pbxproj` (pod kısmı) | **C-222'den (permission_handler) beri iOS pod katmanı `pubspec` ile senkron DEĞİLDİ.** Derlemenin kendi çağırdığı `pod install` senkronladı: `permission_handler_apple 9.4.8` + `[CP] Copy Pods Resources` fazı. **Geri almak, bir sonraki iOS derlemesinde ağacı yine kirletirdi** — o yüzden alınmadı |

---

## 3. SIRADAKİ SOMUT ADIM — bir cümle

> **`lib/app/onboarding/first_run_flag.dart`'ın (satır 33-60) `FirstRunFlag`
> dikişini örnek alarak `SessionStore`a bir YAZMA yolu aç** — çünkü
> `git grep "append\|save(\|write(" -- 'lib/*.dart' | grep -i "session\|store\|history"`
> bugün **exit 1** (hiç eşleşme) döndürüyor, ve **yazma yoksa gösterilecek
> sonuç da yoktur** ⇒ A1'in üçüncü parçası (sonuç yüzeyi) tanım gereği
> imkânsız.

**Sıra (koordinatör onaylı):** ~~① A8~~ ✅ → **② A6** → **③ A1**.
- **A6** — kurulacak şey: **iki yönlü tazelik kapısı**. ⚠️ Bugün ölçüldü ki
  *durum* zaten sağlanıyor (aşağıda §4), ***eksik olan koşul değil KAPI*** ⇒
  bugün kurmak en ucuz gün. ⛔ **Sabotajla kanıtla, iki yönü AYRI AYRI**
  (iş→kayıt **ve** kayıt→iş); yeşil tek başına kanıt değil.
- **A1** — asıl kalem, **tek ⛔ ki başka bir ⛔'yü kilitliyor** (A12).

---

## 4. ÖLÇTÜĞÜM AMA HENÜZ BAŞKA HİÇBİR YERE YAZILMAYAN HER ŞEY

⚠️ `scratch/2026-08-12-choreia-yayin-mesafe/YAYIN-MESAFE-OLCUMU.md` **BAYAT** —
A3'ü *bilinmiyor*, A11'i *ölçülüyor* gösteriyor. **Aşağısı geçerlidir.**

**Güncel mesafe: ✅7 · ⛔5 · bilinmiyor 0** (önceki tur: ✅5 · ⛔5 · bilinmiyor 1).

**① A3 — `bilinmiyor` → ✅.** JabLab'ın üç şartlı tanımı bulundu
(`devir/05-JABLAB.md:29`: `30 = 20 iş sunan + 10 ADIYLA BOŞ + 0 ÇIKMAZ`).
Choreia'da **payda 34** (`content/library.json`; statüler: `comingSoon 31 ·
demoOpen 1 · live 1 · onHold 1`; stil-kapsamlı kapalı kapı yalnız
`salsa_shines/bpmResolved`):
> **34 = 1 iş sunan + 33 adıyla boş + 0 sessiz ⇒ sessiz oranı %0 · boş oranı %97**

Çalıştırılabilir kanıt: `test/library_catalog_test.dart:167` *"every unopenable
style carries a reason the user can read"* — **gerçek külliyat üzerinde** koşuyor.
🔴 **AÇIK ŞERH (kimse yazmadı, kaybolmasın):** `StyleView.derive`
(`lib/app/style_availability.dart:67`) **`excluded` dalında
`userFacingReason = null`** döndürüyor ⇒ *açılamayan ama sebepsiz* bir yüzey
üretilebilir. Bugün popülasyonu **0**, ve `test/style_availability_test.dart:86`
üç sentetik vakası (`live+gate`·`comingSoon`·`onHold`) **bu dalı hiç denemiyor**.
⇒ **sıfır paydayla geçilmiş gizli bir sessiz-yüzey dalı.**

**② A11 — `ölçülmedi` → ✅ (iki platform da ölçüldü).**
`flutter build apk --release` → exit 0, **51 s**, `app-release.apk`
**85 284 018 bayt**, md5 `8dff984cbd8f7e1765129743a923f6b9`.
iOS: yukarıda. ⚠️ APK **debug anahtarıyla** imzalı (B1 keystore yok) — ölçüt
*"imzasız da olsa"* diyor. Önceki turun `exit 144`ü **iptalin kodu**ydu, arıza
değil — **doğrulandı**.

**③ A6 — durum sağlanıyor, KAPI yok.** HEAD `c54c957`ün commit saati
**2026-08-12 18:01:37** = `DEFTER.md` mtime **18:01:37** (*aynı saniye*), son
kayıt C-265 ↔ HEAD *(R24)* ⇒ **gedik iki yönde de 0**. Defterde **242 kayıt**,
23 numara boşluğu (C-002..006, C-183..194, C-197..201, C-204).
`closure_authority.py` **tek yönlü** (iddia → kaydın kendi `Durum` sütunu);
`ls tools/ | grep -iE 'fresh|taze|defter|ledger|stale'` → **exit 1** (pozitif
kontrol: aynı grep `closure_authority.py`'yi buluyor).

**④ A12 — donanım VAR, artefakt yok.** `flutter devices` →
**`Mustafa Kaan iPhone'u (wireless) · 00008120-001804D83E13C01E · iOS 26.6`**;
`xcrun devicectl list devices` → **`available (paired)`**.
⇒ *"donanım yok"* **yanlıştı**; engel **A1 + imza**. Cihazda hiçbir şey
koşturulmadı (yan etkili, ve koşacak akış yok).

**⑤ A10 — aile kalemi, kurucuda.** Android **5/5 bayt-aynı**
(`mdpi 6270344430679711b81476e29878caa7` · `hdpi 13e9c72e…` · `xhdpi a0a8db59…`
· `xxhdpi afe1b655…` · `xxxhdpi 57838d52…`); iOS 1024 md5
**`c785f8932297af4acd5f5ccb7630f01c`** = Flutter **modül şablonunun ham PNG'si**
(10932 bayt — **gerçek referans**; `app/ios.tmpl`deki **0 bayt**, tuzak) **ve
beş Motion hattının beşinde de aynı**. ⛔ Koordinatör kurucuya taşıdı — **ikona
dokunma**.

**⑥ 🔴 YENİ BULGU, HİÇBİR YERDE YAZILI DEĞİL — motion-core kalemi.**
`motion_camera` **kendi `PrivacyInfo.xcprivacy`'sini taşıyor**
(`…/motion-core-f13bdc9/packages/motion_camera/ios/Resources/PrivacyInfo.xcprivacy`)
**ama podspec'i `resource_bundles`/`resources` BEYAN ETMİYOR** ⇒ manifest
**pakete hiç girmiyor** (ölçüldü: `Runner.app`ta 3 manifest, motion_camera
aralarında **yok**). **Bu ailenin KAMERA eklentisi** ve pin `f13bdc9` **beş
hatta da ortak** ⇒ **beş app birden etkileniyor.** ⛔ Benim düzeltme alanım
değil (motion-core), koordinatöre.

**⑦ 🪤 Bir YANLIŞ P0'dan son anda dönüldü — kaydı dursun.**
`path_provider_foundation` ne `Podfile.lock`ta, ne `GeneratedPluginRegistrant.m`de,
ne pakette. *"iOS'ta `getApplicationSupportDirectory` implementasyonsuz"* diye
raporlanmak üzereydi. Ölçüm sebebi buldu: **2.6.0 yalnız `dartPluginClass`
beyan ediyor** (podspec YOK, FFI/`objective_c`), ve **`objective_c.framework`
pakette duruyor** ⇒ **kusur değil**.
> ***BİR BİLEŞENİN ESKİ YERİNDE OLMAMASI, OLMADIĞI ANLAMINA GELMEZ.***

**⑧ Sözleşme panosu — koordinatör düzeltiyor, DOKUNMA.**
`GEZILEBILIRLIK-SOZLESMESI.md` DURUM tablosunda **Choreia satırı dört hücreli**
(diğer dördü üç); fazladan hücre *"(a) KISMİ · (c) sebep ÖLÇÜLMEDİ · 🔴 (e) YOK"*
diyor — üçüncü hücrenin tersi, ve **kod üçüncü hücreyi doğruluyor** (C-254
öncesi bir değerlendirme kayık bir sütunda yaşıyor). Koordinatör *"o benim
kalemim, sen dokunma"* dedi.

**⑨ A5'in kapı-kırmızı kanıtı.** `PATH` shim ile `python3` exit 3 →
`gates.sh` **exit 1**, **16 🔴**, `⛔ KAPI KIRMIZI`. Kapı yeşile **sıkışmış
değil**. (Shim silindi.)

---

## 5. TUZAKLAR — bu turda gerçekten ödendi, tekrar ödeme

- ⛔ **`flutter build ios` DEPOYU KİRLETİR** — `pod install` `ios/Podfile.lock` +
  `project.pbxproj` yazar. Paket kanıtı istiyorsan bu bedeli ödersin;
  ***`git status`u turun BAŞINDA değil SONUNDA ölç.***
- ⛔ **`find` symlink TAKİP ETMEZ** — `find ios -name '*.xcprivacy'` **0** der,
  `find -L` **1** der (eklentiler `.symlinks/plugins/` arkasında).
  *Bu turda ilk ölçümüm buna takıldı ve düzeltildi.*
- ⛔ **`timeout` bu makinede YOK**, `gtimeout` da yok. Uzun iş = arka plan.
- ⛔ **Bir karşılaştırmanın sonucu, referansının GERÇEK olduğu kadar geçerli**
  (iOS ikon şablonu **0 bayt** ⇒ *"15/15 farklı"* hiçbir şey ölçmüyordu).
- ⛔ **`grep -c` SATIR sayar** · boru varsa `$?` son komutundur ·
  `2>&1 | wc -l` hatayı **sayıya** çevirir.
- ✅ **Lissom'un `tools/privacy_manifest_check.py`si referans** — okundu,
  **kopyalanmadı**: Choreia'nınki ikinci yönü + vakum korumasını ekliyor,
  ve **beyanı bu ağaçta ölçtü** (Lissom'un bağımlılık kümesi farklı).

---

## 6. ÖLÇEMEDİKLERİM, ADIYLA — geri dönüş adresi

1. **A3'ün `excluded` dalı** — sıfır popülasyon; çürütülebilirliği **koddan
   çıkarıldı, koşturularak değil**.
2. **A5'in "engelliyor" kanıtı** 16 python koşucusu üzerinden; `flutter test` ·
   `analyze` · `dart test` **ayrı ayrı** sabote edilmedi.
3. **A11'in imza zinciri** — APK'nın hangi anahtarla imzalandığı
   `apksigner verify` ile **doğrulanmadı**; *"debug anahtarı"* bir çıkarım.
4. **A12** — cihazda **hiçbir şey koşturulmadı**.
5. **A7 (b)'nin tanığı** — `_RouteSpy` sabote edilince ötüyor mu, bu turda
   **tekrar ölçülmedi** (maddeler metne karşı **okunarak** doğrulandı).
6. **`docs/design/GEZILEBILIRLIK-SAYMA-KURALI.md` açılmadı** — A7 aile
   sözleşmesinin metnine karşı ölçüldü, hattın kendi sayma kuralına karşı
   **çapraz okunmadı**.
7. **`motion_camera` manifestinin podspec'i** — düzeltme denenmedi (alan dışı).

---

## 7. DURMA KOŞULU (C) — bu turun cevabı

> *"Bu tur, A tablosundaki hangi kalemi `⛔` → `✅` yaptı?"*

**`A8`.** (Ayrıca `A3` *bilinmiyor*→✅ ve `A11` *ölçülmedi*→✅ **taşındı** —
bunlar düzeltme değil **ölçüm**.) ⇒ **Sayaç sıfırlandı; durma koşulu
tetiklenmedi.** Kalan ⛔: **A1 · A6 · A10 · A12** (dördü de §4'te sayıyla).
