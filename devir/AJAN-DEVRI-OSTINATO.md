# 🥁 OSTİNATO — AJAN DEVRİ (ölçüm ajanı → üretim oturumu)

> **Yazan:** ölçüm ajanı · **Tarih:** 2026-08-13 · **Depo mührü:** `HEAD = 3697b86 == origin/main` ·
> **push-bekleyen 0** · **kurucu kararı: üretim OTURUMLARIN, ajan değil** — bu not devirdir, sevk değil.

⚠️ **Bu dosya `git` deposu DEĞİL** (`ventures/motion-core/workspace/` ölçüldü: `not a git repository`) —
yazılır, commit'lenemez.

---

## 0. TEK CÜMLELİK DURUM

**A11-iOS ✅ YEŞİLE DÖNDÜ** (kök neden ölçüldü, kod değişmedi) · **A8 taze paketten yeniden çıkarıldı ✅** ·
ve kapanışta **bir veri bütünlüğü kalemi bulundu: çalışma ağacında KALINTI MUT-A SABOTAJI** (geri alındı, aşağıda adıyla).

---

## 1. A11-iOS — ✅ KAPANDI, ve kök neden **ölçüldü**

### Koordinatörün diferansiyeli DOĞRULANDI: kusur **YEREL**, pin değil
Kendi ölçümüm (`ventures/` altında beş ağaç):

| kontrol | sonuç |
|---|---|
| `build` sembolik bağlantısı | **beşinde de var** ⇒ sembolik bağlantı **sebep değil** |
| `objective_c` | beşinin de `pubspec.lock`unda ⇒ **sebep değil** |
| `motion_core` | beşinde de aynı ⇒ **pin sebep değil** (benim ilk hipotezim **ÇÜRÜDÜ**) |
| `build/native_assets/ios` | Lissom ✅ · Gravita ✅ · JabLab ✅ · **Choreia ❌** · **Ostinato ❌** |

📌 **Şerh:** `native_assets/ios` bir **girdi değil ÇIKTIDIR** — yokluğu sebep değil **belirtidir**.
Choreia'da da yok, çünkü Choreia iOS tarafında ölçülmemişti (koordinatörün notu: *"Choreia tarafı APK"*).

### İki hipotez kuruldu ve **ikisi de ÇÜRÜDÜ** — üçüncüsü tuttu
1. ⛔ **"Bayat `build/ios` çıktısı"** → tüm `build/ios` ağacı kenara alındı, yeniden derlendi → **yine `EXIT=1`**.
2. ⛔ **"iOS hook'u hiç koşmamış"** → `.dart_tool/hooks_runner/objective_c/*/input.json` **hepsi** okundu:
   Ostinato'da **3 iOS hook koşumu var** (`63843f2ee8` arm64 · `6491424e80` x64 · `84fd4fa0ea` arm64),
   **hash'ler Lissom'unkiyle birebir aynı**, hepsinde `output.json` var. ⇒ hook **koşmuş**.
   *(Lissom'daki tek fazlalık `9fb02c5622` = **macos**, iOS'la ilgisiz.)*
3. ✅ **TUTAN:** `.dart_tool` ÖNBELLEĞİ BOZUK/EKSİK. Kanıt: `build/ios` **tamamen silindiğinde bile**
   yeni paketin içindeki `NativeAssetsManifest.json` hâlâ **7 Ağu 11:50** tarihliydi ⇒ dosya yeniden
   üretilmiyor, bir önbellekten kopyalanıyordu.

### ÇÖZÜM (kod değişikliği YOK)
```
flutter clean  →  bash tools/run_gates.sh   (sembolik bağlantıyı KENDİ kurar)  →  flutter build ios --release --no-codesign
```
**Sonuç:** `EXIT=0` · `✓ Built build/ios/iphoneos/Runner.app (45.0MB)` · Xcode 24,9s ·
`build/native_assets/ios/objective_c.framework` **artık üretiliyor**.

> ⭐ **Depoda hiçbir dosya değişmedi.** ⇒ A11-iOS kırmızısı bir **ÜRÜN kusuru değil, ORTAM kusuruydu**;
> taze klon / CI bunu **hiç görmezdi.** Aile hafızasındaki *"`flutter clean` şart"* kaydının **üçüncü vakası.**

### A8 — koordinatörün istediği gibi **YENİDEN ÖLÇÜLDÜ** ✅
Eski kanıt **başarısız** bir derlemedendi; şerh kalktı.
`~/ostinato_buildout/app/ios/iphoneos/Runner.app/PrivacyInfo.xcprivacy` (13 Ağu 00:33, 167 B) →
`plutil -p`: `NSPrivacyTracking=false · TrackingDomains=[] · CollectedDataTypes=[] · AccessedAPITypes=[]`.
🪤 **md5 depo kopyasıyla AYRIŞIR ve bu bir kusur DEĞİL:** Xcode XML plist'i **binary plist**'e çevirir
(`file` ile ölçüldü). *Bir md5 farkı, bir içerik farkı değildir.*

---

## 2. 🔴 KAPANIŞTA BULUNAN VERİ BÜTÜNLÜĞÜ KALEMİ — **kalıntı MUT-A sabotajı**

Derlemelerden sonra çalışma ağacı **kirlendi**. Ölçüm:

- `git diff --stat` → **996 satır** değişmiş görünüyordu (piano ruleset 500+/500−)
- `git diff -w --stat` → **2 satır**. ⇒ *996'nın 994'ü satır-sonu/boşluk gürültüsüydü.*
  > ***BİR FARKIN BÜYÜKLÜĞÜ, ONU GÖSTEREN ARACIN AYARI KADARDIR.***
- **Gerçek fark, iki dosyada da tek ve aynı:** `"contributingTakes": 3 → 99`

Bu, **MUT-A mutasyon #12'nin kendisi**: `[both] İKİ KAYNAK: take sayısı config+artefakt birlikte 3→99`
(`tools/gate_mutation_test.py`). Yani bir MUT-A koşumu **yarıda kaldı ve sabotajı geri koymadı** —
`config/rulesets/piano@0.2.0-draft.json` **ve** `config/references/piano-posture-setup.v1.json`.

**⚖️ KARARIM: COMMIT ETMEDİM, HEAD'e GERİ ALDIM — ve bunu sessizce yapmadım, burada ve raporda yazılı.**
Gerekçe: bu benim iş ürünüm değil, yarıda kalmış bir test koşumunun kalıntısı; devir promptunun sert kuralı
***"sabotajı COMMIT'LEYEREK kurma"***; ve `contributingTakes: 99` bir **dürüstlük** değeridir — 3 kaynak
varken 99 iddia eder. Kanıt diff'i saklandı:
`scratchpad/ostinato/KALINTI-MUTASYON.diff` (1048 satır).

### iCloud imzası — koordinatörün uyarısı **KISMEN** doğrulandı
- ⚠️ Koordinatörün gördüğü `error: short read while indexing config/rulesets/piano@0.2.0-draft.json`
  **aynı dosyada**, aynı pencerede.
- ✅ Ama **`git fsck` TEMİZ** (`çıkış 0`, yalnız zararsız `dangling` nesneler) ⇒ **`.git` nesne deposu
  BOZULMADI.** Bozulma **çalışma ağacı okumasında**, `.git`'te değil. *Bu ayrım kayda geçsin: aile hafızası
  "iCloud `.git`'i bozuyor" diyor; bu vakada `.git` sağlamdı.*
- 🔴 **Kanıt:** `.mutA-log 2.jsonl` — iCloud **çakışma kopyası** (00:30), gerçeği `.mutA-log.jsonl` (00:31).
  ⇒ MUT-A tam koşarken iCloud dosyayı çoğalttı; kalıntının en olası mekanizması bu.
- ⛔ **O dosyaya DOKUNMADIM** (untracked + paylaşımlı workspace kuralı — önce sorulur).
- 📌 **Ve `.gitignore` bunu KAÇIRIYOR:** satır 19 `.mutA-log.jsonl` yazıyor, iCloud kopyası
  `.mutA-log 2.jsonl` **desene uymuyor** ⇒ her çakışmada `git status` kirlenir.

---

## 3. ⭐ SIRADAKİ SOMUT ADIM — dosya + satır

### A1'in *"oturum → sonuç"* bacağı **sanıldığından ÇOK daha yakın** — dikiş **zaten var**

`lib/app/screens/live_screen.dart:31-49`:
```dart
class LiveScreenRoute extends StatefulWidget {
  const LiveScreenRoute({..., this.source, this.skipCountdown = false});
  final PoseSource? source;   // "Testlerin/harness'ın kendi kaynağını vermesi için"
  final bool skipCountdown;   // "Testler 3-2-1 geri sayımı beklemeden ölçüme geçer"
}
```
`lib/app/screens/live_screen.dart:57` → `late final PoseSource _source = widget.source ?? CameraPoseSource();`

**Ve bu dikiş ZATEN 5 testte kullanılıyor** — `widget_test.dart:44,172` · `timer_path_test.dart:36` ·
`cue_cooldown_visibility_test.dart:46` · `real_content_overflow_test.dart:108` ·
**`route_path_test.dart:58` — GERÇEK `Navigator.push` ARKASINDA.**
`FakePoseSource` hazır: `packages/ostinato_posture/lib/src/pose_source.dart:44`.
Ve `live_screen.dart:182` zaten `ReviewScreenRoute` push ediyor.

⇒ **Yapılacak iş:** `test/reachable_screens_test.dart`teki yürüyüşü, ders ekranından sonra
`LiveScreenRoute(source: FakePoseSource(...), skipCountdown: true)` ile **sürdürmek** ve `ReviewScreenRoute`a
kadar yürümek. **Cihaz gerekmez, üretim kodu değişmez.**

### 🔴 VE BU, SÖZLEŞME (c)'DE BİR KUSUR AÇIYOR — A7'nin şerhi
`tools/gen_screen_candidates.py:88-89` sebebi şu desenle türetiyor:
```python
CAMERA_TRACE = re.compile(r"requestAndStartCamera|MotionCameraController|CameraPoseSource")
```
Bu desen `widget.source ?? CameraPoseSource()` satırındaki **YEDEK**i, **zorunlu bağımlılık** sanıyor.
Üç sebebin ölçümü:

| ekran | üretilen sebep | **ölçüm** |
|---|---|---|
| `SetupCheckScreenRoute` | *"kamerayı KENDİSİ kullanıyor"* | ✅ **DOĞRU** — `setup_check_screen.dart` State'inde `final MotionCameraController _camera = MotionCameraController();` **koşulsuz**, dikiş YOK |
| `LiveScreenRoute` | *"kamerayı KENDİSİ kullanıyor"* | 🔴 **YANILTICI** — `source` zerk edilirse kamera **hiç kurulmaz**; 5 test bunu zaten yapıyor |
| `ReviewScreenRoute` | *"kamera gerektiren bir ekranın ARKASINDA"* | 🔴 **TÜREV** — dayandığı önerme yanlış olunca bu da düşer |

> Sözleşmenin kendi cümlesi: ***"YANLIŞ BİR SEBEP, SEBEPSİZLİKTEN DAHA KÖTÜDÜR: DENETİMİ DOĞRULANMIŞ
> GÖSTERİR."*** Ostinato (c)'nin **biçimini** karşılıyor (sebep kaynaktan türüyor) ama **yüklemi fazla kaba**:
> *"kamerayı kullanır"* ile *"kaynak verilmezse kameraya düşer"* aynı şey değil.
> ⇒ **A7 `5/5` hükmü düşmüyor** (mekanizma metnin istediğini yapıyor), ama **bir ŞERH kazandı.**

**Düzeltme yönü:** deseni *"`CameraPoseSource` geçiyor"*tan *"kamera **zerk edilemez** biçimde kuruluyor"*a
çevir (ör. yapıcıda `PoseSource?` parametresi olan sınıfı muaf tut). O gün `aday 11 = varılan 8 ⊎ varılamayan 3`
denklemi **kendiliğinden** `varılan 10 ⊎ varılamayan 1`e döner ve **KATI'nın sıfır payı da açılır**
(`test/reachable_screens_test.dart:397` eşiği `>= 8`, bugünkü sayı **8**).

---

## 4. DEVREDİLEN ÖLÇÜMLER (kapanmamış, ama ADIYLA yazılı)

- **`awaiting-content` ↔ `awaiting-capability` ayrımı — KOORDİNATÖR KABUL ETTİ, taksonomiye girecek.**
  Ostinato'nun 13 açılmayan kaleminin **10'u `locked`**, ve bunların **en az 4'ü veri değil ÖLÇÜM YETENEĞİ**
  eksiği beyan ediyor: `piano.foundations.hands_and_wrists` (*"a missing measurement **TOOL**, not a missing
  threshold"*) · `piano.foundations.shoulder_tension` (*"we only measure angles today"*) ·
  `piano.foundations.five_finger` (*"a fix for the engine's asymmetric bias"*) ·
  `guitar.foundations.strum_timing` (*"the step that maps six near-simultaneous attacks"*).
  A/B/C/D **yalnız içerik/kablolama** eksikliğini modelliyor. Ailenin doğru kelimesi **zaten var** (M-F-376).
- **A3 ölçümü** (birim: **ders kartı yüzeyi**): `28 = 15 iş sunan (guide 6 + scored 9) ⊎ 13 ADIYLA BOŞ ⊎ 0 ÇIKMAZ`
  ⇒ **sessiz oranı %0**; 13/13'ü gerekçe **ve** `unblockedBy` taşıyor, `tools/validate_library.py`de kapılı.
  ⚠️ Payda 3 varılamayan ekranı **kapsamıyor** (§3 kapanınca genişler).
- **A4 dağılımı** (payda 13): `A 0 · A′ 10 · B 0 · C 0 · D 3`. ⚠️ Eşleme **ölçüm ajanınındır**, taksonomi metni
  `YAYIN-HAZIRLIK-OLCUTU.md`de **tanımsız** (yalnız M-F-575'te) — koordinatör ölçüte yazıyor.
- **📌 B2 — kurucu kalemi:** `pubspec.yaml:19` → **`version: 1.0.0+1`**. B2 *"5 hattın 4'ünde `0.1.0+1`"*
  diyor; **Ostinato o dördün DIŞINDA.** ASC tarafını koordinatör ölçecek.
- **A10 → B tablosuna taşındı** (koordinatör hükmü). Ölçüm hazır: Android **5/5 şablonla bayt-aynı**,
  iOS 1024 `c785f893…` şablonla aynı, **gözle doğrulandı: Flutter logosu**, tek commit `b5bd37c`.
- **A12 ⛔ — ve sebep *"donanım yok" DEĞİL***: `flutter devices` gerçek iPhone'u **görüyor**
  (`00008120-… · iOS 26.6`, kablosuz), ama `xcrun xctrace` onu **`Devices Offline`** altında listeliyor.
  Var olan tüm kanıt **simülatör + SAHTE kaynak** (`docs/evidence/README.md` bunu kendisi yazıyor).

---

## 5. MÜHÜR

- `HEAD = 3697b86 == origin/main` · **push-bekleyen 0** · **hiçbir commit atılmadı**
- Çalışma ağacı: **kalıntı mutasyon geri alındı**, geriye yalnız **untracked** `.mutA-log 2.jsonl` kaldı
  (iCloud çakışma kopyası — **dokunulmadı**, kurucu/oturum kararı)
- Kapılar: kapanış koşumu `tools/run_gates.sh` **borusuz** → **`EXIT=0` · `✅ TÜM KAPILAR YEŞİL` ·
  `BAŞARISIZ` 0** (`flutter clean` sonrası **soğuk** ağaçta, yani hiçbir yeşil bayat önbelleğe dayanmıyor)
- ⭐ **Ve bu koşum kalıntı sorusunu da cevapladı:** MUT-A bu kez sabotajını **düzgün geri koydu** —
  koşum sonrası ağaç yine yalnız `?? .mutA-log 2.jsonl`. ⇒ **kalıntı, MUT-A'nın YAPISAL kusuru DEĞİL**,
  yarıda kalmış tek bir koşumun izi. *Ama tek koşumluk bir kalıntı bile commit'lenebilir olduğu için
  `.gitignore` deseni (§2) yine de düzeltilmeli.*
- ⛔ **Bu tur A tablosunda `A11-iOS`i `⛔ → ✅` yaptı** (A8'in şerhini de kaldırarak) — C durma koşulu sayacı **sıfırlandı**
