# Motion yayın profili taslağı — gizlilik, koşullar, mağaza beyanları, veri rolleri (22 Ekim 2026)

Motion Core oturumu. **Taslak; hukuki görüş değildir. Siteye, mağaza konsollarına veya app repolarına yazılmadı.**
Dayanak: Core `5832031` (origin/main, CI 39733713974 yeşil), `lib/docs/compliance/YAS-VELI-VE-SAKLAMA.md`,
kurucu kararları (21 Ekim): global, 13+ gençler dahil; kısa saklama profili.

## 1. Site: `ventures/yulalab-com/site/src/app/[locale]/privacy/motion/page.tsx` (HEAD `242e679`)

Sayfa `text(locale, TR, EN)` kullanır; diğer 12 dil `messages/content-<locale>.json` içinde **EN metni anahtar** olarak
çevrilir → her yeni/değişen EN cümlesi için 12 katalog girdisi gerekir (YULALAB oturumu). Önerilen değişiklikler:

| # | Satır | Değişiklik |
|---|---|---|
| P1 | 9 | `LAST_UPDATED` → yayın tarihi |
| P2 | 86–92 "Ortak hesap ve üyelik" | 1. paragrafın sonuna **yaş verisi** cümlesi ekle (aşağıda P2 metni) |
| P3 | 95–101 "Sağlayıcı günlükleri" | 2. paragrafa **saklama süresi** cümlesi ekle (P3) |
| P4 | 116–135 silme bölümü | 1. paragrafa **beş app / çevrimdışı cihaz**; 3. paragraftaki "kendi saklama döngülerine tabidir…" cümlesini **kısa saklama profili** ile değiştir (P4) |
| P5 | 143–147 "Çocuklar" | Başlık "Gençler ve yaş sınırı / Teens and minimum age"; metni tamamen değiştir (P5) |
| P6 | yeni bölüm, 147'den sonra | "Veli veya vasi onayı / Parent or guardian approval" (P6) |
| P7 | yeni bölüm, P6'dan sonra | "Saklama süreleri / Retention" tablosu (P7) |
| P8 | yeni bölüm, 161'den önce | "Veri rolleri ve alt işleyenler / Data roles and processors" (P8) |
| P9 | 149–153 "Haklarınız" | Gençlerin ve velilerin hakları + yaş beyanı düzeltmesi cümlesi (P9) |

### Önerilen metinler (TR / EN)

**P2** — TR: "Hesap oluştururken doğum ayınızı ve yılınızı (gün sorulmaz) ve ülkenizi beyan edersiniz; bu bilgiler hangi hesap özelliklerinin ve korumaların uygulanacağını belirlemek için hesabınızla birlikte saklanır ve bir kez beyan edildikten sonra yalnız destek üzerinden düzeltilebilir." / EN: "When you create an account you declare your birth month and year (we do not ask for the day) and your country; they are stored with your account to decide which account features and protections apply, and after the first declaration they can be corrected only through support."

**P3** — TR: "Uygulamalar parola, oturum belirteci veya e-posta içeriğini günlüğe yazmaz. Sağlayıcı günlükleri en fazla 30 gün saklanır." / EN: "The apps do not write passwords, session tokens or email contents to logs. Provider logs are kept for at most 30 days."

**P4a** (1. paragraf sonu) — TR: "Tek Motion hesabı beş uygulamada ortaktır; silme beşini birden etkiler. Çevrimdışı bir cihaz, internete bağlanıp uygulamayı açana kadar o hesabın yerel geçmişini tutar ve silme kaydını gördüğünde temizler; silme kanıtı yoksa yerel veriyi silmez." / EN: "One Motion account is shared by all five apps, so deletion affects all of them. An offline device keeps that account's local history until it is online and the app is opened; it then clears the history after seeing the deletion receipt and never deletes local data without that proof."

**P4b** (3. paragraftaki son cümlenin yerine) — TR: "Hesap silindiğinde sunucudaki ürün verileri hemen silinir. Yedekler en fazla 30 günlük bir döngüde tutulur; bir yedekten geri dönülürse, o tarihten sonra silinmiş hesaplar yeniden silinir." / EN: "When an account is deleted, its product data on the server is deleted immediately. Backups are kept on a cycle of at most 30 days; if a backup is ever restored, accounts deleted after that point are deleted again."

**P5** (başlık: "Gençler ve yaş sınırı" / "Teens and minimum age") — TR: "Motion hesabı 13 yaş ve üzeri içindir; 13 yaşından küçükler için hesap açılmaz. Bulunduğunuz ülkenin dijital rıza yaşının altındaysanız (ülkeye göre 13–18), hesap özellikleri bir ebeveyn veya vasinin onayına kadar kısıtlı kalır; bu süre içinde cihazdaki pratik kullanılabilir. 18 yaşından küçük kullanıcılara pazarlama iletisi gönderilmez ve kişiselleştirilmiş reklam gösterilmez; uygulamalarda reklam veya analitik izleme yoktur; ileride ürün analitiği eklenirse 18 yaş altında yalnız açık izinle etkinleşir." / EN: "A Motion account is for people aged 13 and over; no account is created for anyone under 13. If you are below your country's digital consent age (13–18 depending on the country), account features stay limited until a parent or guardian approves; practice on the device remains available meanwhile. Users under 18 receive no marketing messages and no personalised advertising; the apps contain no advertising or analytics tracking, and if product analytics is added later it is enabled for users under 18 only with explicit permission."

**P6** (başlık: "Veli veya vasi onayı" / "Parent or guardian approval") — TR: "Onay gereken gençler, ebeveyn veya vasilerinin e-posta adresini girer. Bu adrese bir kez onay bağlantısı gönderilir; adresin kendisi saklanmaz, yalnız tek yönlü özeti (tekrarlanan istekleri sınırlamak için) tutulur. Bağlantı 7 gün geçerlidir ve onay sayfasında gencin e-posta adresi maskeli gösterilir. Onaylanırsa hesap özellikleri açılır; reddedilirse hesap silinir. 30 gün içinde onaylanmayan hesap silinir." / EN: "Teens who need approval enter a parent's or guardian's email address. One approval link is sent to it; the address itself is not stored, only a one-way digest used to limit repeated requests. The link works for 7 days and the approval page shows the teen's email address masked. If approved, account features open; if declined, the account is deleted. An account not approved within 30 days is deleted."

**P7** (başlık: "Saklama süreleri" / "Retention") — madde listesi:
- TR "Hesap ve ürün verileri: hesap silinene kadar; silmede hemen." / EN "Account and product data: until the account is deleted; immediately on deletion."
- TR "Silme kaydı (hesap kimliğinin tek yönlü özeti): diğer cihazların silmeyi tanıması için." / EN "Deletion receipt (one-way digest of the account ID): kept so other devices can recognise the deletion."
- TR "Sağlayıcı günlükleri: en fazla 30 gün." / EN "Provider logs: at most 30 days."
- TR "Yedekler: en fazla 30 günlük döngü; geri dönüşte silmeler yeniden uygulanır." / EN "Backups: cycle of at most 30 days; deletions are reapplied after any restore."
- TR "Onaylanmamış genç hesabı: 30 gün." / EN "Unapproved teen account: 30 days."
- TR "Kapanan destek yazışmaları: 90 gün." / EN "Closed support conversations: 90 days."
- TR "Abonelik hakkı kayıtları (uygulama, ürün, mağaza işlem referansı, durum, bitiş): abonelik süresince ve hesap silinene kadar; silmede hemen. Ödeme ve fatura kayıtlarını Apple/Google yasal süre boyunca tutar." / EN "Subscription entitlement records (app, product, store transaction reference, state, expiry): for the subscription and until the account is deleted; immediately on deletion. Apple/Google keep payment and invoice records for the legally required period."

**P8** (başlık: "Veri rolleri ve alt işleyenler" / "Data roles and processors") — TR: "Veri sorumlusu YULA Lab'dir. Supabase (Frankfurt, AB) hesap, kimlik doğrulama ve veritabanı hizmetini; [e-posta sağlayıcısı] hesap ve veli onayı e-postalarını bizim adımıza işler. Apple ve Google, mağaza satın almaları ve abonelikleri için kendi politikalarıyla bağımsız sorumludur." / EN: "YULA Lab is the data controller. Supabase (Frankfurt, EU) provides the account, authentication and database service, and [email provider] sends account and parental-approval emails, both on our behalf. Apple and Google act as independent controllers for store purchases and subscriptions under their own policies." — *[e-posta sağlayıcısı] seçilince doldurulur.*

**P9** (Haklarınız 1. paragrafa ek) — TR: "Ebeveyn veya vasiler, gencin hesabıyla ilgili taleplerini aynı adrese iletebilir. Yanlış beyan edilen doğum tarihi destek üzerinden düzeltilir." / EN: "Parents or guardians can send requests about a teen's account to the same address. An incorrectly declared birth date is corrected through support."

**Yeni sayfa (YULALAB):** `src/app/[locale]/motion/consent/page.tsx` — `#token=` fragment'ini okur, `motion-parental-consent`'e
`{action:"view"}` ile maskeli e-posta/son tarih gösterir, Onayla/Reddet → `{action:"decide"}`. Publishable key ile
`POST https://<ref>.supabase.co/functions/v1/motion-parental-consent` (verify_jwt=false). Metin: P6 özeti + "Reddederseniz hesap silinir"
+ sonuç durumları (onaylandı / reddedildi ve silindi / süresi doldu / geçersiz bağlantı). 14 dil.

## 2. Site: `src/app/[locale]/terms/page.tsx` — Motion özel şartları

Yeni bölüm, satır 107 ("5. Burun Farkı — özel şartlar") öncesine; sonraki bölüm numaraları +1:
**"5. Motion uygulamaları — özel şartlar" / "5. Motion apps — special terms"** — TR: "Choreia, Lissom, Gravita, JabLab ve Ostinato tek bir Motion hesabını paylaşır; hesap 13 yaş ve üzeri içindir ve bazı ülkelerde 18 yaşından küçükler için ebeveyn/vasi onayı gerekir. Bir uygulamada satın alınan bireysel abonelik yalnız o uygulamada geçerlidir; Motion+ beş uygulamayı kapsar. Abonelikler aylık veya yıllık olarak Apple App Store ya da Google Play üzerinden satın alınır ve otomatik yenilenir; yenileme ve iptal mağaza hesabınızdan yönetilir. Abonelik başka bir uygulamada etkinse aynı hesapta ikinci bir Motion+ satın alımı önerilmez. Hesabı silmek beş uygulamadaki hesabı birlikte siler ancak Apple veya Google aboneliğini iptal etmez; aboneliği mağaza hesabınızdan ayrıca iptal etmelisiniz. Motion uygulamaları tıbbi cihaz değildir." / EN: "Choreia, Lissom, Gravita, JabLab and Ostinato share one Motion account; the account is for people aged 13 and over, and in some countries users under 18 need a parent's or guardian's approval. An individual subscription bought in one app applies only to that app; Motion+ covers all five. Subscriptions are bought monthly or yearly through the Apple App Store or Google Play and renew automatically; you manage renewal and cancellation in your store account. While a subscription is active in another app, the same account is not offered a second, overlapping Motion+ purchase. Deleting the account deletes it in all five apps together but does not cancel an Apple or Google subscription; cancel it separately in your store account. The Motion apps are not medical devices."
Ayrıca "1. Kabul" (80–84): 18 yaş altındakiler için "ebeveyn/vasinizin bu şartları sizinle birlikte kabul etmesi gerekebilir" cümlesi.

## 3. Mağaza beyanları (beş app, aynı profil)

| Alan | Öneri | Not |
|---|---|---|
| Apple yaş derecesi anketi | İçerik soruları değişmeden (şiddet/kumar/UGC/web yok) → içerik derecesi düşük kalır; **Kids Category: seçilmez** | Hesap 13+ kuralı içerik derecesi değil, kayıt kapısıdır; inceleme notunda belirtilir |
| Apple "Made for Kids" / Kids Category | **Hayır** | Families/çocuk kategorisi dışı |
| Apple App Privacy | Hesap: e-posta, kullanıcı ID, ad (görünen ad), **diğer: doğum ay/yılı, ülke**; amaç App Functionality; Linked=evet; Tracking=hayır | Veli e-postası: gönderim amaçlı, saklanmaz (özet) → "Contact Info / Email" kapsamında App Functionality |
| Google Play hedef kitle | **13–15, 16–17, 18+** (12 ve altı seçilmez) | Families programı dışı; mağaza girişi çocuklara hitap etmemeli (görseller/metin) |
| Google Play "çocukları da çekebilir mi?" | Hayır (gerekçe: 13+ hesap, eğitim/fitness içerik yetişkin/genç odaklı) | Play inceleme sonucu değiştirebilir |
| Google Play içerik derecelendirmesi (IARC) | Mevcut anket cevapları korunur | Mevcut taslak tahmini: Everyone/PEGI 3 |
| Google Play Veri güvenliği | Toplanan: e-posta, kullanıcı ID, ad, **diğer kişisel bilgi (doğum ay/yılı, ülke)**; paylaşım yok; aktarımda şifreli; silme talebi URL'si `/privacy/motion#motion-account-deletion` | Veri silme: hesap + "kısmi silme" (yalnız yerel) |
| ABD eyalet app-store yaş yasaları (Utah, Texas 2026) | **Karar gerekli**: Apple Declared Age Range / Play Age Signals API entegrasyonu | Mağaza sinyali Core yaş kapısına ek bir girdi olabilir; Core'da yok |

Tutarlılık riski: app `docs/store/listing*.json` içindeki `$ageRating.expectedTier = 4+/Everyone` tahmini içerik içindir
ve kalabilir; ama `description`/`account-data-safety-draft.md` yaş/ülke verisini henüz içermiyor → beş app oturumu günceller.

## 4. Veri rolleri (KVKK/GDPR)

| Rol | Taraf | Açık iş |
|---|---|---|
| Veri sorumlusu | YULA Lab — Mustafa Kaan Koçak (Türkiye) | **VERBİS** kayıt yükümlülüğü/muafiyeti hukuk kontrolü |
| Veri işleyen | Supabase (AB, Frankfurt) | DPA kabulü kaydı (Supabase hesap ayarı) |
| Veri işleyen | E-posta sağlayıcısı (seçilecek) | DPA + AB/ABD aktarım dayanağı |
| Bağımsız sorumlu | Apple, Google | — |
| AB/BK temsilcisi | **GDPR Art. 27 / UK GDPR Art. 27**: AB dışındaki sorumlunun AB/BK kullanıcılarına düzenli hizmeti → temsilci atama gerekebilir | Hukuk kararı; gizlilik sayfasına temsilci iletişimi eklenir |
| Yurt dışı aktarım | TR → AB (Supabase) KVKK md. 9 | Standart sözleşme/bildirim hukuk kontrolü |

## 5. Kurucu kararı gereken iki ürün sorusu

1. **Misafir (hesapsız) kullanım ve 13 altı:** Core yalnız hesap açmayı engeller. Misafir pratiği cihazda kalır, veri toplanmaz.
   Seçenek A (önerilen): mevcut — misafir açık, hesap 13+. Seçenek B: ilk açılışta yaş ekranı; 13 altı tüm uygulama kapalı
   (host `onAgeBlocked` kalıcı kaydını uygulama girişine bağlar).
2. **Ülke kaynağı:** cihaz bölgesi (mevcut varsayılan) mı, mağaza storefront ülkesi mi (`MotionAccountPage(countryCode:)`)?
   Öneri: storefront, yoksa cihaz bölgesi.

## 6. Minimum kullanıcı adımları (yürütülmedi; her biri ayrı onay)

**Supabase/Mailpit yerel entegrasyon (5 SKIP + gerçek Supabase replay):**
1. Onay: "Docker Desktop ile `supabase start` için Supabase yerel imajlarını çek ve çalıştır" (ağ indirme ~GB; yalnız yerel konteyner).
   Makinede Supabase CLI (`/opt/homebrew/bin/supabase`) ve Docker Desktop zaten kurulu (22 Ekim `which` kontrolü); ek kurulum yok,
   yalnız Docker Desktop'ın açık olması ve imaj çekme onayı gerekir.
2. Sonra Core oturumu kendisi yürütür: `supabase start` → `supabase db reset --local` → SQL testleri → `MOTION_LOCAL_*` ile
   `local_account_integration_test.dart` → `supabase functions serve` + Deno → `supabase stop`. Kullanıcı girdisi gerekmez
   (yerel anon anahtar `supabase status` çıktısından, sır değildir).

**Canlı proje (deploy ve readback):**
3. Supabase Motion proje ref'i + CLI erişim onayı (kullanıcı `supabase login` yapar; Core oturumu token görmez/yazmaz).
4. Onay: `supabase db push` (yalnız `20261021190000`) + `supabase functions deploy motion-parental-consent` + secret'lar.
5. Kullanıcı girdisi: e-posta sağlayıcısı seçimi ve hesabı, `yulalab.com` DNS'e SPF/DKIM kayıtları (DNS değişikliği onayı),
   ~~`MOTION_MAIL_API_KEY`~~ **(geçersiz — R2'de HTTP posta adaptörü kaldırıldı; bkz. §8 ve §9)**: posta secret'ları `MOTION_SMTP_HOST`/`PORT`/`USER`/`PASSWORD`/`TLS` + `MOTION_MAIL_FROM` + `MOTION_CONSENT_PAGE_URL`, değerleri kullanıcı `supabase secrets set` ile girer (`scratch/2026-10-25-motion-core-packages/CORE-07-CANLI-DEPLOY.tr.md`).

**TLS 1.2 CBC (en erken 10 Kasım) cihaz kabulü:**
6. Kullanıcı: iOS 15.x çalışan bir iPhone ve Android 7.0 (API 24) cihaz sağlar (veya en düşük desteklenen gerçek sürüm kararı).
7. Onay: G1–G3 sonrası imzalı aday paket (IPA/AAB) üretimi ve cihaza kurulum; Core oturumu senaryo listesini (PREP-PLAN D1–D2) verir.
8. Onay: `openssl s_client -connect <ref>.supabase.co:443 -tls1_2` ile cipher readback (salt okuma, proje ref'i gerekir).

**Hukuk:** 9. ülke yaş tablosu + P2–P9 metinleri + Art. 27 temsilcisi + VERBİS için danışman incelemesi.

## 7. 23 Ekim — satış ilk sürümde AÇIK (kurucu kararı) güncellemesi

**Gizlilik sayfası (`privacy/motion/page.tsx`)**
- Satır 88: "İlk sürümde beş uygulamada da ücretli satış kapalıdır. Abonelikler açılırsa…" → TR "Beş uygulamada da uygulamaya özgü abonelik ve beş uygulamayı kapsayan Motion+ satın alınabilir; bireysel abonelik yalnız satın alındığı uygulamada, Motion+ beş uygulamada geçerlidir." / EN "All five apps sell their own subscription and Motion+, which covers all five; an individual subscription applies only to the app it was bought in, Motion+ to all five."
- Satır 104–108 "Satın alma doğrulaması": "İlk sürümde … başlatılamaz. Ücretli üyelik ileride açılırsa" → TR "Abonelik satın aldığınızda Apple veya Google mağaza ürünü ve işlem kanıtı sunucuda doğrulanır." / EN "When you buy a subscription, the Apple or Google store product and transaction evidence are verified on our server." (geri kalan cümleler aynı; "tasarlanmıştır" → "saklar").
- Gençler (P5) ek cümle: TR "Veli onayı bekleyen hesaplara satın alma önerilmez; 18 yaş altındaki satın almalar mağazanın aile/ebeveyn denetimlerine tabidir." / EN "Accounts awaiting parental approval are not offered purchases; purchases by users under 18 are subject to the store's family and parental controls."

**Koşullar (`terms/page.tsx`)** — "3. Abonelikler ve ödemeler" (95–99) mevcut metin yeterli; sonuna TR "Motion uygulamalarında fiyatlar mağazanın gösterdiği yerel fiyattır; ücretsiz deneme sunulursa süresi ve yenileme tutarı satın alma ekranında gösterilir." / EN "Motion prices are the local prices shown by the store; if a free trial is offered, its length and the renewal price are shown on the purchase screen." 5. Motion bölümü yukarıdaki satış metniyle güncellendi.

**App Review / mağaza açıklaması (abonelik bilgisi, Apple 3.1.2 ve Play abonelik politikası)** — her app'in açıklama sonuna ve inceleme notuna:
- EN "Subscriptions: <App> Monthly and Yearly (this app only) and Motion+ Monthly and Yearly (all five Motion apps). Payment is charged to your Apple ID / Google account at confirmation. Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period; your account is charged for renewal within 24 hours before the period ends. Manage or cancel in your App Store / Google Play account settings. Deleting your Motion account does not cancel a subscription. Terms: https://yulalab.com/terms · Privacy: https://yulalab.com/privacy/motion"
- Uygulama içi satın alma ekranında zaten olanlar (Core `MotionMembershipPage`): mağazanın gerçek yerel fiyatı ve dönemi, otomatik yenileme metni, Satın alımları geri yükle, Mağazada yönet, Koşullar ve Gizlilik bağlantıları.
- İnceleme notu: "Paid camera coaching is not part of this version; the subscription unlocks <app-specific paid content>." ← **kurucu girdisi gerekli** (aşağı bakınız).

**Açık ürün sorusu (kurucu):** dört app `motionPaidFeaturesAvailable`'ı kamera koçluğu/ölçüm kapısı olarak kullanıyor; Core bu sabiti **kapalı** tuttu ve satış için ayrı `motionSubscriptionSalesAvailable = true` ekledi. İlk sürümde kamera koçluğu kapalıyken aboneliğin **hangi içeriği** açacağı her app için tanımlanmalı (Apple 3.1.1/2.3: satılan dijital içerik gerçekten sunulmalı). Tanım gelene kadar app'ler üyelik yüzeyini açabilir ama "kilitli ders" eşlemesi app işi.

## 8. 25 Ekim — finalizasyon (CORE-08: fiyat, 14 gün deneme, paywall A, Workspace SMTP)

Durum: **ekip taslağı son hâl**; hukuk incelemesi ve app başına ders eşleme onayı (kurucu) açık. YULALAB ekibi 14 dile işler (Core işlemez).
Önceki bölümlerle çelişkide bu bölüm esastır. Fiyat tutarı hiçbir metne yazılmaz (mağazanın yerel fiyatı).

**P8 / §4 veri rolleri — e-posta sağlayıcısı = Google (Workspace)**
- P8 TR: "Veri sorumlusu YULA Lab'dir. Supabase (Frankfurt, AB) hesap, kimlik doğrulama ve veritabanı hizmetini; Google (Google Workspace) hesap ve veli onayı e-postalarını bizim adımıza işler. Apple ve Google, mağaza satın almaları ve abonelikleri için kendi politikalarıyla bağımsız sorumludur." / EN: "YULA Lab is the data controller. Supabase (Frankfurt, EU) provides the account, authentication and database service, and Google (Google Workspace) sends account and parental-approval emails, both on our behalf. Apple and Google act as independent controllers for store purchases and subscriptions under their own policies."
- §4 tablo satırı "E-posta sağlayıcısı (seçilecek)" → **Google Workspace (veri işleyen)**; açık iş: Workspace Cloud Data Processing Addendum kabul kaydı + AB/ABD aktarım dayanağı (UNKNOWN, hukuk/kurucu). Yeni servis yok (mevcut yulalab.com Workspace).
- §6 madde 5 (HTTP posta API anahtarı, sağlayıcı seçimi) **geçersiz** → yerine: gönderen Workspace hesabında 2SV + uygulama şifresi; `MOTION_MAIL_FROM` = kimliği doğrulanan hesap veya "send as" takma adı; secret'lar `MOTION_SMTP_*` (CORE-07 paketi). yulalab.com SPF/DKIM'in Workspace için zaten yayında olup olmadığı UNKNOWN → kurucu Admin konsolunda DKIM durumunu okur.

**Koşullar `terms/page.tsx` §5 Motion — paywall A ve deneme cümleleri (ek)**
- TR: "Yeni abonelere mağaza sunduğunda 14 günlük ücretsiz deneme verilir; deneme, bitiminden en az 24 saat önce iptal edilmezse seçilen pakete mağazanın gösterdiği fiyattan otomatik geçer. Her kursun ilk modülü (yaklaşık ilk üçte biri) ücretsizdir; kalan dersler ve bağımsız pratik aşaması abonelik gerektirir. İlerleme kayıtlarınız abonelik bitse de görüntülenebilir. Kamera koçluğu ve hareket puanlaması bu sürümde sunulmaz." / EN: "Where the store offers it, new subscribers get a 14-day free trial; unless cancelled at least 24 hours before it ends, the trial continues as the selected plan at the price shown by the store. The first module of each course (about the first third) is free; the remaining lessons and the independent practice stage require a subscription. Your progress records stay viewable even after a subscription ends. Camera coaching and movement scoring are not offered in this version."

**App Review notu + mağaza açıklaması (abonelik; Apple 3.1.2, Play abonelik politikası)** — §7 EN metnine ek cümle:
- EN "New subscribers get a 14-day free trial where the store offers it; after the trial the subscription renews at the price shown unless cancelled at least 24 hours before the trial ends."
- İnceleme notu kalıbı (yer tutucu yalnız kurucu onaylı eşlemeyle dolar): EN "Paid camera coaching is not part of this version. In each course the first module (about the first third of the lessons) is free; the subscription unlocks the remaining lessons <APP: kurs/ders sayıları, ör. 'lessons 25–60 of Course A'> and the independent practice stage. Progress records stay readable without a subscription. Review account: provided separately." — app başına sayılar Core `motionFreeLessonLimit` / app `freeLessonLimit` override'ından gelir (Lissom onaylı: 24/60, 6/15, 5/14, 5/12, 7/19; diğer dört app UNKNOWN).

**Uygulama içi (Core, kanıtlı)**: R1 `cdcbf04` + R2 (CORE-03) `MotionMembershipPage`: mağazanın yerel fiyatı ve dönemi; mağaza bu hesaba deneme sunuyorsa "N gün ücretsiz, ardından aylık/yıllık {fiyat}" + deneme yenileme/iptal metni (14 dil); otomatik yenileme metni; geri yükle; mağazada yönet; Koşullar/Gizlilik. Deneme iddiası yalnız mağaza deneme teklifini bu hesaba döndürdüğünde gösterilir (Play: uygun teklif; App Store: SK2 tanıtım teklifi + `isIntroductoryOfferEligible`).

**Açık (kurucu/hukuk):** (1) app başına ücretsiz/ücretli eşleme onayı (Choreia "Salsa 6/18" dahil); (2) hukuk incelemesi P2–P9 + §5; (3) Motion+ denemesinin beş app'te ayrı ayrı alınabilmesi (CORE-11 maddesi 3); (4) Workspace DPA kaydı.

## 9. 27 Ekim — R4 (CORE-12 genç satın alma politikası) ve belge tutarlılığı (CORE-14)

Önceki bölümlerle çelişkide bu bölüm esastır.

**Posta secret adları (ET3-3 teyidi):** canlıda yalnız `MOTION_SMTP_HOST` (`smtp.gmail.com`), `MOTION_SMTP_PORT` (465), `MOTION_SMTP_USER`, `MOTION_SMTP_PASSWORD` (Workspace uygulama şifresi), `MOTION_SMTP_TLS` (`implicit`), `MOTION_MAIL_FROM`, `MOTION_CONSENT_PAGE_URL` okunur. `MOTION_MAIL_API_URL` / `MOTION_MAIL_API_KEY` R2'den (`2451428`) beri **yok**; §6 madde 5'teki eski metin geçersizdir.

**13–17 satın alma (kurucu OST-K1, 25 Ekim; kapsam K-2 = beş app, kurucu 27 Ekim → P5 için (B) geçerli; (A)/(C) yalnız tarihsel):** Core R4 app başına `MotionTeenPurchasePolicy` sunar. Varsayılan `parentalConsentRequired` (bugünkü davranış: veli onayı bekleyen hesaba satın alma önerilmez). `storeFamilyControls` seçen app'te teklifler açık kalır, ödeme kararını mağazanın aile/ebeveyn denetimi (Ask to Buy, Google Play ebeveyn onayı) verir; satın alma sayfası 18 yaş altı notunu gösterir. Hesap özellikleri iki politikada da veli onayına kadar kapalıdır; 13 yaş altı satın alamaz. P5 gençler cümlesi K-2 sonucuna göre seçilir (site tek gizlilik sayfasında beş app'i anlatır):
- **(A) beş app `parentalConsentRequired`** (bugün): §7 cümlesi aynen — TR "Veli onayı bekleyen hesaplara satın alma önerilmez; 18 yaş altındaki satın almalar mağazanın aile/ebeveyn denetimlerine tabidir." / EN "Accounts awaiting parental approval are not offered purchases; purchases by users under 18 are subject to the store's family and parental controls."
- **(B) beş app `storeFamilyControls`** (**seçildi — K-2, 27 Ekim**): TR "18 yaş altındaki kullanıcıların satın almaları mağazanın aile/ebeveyn denetimlerine tabidir; mağaza bir ebeveynin onayını isteyebilir. Veli onayı gereken hesaplarda hesap özellikleri onaya kadar kapalı kalır." / EN "Purchases by users under 18 are subject to the store's family and parental controls, which may ask a parent to approve. Where parental approval is required, account features stay closed until it is given."
- **(C) karışık** (yalnız Ostinato `storeFamilyControls`): TR "Veli onayı bekleyen hesaplara Choreia, Gravita, JabLab ve Lissom'da satın alma önerilmez; Ostinato'da satın alma kararı mağazanın aile/ebeveyn denetimine bırakılır. 18 yaş altındaki tüm satın almalar mağazanın aile/ebeveyn denetimlerine tabidir." / EN "Choreia, Gravita, JabLab and Lissom do not offer purchases to accounts awaiting parental approval; in Ostinato the store's family and parental controls decide. All purchases by users under 18 are subject to the store's family and parental controls."
- App Review notu (K-2 ile **beş app'in her biri** için) EN ek: "Teens below their country's digital-consent age can purchase through the store's family controls (Ask to Buy / Google Play parental approval); Motion account features stay closed until a parent approves by email."
- **Açık (hukuk/ürün):** onaylanmayan genç hesabı 30 gün sonra silinir (`motion_purge_unconsented_accounts`, zamanlama ayrı onay); mağaza aboneliği bununla iptal olmaz, yeni hesapta geri yüklenir. `storeFamilyControls` ile satın alıp veli onayı almayan genç için silme metni/iade beklentisi hukuk incelemesine eklenmeli.

**Veli onayı sayfası origin'leri (kurucu K-3, 27 Ekim):** `motion-parental-consent` yalnız `https://yulalab.com` ve `https://www.yulalab.com`'a CORS verir (Core R4.1 varsayılanı); önizleme origin'i yok. Önizleme ortamından onay sayfası canlı fonksiyonu çağıramaz (beklenen).

**Ders eşleme (25–26 Ekim kararı, §8 açık (1) güncellemesi):** Ostinato, JabLab, Gravita ve Choreia uygulamadaki mevcut sayıları `freeLessonLimit` override ile korur (Core formülü kullanılmaz); Choreia Salsa 18, Hip-Hop giriş kursu tamamen kilitsiz. Lissom için açık onay yok (K-7). İnceleme notundaki `<APP: …>` yer tutucusu app oturumlarının sayılarıyla dolar.
