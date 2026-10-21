# Motion Core tüketici pin geçişi — 21 Ekim 2026

Motion Core oturumu app repolarına **yazmadı**. Bu belge app oturumlarına iletilecek exact
değişiklik ve regresyon listesidir. Önkoşul: Core commit'lerinin GitHub'a push'u
(**onay gerekiyor**; app'ler `git url + ref` ile çözüyor, push olmadan `pub get` bulamaz).

## Hangi SHA

**Tek önerilen pin: `5832031`** (K08 `a235f21` + J01 `4eba5e9` + getter `7eb5c4d` + yaş/veli/saklama
`5011c6a` + CI allowlist yenilemesi). Ara commit'ler (`a235f21`…`5011c6a`) Core CI'daki satır-anahtarlı
app-özgü kelime taramasında NONPASS (enum satırı 5→13 kaydı; `5832031` düzeltir); bu yüzden pin
olarak kullanılmamalı.

Önkoşul: yaş/veli özellikleri `20261021190000` migration'ı + `motion-parental-consent` deploy'u +
mail secret'ları canlıda olmadan kullanıcıya ulaşan bir build'e girmemeli (aksi halde kayıt yaş
metadata'sı Auth'ta soyulmadan kalır, onay bölümü görünmez). Mağaza upload'u zaten G1–G3 ve
onay kapısında olduğundan pin bu deploy'dan önce yerel regresyon için alınabilir.

d69 → `5832031` davranış değişikliği: hesap mutasyonları kesin 4xx dışı hatalarda
`MotionOperationUnknown` fırlatır (eskiden ham SDK hatası). Core sayfası bunu işler;
host kodu ham hata türü yakalıyorsa güncellenmeli. Paket sürümü 0.2.0→0.3.0.

## Exact değişecek satırlar (`d69e10786e2f1cd509b9eeadeb3ef6ea42d93b5d` → yeni SHA)

| App (HEAD) | pubspec.yaml ref satırları | Alt paket pubspec | Sabit SHA içeren test/doküman |
|---|---|---|---|
| Ostinato `cf00851` | `app/pubspec.yaml` 42, 59, 66, 70 | `packages/ostinato_audio/pubspec.yaml:24`, `packages/ostinato_posture/pubspec.yaml:14` | `test/flutter_bundle_content_asset_reader_test.dart:12`, `packages/ostinato_audio/test/dependency_pin_test.dart:16,26`, `docs/store/listing.json:71`, `docs/store/listing.tr-TR.json:50`, `docs/store/RELEASE-REVIEW.md:11,95` |
| Choreia `f5b71ee` (16 dosya WIP!) | 21, 47, 55, 65, 106 | — | `test/current_core_adoption_test.dart:6`, `test/pin_equality_test.dart:10` |
| JabLab `88d65b4` | 20, 49, 56, 71 | `packages/jablab_engine/pubspec.yaml:25` | `test/core_adoption_contract_test.dart:6`, `test/support/local_core_intake.dart:6` |
| Gravita `ff995d9` | 22, 48, 55, 67 | `packages/gravita_engine/pubspec.yaml:15` | `test/shell_contract_test.dart:13,450` |
| Lissom `aaf118e` | 23, 39, 47, 69 | `packages/lissom_engine/pubspec.yaml:23` | `test/core_8f_consumer_smoke_test.dart:2`, `test/pin_equality_test.dart:38,85` |

Ardından her app'te `flutter pub get` (ağ: GitHub git fetch — onaylı pub koşusu) ile
`pubspec.lock` `ref`/`resolved-ref` satırları (app başına 10–12) güncellenir.

## Kaynak uyum notları

- **Lissom** `LissomEpochAccountClient.signUp` override'ı d69 imzasıyla uyumlu kalır
  (Core `signUp` imzasını değiştirmedi; yaşlı kayıt ayrı `signUpWithAge`). B aşamasında
  sarmalayıcı `signUpWithAge`/`ageStatus`/`requestParentalConsent`'i override etmezse temel
  uygulama aynı Supabase istemcisiyle çalışır (sahiplik koruması gerektirmeyen okuma/istek).
- **Gravita** `EpochBoundMotionAccountClient` ve **JabLab** `_OwnerBoundAccountClient`
  `super.deleteCommonAccount` çağırıyor: `super(... deletionReceipt: original.deletionReceipt,
  operationTimeout: original.operationTimeout, readTimeout: original.readTimeout)` eklenmeli;
  eklenmezse yanıt kaybında makbuz okuması yapılmaz → UNKNOWN + dosyalar korunur (güvenli).
- **Ostinato/Choreia/Lissom** sarmalayıcıları `_delegate.deleteCommonAccount`'a devrediyor →
  makbuz okuması çalışma zamanı istemcisinden gelir, değişiklik gerekmez.
- `implements MotionAccountClient/MotionAccountRuntime` test fake'lerinin hepsi
  `noSuchMethod` kullanıyor → yeni üyeler derlemeyi kırmaz.
- **P1 (startup deadline)** Core'da değil: Ostinato `main` runApp öncesi `initialize`'ı
  bekliyor; Choreia'nın 20 s gözlemci + geç runtime dispose deseni Ostinato'ya taşınmalı.
- B aşamasında host'lar `MotionAccountPage(countryCode: <storefront/bölge>, ageBlocked:
  <kalıcı>, onAgeBlocked: <kalıcı yaz>)` geçmeli; gençler için pazarlama/reklam yok,
  analitik açık katılım (`MotionAgePolicy.marketingAllowed/analyticsNeedsOptIn`).

## App başına regresyon listesi (onaylı SDK/pub koşusu ile)

Her app: `flutter analyze` + aşağıdaki hedefli dosyalar + pin eşitlik testleri; sonra tam suite.

| App | Hedefli testler |
|---|---|
| Ostinato | `motion_account_consumer_test`, `account_session_identity_test`, `ostinato_identity_gate_test`, `account_delete_ownership_test`, `account_delete_auth_lag_test`, `account_delete_page_lifetime_test`, `account_resource_drain_registry_test`, `flutter_bundle_content_asset_reader_test`, `packages/ostinato_audio/test/dependency_pin_test` |
| Choreia | `account_host_smoke_test`, `account_confirmed_namespace_test`, `account_deletion_initiation_test`, `account_identity_appearance_test`, `startup_deadline_test`, `current_core_adoption_test`, `pin_equality_test` |
| JabLab | `account_host_smoke_test`, `core_account_locale_consumption_test`, `identity_appearance_gate_test`, `owner_bound_account_page_test`, `core_adoption_contract_test` |
| Gravita | `gravita_account_page_test`, `account_action_ticket_test`, `confirmed_erasure_refresh_test`, `runtime_owner_refresh_test`, `gravita_dialog_lifetime_test`, `motion_host_presentation_test`, `shell_contract_test` |
| Lissom | `local_account_bridge_test`, `owner_session_contract_test`, `owner_host_recovery_test`, `account_native_contract_test`, `core_8f_consumer_smoke_test`, `core_8f_production_wiring_test`, `core_8f_host_presentation_test`, `pin_equality_test` |

Yeni davranış için app'lerde eklenmesi önerilen kabul: (1) tutulan giriş yanıtında Core sayfası
UNKNOWN + OK gösterir ve ikinci istek göndermez; (2) silme yanıt kaybında host dosyaları korunur
(Gravita/JabLab getter iletilmeden ve iletilerek); (3) B aşamasında 13 altı kayıt kapalı ve kalıcı.
