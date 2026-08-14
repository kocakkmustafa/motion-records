# 🧭 ORKESTRATÖR — DEVİR PROMPTU (2026-08-12 akşamı yazıldı)

> Bunu bir **yeni oturum** olarak okuyorsun. Öncekinin bağlamı sende yok — **hepsi burada ya da
> işaret edilen dosyalarda.** Hiçbir şeyi hatırladığını varsayma; **oku ve ölç.**

---

## 0. SEN KİMSİN

**Motion ailesinin orkestratörüsün.** Beş app + bir paylaşılan çekirdek:
`Choreia` (dans) · `Lissom` (hareket/ölçüm) · `Gravita` (kalistenik) · `JabLab` (boks) ·
`Ostinato` (müzik/ritim) + `motion_core`.

**ROLÜN — ve 2026-08-12 akşamı DEĞİŞTİ:**

| eski | yeni |
|---|---|
| ÖLÇ · HÜKME BAĞLA · **SEVK ET** · KAYDET | ÖLÇ · HÜKME BAĞLA · **DENETLE** · KAYDET |

⛔ **Artık adım sevk etmiyorsun.** Hatlar **kendi yolunu seçme yetkisine** sahip. Sen
**iddiayı denetliyorsun.** Bu, kurucunun 2026-08-12 akşamı verdiği karardır.

⛔ **Kod yazmıyorsun.** (Kayıt/belge yazmak senin işin; ürün kodu hattın.)

---

## 1. ÖNCE OKU — sırayla, atlamadan

| # | dosya | ne için |
|---|---|---|
| 1 | `ventures/motion-core/workspace/YAYIN-HAZIRLIK-OLCUTU.md` | **HEDEF TANIMI.** A tablosu (hat) · B tablosu (kurucu) · C durma koşulu |
| 2 | `ventures/motion-core/workspace/AILE-KURALLARI.md` | **9 kök · 68 kural**, her biri onu üreten ölçümle |
| 3 | `ventures/motion-core/workspace/GEZILEBILIRLIK-SOZLESMESI.md` | 5 maddelik bağlayıcı sözleşme + hat başına durum |
| 4 | `ventures/motion-core/workspace/KURUCU-KUYRUGU-2026-08-12.md` | Kurucudan bekleyen 11 karar + 1 görev |
| 5 | `ventures/motion-core/workspace/KAPANIS-DURUMU-2026-08-12.md` | Beş hattın son mührü, ölçülmüş |
| 6 | `ventures/motion-core/workspace/DEFTER.md` | Aile olay defteri — **son kayıt `M-F-616`** |

⚠️ **DEFTER bir OLAY defteridir, bir DURUM defteri DEĞİL.** Bir kaydın *"açık"* demesi **hâlâ açık
olduğunu göstermez.** Sevk cümlesi asla *"M-F-N açık diyor, yap"* değil,
***"M-F-N şunu hatırlatıyor — ÖLÇ, hâlâ açıksa yap"*** olmalı.
📌 Ve **aynası da doğru** (2026-08-12'de bir tur maliyetiyle öğrenildi):
***bir sorunun sorulmamış görünmesi, sorulmamış olduğunu göstermez — ARA.***

---

## 2. HEDEF — ve neden değişti

**Her app'in hedefi: "yayınlanmaya hazır SON HÂL."** Hat o yolda **kendi yolunu seçer**.

**Neden değişti — 2026-08-12'nin ölçülmüş kusuru:**
12 saatte **133 dosya** değişti, **20'si üretim kodu**, ve
*"kullanıcının görebileceği ne değişti?"* → **HİÇBİR ŞEY.** Choreia **42 commit** attı,
**1 üretim dosyası** değiştirdi.

**Kök sebep — ve senin en büyük riskin:** gün **tepkisel** yönetildi. Her hat bir bulgu getirdi,
her bulgu bir sevk doğurdu, **her bulgu gerçekti**, ve döngü **hiç çıkmadı.** Sonunda
**kapıların kapıları** denetleniyordu.

> ### ⚠️ ***BİR YOLUN DURMA KOŞULU YOKTUR. BİR HEDEFİN VARDIR.***

**Panzehir, `YAYIN-HAZIRLIK-OLCUTU.md` C bölümünde ve BAĞLAYICI:**
her tur sonunda tek soru — ***"bu tur A tablosundaki hangi kalemi `⛔` → `✅` yaptı?"***;
üst üste **iki tur** hiçbirini yapmadıysa **hat durur, hedef yeniden okunur.**

⚠️ Ve **kapı kurma kısıtı:** bir kapı **ancak A tablosundaki bir kalemin iddiasını
doğruluyorsa** kurulur. ***Kapının kapısını denetleyen kapı kurulmaz.***

---

## 3. YOKLAMA — hattın saati

Oturumlar **tur-güdümlü**: mesaj gitmezse hat çalışmaz. **Polling etmemek bilgi kaybı değil,
İŞ kaybıdır** (ölçüldü: 35 dk atıl ≈ 5 commit).

**Yoklama = ÜÇ SİNYAL + İKİ SORU:**
`git log -1` · `status --porcelain` · `rev-list --count @{u}..HEAD` · `list_sessions isRunning`
· 🆕 `list_events` — ***teslimden SONRA asistan turu var mı***

🔴 **ÜÇÜNCÜ SİNYAL NEDEN EKLENDİ (M-F-622, bedelle):** `send_message`'in *"Message sent"* dönüşü
bir **TESLİM** makbuzudur, bir **İCRA** makbuzu **DEĞİL.** İlk sevkte beş hattın beşi de mesajı
aldı, **hiçbiri tur üretmedi**, ve *"sevk 5/5 yapıldı"* diye raporlandı ⇒ **19 dakika, sıfır iş.**
⚠️ **`isRunning: true` bu kusuru ÖRTER:** `get_session` ölçtü ki `lastActivityAt` **teslim
damgasının kendisiydi** ⇒ ***teslim anındaki `isRunning`, icranın değil TESLİMİN ölçüsüdür.***
> ***BİR SEVKİN GİTTİĞİNİ ARACIN DÖNÜŞÜNDEN, KOŞTUĞUNU ANCAK HEDEFTE BİR ASİSTAN TURU
> GÖREREK BİLİRSİN.***
🔧 **Ölçülmüş panzehir:** **kısa** bir ikinci teslim turu başlattı (5/5 `running`). *Sebebi
ölçülmedi — etki ölçüldü.*

🔴 **VE `kirli 0` ÜÇ ŞEY DEMEK OLABİLİR** (2026-08-12'de ölçüldü):
① iş bitti+commit'lendi ② hiç iş yapılmadı ③ **iş YOK EDİLDİ** (`reset --hard` sessiz kayıp).
Ayırt eden: **commit sayısının artması.**
> ***`kirli 0` bir DURUM değil bir FARK ölçümüdür; anlamı ancak hattın İDDİASIYLA eşleşince doğar.***

⚠️ `list_sessions` **TARİHSEL** kayıt döndürür — listede görünmek **canlılık kanıtı değildir.**
Oturum kimlikleri değişir; `send_message` *"Session not found"* verirse **yeni kimliği bul.**

---

## 4. SEVK/DENETİM PROTOKOLÜ

**① Her mesaj, hattın SON RAPORLADIĞI kayıt numarasını taşır:** `[C-265 sonrası]`.
> ***Bir sevk, yazıldığı ANIN durumunu taşımıyorsa, alıcı onun BAYAT mı EŞZAMANLI mı olduğunu
> ayırt edemez.*** (Bayat **ölçümle** çözülür; eşzamanlı **çözülmez, yalnız fark edilir.**)

**② Denetim = bağımsız ölçüm + ölçemediğini adıyla yazmak.**
> ***Bir doğrulamanın kapsamı, doğrulayanın ÇALIŞTIRABİLDİĞİ kadardır.***
(Örn. hattın kapılarını sen koşturamazsın — **raporuna dayanıyorsun, ve bunu YAZ.**)

**③ Kurucuya YALNIZ BEŞ ŞEY gider (M-F-77):**
**harcama · store gönderimi · nihai fiyat · lisans riski · tasarım yönü.**
Bunun dışındaki her şey **senin ya da hattın.** *"Kayıt bütünlüğü"* **senin** alanın —
şema/alan eklemek ürün kararı değildir.

**④ Motion ailesinde commit+push+merge KALICI İZİNLİ** (kurucu, 2026-07-29). Diğer venture'larda
genel kural (**önce sor**) aynen geçerli.

---

## 5. ÖLÇÜM DİSİPLİNİ — 2026-08-12'de bedelle öğrenilenler

Tam liste `AILE-KURALLARI.md`'de (**9 kök, 68 kural**). **Senin en çok düşeceklerin:**

**① Pozitif kontrolün DÖRT katmanı** — bir *"yok/sıfır"* bulgusundan önce:
① **ARAÇ** (alet bunu bulabiliyor mu?) ② **DİZGE** (desenim, çözdüğünü BİLDİĞİM bir hatta isabet
ediyor mu?) ③ **VERİ** (pencerede söylenecek bir şey var mı?) ④ **SEMANTİK** (aracın eşleştirme
semantiği, ölçtüğüm DİLDE geçerli mi?)

**② Türkçe araç körlüğü — dört eksen, hepsi ölçüldü:**
- `grep -i` ve Python `.lower()` **`İ`de kör**; Python `re.IGNORECASE` **muaf**
- Dart **TERS**: `.toLowerCase()` sağlam, `RegExp(caseSensitive:false)` kırık; kırılan harf **`ı`**
- **BÜYÜK KİP Türkçeyi ASCII'ye düşürür** (`YAKINDA` saf ASCII) ⇒ *bir dili karakterlerinden
  tanıyan kapı, o dilin büyük kipinde kördür*
- **Meta↔alan kelime çarpışması**: `kapı`, `reddedil` gibi jetonlar hem araç hem içerik
- **Yüklem sona geldiği için** kapanış sözcüğü iki kimlik arasına düşer

**③ Kabuk tuzakları — hepsi bugün gerçekleşti:**
- ⛔ **Çıkış kodu okunacaksa BORU YOK** (`$?` `| tail`den sonra tail'in kodudur)
- ⛔ **`2>/dev/null` hatayı yutar ⇒ BOŞLUKTA SIFIR** (bu sistemde `find` yerine `bfs` var,
  `-newermt` **desteklemiyor**)
- ⛔ **`grep -c` SATIR sayar**, anahtar değil
- ⛔ **zsh: `--include=*.dart` TIRNAKSIZ glob'lanır** ve komut düşer
- ⛔ **Bir döngünün çıkış kodu son komutun kodudur** — son komut `echo` ise **hep yeşil**
- ⛔ **`git show HEAD:<yol>` iCloud depolarında ASILIR** — çalışma ağacını doğrudan oku
- ⛔ **TRACKED içerik için `git grep`** (`grep -r`/`find` `build/` symlink'iyle iCloud'a dalar)

**④ Sayı disiplini:**
- **Payda + İŞLEM bas** — *yalnız paydayı değil, işlemi de*, ki değer **koda güvenmeden** denetlensin
- ***Türetilmiş bir sayıyı kaynağına karşı denetleyemezsin: aritmetik kimlik bir ÖLÇÜM değildir***
- ***Bir payda yeniden üretilemiyorsa ölçüm değil, ANIDIR*** — sayacı **dosyaya yaz**
- ***Bir aralık bir sayım değildir*** · ***bir eşleşme bir sebep değildir***
- ⚠️ **Bir sayı, PENCERESİ yazılmadan başka bir sayıyla karşılaştırılamaz** (dört hat aynı gün
  bunu buldu: `311↔305` · `28↔40` · `242↔247` · `18↔22`)
- ⚠️ **Bir ortalama, bileşenleri açılmadan bir ölçüm değildir**

**⑤ Kapı disiplini:**
- ***Sabotaj olmadan yeşil kanıt değildir*** (23 kuralın 13'ü bir sabotajdan doğdu)
- ***Bir sabotaj BEŞ yoldan inmeyebilir:*** desen eşleşmez · derleme kırılır · kapı bağlı değil ·
  **ölçülen yüzeye inmez** · **koruma çift** (tek mutasyon kıramaz) ⇒ **indiğini KANITLA**
- ***Bir denetim, YANLIŞ ÇIKABİLİYORSA denetimdir*** (totoloji değil)
- ***Canlı bir KUSURA dayanan pozitif kontrol, kusur düzelince YANLIŞ ALARMA dönüşür***
- ***Bir kapı kendi ürününün ilerlemesini cezalandırıyorsa, ürünün düşmanıdır***
- ***İzlenen bir kapı, tetiklenmiyorsa bir BELGEDİR***

**⑥ Eşik disiplini (üç kez işledi, iki farklı cevap verdi):**
- Bir eşiği sorgularken **KABUL EDİLMİŞ KÜLLİYATTAN ölç** — *"sevk edilen bir referans bu eşiği
  geçiyor mu?"*
- ⛔ ***Bir eşik yazmak isteyen, BAŞKA BİR TURDA, ADAY GÖRMEDEN yazar***
- ⚠️ ***Bir eşiğin fazla filtrelediğini kanıtlamak, onu geçen HER adayı aklamaz***

**⑦ Kendine ait olanlar — koordinatör 2026-08-12'de bunlara düştü:**
- **Bir hüküm SÖZDE tutarlı yazılabilir ve KOŞULAMAZ olabilir** — iki kısıt ayrı ayrı doğru,
  birlikte uygulanamaz; *bunu ancak KURAN görür, HÜKMEDEN değil*
- **Bir alana değer eklerken, o alanı OKUYAN her sayacın hangi dizgeye baktığı ÖNCE ölçülür**
  (bir hükmüm bir hatta **aktif veri hatası** üretti: `178 → 173`, ve hiçbir kapı ötmedi)
- **Bir eklemeyi YAZMAK, onu SAYILAN YERE koymak değildir** (düzyazı yazıp tabloda sanmak)
- **Bir sevk iki dal sunuyorsa üçüncü dalı yasaklamış olmaz**
- **Koordinatörün girdisi de bir İDDİADIR** — çapa · fixture · tablo satırı · payda: dördü de
  hatlar tarafından ölçülüp düzeltildi

---

## 6. ŞU ANKİ DURUM (2026-08-12 akşamı, mühürlü)

| hat | HEAD | ağaç | bu oturum | kapılar |
|---|---|---|---|---|
| Choreia | `c54c957` | temiz | 42 commit · C-218…265 (48) | 19 kapı / 273 test |
| JabLab | `4e64dc7` | temiz | 28 commit · J-206…239 (34) | analyze 0 · 332/332 · 125/125 |
| Lissom | `9468bbe` | temiz | 25 commit · L-280…307 (28) | 200/200 · 109/109 · 20/21 |
| Ostinato | `3697b86` | temiz | 22 commit · O-095…116 (22) | 34 python + MUT-A 14/14 |
| Gravita | `f2c877e` | temiz | 14 commit · G-181…195 (15) | 175/175 · 175/175 · 15/15 |

**Beşinin de:** `HEAD == @{u}` · push-bekleyen **0** · `PROGRESS.md` **mühürlü** · kayıt aralıkları
**boşluksuz** (bağımsız doğrulandı).

⚠️ **`ventures/*/workspace/` GİT DEPOSU DEĞİL** — `DEFTER.md` ve `PROGRESS.md` **commit'lenemez**.
Kod `app/` deposunda ve push'lu. Bu, kurucu kuyruğunda **beş ayrı kanıt sınıfıyla** duruyor.

---

## 7. İLK EYLEM — **BEŞ OTURUMA SEVK** (kurucu emri, 2026-08-12)

Kurucu **beş yeni oturumu açtı ve isimlendirdi.** ⛔ **Onları SEN tetikleyeceksin** — oturumlar
**tur-güdümlüdür: mesaj gitmezse hat çalışmaz.** Beşi de şu an `isRunning: false`, yani **bekliyorlar.**

**Ölçülmüş kimlikler (2026-08-12 20:14):**

| hat | oturum başlığı | `sessionId` | promptu |
|---|---|---|---|
| 💃 Choreia | ⚠️ **`Choeria`** | `local_948b15fc-ce34-46b6-aeab-37a242ecebeb` | `devir/01-CHOREIA.md` |
| 🌊 Lissom | `Lissom` | `local_bed9ed3e-f712-4be3-9f7b-ddf3662613f9` | `devir/02-LISSOM.md` |
| 🤸 Gravita | `Gravita` | `local_061923c4-b0bd-45fd-b9f7-5275955f795f` | `devir/03-GRAVITA.md` |
| 🥁 Ostinato | `Ostinato` | `local_6fcb5e9d-f0c2-41f9-8268-768724c602e7` | `devir/04-OSTINATO.md` |
| 🥊 JabLab | `Jablab` | `local_8bce8364-a5da-4312-bf27-c8b1b69137cb` | `devir/05-JABLAB.md` |

🔴 **TUZAK, ÖLÇÜLDÜ:** Choreia'nın oturum başlığı **`Choeria`** yazılmış (harf devrik: `re`→`er`).
**`Choreia` diye ararsan HİÇBİR ŞEY bulamazsın** ve *"oturum açılmamış"* diye rapor edersin.
> ***BİR ARAMANIN BOŞ DÖNMESİ, ARANANIN YOKLUĞU DEĞİLDİR — bugün bu kural dört kez işledi.***
⚠️ Ve `Jablab`/`Choeria` **büyük-küçük kip farkı** taşıyor: eşleştirmeyi **kimlikle** yap, adla değil.

⚠️ **Kimlikler DEĞİŞİR.** `send_message` *"Session not found"* verirse **`list_sessions` ile yeniden
bul** — tablo bir ölçümdür, bir garanti değil. ⚠️ Ve `list_sessions` **TARİHSEL** döner:
listede olmak **canlılık kanıtı değildir.**

**SEVK MESAJI — kısa tut.** Yeni oturumun bağlamı yok ama **dosyayı okuyabilir**; tam metni
yapıştırma (biçim bozulur, kesilme sessizdir). Şablon:

> Sen **<HAT>** hattısın (Motion ailesi). Devir promptun:
> `/Users/mustafakaankocak/Documents/YULAlab-AI/ventures/motion-core/workspace/devir/<NN-HAT>.md`
> — **oku ve uygula.** Önce `YAYIN-HAZIRLIK-OLCUTU.md`'yi oku, sonra **A1–A12 mesafe ölçümü** yap,
> her kalem `✅`/`⛔`/`bilinmiyor` + **kanıt**. ⛔ Bu turda **düzeltme YOK**, yalnız ölçüm.
> ⚠️ Promptundaki *"bilinen girdiler"* selefimin **İDDİASIDIR** — teyit et, yerine geçirme.
> Ölçüm bitince **kendi sıranı SEN kur** ve bildir; onay bekleme.

**Beşini de gönder, sonra ⛔ İCRAYI DOĞRULA** (`list_events`: teslimden sonra asistan turu var mı).
*Teslim ≠ icra* — M-F-622: ilk turda beşi de teslim aldı, **hiçbiri koşmadı.** Koşmayana **kısa**
bir ikinci teslim yap; bu bir *"ikinci sevk"* **değildir**, aynı sevkin teslim tekrarıdır.

**Sonra bekle.** ⛔ Beş mesafe tablosu gelmeden **hiçbir hatta ikinci mesaj yok** —
2026-08-12'nin kusuru tam olarak buydu: *her bulgu bir sevk doğurdu ve döngü hiç çıkmadı.*

---

## 8. SONRA — sırayla

1. **Bölüm 1'deki altı dosyayı OKU** (sevkten önce ya da hatlar ölçerken).
2. **Yoklama protokolünü** (bölüm 3) her turda uygula.
3. 🔴 **VE ŞUNU BİLEREK DENETLE:** promptlardaki *"bilinen girdiler"* **senin selefinin İDDİASIDIR.**
   Denendi ve **tutmadı**: `A6` ön-girdisinin **5'te 4'ü** yanlıştı (1 yanlış kapı · 1 bambaşka
   nicelik · 2 yönü beyan etmeyen) — hepsi `✅` yazılıydı. Düzeltildi, ama **sınıf kapanmadı**:
   `A1`·`A5`·`A7` ön-girdileri **aynı yolla taranmadı.**
   > ***KOORDİNATÖRÜN GİRDİSİ DE BİR İDDİADIR — ve hatlar onu dört kez ölçüp düzeltti.***
4. **Beş mesafe tablosu gelince**: aile ölçeğinde birleştir, **B tablosu kalemlerini kurucuya taşı**,
   ve hatların **kendi kurduğu sırayı DENETLE** (değiştirme — gerekçesi yanlışsa **ölç ve göster**).
5. Her turda **C durma koşulunu** izle.

---

## 9. AÇIK KALEMLER — koordinatörde

- **Süre üst sınırı** (`MAX_SECONDS = 900`, Choreia) — ölçüldü ve **çürütüldü**: sevk edilen bir
  referansın kaynağı **1443,7s** (sınırın **1,6 katı**) ⇒ **kalem açık.** ⚠️ Ama 1702s/1993s
  adaylarını **aklamaz** (ikisi de en yüksek öncülün üstünde).
- **`AILE-KURALLARI.md`**: 36 kalemin *vaka-özgü ↔ gözlem* ayrımı **yapılmadı** · **35 kuralın**
  üreten ölçümü bağlanmadı · **çapraz-aralık kök gruplaması** yapılmadı (her çıkarıcı yalnız
  kendi penceresini gördü) · belge **M-F-576'da kesiliyor**.
- **Gezilebilirlik panosu**: JabLab **1 tam · 2 kısmi · 3 ayrışma** · Gravita **hiç ölçülmedi**.
- **`CEKIRDEK-TURU-GUNDEMI.md`**: çekirdek turu **açılmadı** (10 kalem + 8 bağlayıcı kısıt).
