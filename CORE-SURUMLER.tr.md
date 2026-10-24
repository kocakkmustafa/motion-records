# Motion Core sürüm defteri

Core'a yalnız Ekip-2 yazar. Tüketiciler (Lissom: Ekip-2 · Ostinato, Choreia: Ekip-3 · JabLab, Gravita: Ekip-4)
Core'a bağlı işe başlamadan bu dosyayı okur. **Yalnız burada duyurulan SHA pinlenir**; ara commit'ler pinlenmez.
Pin her yerde **tam 40 karakter SHA** ile yazılır (pub `ref:` metin karşılaştırır; kısa SHA/tag ayrı kaynak sayılır).

Bölüm düzeni: SHA + CI · paket sürümleri · API farkı · kırıcı/deprecated · app başına değişecek satırlar ·
fikstür etkisi · canlı önkoşul · hedefli regresyon.

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
