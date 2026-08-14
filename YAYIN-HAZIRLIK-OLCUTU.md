# 🎯 YAYIN HAZIRLIK ÖLÇÜTÜ — Motion ailesi

> **Kurucu kararı, 2026-08-12:** her app'in hedefi ***"yayınlanmaya hazır son hâl"***; hat o yolda
> **kendi yolunu seçme yetkisine** sahiptir, koordinatör **adım sevk etmez, ÖLÇÜMÜ DENETLER.**
>
> ⚠️ **Bu dosya ölçütü BİR KEZ tanımlar.** Sebebi bugün on yedi kez ölçüldü:
> ***aynı kelime, beş hatta beş birim olur*** — ve *"yayına hazır"* en kolay ayrışan kelimedir.

---

## ⚠️ ÖNCE: DEVİR PROMPTLARINDAKİ "BİLİNEN GİRDİLER" BİRER **İDDİADIR**

Her hattın devir promptunda *"bilinen girdiler"* tablosu var. **Onlar ölçüm değil, koordinatörün
iddiasıdır** — ve **ilk turda biri zaten yanlış çıktı**: Choreia'nın `A6`'sı `✅` yazılmıştı, oysa
hattın kapısı **tek yönlü** ve **başka bir kapıydı**; A6 ***iki yönlü tazelik kapısı*** istiyor.

> ***AYNI KELİME, İKİ KATMANDA İKİ BİRİM OLABİLİR — ve bu tabloda en çok orada olur.***

⇒ **Ön-girdiyi TEYİT ET, yerine geçirme.** Uymuyorsa **ölçümü yaz, ön-girdiyi düzelt.**

📊 **Ve bu tek vaka değildi — bulunca AYNI SINIFI beş promptta da taradım:**
**`A6` ön-girdisinin 5'te YALNIZ 1'i** (Ostinato) A6'nın istediği kanıtı taşıyordu.
Kalan dördü: **1 yanlış kapı** (Choreia) · **1 bambaşka nicelik** (Lissom: *kapanış-kaydı sayısı*) ·
**2 yönü hiç söylemeyen** (Gravita · JabLab). Hepsi `✅` yazılmıştı.

> ***BİR HATA BULUNDUĞUNDA SORULACAK İKİNCİ SORU, "AYNISINDAN KAÇ TANE DAHA VAR?"DIR.***
> Bir vaka düzeltilir; **bir sınıf taranır.**

---

## KURAL: her kalem **İKİLİ** ve **ÖLÇÜLMÜŞ**

Bir kalem `✅` sayılır ancak **çalıştırılabilir bir kanıt** varsa (kapı · test · artefakt · ekran
görüntüsü). ***Beyan `✅` değildir.*** Ölçülemeyen kalem `⛔ ÖLÇÜLEMEDİ` yazılır — `❌` değil.

> ***BİR ÖLÇÜTÜN DEĞERİ, "HAYIR" DİYEBİLMESİNDEDİR.***

---

# A. HAT KAPATABİLİR (yetki hatta — kurucuya sormadan)

| # | kalem | kanıt ne olmalı |
|---|---|---|
| **A1** | **En az bir TAM AKIŞ baştan sona çalışıyor** — ilk açılış → seçim → oturum → sonuç | yürüyüş testi, **taze kurulumdan**, `NavigatorObserver` tanığıyla |
| **A2** | **Onboarding var ve ÇIKIŞI var** — düğmeye basılarak geçiliyor | A1'in içinde, **bayrak set edilerek değil** |
| **A3** | **Sessiz boş yüzey YOK** — her boş yüzey ya iş sunuyor ya **neden sunmadığını söylüyor** | *sessiz oranı* ölçümü (JabLab'ın üç şartlı tanımı) |
| **A4** | **Çıkmaz sokak sayısı ölçülmüş ve ADIYLA yazılmış** | **taksonomi ↓** + payda **ve İŞLEM** |
| **A5** | **Kapılar yeşil, sayısıyla** + öz-testler **koşuyor ve engelliyor** | `run_gates` çıktısı, **borusuz** |
| **A6** | **DEFTER taze** — gedik 0, iki yönde | tazelik kapısı exit 0 |
| **A7** | **Gezilebilirlik sözleşmesi 5/5, METNE karşı** | `GEZILEBILIRLIK-SOZLESMESI.md` maddelerine karşı ölçüm |
| **A8** | **Gizlilik manifesti PAKETTE** (yalnız depoda değil) | paket içinden çıkarılıp doğrulanmış |
| **A9** | **Ağ beyanı ölçümle uyuşuyor** | `network_claim_audit` benzeri kapı yeşil |
| ~~A10~~ | 🔻 **B8'E TAŞINDI** (2026-08-13, koordinatör hükmü) | ⛔ hat kapatmaz — gerekçe B tablosunda |
| **A11** | **Release derlemesi geçiyor** (imzasız da olsa) | `assembleRelease` / `build ipa --no-codesign` |
| **A12** | **Cihaz gerçeği** — gerçek cihazda en az A1 akışı koştu | ekran kaydı ya da cihaz logu |

---

## 🔻 A4 TAKSONOMİSİ — burada TANIMLI (2026-08-13'te eve taşındı)

🔴 **Neden burada:** ölçüt *"A/B/C/D dağılımı"* diyordu ama **hiçbir yerde tanımlamıyordu**;
tanım yalnız `DEFTER M-F-575`te ve **Choreia'nın promptunda** yaşıyordu. Ostinato ölçtü ve
adıyla yazdı: bu, ailenin ***"kural evsiz"*** vakalarının **dördüncüsü** (öncekiler: `PROGRESS.md`
kapanış zincirinde · günün kuralları · gezilebilirlik sözleşmesi).
⇒ Ostinato'nun verdiği `A 0 · A′ 10 · B 0 · C 0 · D 3` eşlemesi **onun okumasıydı, ölçüm değil** —
çünkü ölçecek metin yoktu. Artık var.

| sınıf | tanım | kim kapatır |
|---|---|---|
| **A** | içerik **hiç yazılmamış** | içerik kapasitesi (aylar) |
| **A′** | içerik **başlamış**, referans **yok** | hasat turu |
| **B** | içerik **var**, **bağlı değil** (kablolama boşluğu) | hat |
| **C** | kart/yüzey **hiç olmamalıydı** | hat |
| **D** | içerik **TAM + BAĞLI**, **bilerek KAPALI** | çoğu zaman **kurucu** |

🔴 **`D` koordinatörün ilk sınıflandırmasının kusurundan doğdu** (M-F-575): üç kova **yalnız
EKSİKLİĞİ** modelliyordu, **kasıtlı kapalılık** hiçbirine girmiyordu.
> ***BİR SINIFLANDIRMA, YALNIZ KUSUR BİÇİMLERİNİ SAYIYORSA, DOĞRU KARARLARI DA KUSUR KOVASINA ATAR.***

🆕 **`E` — `awaiting-capability` (Ostinato ölçtü, 2026-08-13, KABUL):** *ölçüm YETENEĞİ yok.*
10 `locked` kaleminin **en az 4'ü** veri değil **alet** eksikliğini adlandırıyor
(`hands_and_wrists`: *"a missing measurement **TOOL**, not a missing threshold"`).
A–D **yalnız içerik/kablolama** eksikliğini modelliyor ⇒ beşinci kova. Ailenin kelimesi
**zaten vardı** (M-F-376: `awaiting-content` ↔ `awaiting-capability`), **A4'e bağlanmamıştı.**

⚠️ **Ve sınıfın kendi sınırı yazılı (M-F-603):** *bir sınıflandırma, kalemlerin **BUGÜNKÜ**
engelini gösterir, bir sonrakini değil* — `A′` bir referans indiği gün **`B`'ye döner.**

---

# B. KURUCU KAPATABİLİR (⛔ hat DOKUNMAZ — M-F-77)

| # | kalem | neden kurucuda |
|---|---|---|
| **B1** | **Android release keystore** | güvenlik/imza sahipliği |
| **B2** | **Sürüm hizası** (`0.1.0+1` ↔ ASC `1.0`) | **gönderim blokajı**, 5 hattın 4'ünde |
| **B3** | **Store metni + ekran görüntüleri** | ürün sesi / tasarım yönü |
| **B4** | **`AFTER_APPROVAL` duruşu** — onayda otomatik yayın | store gönderimi |
| **B5** | **`google_fonts` duruşu** (paketle ↔ indir) | tasarım yönü + gizlilik beyanı; **bugün 3 sonuca bağlandı** |
| **B6** | **Nihai fiyat / IAP** | fiyat |
| **B7** | **Gönderimin kendisi** | store gönderimi |
| **B8** | 🔻 **İkon ŞABLON DEĞİL** (eski `A10`) | **tasarım yönü** — aşağıda |

### 🔻 A10 → B8: neden taşındı (2026-08-13, koordinatör hükmü)

**Dört hat BAĞIMSIZ olarak aynı çelişkiyi buldu** (Choreia · Gravita · Ostinato · JabLab):
ölçüt `A10`'u **A tablosuna** koyuyordu (*hat kapatır*), ama **M-F-77** hattın dokunmadığı beş
şeyden biri olarak **tasarım yönünü** sayıyor — ve *bir uygulama ikonu üretmek* tasarım yönüdür.
⇒ Hat `A10`'u kapatmak için **dokunmaması gereken şeye dokunmak zorunda kalıyordu.**

> ***BİR KURUCU DİREKTİFİ İLE BİR KOORDİNATÖR METNİ ÇELİŞİRSE, DİREKTİF KAZANIR —
> VE BUNU ÇÖZMEK KOORDİNATÖRÜN İŞİDİR, HATTIN İKİLEMİ DEĞİL.***

📊 **Ölçüm tarafı BİTTİ, karar tarafı kurucuda:** beş hat da **şablon varsayılanı** taşıyor —
Choreia Android 5/5 + iOS `c785f893…` · Lissom 5/5 + iOS Flutter logosu · **Gravita 20/20** ·
Ostinato 6/6 (tek commit `b5bd37c`) · **JabLab 20/20**.
🪤 Ve ölçüm iki hatta **ters çıkmıştı**: `templates/app/ios.tmpl/…` dosyaları **0 BAYT**
(`md5 d41d8cd9…` = `/dev/null`) ⇒ naif karşılaştırma *"15/15 FARKLI"* diyordu.
Geçerli yer doğrusu **taze `flutter create`**; Gravita ve JabLab bunu **bağımsız** buldu.
> ***BİR KARŞILAŞTIRMANIN SONUCU, REFERANSININ GERÇEK OLDUĞU KADAR GEÇERLİDİR.***

---

# C. DURMA KOŞULU (bugünün dersinden — bağlayıcı)

Her turun sonunda **tek soru**:

> ### ***"Bu tur, A tablosundaki hangi kalemi `⛔` → `✅` yaptı?"***

- **Hiçbirini** yaptıysa → tur **sayılır ama işaretlenir**
- ***Üst üste İKİ tur hiçbirini yapmadıysa*** → ⛔ **hat DURUR ve koordinatöre bildirir**;
  hedef yeniden okunur, yol değiştirilir

📌 **Gerekçe ölçülmüş:** 2026-08-12'de bu sayaç **12 saat boyunca sıfırdı** ve hiçbir şey ötmedi
(133 dosya değişikliğinin **20'si** üretim kodu, ve *"kullanıcının görebileceği ne değişti?"*
sorusunun cevabı **hiçbir şey**).

⚠️ **Ve kapı kurma kısıtı:** *bir kapı, ancak **A tablosundaki bir kalemin** iddiasını
doğruluyorsa kurulur.* Kapının kapısını denetleyen kapı **kurulmaz**.

---

# D. YETKİ VE DENETİM

**HATTIN YETKİSİ:** A tablosundaki kalemleri kapatmak için **kendi yolunu seçer** — adım sevki
beklemez. Motion ailesi için **commit + push + merge kalıcı izinli** (kurucu, 2026-07-29).

**KOORDİNATÖRÜN ROLÜ — sevk değil DENETİM:**
1. Her milestone raporunda **iddiayı bağımsız ölçer** (yapabildiği kadar)
2. **Ölçemediğini ADIYLA yazar** — > ***bir doğrulamanın kapsamı, doğrulayanın ÇALIŞTIRABİLDİĞİ kadardır***
3. **B tablosunu kurucuya taşır**, hat adına karar **vermez**
4. **C durma koşulunu** izler ve tetikler

⛔ **HATTIN DOKUNMADIĞI BEŞ ŞEY (M-F-77):** harcama · store gönderimi · nihai fiyat ·
lisans riski · tasarım yönü.

---

# E. İLK İŞ — MESAFE ÖLÇÜMÜ

Her hat **önce kendini bu tabloya karşı ölçer** ve **A1–A12 için `✅ / ⛔ / bilinmiyor`** verir.

> ***Yolun ne kadar kaldığını bilmeden yola çıkmak, ilerlemeyi ölçülemez kılar.***

⚠️ Ve ölçüm kuralı bugünden: **`⛔` ile `bilinmiyor` AYNI KOVAYA GİRMEZ** — birincisi *ölçüldü ve
yok*, ikincisi *hiç bakılmadı*.
