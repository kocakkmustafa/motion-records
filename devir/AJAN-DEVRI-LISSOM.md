# 📐 LISSOM — AJAN DEVRİ (ölçüm ajanı → Lissom oturumu)

> **Kurucu kararı:** üretim **oturumların**, ajanın değil. Bu not, ölçüm
> ajanının bıraktığı yeri **ölçümle** devreder — iddiayla değil.
> **Yazıldı:** 2026-08-13 · **Devreden:** A1–A12 ölçüm ajanı

## 0. MÜHÜR — kapanış ANINDA ölçüldü (turun başında değil)

| ne | değer |
|---|---|
| Depo | `ventures/lissom/app` |
| `HEAD` | **`8843a30`** |
| ahead / behind | **0 / 0** (push'landı) |
| çalışma ağacı | **temiz** (`kirli=0`) |
| kapılar | `all_gates.py` **exit 0** — app **202/202** (~6 atlandı) · engine **109/109** · python **20/21** |
| 21'inci kapı | `fixture_check.py` — **BİLİNEN**, paylaşımlı rig `anatomical_mode()` taşımıyor (M-F-280) |
| defter | son kayıt **`L-309`** (`ventures/lissom/app/workspace/DEFTER.md`, git İÇİNDE — 2026-08-15) |

⚠️ **Ve bu satırın kendisi bir ders taşıyor:** ölçüm ajanı bu mührü ilk turda
**turun BAŞINDAKİ** `git status` ile yazdı ve **çürüdü** (A11 iOS derlemesi
iki dosya yazmıştı). ⇒ ***Bir kapanış iddiası, turun başındaki bir ölçümle
kurulamaz: tur, o ölçümü GEÇERSİZLEŞTİRMEK için vardır.*** Kapanış
sinyallerini **kapanışta** ölç.

---

## 1. A TABLOSU — devredilen mesafe

| # | durum | tek cümlelik dayanak |
|---|---|---|
| **A1** | ✅ **BU TURDA KAPANDI** | `test/full_flow_walk_test.dart` — taze kurulum → sonuç, tek yürüyüş, tanıklı |
| **A2** | ✅ | A1'in içinde: bayrak `false` → 7 düğme → `completed true` |
| **A3** | ✅ | `6 aile hedefi = 1 içerikli ⊎ 5 boş-BEYANLI ⊎ 0 boş-SESSİZ` |
| **A4** | ⛔ | çıkmaz-sokak YASAĞI var, **A/B/C/D dağılımı yazılı DEĞİL** (sayılar §4'te hazır) |
| **A5** | ✅ *(şerhli)* | 20/21 · ⚠️ **6 öz-test tam-cümleye girmiyor** (§4) |
| **A6** | ⛔ | kapı **TEK YÖNLÜ** (§5) |
| **A7** | ✅ | 5/5 **metne karşı**, 4 sabotajla ötürtüldü |
| **A8** | ✅ | **paketten çıkarıldı** — `Runner.app/PrivacyInfo.xcprivacy` |
| **A9** | ✅ | 14 yüzey · 0 yükleyici izi · 3+60 bağımlılık bölünmüş |
| **A10** | ⛔ | Android **5/5 şablon md5'i** · iOS 1024 = Flutter logosu → **KURUCUDA** (tasarım yönü) |
| **A11** | ✅ | APK 85.8MB (`-PallowDebugSigning=true`) · `Runner.app` 45.1MB (`--no-codesign`) |
| **A12** | ⛔ ÖLÇÜLEMEDİ | cihaz VAR ama `xctrace`'e offline + `com.yulalab.lissom` **profili yok** → **KURUCUDA** |

---

## 2. A1 KÖPRÜSÜ — nereye gelindi (`8843a30`)

### Ölçülen boşluk bir SAYIYDI
`grep -rl "onboarding.continue" test/` → **5** · `grep -rl "liveCapture.finish"
test/` → **2** · **kesişim BOŞ**. Pozitif kontrol: iki tarama da dolu döndü ⇒
gerçek boşluk, aletin körlüğü değil.

> ***İKİ YEŞİL YARIM BİR YEŞİL BÜTÜN DEĞİLDİR.***

### Dikiş — yeni desen İCAT EDİLMEDİ
`LiveCaptureScreen.sourceOverride` **zaten vardı**; ona ulaşamayan
`HomeScreen`di (`lib/app/home_screen.dart`, `LiveCaptureScreen` kurulumu).
Dikiş `ageBand`ın izlediği yoldan geçirildi:

```
OnboardingGate → LissomShell → HomeScreen → LiveCaptureScreen
   (lib/app/onboarding_gate.dart · shell.dart · home_screen.dart)
```

İki yeni alan, **`storeLoader`/`shellLoader` sözleşmesiyle aynı**
(*yükleyici çağırana ait*):
- **`poseSourceLoader`** — `PoseSource Function()?`
- **`sessionStoreLoader`** — `Future<SessionStore> Function()?`

**İki adlandırma kararı, ikisi de gerekçeli (değiştirme, gerekçeyi oku):**
1. **`…Loader` = FABRİKA · `…Override` = ÖRNEK.** `FakePoseSource` akışı
   **tüketir**; tek örnek paylaşılsaydı ikinci ölçüm sessizce olaysız açılır,
   yürüyüş *"kaynak kuru"* hâlini **ürün kusuru** sanardı.
2. **`sessionStoreLoader` ≠ `storeLoader`** — ikinci ad bu ağaçta
   `OnboardingStore` için kullanılıyor; iki depo tek ad taşısaydı bir katman
   yukarıda hangisinin geçtiği **okunarak ayırt edilemezdi.**

**Üretimde davranış DEĞİŞMEDİ:** iki alan da `null` ⇒ `CameraPoseSource` /
`openSessionStore`. *Enjeksiyon yürüyüşü mümkün kılar, davranışı değiştirmez.*

### Ne denendi ve ne ödendi
🪤 `_RecordingStore` ilk yazımda `SessionStore`un üç üyesini
(`recent` · `workedSecondsFor` · `unreadableRecords`) taşımıyordu → dosya
**derlenmedi**. `unreadableRecords` için `0`, varsayılan değil **BEYAN**
olarak yazıldı (çekirdeğin kendi hükmü, M-F-228).

### Yürüyüşün ölçümü
taze kurulum (bayrak `false`, onboarding **7 dokunuş**) → Home →
*Start a measurement* → **1 rota push'u tanıklı** → enjekte kaynak →
*I'm done* → **sonuç yüzeyi** → **depoya 1 kayıt**
(`active_straight_leg_raise:right`; canlı **3/12**).
🔒 **Sabotaj ikizi:** aynı yol + boş kaynak ⇒ `finish` yok, depo boş.

### ⚠️ SINIR — dar yazıldı, genişletme
Bu yürüyüş **kamerayı KANITLAMAZ**. Kaynak `FakePoseSource`; gerçek kare
akışı, gerçek ışıkta landmark kalitesi ve kalibrasyon eşiği **cihazda
doğrulanmadı** (`live_capture_screen.dart` başlığındaki *"Bağlandı ≠ canlı"*
tablosu aynen geçerli). Kanıtlanan tam olarak: ***kullanıcının bastığı
düğmeler, taze kurulumdan bir ölçüm sonucuna kadar birbirine bağlı.***

---

## 3. SIRADAKİ SOMUT ADIM — dosya + satır

**⓵ `818d5b9`'un AÇTIĞI KAPI ADAYI (kendi commit mesajında *"sıraya alındı"*).**

**Kusur:** `pubspec.yaml` bir pod bağımlılığı kazandı (`permission_handler`,
commit `0b911ae`), `ios/Podfile.lock` **bayatladı**, ve
`ios/Runner.xcodeproj/project.pbxproj`te **`[CP] Copy Pods Resources` fazı
hiç yoktu** — yani pod kaynak paketlerini (gizlilik bundle'ı dahil) pakete
kopyalayan fazın kendisi eksikti. **21 kapının hiçbiri bunu ölçmüyor.**
`L-288`in ikizi: *dosya depoda durur, `git` mutlu, kimse fark etmez.*

**Yapılacak:** `app/tools/` altına bir kapı — `pubspec.yaml`in iOS-pod
üreten bağımlılıkları ⊆ `ios/Podfile.lock`, **ve** pod varsa
`project.pbxproj`te `Copy Pods Resources` fazı **zorunlu**.
**Model olarak `tools/privacy_manifest_check.py` alınmalı** — o dosya tam da
bu sınıfı (*"depoda var ≠ pakette var"*) çözüyor ve **paket-içi kanıt aile
referansı oldu**.

⚠️ **Kapı kurma kısıtı (ölçüt, C bölümü):** *bir kapı, ancak A tablosundaki
bir kalemin iddiasını doğruluyorsa kurulur.* Bu kapı **A8**i (manifest
PAKETTE) ve **A11**i (release derlemesi) doğrular — **kurmadan önce hangisi
olduğunu yaz.**

**⓶ A6 — ikinci yön (§5'i ÖNCE oku).**
**⓷ A4 — dağılımı yaz (§4'te sayılar hazır).**
**⓸ A5 şerhi** — `tools/all_gates.py` kapıları **argümansız** çağırıyor
(`_run([sys.executable, str(g)], ROOT)`); 6 kapının öz-testi yalnız
`--self-test` ile ateşleniyor ⇒ **tam-cümle hükmüne girmiyorlar**:
`defter_freshness` · `direction_check` · `noverdict_liveness` ·
`reachability_candidates` · `status_weave_check` · `validate_placeholder_surface`.
(Payda: 21 kapı · öz-test izi 13 · varsayılanda ateşlenen 7 · izi olmayan 8.)

**⛔ HATTA GİTMEYENLER:** **A10 ikon** (tasarım yönü) · **A12 cihaz turu +
provizyon profili** (store/kurucu). İkisi de M-F-77 gereği **kurucuda**.

---

## 4. A4 — dağılım ÖLÇÜLDÜ, YAZILMADI (ağaca geçirilmeyi bekliyor)

Choreia'nın `C-239` taksonomisi (**A** içerik yok · **A′** malzeme eksik ·
**B** kablolama boşluğu · **C** kart olmamalıydı · **D** tam ama bilerek
kapalı) bu ağaca uyarlandı:

- **Aile düzeyi — payda 6 − 1 başlatılabilir = 5 çıkmaz:**
  **A=5** (`coming_soon`, `itemsSource` yok, yalnız çocuk adları) ·
  A′=0 · B=0 · **C=0** (6 kartı göstermek IA config'te **beyan edilmiş
  kapsam standardı** + `honestyBox`, kaza değil) · D=0.
- **Test düzeyi — payda 12 = canlı 3 ⊎ engelli 9.**
  ⚠️ **En önemli bulgu: 9'u çıkmaz sokak DEĞİL** — `lib/app/library_screen.dart`
  onları **dokunulamaz** `_TestRow` olarak *"Not measured by camera (9)"*
  altında **gerekçesiyle** basıyor. *Varılamayan bir yer, çıkmaz sokak
  değildir.*

---

## 5. A6 — `262`, ve neden HAM HÂLİYLE SAHTE GEDİK olduğu

`tools/defter_freshness.py` **exit 0**, öz-test **4/4**. Ama `gap()` yalnız
`ids not in recorded` hesaplıyor ⇒ **TEK YÖN** (commit → defter).

**Payda + işlem:** taranan commit **183** · commit'in iddia ettiği benzersiz
kayıt **44** · defterde **306**.
· **YÖN-1** (commit→defter) gedik = **0** ✅
· **YÖN-2** (defter→commit) gedik = **306 − 44 = 262**

🔴 **262'yi bir kapıya bağlama.** Defter kayıtlarının çoğu **meşru olarak
commit'sizdir** (ölçüm · analiz · reddedilmiş yol · karar kaydı — hiçbiri kod
değişikliği değil). Ham ters yönü kapıya bağlamak **262 sahte gedik** üretir
ve kapı **doğduğu gün susturulur** (Gravita'nın 47 yanlış pozitifiyle aynı
sınıf).

**Doğru birim:** *"**kod değişikliği İDDİA eden** bir defter kaydının commit'i
olmalı"*. Bu bir **tanım işidir** ve önce yazılmalı.

⚠️ **Ve tanımı kurarken M-F-588 bağlayıcı:** *bir alana ayırt edici bir değer
eklerken, o alanı okuyan HER sayacın hangi dizgeye baktığı ÖNCE ölçülür* —
aksi hâlde bir iyileştirme sessizce bir sayıyı düşürür. (`L-305`te bu tam
olarak yaşandı: `REDDEDİLDİ` eklendi, kapalı sayısı **178 → 173** düştü ve
**hiçbir kapı ötmedi**; çapası `defter_freshness.reddedildi_capasi()`.)

---

## 6. TAŞINAN, ÇÖZÜLMEDİ (ölçüm ajanı dokunmadı)

- **`invert` hiçbir kontrolle korunmuyor** — `kSealedBridgedJoints` yalnız
  `metric→coreJointId`yi mühürlüyor. Borç **testin kendi gövdesinde**:
  `packages/lissom_engine/test/metric_coverage_test.dart` **~L110**.
  8 binding'in hepsi `invert: false` ⇒ **yanlış bir `true` SESSİZCE geçer.**
- Köprülenemeyen `measureKind` metrikleri (**11 adet**) + Library/Progress derinliği.
- ID çakışması **3** (`L-089`·`L-090`·`L-187`) — **SAYILI muafiyet**, yeniden
  numaralandırma **YOK**.
- **A3'ün paydası** aile hedefleridir; kalan 6 yüzeyin sessiz-boşluk oranı
  **hiç ölçülmedi** (`bilinmiyor`, `⛔` değil).

## 7. C DURMA KOŞULU

Bu tur **`⛔ → ✅` = 1** (**A1**). Sayaç sıfırlandı; hat **durmadı**.
⚠️ Ayrım: A2·A8·A9·A11 `bilinmiyor → ✅` oldu — o **kapatma değil, mesafenin
doğru ölçülmesidir** ve C sayacına **girmez**.
