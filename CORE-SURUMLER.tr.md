# Motion Core sürüm defteri

Core'a yalnız Ekip-2 yazar. Tüketiciler (Lissom: Ekip-2 · Ostinato, Choreia: Ekip-3 · JabLab, Gravita: Ekip-4)
Core'a bağlı işe başlamadan bu dosyayı okur. **Yalnız burada duyurulan SHA pinlenir**; ara commit'ler pinlenmez.
Pin her yerde **tam 40 karakter SHA** ile yazılır (pub `ref:` metin karşılaştırır; kısa SHA/tag ayrı kaynak sayılır).

Bölüm düzeni: SHA + CI · paket sürümleri · API farkı · kırıcı/deprecated · app başına değişecek satırlar ·
fikstür etkisi · canlı önkoşul · hedefli regresyon.

---

## R4.2 — `8287c5852b41b9c10994ffb22d9fab192e3c7cdd` (2026-10-29) — sunucu canlıda, Dart koruması pinle

- **Tam SHA:** `8287c5852b41b9c10994ffb22d9fab192e3c7cdd` (`main`, FF `d9dfed0..acc108d..f6fe46b..b63e8ad..8287c58`; PR kocakkmustafa/motion-core#11).
- **CI:** PR 13/13 + push run `40941209154` **13/13 success** (Yönetim: 26/26).
- **Canlı:** 2026-10-29 19:34Z, kurucu onayı, Yönetim, temiz klon @`8287c58`.
  - `db push` → `migration list --linked` 11/11.
  - `motion-parental-consent` v7 ACTIVE (`verify_jwt=false`).
  - smoke-6 PASS; doğrulama SQL `true|true|true`.
  - Log: `scratch/2026-10-29-motion-core-r42/DEPLOY-LOG.txt`. Diğer beş fonksiyon değişmedi.
- **Yerel kanıt** (exact `8287c58`, makine mutex'i, ağaç değişmedi; `runs/r42-gate-20261029T192458Z/`):
  - CI matrisi: tarama PASS, Deno **69/69**; dart 263/69/61; flutter `motion_account` **287 PASS / 5 SKIP**, diğerleri R4 ile aynı; 11 paketin analyze'ı temiz.
  - Yerel Supabase: 11 migration temiz replay, SQL **3/3**, entegrasyon **5/5**, veli onayı E2E **23/23**.
- **İçerik** (kaynak: CORE-07 §6.11 canlı testi, 29 Eki; log `scratch/2026-10-29-core-07-canli/6.11-LOG.txt`):
  - `acc108d` SMTP:
    - `MOTION_SMTP_PASSWORD`'ün baş/son boşluğu ve satır sonu her zaman silinir; iç boşluk yalnız 16 harflik Google uygulama şifresi kalırsa silinir.
    - `submitSmtpMail` sırsız sonuç döndürür (sınıf/aşama/kod).
    - `motion-parental-consent` başarısız postada tek satır loglar: `{"event":"motion_consent_mail_failed","failure":"config|network|auth|sender|recipient|message","stage":…,"code"?:…,"issue"?:"missing:<DEĞİŞKEN>"}`. Yanıt yine `503 mail_unavailable`; başarıda log yok.
  - `f6fe46b` `motion_account`: "Şifremi unuttum" ve "Doğrulamayı yeniden gönder" yalnız teslim edilebilir görünen adresle açılır. `sendPasswordReset` / `resendConfirmation` boş veya biçimsiz adreste istek atmadan `AuthException` fırlatır. auth_logs'taki `/recover` ve `/resend` 400'lerini keser.
  - `b63e8ad` migration `20261029120000_motion_restriction_own_account`: `motion_account_restricted(p)` oturumlu çağıran başka UUID sorarsa `42501` verir. `service_role` ve claim'siz oturum (SQL Editor, pg_cron) değişmez.
  - `8287c58`: tarama izin listesinde `enum MotionApp` satırı 13→14 (metin aynı).
- **Paket sürümleri:** değişmedi (`motion_account` 0.8.0). Pin tam SHA ile yapılır.
- **API farkı:** yeni public API yok (`motion_email.dart` dışa aktarılmaz).
  - Davranış farkı: iki mail metodu geçersiz adreste ağdan önce reddeder.
  - Sayfada iki düğme e-posta alanı geçerli adres taşıyana kadar `onPressed: null`.
- **R4/R4.1'den geçiş (app'ler):** **isteğe bağlı, yalnız pin.**
  - Sunucu parçaları canlıda; eski pinli build'ler de yararlanır.
  - Boş e-posta koruması yalnız R4.2 pinli **yeni build**le kullanıcıya ulaşır.
  - Kurucu/Yönetim kararı (29 Eki): **mağaza adayları şimdilik eski pinde kalır**; R4.2 sonraki build'de.
- **Fikstür etkisi (app testleri):** e-posta yazıp **aynı karede** "Forgot password"/"Resend verification email"e basan widget testi artık düşer. Düğme bir sonraki karede açılır: `enterText` sonrası `await tester.pump();` ekleyin (Core T08 aynı düzeltmeyi aldı). Boş alanla bu düğmelere basıp çağrı bekleyen testler de değişmeli.
- **Hedefli regresyon (pinleyen app):** giriş ekranında boş/yarım adresle iki düğme kapalı, geçerli adresle açık; sıfırlama ve yeniden gönderme postası geliyor; mevcut hesap/üyelik akışları R4 listesiyle.
- **Açık iş (Core dışı, Yönetim):** 30 gün temizlik cron'u kurucu onaylı. yulalab.com'da "abonelik iptal olmaz" metni yayınlanınca Yönetim kuru sayım + `cron.schedule` kuracak. Silme günlüğü önerisi: `scratch/2026-10-29-motion-core-r42/HUKUK-5-SAKLAMA-ONERI.tr.md`.

---

## R4.1 — `d9dfed0675a2282a7cf380de774b87e0489df277` (2026-10-27) — yalnız sunucu + belge

- **Tam SHA:** `d9dfed0675a2282a7cf380de774b87e0489df277` (`main`, FF `0d29d1b..d9dfed0`)
- **CI:** run `40484987831` — **13/13 success**
- **Yerel kanıt:** `deno fmt --check` + `deno check` (CI komutu) temiz; Deno **64/64** (R4 63 + 1 yeni); kelime taraması PASS. Dart kodu değişmedi (yalnız `motion_account/README.md`).
- **İçerik:** kurucu **K-3** — `motion-parental-consent` varsayılan CORS izin listesi = `https://yulalab.com` + `https://www.yulalab.com` (önizleme origin'i yok); canlıda `MOTION_CONSENT_ALLOWED_ORIGINS` secret'ı **girilmez**. Sözleşme testleri: iki origin preflight `204` + ACAO yansıtma + `view` yanıtında ACAO; `https://evil.example`, `http://yulalab.com`, `https://yulalab.com.evil.example`, `https://preview.yulalab.com`, `https://www.yulalab.com:8443`, `null` → `403`, ACAO yok. Kurucu **K-2** belgelere işlendi (beş app `storeFamilyControls`; paket varsayılanı aynı).
- **R4'ten geçiş (app'ler):** **gerekmez** — R4 pini geçerli; R4.1'e pin isteğe bağlıdır (Dart farkı yok). K-2 için app'ler R4 API'siyle `teenPurchasePolicy: MotionTeenPurchasePolicy.storeFamilyControls` verir (satırlar R4 "App başına").
- **Canlı:** CORE-07 paketi kaynak R4.1 olarak tazelendi (3.2 secret yok/varsa unset; 6.2 iki origin `204`; 6.3 dört yabancı origin `403`; 7.2 yalnız-CORS geri alma).
- **Site (YULALAB):** CSP `connect-src https://aljdbngmeqwmsqhvfeau.supabase.co` aynı; `www` bugün 301 ile apex'e yönleniyor, yönlendirme kalkarsa da onay sayfası çalışır.

## R4 — `0d29d1b019033f00828be741aa3e23e3923841be` (2026-10-27)

- **Tam SHA:** `0d29d1b019033f00828be741aa3e23e3923841be` (`main`, FF `f43d71a..6b845d6..826cdfc..0d29d1b`)
- **CI:** run `40434457573` — **13/13 success** (ara SHA'lar pinlenmez: `6b845d6` 40431425936 13/13 success; `826cdfc` 40432226713 **12/13 FAIL** — `motion_camera` analyze `prefer_initializing_formals`, kök: Dart 3.12 dil sürümü bump'ı, `0d29d1b` ile düzeltildi)
- **Yerel kanıt (exact `0d29d1b`, kendi klonu + `pub get --offline`, makine mutex'i, CI'nın 13 işinin tamamı — `scratch/2026-10-27-motion-core-r4/ci_full.sh`):** tarama PASS, Deno **63/63**; dart `motion_core` **263**, `motion_content` **69**, `motion_media` **61**; flutter `motion_camera` **60**, `motion_feedback` **12**, `motion_audio` **20**, `motion_store` **58**, `motion_entitlements` **80**, `motion_account` **285 PASS / 5 SKIP**, `motion_platform_signals` **4**, `motion_telemetry` **79**; 11 paketin analyze'ı temiz; ağaç değişmedi (`runs/r4-gate-0d29d1b-20261027T012620Z/`). **Android release AAB:** Choreia `ceb612e` klonu + `pubspec_overrides.yaml` ile yerel R4 (`motion_*` 7 paket), `flutter build appbundle --release`, debug anahtarı (`allowDebugSigning`; gerçek anahtar/define yok, **upload yok**) → PASS, 98 MB, sha256 `80713125fc834c0d…`; **"plugins that apply Kotlin Gradle Plugin" uyarısı artık yok** (25 Ekim R3 AAB'sinde `motion_camera, motion_platform_signals` listeleniyordu); iki eklentinin `kotlin-classes/release` çıktısı ve dex'te kanal adı + Play Age Signals referansları var (`runs/r4-aab-826cdfc-20261027T011440Z/`; `0d29d1b`'de aynı tutuşta yeniden PASS, aynı sha256). Kalan uyarı yalnız app'in kendi `android/app/build.gradle.kts` KGP'si (app oturumlarının işi, aşağıda).
- **İçerik:** CORE-12 `6b845d6` (ET3-4, OST-K1) app başına 13–17 satın alma politikası · CORE-13 `826cdfc` + `0d29d1b` (ET3-5) `motion_camera` + `motion_platform_signals` → Flutter Built-in Kotlin · CORE-14 (ET3-3) belge tutarlılığı (workspace; posta secret adları yalnız `MOTION_SMTP_*`).
- **R3'ten geçiş:** **yalnız pin.** Kaynak kırıcı değişiklik yok; varsayılan davranış R3 ile aynı. `supabase/` ve `.github/` R3 → R4 değişmedi (canlı deploy içeriği aynı).

### Paket sürümleri
| Paket | R3 | R4 |
|---|---|---|
| `motion_account` | 0.7.0 | **0.8.0** |
| `motion_platform_signals` | 0.2.0 | **0.3.0** (Built-in Kotlin; Flutter ≥3.44; Dart dil sürümü 3.11 kalır) |
| `motion_camera` | 0.2.0 | **0.3.0** (Built-in Kotlin; Flutter ≥3.44; Dart dil sürümü 3.11 kalır) |

### API farkı
| Alan | R4 |
|---|---|
| `MotionTeenPurchasePolicy` (yeni enum, `motion_release_policy.dart`) | `parentalConsentRequired` (**varsayılan**, R3 davranışı: veli onayı bekleyen gence satın alma teklifi yok, geri yükleme açık) · `storeFamilyControls` (teklifler açık; ödeme kararı mağazanın aile/ebeveyn denetiminde — Ask to Buy / Google Play ebeveyn onayı; sayfada 14 dil 18 yaş altı notu `storeFamilyControlsNote`). İki politikada da hesap özellikleri veli onayına kadar kapalı (RLS aynen), **13 yaş altı bandı hiç satın alamaz**, sunucu doğrulaması değişmez. |
| `teenPurchasePolicy:` (yeni isteğe bağlı parametre) | `MotionMembershipPage`, `MotionAccountPage` (açtığı üyelik sayfasına iletir), `requireMotionPaidAccess` ve `requireMotionCameraAccess` (varsayılan üyelik sayfasına iletir). **Kendi `membershipPageBuilder`'ını veren host, politikayı oradaki `MotionMembershipPage`'e de vermelidir.** |
| `MotionAgeStatus.purchaseRestrictedOn(today, policy)` / `.storeDecidesPurchaseOn(today, policy)` | Yeni extension (`MotionTeenPurchaseStatus`); host kendi yüzeylerinde aynı kuralı okuyabilir. |
| Android eklentileri | `kotlin-android` + `kotlinOptions` kaldırıldı → `kotlin.compilerOptions { jvmTarget = JVM_17 }` (Flutter plugin-author kılavuzu; `in_app_purchase_android` 0.5.3 deseni). Dart API'si ve native davranış aynı. |

### Kırıcı / dikkat
1. Kaynak kırıcı değişiklik yok (yalnız isteğe bağlı parametre/enum/extension).
2. **Asgari araç zinciri:** `motion_camera` ve `motion_platform_signals` artık Flutter ≥3.44 ister (Dart alt sınırı `^3.11.0` aynı). Beş app'in CI'ı `stable` (JabLab/Gravita 3.47.5) ve yerel 3.47.5 → etkilenmez; daha eski bir Flutter ile `pub get` reddeder.
3. Android: app'ler `android.builtInKotlin=false` + AGP 9.4 + KGP 2.4.10 ile derlemeye devam eder (Choreia AAB kanıtı). App'in **kendi** KGP uyarısı ayrı iştir (Flutter app-developer kılavuzu: `android.builtInKotlin=true` + app `build.gradle.kts`'ten `kotlin-android`'i kaldırma) — R4 bunu gerektirmez.
4. **Hukuk/ürün (K-2 ile birlikte):** onaylanmayan genç hesabı 30 gün sonra silinir (`motion_purge_unconsented_accounts`, zamanlaması ayrı onay); `storeFamilyControls` ile satın alan gencin mağaza aboneliği bununla iptal olmaz, yeni/onaylı hesapta geri yüklenir. Yayın profili §9 ve `lib/docs/compliance/YAS-VELI-VE-SAKLAMA.md`.

### App başına değişecek satırlar
- **Beş app:** pin satırlarında SHA → `0d29d1b019033f00828be741aa3e23e3923841be`; ağlı `flutter pub get` (`pubspec.lock`'ta Core ref/resolved-ref satırları); iOS `pod install` (pod sürümü değişmez). Başka satır **gerekmez** (varsayılan politika).
- **Ostinato (OST-K1, `storeFamilyControls`):** `lib/app/motion_account_bootstrap.dart:86` `MotionAccountPage(…, teenPurchasePolicy: MotionTeenPurchasePolicy.storeFamilyControls)`, `:120` `requireMotionPaidAccess(…, teenPurchasePolicy: …)`, `:126` `requireMotionCameraAccess(…, teenPurchasePolicy: …)` (kamera kapalıyken etkisiz ama tutarlılık için). Doğrudan `MotionMembershipPage` açılan yer varsa orada da. S12 senaryosu: `scratch/2026-10-25-motion-core-packages/CORE-R3-KABUL-KONTROLLERI.tr.md` "R4 eki" S-R4-1…5.
- **K-2 = beş app (kurucu 2026-10-27, karar verildi):** diğer dört app de aynı parametreyi şu yerlere verir: Lissom `lib/main.dart:518, 605, 612`; Choreia `lib/main.dart:290, 361, 396`; JabLab `lib/main.dart:125, 131` (kendi `MotionMembershipPage` builder'ı), `:166`, `lib/app/owner_bound_account_page.dart:104`; Gravita `lib/app/motion_account_bootstrap.dart:109` (kendi builder), `:111`, `lib/app/gravita_account_page.dart:181`. (Satırlar app main HEAD'lerine göre: Lissom `e455e27`, Ostinato `9a5e570`, Choreia `ceb612e`, JabLab `b4a3d0f`, Gravita `df9f14c`.)

### Fikstür etkisi
- Varsayılan politikada yok. `storeFamilyControls` testlerinde onay bekleyen genç (`MotionAgeStatus` band `parentalConsentRequired`, consent ≠ approved) için teklifler ve not metni beklenir; satın alma başlayınca sayfa mağaza yanıtına kadar meşgul kalır (`pumpAndSettle` yerine `pump`).

### Canlı önkoşul
- R3 ile aynı (CORE-07, `scratch/2026-10-25-motion-core-packages/CORE-07-CANLI-DEPLOY.tr.md`, kaynak R4 olarak tazelendi; ref `aljdbngmeqwmsqhvfeau` Y1 teyitli). R4 yeni migration/fonksiyon/secret getirmez.

### Hedefli regresyon
- Beş app: pin eşitlik testleri yeni tam SHA'da; hesap/üyelik sayfası açılışı; onay bekleyen genç → (varsayılan) teklif yok + geri yükleme açık; Android release/debug derleme (yeni Gradle eklenti yapılandırması).
- Ostinato: S12 / S-R4-1…5 (onay bekleyen genç teklifleri ve notu görür; Ask to Buy / Play ebeveyn onayı bekleyen satın alma aktif sayılmaz; 13 altı satın alamaz).

---

## R3 — `f43d71a375431e96c689a7a4a04fb53ff01af693` (2026-10-25)

- **Tam SHA:** `f43d71a375431e96c689a7a4a04fb53ff01af693` (`main`, FF `2451428..f43d71a`)
- **CI:** run `40145997799` — 13/13 success (ara: `c190d03` 40144648401, `dbab1af` 40144654422, `3b3a840` 40145470685 — 12/12; `2bc72f0` 40145476157 — 13/13; `ce16d70`/`c4b8c21`/`d23297b` ayrı push edilmedi) — **artık 13 iş** (yeni `motion_platform_signals` paketi flutter matrisine girdi; "12/12" yerine 13/13 beklenir)
- **Yerel kanıt:** exact `f43d71a` (ekip kilidi + makine mutex'i, RELEASED): tarama PASS, Deno **63/63**, `motion_entitlements` **80/80**, `motion_account` **281 PASS / 5 SKIP**, `motion_platform_signals` **4/4**; aynı tutuşta **native derleme**: imzasız probe app → `pod install` + iOS simülatör `Runner.app` + Android `app-debug.apk` (age-signals 0.0.4 çözüldü). Makbuz `scratch/2026-10-25-motion-core-r3/runs/k1-full-f43d71a-*` + `runs-multi/k1/` + `native-probe/`. Yerel Supabase (Docker) `2bc72f0`'da: replay + SQL **3/3** (deneme defteri dahil) + entegrasyon 5/5 + consent E2E 23/23 (`runs/k3-full-2bc72f0-*`, `local-acceptance-2bc72f0/`); `supabase/` ve `.github/` `2bc72f0..f43d71a` arasında değişmedi.
- **Kurucu kararı (2026-10-25):** K1 mağaza yaş sinyali, K2 mağaza sunucu bildirimleri, K3 hesap başına tek Motion+ denemesi — üçü de ilk sürümden önce. Plan: `scratch/2026-10-25-motion-core-r3/PLAN.tr.md`.
- **İçerik (ara SHA'lar pinlenmez):** K2 `c190d03` (paylaşılan mağaza yeniden doğrulaması) + `dbab1af` (`motion-store-notifications`) · K3 `3b3a840` (sunucu) + `ce16d70`/`c4b8c21`/`2bc72f0` (istemci, native paket) · K1 `d23297b` + `f43d71a`.

### Paket sürümleri
| Paket | R2 | R3 |
|---|---|---|
| `motion_account` | 0.5.0 | **0.7.0** |
| `motion_entitlements` | 0.3.0 | **0.4.0** |
| `motion_platform_signals` | — | **0.2.0 (yeni, native Flutter eklentisi: iOS Swift + Android Kotlin)** |

### API farkı
| Alan | R3 |
|---|---|
| **Yeni paket** `motion_platform_signals` | `MotionPlatformSignals.appTransactionId()` (StoreKit 2 `AppTransaction.appTransactionID`, iOS 16+, yalnız doğrulanmış; Android null) · `MotionPlatformSignals.requestAgeSignal()` → `MotionStoreAgeSignal{source, shared, lower, upper, declaration}` (iOS 26+ Declared Age Range, eşikler 13/16/18; Android Play Age Signals 0.0.4). Her hata/desteklenmeyen durum `null`. `motion_account` bunu bağımlılık olarak çeker ve `MotionStoreAgeSignal`'ı re-export eder. |
| `MotionAccountPage(storeAgeSignal:)` | **Yeni** isteğe bağlı (varsayılan `MotionPlatformSignals.requestAgeSignal`). Kayıt ve tek seferlik yaş onayında **sayfa başına bir kez** okunur (en fazla 2 dk). |
| `MotionAgePolicy.storeCheck(declaredAge, signal)` → `MotionStoreAgeCheck{proceed, under13, mismatch}` | Mağaza sinyali **yalnız sıkılaştırır**: mağaza <13 → kalıcı blok (`onAgeBlocked`, misafir kullanım açık); beyan mağaza üst sınırından büyük → reddedilir, düzeltme mesajı (14 dil, `ageStoreMismatch`); aksi hâlde ülke/veli onayı akışı aynen. Sinyal yoksa bugünkü akış. |
| `MotionTrialGate` / `SupabaseMotionTrialGate` (`motion_entitlements`) | **Yeni.** Hesap başına tek Motion+ denemesi: kendi `motion_trial_ledger` satırı (RLS) + `motion-offer-eligibility`. |
| `FlutterPurchaseAdapter(trialGate:)` | **Yeni** isteğe bağlı. Motion+ ürünlerinde kullanılmış/bilinmeyen deneme: Play deneme teklifi seçilmez (base plan), App Store satın almasına imzalı `introductoryOfferEligibility=false` eklenir (`Sk2PurchaseParam`), deneme iddiası gösterilmez. Bireysel planlar etkilenmez. Kapı verilmezse davranış R2 ile aynı. `MotionMembershipPage` varsayılan adaptörüne kapıyı kendisi bağlar. |
| `motion-check-membership` yanıtı | Ek alan `motionPlusTrialAvailable: bool` (geriye uyumlu). |
| Yeni Edge `motion-store-notifications` | `POST …/apple` (ASSN v2, Apple JWS zinciri) · `POST …/google` (Play RTDN Pub/Sub push, Google OIDC). İmzasız → 401; doğrulanmış bildirim yalnız mağazadan yeniden doğrulamayı tetikler. `verify_jwt=false`. |
| Yeni Edge `motion-offer-eligibility` | Bearer; `{appId, productId(Motion+ App Store), appTransactionId}` → `{trialAvailable:true}` veya `{trialAvailable:false, introductoryOfferEligibilityJws}`. |
| Migration `20261025120000_motion_trial_ledger` | Hesap başına tek satır (Motion+), sunucu yazar, istemci yalnız kendi `app_id/started_at`'ini okur, hesapla silinir. |

### Kırıcı / dikkat
1. **Yeni native bağımlılık:** pin sonrası iOS `pod install` (yeni pod `motion_platform_signals`, min iOS 15) ve Android'de yeni Maven bağımlılığı `com.google.android.play:age-signals:0.0.4` (Gradle indirir). Derleme doğrulandı: imzasız probe app (iOS simülatör + Android debug) — makbuz aşağıda.
2. **Widget testleri:** Kayıt/yaş onayı yapan `MotionAccountPage` testleri artık platform kanalını çağırır (eklenti yoksa `null`, ama asenkron) → testte `storeAgeSignal: () async => null` geçin; mağaza sinyali senaryoları için sahte `MotionStoreAgeSignal` verin.
3. **Varsayılan `MotionMembershipPage`** (enjekte adaptör yoksa) Motion+ ürünlerinde `GET /rest/v1/motion_trial_ledger` okur → `extends` eden fake'ler bu isteğe `[]` dönmeli (yoksa deneme gösterilmez, satın alma çalışır).
4. Kaynak kırıcı imza değişikliği yok (yalnız isteğe bağlı parametre/alan).

### App başına değişecek satırlar
- Pin satırlarında SHA → `f43d71a375431e96c689a7a4a04fb53ff01af693`; ağlı `flutter pub get` (`pubspec.lock`'a `motion_platform_signals` git girdisi eklenir) + iOS `pod install`.
- **iOS (beş app):** `ios/Runner/Runner.entitlements`'a `com.apple.developer.declared-age-range` = `true` + Xcode Signing & Capabilities → Declared Age Range; Apple Developer'da App ID capability (Yönetim, CORE-07 2.5d). Entitlement yoksa sinyal `null` → mevcut akış (zararsız ama K1 devre dışı).
- **Android:** ek satır yok (izin gerekmiyor; Play Age Signals yalnız desteklenen bölgelerde döner).
- R1/R2 kaynak değişiklikleri yapılmadıysa onlar da.

### Fikstür etkisi
- Bkz. kırıcı/dikkat 2–3. Deno/SQL fikstürleri app'leri etkilemez.

### Canlı önkoşul (CORE-07 2.5b–2.5d, 3.7–3.8)
- Deploy: migration `20261025120000`; fonksiyonlar `motion-store-notifications` (verify_jwt=false), `motion-offer-eligibility` + güncel `motion-verify-purchase`/`motion-check-membership`.
- Secret adları (sır değil): `MOTION_RTDN_AUDIENCE`, `MOTION_RTDN_PUSH_SERVICE_ACCOUNT`; mevcut `MOTION_APPLE_IAP_*` (bildirim doğrulama + eligibility imzası), `MOTION_APPLE_ROOT_CAS_BASE64`.
- ASC: 5 app × ASSN v2 URL (prod + sandbox). GCP: Pub/Sub topic + push abonelik (OIDC). Play: RTDN topic; Motion+ deneme teklifi "Developer determined" + tag `motion-plus-trial`. Apple: Declared Age Range capability.

### Bilinen sınırlar / UNKNOWN
- **iOS 15** veya doğrulanmış app transaction yoksa ikinci Motion+ denemesi engellenemez (Apple grup bazlı uygunluk).
- Play `offerPhase` alan yeri belge çelişkili → deneme tespiti tag **veya** faz; sandbox'ta doğrulanmalı.
- Gerçek mağaza sinyali yalnız cihaz/mağaza hesabıyla ölçülür (iOS 26+, ilgili bölgeler) → UNKNOWN; mağaza ebeveyn onayı durumu ve "önemli değişiklik" bildirimi R3'te yok.
- Hesap silinip yeniden açılırsa deneme defteri sıfırlanır (kısa saklama kuralı); mağazaların kendi uygunluk kuralları ayrıca geçerli.

### Hedefli regresyon
- R2 listesi + kayıt formu: mağaza sinyali yok/aralık içi/uyuşmazlık/13 altı (sahte sinyal).
- Üyelik sayfası: Motion+ deneme gösterimi kapı açık/kapalı; bireysel plan değişmez.
- Derleme: `pod install` + iOS sim build + Android debug build (yeni native paket).
- Sandbox (Yönetim): app A'da Motion+ denemesi → app B'de deneme yok (iOS 16+ ve Play).

---

## R2 — `2451428dea30fb9e29db819441bfd5a4fe35adaf` (2026-10-25)

- **Tam SHA:** `2451428dea30fb9e29db819441bfd5a4fe35adaf` (`main`, fast-forward push `cdcbf04..2451428`)
- **CI:** run `40142159830` — 12/12 success (ara SHA'lar: `b0b27b7` 40142149306, `0bae251` 40142154564; ikisi de 12/12, yalnız R2 ucu pinlenir)
- **Yerel kanıt (exact SHA, ekip kilidi + makine mutex'i):** `2451428` CI-eşdeğeri — tarama PASS, Deno **42/42** (+6 SMTP birim, +1 Play deneme fazı, +2 sözleşme dosyasında SMTP), `motion_entitlements` **70/70** (+8 deneme), `motion_account` **276 PASS / 5 SKIP**; aynı tutuşta yerel Supabase (Docker): temiz replay 9 migration + SQL **2/2** + entegrasyon **5/5** + veli onayı E2E **23/23**, posta **SMTP üzerinden** (functions → `host.docker.internal:5498` düz metin yerel havuz; 2 posta, TR konu UTF-8). Makbuz: `scratch/2026-10-25-motion-core-r2/runs/r2-full-2451428-20261024T231330Z/` + `local-acceptance-2451428/`. Ara SHA'lar exact PASS: `runs/r2-exact-b0b27b7-0bae251-20261024T224715Z/`. **Implicit TLS (465) loopback makbuzu:** üretim `sendSmtpMail` + `Deno.connectTls` → test CA'lı SMTPS havuzu, el sıkışma OK, posta alındı (`scratch/2026-10-25-motion-core-r2/smtps/receipt.txt`). Canlı Edge'den 465 çıkışı UNKNOWN (CORE-07 smoke 3.4).
- **İçerik:** CORE-03 `b0b27b7` mağaza ücretsiz denemesi (Android deneme teklifi + iOS SK2 tanıtım teklifi) · CORE-05 `0bae251` veli onayı postası Google Workspace SMTP 465 · Lissom LIS-01 talebi `2451428` (kalıcı yaş bloğunda açıklama).
- **R1'den geçiş:** R1 (`cdcbf04`) için yapılan app değişiklikleri aynen geçerli; R2 ek kaynak değişikliği istemez. **Doğrudan R2'ye pinlemek önerilir** (R1 pin'i atlanabilir).

### Paket sürümleri
| Paket | R1 | R2 |
|---|---|---|
| `motion_account` | 0.4.0 | **0.5.0** |
| `motion_entitlements` | 0.2.0 | **0.3.0** (yeni doğrudan bağımlılık `in_app_purchase_storekit ^0.4.13`; önceden geçişli olarak çözülüyordu) |

### API farkı
| Alan | R2 |
|---|---|
| `StoreProductRef.freeTrialPeriod` | **Yeni** `String?` (ISO-8601; gün/hafta → gün, ör. `P14D`) + `freeTrialDays` getter. Yalnız mağaza bu hesaba ücretsiz deneme sunduğunda dolu; yoksa/uygunluk okunamazsa null (deneme iddiası yok). `localizedPrice` her zaman yinelenen fiyattır. |
| `FlutterPurchaseAdapter` (Android) | İlk fazı ücretsiz + sonlu, ardından ücretli faz gelen Play teklifi base plan'a bağlanır; satın alma o teklifin `offerToken`'ı ile yapılır. Ücretli tanıtım fiyatları satılmaz. Teklif kimliğine değil faza bakılır. |
| `FlutterPurchaseAdapter` (iOS) | StoreKit 2 tanıtım teklifi `freeTrial` ise ve `SK2Product.isIntroductoryOfferEligible` true dönerse deneme gösterilir. Yeni isteğe bağlı kurucu parametresi `introductoryOfferEligible` (test enjeksiyonu). |
| `MotionMembershipPage` | Deneme varsa satır: "N gün ücretsiz, ardından aylık/yıllık {mağaza fiyatı}" + deneme yenileme/iptal metni (24 saat kuralı), 14 dil. Yeni `MotionAccountLocalizations.trialThenPrice(...)`. |
| `MotionAccountPage(ageBlocked: true)` | Kayıt formunda 13+ açıklaması artık açılışta da görünür (önceden yalnız oturum içi engelde). |
| Veli onayı postası (Edge) | HTTP posta adaptörü ve `MOTION_MAIL_API_URL` / `MOTION_MAIL_API_KEY` **kaldırıldı**. Yeni: `MOTION_SMTP_HOST` (`smtp.gmail.com`), `MOTION_SMTP_PORT` (465), `MOTION_SMTP_USER`, `MOTION_SMTP_PASSWORD` (Workspace uygulama şifresi), `MOTION_SMTP_TLS` (`implicit`; `none` yalnız `127.0.0.1`/`localhost`/`::1`/`host.docker.internal`), `MOTION_MAIL_FROM` (doğrulanan hesap veya "send as" takma adı), `MOTION_CONSENT_PAGE_URL`. Eksik/güvensiz yapılandırma → `503 mail_unavailable` (fail closed). Parola/adres/gövde loglanmaz. HTTP sözleşmesi (view/decide/CORS) değişmedi. |

### Kırıcı / deprecated
- Kaynak kırıcı değişiklik yok (yalnız isteğe bağlı alan/parametre eklendi).
- `StoreProductRef`'i `implements` eden fake yoksa etki yok; const kurucu genişledi (isteğe bağlı alan).
- **Canlı kırıcı:** Edge posta ayarları HTTP'den SMTP'ye geçti — eski `MOTION_MAIL_API_*` secret'larıyla posta gitmez (canlıda hiç deploy edilmemişti).

### App başına değişecek satırlar
- Yalnız pin: R1 tablosundaki pin satırlarında SHA → `2451428dea30fb9e29db819441bfd5a4fe35adaf` + ağlı `flutter pub get` (`pubspec.lock`'ta Core ref/resolved-ref satırları değişir; `in_app_purchase_storekit` zaten geçişli olarak çözülüyordu, sürüm aynı kalmalı — farklıysa bildirin).
- R1 kaynak satırları henüz yapılmadıysa onlar da (R1 bölümü).

### Fikstür etkisi
- Sahte `PurchaseAdapter`/`StoreProductRef` kullanan testler değişmez (alan isteğe bağlı). Deneme metnini test etmek için `freeTrialPeriod: 'P14D'` geçin.
- `FlutterPurchaseAdapter` + sahte `InAppPurchasePlatform` (iOS) testleri: `AppStoreProduct2Details` kullanılıyorsa `introductoryOfferEligible` enjekte edin (yoksa gerçek native çağrı denenir → hata → deneme gösterilmez).
- Hesap sayfası testlerinde `ageBlocked: true` ile kayıt formunda 13+ metni artık **bir kez** görünür; metni sayan testler güncellenir.
- Deno: `deno test` artık `--allow-net=127.0.0.1` ister (Core CI'da; app'leri etkilemez).

### Canlı önkoşul (CORE-07)
- R1 önkoşullarına ek: posta secret adları `MOTION_SMTP_HOST=smtp.gmail.com`, `MOTION_SMTP_PORT=465`, `MOTION_SMTP_TLS=implicit`, `MOTION_SMTP_USER`, `MOTION_SMTP_PASSWORD`, `MOTION_MAIL_FROM`, `MOTION_CONSENT_PAGE_URL`; gönderen hesapta 2SV + uygulama şifresi + "send as". Paket: `scratch/2026-10-25-motion-core-packages/CORE-07-CANLI-DEPLOY.tr.md` (deploy bu SHA'dan).
- Mağaza: deneme ancak konsolda kurulursa uygulanır (CORE-09 kataloğu: Apple "Free, 2 weeks", Play `free-trial` teklifi P14D).
- Gerçek Edge'de `Deno.connectTls` 465'in çalıştığının ilk kanıtı canlı smoke 3.4'tür; yerel kanıt SMTP protokolü + loopback TLS'tir.

### Hedefli regresyon
- R1 listesi + üyelik sayfası: deneme satırı (sahte `freeTrialPeriod: 'P14D'`) ve denemesiz satır; satın alma akışı değişmeden çalışır.
- Kalıcı yaş bloğu: öldür-aç sonrası kayıt formunda 13+ açıklaması (Lissom B07).
- Android sandbox (Yönetim): deneme teklifiyle satın alma `offerToken` = deneme teklifi (Play Console'da yeni müşteri koşulu).

---

## R1 — `cdcbf0484e82806094ecf010b294debc3c8c5c83` (2026-10-25)

- **Tam SHA:** `cdcbf0484e82806094ecf010b294debc3c8c5c83` (`main`, origin'e fast-forward push)
- **CI:** run `40139998394` — 12/12 success (ara SHA'lar: `284298b` 40139626246, `5fadcaf` 40139989949; ikisi de 12/12, ama yalnız R1 ucu pinlenir)
- **Yerel kanıt (exact SHA, ekip kilidi + makine mutex'i, RELEASED):** `cdcbf04` CI-eşdeğeri — tarama PASS, Deno **33/33**, `motion_entitlements` **62/62**, `motion_account` **273 PASS / 5 SKIP** (5 SKIP = yerel Supabase entegrasyonu). Makbuz: `scratch/2026-10-25-motion-core-r1/runs/r1-exact-5fadcaf-cdcbf04-20261024T224527Z/` + `runs-multi/r1-exact-3/`. Yerel Supabase kabulü (Docker, exact `cdcbf04`): temiz replay 9 migration + SQL **2/2** + entegrasyon **5/5** + veli onayı E2E **23/23** PASS (`scratch/2026-10-25-motion-core-r1/runs/local-acceptance-cdcbf04-20261024T224654Z/`, çıktılar `local-acceptance-cdcbf04/`). **CORS curl yerelde kanıt değil:** Supabase CLI'nin yerel Kong'u fonksiyon rotasına kendi `cors` eklentisini koyuyor (OPTIONS 200 + `Access-Control-Allow-Origin: *`, POST'ta da `*`), istek fonksiyona ulaşmıyor (`cors.txt`). Fonksiyonun CORS davranışı Deno sözleşme testleriyle kanıtlı (4 test); **canlı ağ geçidinin davranışı UNKNOWN** — CORE-07 smoke 3.2/3.3 ilk gerçek kanıttır (canlı da `*` eklerse izin listesi etkisiz kalır; YULALAB sitesi yine çalışır).
- **Önceki pin:** beş app'in `main`'i `583203112c94…` (`5832031`). `260b2ad` hiçbir app'te pinlenmedi; R1 onu da içerir (`30a2cb2` mağaza ülkesi, `c530309` satış sabiti + kısıtlı gence satın alma engeli, `260b2ad` yaş metadata soyma migration'ı).
- **İçerik:** CORE-01 `284298b` üyelik Future sızıntısı · CORE-02 `5fadcaf` bayrak bölme + ders kilidi API'si · CORE-04 `cdcbf04` veli onayı CORS.

### Paket sürümleri
| Paket | Önce | R1 |
|---|---|---|
| `motion_account` | 0.3.0 | **0.4.0** |
| `motion_entitlements` | 0.1.1 | **0.2.0** |
| diğerleri | değişmedi | — |

### API farkı
| Alan | R1 sözleşmesi |
|---|---|
| Kamera kapısı | **Yeni** `const bool motionCameraCoachingAvailable = false;` (`motion_account`). Kamera/ölçüm/puanlama kapısı **yalnız** buna bağlanır. |
| Eski bayrak | `motionPaidFeaturesAvailable` **@Deprecated**, değeri **false kalır** (= `motionCameraCoachingAvailable`). Asla true yapmayın. |
| Satış bayrağı | `motionSubscriptionSalesAvailable = true` (değişmedi). |
| `requireMotionPaidAccess` | Yeni parametre `salesAvailable` (varsayılan `motionSubscriptionSalesAvailable` = **true**). Eski `paidFeaturesAvailable` deprecated alias; verilirse o kazanır. Ücretli ders / bağımsız pratik başlangıcında çağrılır: oturum yoksa hesap sayfası, üyelik yoksa üyelik sayfası açılır, dönüşte yeniden doğrular. |
| `requireMotionCameraAccess` | **Yeni.** Aynı imza + `cameraCoachingAvailable` (varsayılan `motionCameraCoachingAvailable` = false). Kapalıyken "gelecek güncellemede" bildirimi + `false`; hesap/satın alma adımı yok. Açıldığında `requireMotionPaidAccess` ile aynı kontrol. |
| `MotionAccountPage` | Yeni `membershipAvailable` (varsayılan `motionSubscriptionSalesAvailable` = **true**): üyelik satırı + "Üyelik seçenekleri" + açılışta üyelik sorgusu. Eski `paidFeaturesAvailable` deprecated alias (`bool?`), verilirse o kazanır. |
| Ders kilidi (`motion_entitlements`, yeni) | `int motionFreeLessonLimit({required int totalLessons, required int firstModuleLessonCount, int? freeLessonLimit})` = `max(firstModuleLessonCount, ceil(totalLessons/3))`, `totalLessons` ile sınırlı; `freeLessonLimit` verilirse app'in onaylı sayısı aynen kullanılır.<br>`bool isLessonUnlocked({required int lessonIndex /*0 tabanlı*/, required int totalLessons, required int firstModuleLessonCount, required bool entitled, int? freeLessonLimit})` — `entitled` her dersi açar.<br>`bool isPracticeUnlocked({required bool entitled})` — bağımsız pratik yalnız abonelikle.<br>Geçersiz sayı/indeks `RangeError`. **İlerleme okuma hiç kilitlenmez.** |
| Üyelik sorgusu ömrü (CORE-01) | Sayfanın başlattığı üyelik sorgusu sayfa ömrüne ve sahibine bağlı: yeni sorgu, sahip değişimi, auth stream hatası veya `dispose` eskisinin sonucunu yayınlamaz; geç hata yakalanmamış zone hatası olmaz. Güncel sorgunun hatası yine "Membership unavailable". API değişmedi. |
| Veli onayı HTTP (CORE-04, YULALAB) | `POST https://<ref>.supabase.co/functions/v1/motion-parental-consent` gövdesi değişmedi (`view`/`decide`). **Yeni:** izinli origin'den `OPTIONS` → `204` + `Access-Control-Allow-Origin: <origin>` (yansıtılır, `*` yok), `Access-Control-Allow-Methods: POST, OPTIONS`, `Access-Control-Allow-Headers: authorization, x-client-info, apikey, content-type`, `Access-Control-Max-Age: 600`, `Vary: Origin`. İzinsiz origin preflight → `403`, ACAO yok. Tüm yanıtlarda (hata dahil) `Vary: Origin`, ACAO yalnız izinli origin'e. İzin listesi env `MOTION_CONSENT_ALLOWED_ORIGINS` (virgülle; varsayılan `https://yulalab.com`). `Origin`'siz istekler (app'in `request` eylemi) değişmedi. Site CSP: `connect-src https://<ref>.supabase.co`. |

### Kırıcı / deprecated
1. **Kırıcı davranış — `requireMotionPaidAccess` varsayılanı açıldı.** Bugün parametresiz çağıran her kapı artık oturum/üyelik akışına girer (önceden "gelecek güncellemede" deyip `false` dönüyordu). Kamera/ölçüm yolu bu fonksiyonla kapatılıyorsa önce `requireMotionCameraAccess` (veya `motionCameraCoachingAvailable`) ile kapatılmalı. Ücretsiz dersler bu kapıdan **geçirilmemeli**: kapıyı yalnız `isLessonUnlocked(...) == false` olan ders ve bağımsız pratik için çağırın; yoksa ücretsiz ders de üyelik ister.
2. **Kırıcı davranış — `MotionAccountPage` varsayılanı açıldı.** Parametresiz sayfa artık açılışta `hasActiveMembership` çağırır ve üyelik satırını gösterir (fikstür etkisi aşağıda). Satmayan bir derleme `membershipAvailable: false` geçer.
3. **Deprecated (derleme kırılmaz, `flutter analyze` info/warning):** `motionPaidFeaturesAvailable`, `MotionAccountPage(paidFeaturesAvailable:)`, `requireMotionPaidAccess(paidFeaturesAvailable:)`. Bir app `--fatal-infos`/`--fatal-warnings` ile analiz ediyorsa bu kullanımlar CI'ı kırar → aynı pin commit'inde yeni adlara geçin.
4. Kaynak düzeyinde kaldırılan sembol yok; imzalar genişledi (yeni isteğe bağlı parametreler).

### App başına değişecek satırlar (app `main` HEAD'lerine göre, 2026-10-25 salt okuma)
Pin satırları: eski tam SHA `583203112c94…`'ü (`grep -rn 583203112c94`) `cdcbf0484e82806094ecf010b294debc3c8c5c83` ile değiştirin (`pubspec.yaml` ref satırları, alt paket pubspec'leri, pin eşitlik/smoke testleri, store dokümanları) → ağlı `flutter pub get` → `pubspec.lock` ref/resolved-ref satırları. Liste: `TUKETICI-PIN-2026-10-21.md` tablosu (satır numaraları app HEAD'ine göre kayabilir).

| App (main HEAD) | Kaynak satırları |
|---|---|
| **Lissom** (`bc1efb9`, Ekip-2) | `lib/main.dart:528` `paidFeaturesAvailable: true` → `membershipAvailable: true` (veya parametreyi sil; varsayılan aynı). `lib/main.dart:602` `beforeMeasurement: requireMotionPaidAccess(...)` → **`requireMotionCameraAccess(...)`** (aksi hâlde ölçüm üyelik akışına girer). `lib/main.dart:614` `paidFeaturesAvailable: true` → sil (varsayılan) ya da `salesAvailable: true`. `measurementAvailable = motionPaidFeaturesAvailable` satırları → `motionCameraCoachingAvailable`: `onboarding_flow.dart:26,42`, `profile_screen.dart:16,34`, `shell.dart:28,265`, `surfaces.dart:15,445,536`, `library_screen.dart:24,44,407`, `progress_screen.dart:41,56`, `home_screen.dart:33,65` (+ `onboarding_flow.dart:7` yorum). Ders kilidi: `lib/app/course_access.dart` kendi onaylı sayılarını `freeLessonLimit` ile verebilir (bkz. not). |
| **Ostinato** (`bcc2f9b`, Ekip-3) | `lib/app/motion_account_bootstrap.dart:99` `requirePaidAccess: requireMotionPaidAccess(...)` varsayılana güveniyor → artık açık: hangi yolda çağrıldığını doğrulayın (kamera/duruş ölçümü ise `requireMotionCameraAccess`; ücretli ders ise yalnız kilitli derste çağırın). `lib/app/screens/library_screen.dart:6,144,192` `motionPaidFeaturesAvailable` (kamera metni) → `motionCameraCoachingAvailable`. Hesap sayfası satış için `membershipAvailable` (varsayılan açık). |
| **Choreia** (`d2e5a21`, Ekip-3) | `lib/main.dart:344` `cameraSessionsAvailable: motionPaidFeaturesAvailable` → `motionCameraCoachingAvailable`. `lib/main.dart:348` `beforeLessonStart: requireMotionPaidAccess(...)` varsayılana güveniyor → artık üyelik akışı açar: yalnız kilitli ders/pratikte çağırın (ücretsiz/ücretli eşleme kurucu onayı bekliyor — "Salsa 6/18" sorusu). |
| **JabLab** (`4dcfe7a`, Ekip-4) | `lib/main.dart:113` `cameraLessonsAvailable: motionPaidFeaturesAvailable` → `motionCameraCoachingAvailable`. `lib/main.dart:114` `beforeLessonStart: requireMotionPaidAccess(...)` varsayılana güveniyor → artık açık; Choreia ile aynı not. `lib/app/jablab_app.dart:69` yorum. |
| **Gravita** (`a501db8`, Ekip-4) | `lib/app/gravita_account_page.dart:176` `paidFeaturesAvailable: motionPaidFeaturesAvailable` (kamera sabiti satışa veriliyor!) → `membershipAvailable: motionSubscriptionSalesAvailable` (veya sil). `lib/app/camera_release_policy.dart:2,7` → `motionCameraCoachingAvailable`. `lib/app/motion_account_bootstrap.dart:107` `requirePaidAccess: requireMotionPaidAccess(...)` varsayılana güveniyor → kamera yolu ise `requireMotionCameraAccess`. Not: CORE-01 Gravita'nın bildirdiği sızıntıyı kapatır. |

App'lerin satış `wip/*` dalları (Ostinato `48062c5`, JabLab `6eaa8bf`, Gravita `38473730`, Choreia `apply_sales.py`) `main`'den farklıysa satırları o dalda yeniden doğrulayın.

### Paywall A notu (ders kilidi)
- Varsayılan formül modül ortasında kesebilir. Lissom'un onaylı tam-modül önek sayıları (24/60, 6/15, 5/14, 5/12, 7/19) `freeLessonLimit` override ile birebir korunur (Core testi `lesson_access_test.dart` bu beş bölmeyi doğrular). Varsayılan formül aynı derslerde `ceil(total/3)` = 20, 5, 5, 4, 7 verir (ilk modül daha uzunsa o) — fark Yönetim'e raporlandı; app başına eşleme kurucu onayı bekliyor.
- Ders/app adı Core'da yok; sayılar app'ten gelir.

### Fikstür etkisi
- Varsayılan `MotionAccountPage` artık açılışta `hasActiveMembership` çağırır. `implements MotionAccountClient` + `noSuchMethod` fake'ler hata verir → sayfa "Membership unavailable" gösterir, **yakalanmamış hata yok** (CORE-01). Metin/sayaç bekleyen testler güncellenmeli ya da `membershipAvailable: false` geçmeli.
- `extends` eden fake'ler gerçek REST'e gider → `motion-check-membership` (ve `MotionMembershipPage` için `motion_age_declarations` / `motion_parental_consents` GET) fikstürü gerekir. Gravita testleri bugün geçici olarak false ile koşuyor.
- **Gerçek `MotionAccountClient` (+ sahte HTTP) ile sayfa açan widget testleri:** fake-async zamanda üyelik okuması cevaplanmaz ve istemcinin okuma deadline'ı (`readTimeout`, varsayılan 10 sn) test sonunda "A Timer is still pending" ile düşer. Ya testin sonunda `await tester.pump(const Duration(seconds: 11));` ile süreyi geçirin (Core'un `account_lifecycle_race_test.dart` deseni; geç zaman aşımı sayfada yutulur) ya da `membershipAvailable: false` geçin.
- `requireMotionPaidAccess` varsayılanına güvenen testler "gelecek güncellemede" yerine hesap/üyelik sayfası bekler.
- Deno/SQL fikstürü değişmedi.

### Canlı önkoşul (Yönetim, CORE-07 paketi)
- Migration'lar `20261021190000_motion_age_consent_retention` + `20261023120000_motion_age_metadata_strip` canlıda; `motion-parental-consent` bu SHA'dan deploy (CORS içerir; `verify_jwt=false`); posta secret'ları; isteğe bağlı `MOTION_CONSENT_ALLOWED_ORIGINS` (yalnız `https://yulalab.com` dışı origin gerekiyorsa; `www`/önizleme origin'leri YULALAB ekibinden — UNKNOWN).
- Bunlar canlıda olmadan yaş akışlı hiçbir build kullanıcıya ulaşmamalı (TestFlight dahil).

### Hedefli regresyon (app başına; sonra tam suite)
`TUKETICI-PIN-2026-10-21.md` "App başına regresyon listesi" + R1 için ek:
- hesap sayfası açılışında üyelik satırı (satış açık) ve `membershipAvailable: false` dalı;
- kamera/ölçüm girişi kapalı kalır (`requireMotionCameraAccess` / `motionCameraCoachingAvailable`), hesap/satın alma sayfası açılmaz;
- ücretsiz ders kapıdan geçmez; kilitli ders/pratik üyelik sayfasını açar ve dönüşte yeniden doğrular;
- pin eşitlik testleri yeni tam SHA'da.
