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
- TR "Fatura ve abonelik kayıtları: yalnız yasal olarak gerekli süre (ilk sürümde satış kapalı)." / EN "Billing and subscription records: only as long as the law requires (sales are closed in the first release)."

**P8** (başlık: "Veri rolleri ve alt işleyenler" / "Data roles and processors") — TR: "Veri sorumlusu YULA Lab'dir. Supabase (Frankfurt, AB) hesap, kimlik doğrulama ve veritabanı hizmetini; [e-posta sağlayıcısı] hesap ve veli onayı e-postalarını bizim adımıza işler. Apple ve Google, mağaza satın almaları ve abonelikleri için kendi politikalarıyla bağımsız sorumludur." / EN: "YULA Lab is the data controller. Supabase (Frankfurt, EU) provides the account, authentication and database service, and [email provider] sends account and parental-approval emails, both on our behalf. Apple and Google act as independent controllers for store purchases and subscriptions under their own policies." — *[e-posta sağlayıcısı] seçilince doldurulur.*

**P9** (Haklarınız 1. paragrafa ek) — TR: "Ebeveyn veya vasiler, gencin hesabıyla ilgili taleplerini aynı adrese iletebilir. Yanlış beyan edilen doğum tarihi destek üzerinden düzeltilir." / EN: "Parents or guardians can send requests about a teen's account to the same address. An incorrectly declared birth date is corrected through support."

**Yeni sayfa (YULALAB):** `src/app/[locale]/motion/consent/page.tsx` — `#token=` fragment'ini okur, `motion-parental-consent`'e
`{action:"view"}` ile maskeli e-posta/son tarih gösterir, Onayla/Reddet → `{action:"decide"}`. Publishable key ile
`POST https://<ref>.supabase.co/functions/v1/motion-parental-consent` (verify_jwt=false). Metin: P6 özeti + "Reddederseniz hesap silinir"
+ sonuç durumları (onaylandı / reddedildi ve silindi / süresi doldu / geçersiz bağlantı). 14 dil.

## 2. Site: `src/app/[locale]/terms/page.tsx` — Motion özel şartları

Yeni bölüm, satır 107 ("5. Burun Farkı — özel şartlar") öncesine; sonraki bölüm numaraları +1:
**"5. Motion uygulamaları — özel şartlar" / "5. Motion apps — special terms"** — TR: "Choreia, Lissom, Gravita, JabLab ve Ostinato tek bir Motion hesabını paylaşır; hesap 13 yaş ve üzeri içindir ve bazı ülkelerde 18 yaşından küçükler için ebeveyn/vasi onayı gerekir. Bir uygulamada satın alınan bireysel abonelik yalnız o uygulamada geçerlidir; Motion+ beş uygulamayı kapsar. İlk sürümde satış kapalıdır. Hesabı silmek beş uygulamadaki hesabı birlikte siler ancak Apple veya Google aboneliğini iptal etmez; aboneliği mağaza hesabınızdan ayrıca iptal etmelisiniz. Motion uygulamaları tıbbi cihaz değildir." / EN: "Choreia, Lissom, Gravita, JabLab and Ostinato share one Motion account; the account is for people aged 13 and over, and in some countries users under 18 need a parent's or guardian's approval. An individual subscription bought in one app applies only to that app; Motion+ covers all five. Sales are closed in the first release. Deleting the account deletes it in all five apps together but does not cancel an Apple or Google subscription; cancel it separately in your store account. The Motion apps are not medical devices."
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
   Docker Desktop kurulu ve açık değilse kullanıcı açar/kurar. Supabase CLI kurulu değilse `brew install supabase/tap/supabase` onayı.
2. Sonra Core oturumu kendisi yürütür: `supabase start` → `supabase db reset --local` → SQL testleri → `MOTION_LOCAL_*` ile
   `local_account_integration_test.dart` → `supabase functions serve` + Deno → `supabase stop`. Kullanıcı girdisi gerekmez
   (yerel anon anahtar `supabase status` çıktısından, sır değildir).

**Canlı proje (deploy ve readback):**
3. Supabase Motion proje ref'i + CLI erişim onayı (kullanıcı `supabase login` yapar; Core oturumu token görmez/yazmaz).
4. Onay: `supabase db push` (yalnız `20261021190000`) + `supabase functions deploy motion-parental-consent` + secret'lar.
5. Kullanıcı girdisi: e-posta sağlayıcısı seçimi ve hesabı, `yulalab.com` DNS'e SPF/DKIM kayıtları (DNS değişikliği onayı),
   `MOTION_MAIL_API_KEY`'i kullanıcının kendisi `supabase secrets set` ile girer; `MOTION_MAIL_FROM` ve `MOTION_CONSENT_PAGE_URL` metin.

**TLS 1.2 CBC (en erken 10 Kasım) cihaz kabulü:**
6. Kullanıcı: iOS 15.x çalışan bir iPhone ve Android 7.0 (API 24) cihaz sağlar (veya en düşük desteklenen gerçek sürüm kararı).
7. Onay: G1–G3 sonrası imzalı aday paket (IPA/AAB) üretimi ve cihaza kurulum; Core oturumu senaryo listesini (PREP-PLAN D1–D2) verir.
8. Onay: `openssl s_client -connect <ref>.supabase.co:443 -tls1_2` ile cipher readback (salt okuma, proje ref'i gerekir).

**Hukuk:** 9. ülke yaş tablosu + P2–P9 metinleri + Art. 27 temsilcisi + VERBİS için danışman incelemesi.
