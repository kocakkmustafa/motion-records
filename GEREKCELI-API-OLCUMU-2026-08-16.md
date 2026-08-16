# 🔍 Gerekçeli-API ölçümü — beş app, salt-okunur (2026-08-16, Gravita)

> **Görev:** orkestratörün ataması — beş app için hangi gerekçeli-API kategorisinin
> hangi SEMBOLDEN ve hangi POD/eklentiden geldiğini çıkar. **Salt-okunur** (başka
> hiçbir hattın deposunda tek bayt değiştirilmedi) ve **gerekçe kodu SEÇİLMEDİ**
> (`C617.1` vb. — bu bir yargı, kurucu paketine gidiyor). Bu dosya yalnız GİRDİ
> verir, KARAR vermez.
>
> **Yöntem, kısaca:** üçüncü-taraf derlenmiş ikili dosyalar `nm -u <ikili> | grep
> <sembol>` ile (Apple'ın gerekçeli-API sembol ailelerine karşı) taranır; birinci-
> taraf/kaynak-erişilebilir kod (motion_camera, permission_handler_apple, her
> app'in kendi `ios/Runner/`ı) doğrudan `grep` ile taranır. Aranan semboller bu
> oturumun KENDİ bilgisinden — Apple'ın resmî listesiyle **tek tek** çapraz
> doğrulanmadı, adıyla söylenir (aşağıda "Sınır" bölümü).

---

## ÖZET — beş app'in BEŞİNDE de aynı iki bulgu, artı üçüncü bir YENİ bulgu

| Kategori | Sembol | Kaynak (pod) | Sayı | Kaç app'te |
|---|---|---|---|---|
| **FileTimestamp** | `_stat`, `_fstat` | `MediaPipeTasksCommon` 0.10.21 | 12 | **5/5** (zaten biliniyordu) |
| **SystemBootTime** | `_mach_absolute_time` | `MediaPipeTasksCommon` 0.10.21 | 3 | **5/5** (zaten biliniyordu) |
| **UserDefaults** | `NSUserDefaults standardUserDefaults` | `permission_handler_apple` (3 farklı sürüm) | 2 çağrı yeri | **5/5** ⭐ **YENİ** |
| DiskSpace | — | — | 0 | 0/5 |
| ActiveKeyboards | — | — | 0 | 0/5 |

**Beşinci app'e kadar hiçbiri `PrivacyInfo.xcprivacy` içinde bunları BEYAN ETMİYOR**
— `NSPrivacyAccessedAPITypes` beşinde de **0 girdi** (python ile okunarak
doğrulandı, beyan değil).

---

## 1 — Paylaşılan, PİNLİ bağımlılıklar (5 app'te BİREBİR aynı, çapraz doğrulandı)

### `MediaPipeTasksCommon` 0.10.21 — gerçek cihaz (arm64) ikili dosyası

```
nm -u MediaPipeTasksCommon | grep -Ec '\b_stat\b|\b_fstat\b'        → 12
nm -u MediaPipeTasksCommon | grep -Ec '\b_mach_absolute_time\b'     → 3
nm -u MediaPipeTasksCommon | grep -Ec '\b_statfs\b|...'             → 0 (DiskSpace)
nm -u MediaPipeTasksCommon | grep -ic 'userdefaults'                → 0
nm -u MediaPipeTasksCommon | grep -ic 'inputmode'                   → 0
```
**Beş app'in BEŞİNDE de bağımsız olarak koşuldu, BEŞİ de birebir aynı sayıyı
verdi** (Gravita/Choreia/Lissom/JabLab/Ostinato) — aynı sürüm, aynı ikili, aynı
sonuç; varsayılmadı, ölçüldü. Kalan 3 kategori yalnız Gravita + Choreia'da tam
tarandı (0/0), diğer üçünde sürüm eşitliğinden ÇIKARILDI (aynı SPEC CHECKSUM,
`Podfile.lock`: `MediaPipeTasksCommon: 6cfa29170d4900f...`, beş dosyada aynı).

### `MediaPipeTasksVision` 0.10.21 — sıfır, doğrudan

Kendi ikili dosyasında (Common'a bağımlı ama kendi sembol tablosunda) **sıfır**
gerekçeli-API sembolü — Gravita + Choreia + JabLab'da bağımsız ölçüldü, üçü de
0/0. Lissom/Ostinato ölçülmedi, sürüm eşitliğinden ÇIKARILDI.

### `motion_camera` (birinci-taraf, PAYLAŞILAN aile paketi) — gerçek çağrı YOK

Beş app'in BEŞİ de AYNI pinli SHA'ya sembolik bağlı:
```
~/.pub-cache/git/motion-core-f13bdc93b2eae2f741bfcdb4c9270a88e5d75e5d/packages/motion_camera/
```
(beş `readlink` birebir aynı çıktı — doğrulandı, varsayılmadı). Kaynak GREP
edildi: **tek isabet**, `MotionCameraPlugin.swift:161`, ve o bir YORUM SATIRI
(*"CMSampleBuffer PTS rides the host clock (mach_absolute_time family)"*) —
gerçek bir API çağrısı DEĞİL. Aynı dosya AYRICA `mach_absolute_time`/
`systemUptime`/`creationDate`/vb. için taranıp başka isabet BULUNAMADI.
**motion_camera'nın kendisi hiçbir gerekçeli-API çağırmıyor.**

---

## 2 — `permission_handler_apple`: pinli DEĞİL, ama sonuç 3 sürümde de AYNI

⚠️ **Yan bulgu — pinleme tutarsızlığı, adıyla:** `motion_camera`nın aksine bu
paket ailede PİNLİ DEĞİL. Beş app beş farklı `flutter pub get` anında farklı
sürüm çözümlemiş:

| App | Çözülen sürüm | `Podfile.lock`'taki CocoaPods sürüm dizgesi |
|---|---|---|
| Gravita | `9.5.0` | `9.4.8` (⚠️ dizge UYUŞMUYOR — aşağıda not) |
| Ostinato | `9.5.0` | `9.4.8` |
| Choreia | `9.6.1` | `9.4.8` |
| Lissom | `9.6.1` | `9.4.8` |
| JabLab | `9.4.10` | `9.4.8` |

⚠️ **`Podfile.lock`'un CocoaPods sürüm dizgesi (`9.4.8`), GERÇEKTE çözülen Dart
paket sürümüyle (`9.5.0`/`9.6.1`/`9.4.10`) UYUŞMUYOR** — beş app'in BEŞİNDE de.
Sebep araştırılmadı (federe eklenti deseninde Dart paketi ile podspec'in ayrı
sürümlenmesi OLASI bir açıklama, ama bu bir ÇIKARIM, doğrulanmış değil). Ölçüm
GERÇEKTEN ÇÖZÜLEN yolu (`.symlinks/plugins/` sembolik bağlantı hedefi) kullandı,
çünkü derlenen kod odur.

**Üç sürümün ÜÇÜ de** `Sources/permission_handler_apple/strategies/
LocationPermissionStrategy.m`'de AYNI iki çağrıyı taşıyor:
```objc
// satır 51:
[[NSUserDefaults standardUserDefaults] boolForKey:UserDefaultPermissionRequestedKey]
// satır 94:
[[NSUserDefaults standardUserDefaults] setBool:TRUE forKey:UserDefaultPermissionRequestedKey]
```
→ Kategori: **UserDefaults**. `standardUserDefaults` kendi uygulama container'ına
erişiyor (paylaşımlı/başka-uygulama suite'i DEĞİL) — Apple'ın dokümantasyonunda
kendi-suite erişimi için bir MUAFİYET yolu olduğunu HATIRLIYORUM ama bu oturumda
resmî kaynaktan DOĞRULANMADI ve **bu bir yargı, benim vereceğim bir karar
değil** — yalnız olgu: iki çağrı yeri, `standardUserDefaults`, bu dosyada.

⚠️ **9.6.1 (Choreia/Lissom) sürümünde EK bir isabet, ama İSTİSNAİ — kapsam
DIŞINDA bırakıldı, adıyla:** `Package.swift` dosyasında `modificationDate`
kullanan iki fonksiyon var (satır 367-368, 396-397). **Bu derlenen uygulama
kodu DEĞİL** — dosya `import PackageDescription` taşıyor, yani Swift Package
Manager'ın KENDİ derleme-zamanı betiği (bir YAML config dosyasının üretilmiş
JSON çevirisinden daha yeni olup olmadığını kontrol ediyor). `Package.swift`
uygulama paketine GİRMEZ, yalnız paket ÇÖZÜMLEMESİ sırasında koşar. Tabloya
alınmadı çünkü kategori sorusu "çalışan uygulamada hangi API'ler var" —
derleme betiği bu sorunun dışında.

---

## 3 — `integration_test` (yalnız JabLab) — sıfır

JabLab'ın `Podfile.lock`'unda EK bir bağımlılık: `integration_test (0.0.1)`
(Flutter SDK'nın kendi paketi, `/opt/homebrew/share/flutter/packages/
integration_test/`den çözülüyor — pub-cache değil, SDK kurulumunun kendisi).
Kaynağı tarandı: **sıfır** gerekçeli-API isabeti.
⚠️ **Ölçülmeyen, adıyla:** bu paketin JabLab'ın GERÇEK `--release` arşivine
girip girmediği (Flutter tipik olarak test-only paketleri release build'e
almaz, ama bu VARSAYIM — JabLab'ın kendi `flutter build ipa` çıktısından
`nm`/`otool` ile doğrulanmadı, bu ölçümün kapsamı dışında kaldı).

---

## 4 — Her app'in KENDİ `ios/Runner/` yerel kodu — beşi de sıfır

Beş app'in `ios/Runner/*.swift`/`*.m`/`*.h` dosyaları tek tek grep edildi.
**Gerçek isabet YOK.** (Gravita/Lissom/Ostinato'da `PrivacyInfo.xcprivacy`
dosyasının KENDİSİ eşleşti — ama bu dosyanın içindeki `NSUserDefaults`/vb.
geçişleri kod DEĞİL, manifestin kendi kategori-adı sözlüğü, ör. Gravita
satır 61: `"· UserDefaults (\`SharedPreferences\`/\`NSUserDefaults\`)"`. Yanlış-
pozitif olarak elendi, DOĞRULANARAK.)

---

## 5 — Şu an DEKLARE edilen durum (bağlam, ölçüm değil beyan-okuma)

```
                    NSPrivacyAccessedAPITypes girdi sayısı
Gravita             0
Choreia             0
Lissom              0
JabLab              0
Ostinato            0
```
Python'la `plistlib` üzerinden okunarak doğrulandı — beyan değil, dosyanın
kendi içeriği.

---

## Sınır — bu ölçümün YAPMADIĞI şeyler, adıyla

- **Apple'ın resmî sembol listesiyle TEK TEK çapraz doğrulama yapılmadı.**
  Aranan semboller (`_stat`/`_fstat`/`_mach_absolute_time`/`_statfs`/
  `userdefaults`/`inputmode`) bu oturumun kendi bilgisinden — büyük ihtimalle
  DOĞRU ama Apple'ın "Describing use of required reason API" sayfasındaki
  TAM listeyle bu oturumda satır satır karşılaştırılmadı. Eksik bir sembol
  ailesi varsa (ör. `getattrlist`/`fgetattrlist`/`getattrlistbulk` — hem
  FileTimestamp hem DiskSpace'te geçebilen İKİ-ANLAMLI semboller) bu ölçüm
  ONU KAÇIRMIŞ olabilir.
- **Simülatör dilimi taranmadı** — yalnız gerçek cihaz (`ios-arm64`) dilimi,
  çünkü mağazaya giden budur.
- **Android tarafı ölçülmedi** — görev açıkça iOS gerekçeli-API'ye
  (`PrivacyInfo.xcprivacy`) odaklıydı.
- **`integration_test`in JabLab'ın gerçek release arşivine girip girmediği**
  doğrulanmadı (yukarıda §3).
- **Gerekçe kodu seçilmedi, seçilmeyecek** — bu dosyanın işi değil.

## Kaynak komutlar (yeniden-üretilebilir)

```bash
# Üçüncü-taraf derlenmiş ikili:
BIN=".../MediaPipeTasksCommon.xcframework/ios-arm64/MediaPipeTasksCommon.framework/MediaPipeTasksCommon"
nm -u "$BIN" | grep -Ec '\b_stat\b|\b_fstat\b'

# Birinci-taraf/kaynak-erişilebilir:
grep -rn "mach_absolute_time\|systemUptime\|creationDate\|modificationDate\|statfs\|volumeAvailableCapacity\|NSUserDefaults\|activeInputModes" <kaynak-dizini>

# motion_camera'nın hangi SHA'ya bağlı olduğu:
readlink ios/.symlinks/plugins/motion_camera
```

**Ölçen:** Gravita hattı, 2026-08-16. Beş depoya da yalnız OKUMA erişimiyle
girildi — hiçbir dosya değiştirilmedi (kendi deposu dışında hiçbir `git`/yazma
komutu çalıştırılmadı).
