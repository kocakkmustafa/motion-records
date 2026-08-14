# 📐 LISSOM — DEVİR PROMPTU (2026-08-12 akşamı)

> Yeni oturumsun. **Hiçbir şeyi hatırladığını varsayma — oku ve ölç.**

## 0. KİMSİN · NEREDESİN
`Lissom` = **hareket/ölçüm** app'i. Ağaç: `ventures/lissom/{app,workspace}` · defter
`workspace/DEFTER.md` (**son kayıt `L-307`**, **git İÇİNDE** (2026-08-15, `app/workspace/`)) · kod `app/` (git, push'lu).
**Mühür:** `HEAD = 9468bbe` · ahead 0 / behind 0 · ağaç **temiz** ·
**app 200/200 · engine 109/109 · python 20/21** (21'inci **bilinen**: `fixture_check.py`, paylaşımlı
rig `anatomical_mode()` taşımıyor — **M-F-280**).

## 1. HEDEF — ve yöntem 2026-08-12 akşamı DEĞİŞTİ
🎯 **Hedefin: "yayınlanmaya hazır SON HÂL".** Yolunu **SEN seçersin**; orkestratör **adım sevk
etmez, ÖLÇÜMÜ DENETLER.**
📄 **ÖNCE OKU:** `ventures/motion-core/workspace/YAYIN-HAZIRLIK-OLCUTU.md`
· **A1–A12: SEN** · **B1–B7: KURUCUDA**, ⛔ dokunma · **C: DURMA KOŞULU** (üst üste iki tur
`⛔→✅` yoksa **DUR ve bildir**) · ⚠️ **kapı ancak A'daki bir kalemi doğruluyorsa kurulur.**

🔴 **Neden değişti:** ailede 12 saatte **133 dosya** değişti, **20'si üretim kodu**, ve
*"kullanıcının görebileceği ne değişti?"* → **hiçbir şey.** ***Bir yolun durma koşulu yoktur.***

## 2. İLK İŞ — MESAFE ÖLÇÜMÜ (tek tur, ⛔ düzeltme YOK)
**A1–A12: `✅` / `⛔` / `bilinmiyor`**, kanıtıyla. ⚠️ ***İkisi aynı kovaya girmez.***
Sonra **kendi sıranı SEN kur** ve bildir — **onay bekleme.**

**Bilinen girdiler (teyit et):**
| kalem | bilinen |
|---|---|
| **A1** tam akış | `KATI 3` rota · **6 aile hedefi**, **1'i içerikli** (Assessment Battery) — *bir kullanıcı bir ölçümü baştan sona yapabiliyor mu?* |
| **A3** sessiz boş yüzey | ✅ **BOŞ-SESSİZ 0** — 5/6 boş ama **beşi de `honestyBox` + envanter satırı** taşıyor, sayı **config'ten türetiliyor**, *"yakında N"* **demiyor** |
| **A6** defter | ⚠️ **ÖN-GİRDİ A6'YI KARŞILAMIYOR — bu bir `bilinmiyor`dur, `✅` değil.** Bildiğim şey `Durum KAPALI 178` (gün içinde 173'e düştü, düzeltildi, **ÇAPALANDI**) — ama o bir **kapanış-kaydı sayısı**, A6'nın istediği **defter tazelik gediği DEĞİL**, ve **yönü hiç söylemiyor.** ⇒ **SEN ölç: gedik 0 mı, ve İKİ YÖNDE mi?** |
| **A7** sözleşme | ✅ **5/5 METNE karşı — ailenin İLK hattı** |
| **A5** kapılar | ✅ 20/21 (**21'inci adıyla bilinen**) |
| **A2·A4·A8·A9·A10·A11·A12** | **bilinmiyor** |

## 3. AÇIK KALEMLER — nerede + sıradaki adım
**ⓐ SENDE (⚠️ ikisi de YAYIN ENGELİ DEĞİL, düşük öncelikli):**
1. **`invert` hiçbir kontrolle korunmuyor** — `kSealedBridgedJoints` mührü **YALNIZ**
   `metric→coreJointId`yi koruyor. Borç ***testin kendi gövdesinde*** yazılı:
   `app/packages/lissom_engine/test/metric_coverage_test.dart` **~L110**: *"AÇIK boşluk, bu tur
   kapatılmıyor"*. 8 binding'in hepsi `invert: false` ⇒ ***yanlış bir `true` SESSİZCE geçer.***
   **SIRADAKİ:** mührü `invert`i de kapsayacak şekilde genişlet + sabotajla kanıtla.
2. **Köprülenemeyen `measureKind` metrikleri** + Library/Progress derinliği (⑩ içerikle komşu).

**TAŞINAN (çözülmedi, SAYILI muafiyetle):** ID çakışması **3** (`L-187`·`L-089`·`L-090`, 6 hücrede
şerh) · `L-195` **8 sütunlu** (sayıma etkisi yok ama *"şansa doğru"*) · `Kapanış kanıtı` **BOŞ 13** ·
5 `REDDEDİLDİ (kapalı)` kaydı.

**ⓑ ORKESTRATÖRDE:** ⑨ batarya özeti (`SessionRecord` **değer+bant** taşımıyor → çekirdek turu) ·
`surface_language_test` kapsamı (*vaat kelimesi aranıyor, tutulamayan söz görülmüyor*) ·
GEVŞEK okuma tanımı (**KATI 3 kanonik**).

**ⓒ KURUCUDA:** ④ ikon (**Flutter varsayılanı**) · ⑥ metadata (**build 0**) · ⑩ içerik (5/6
**boş-BEYANLI**, *kusur değil*) · ⑪ IAP · ⑫ sürüm hizası · ⑬b cihaz turu · ⑭ keystore ·
`google_fonts` · **JDK** (venture-ötesi) · ⚠️ **`releaseType: AFTER_APPROVAL`** — onaylanınca
**otomatik yayın**, bilerek seçilsin.

## 4. 🔴 SON TURUN DERSİ — kapanış cümleni GERİ ALDIN, tekrarlama
*"Kod tarafında ölçülebilir kalem kalmadı"* dedin; ölçtüğün küme **yayın engelleriydi.**
> ***BİR KAPANIŞ CÜMLESİ, ÖLÇÜLEN KÜMENİN ADINI TAŞIMALI*** — *"yayın engeli kalmadı"* ile
> *"kod kalmadı"* **aynı ölçümden çıkmaz.**
🪤 Ve iki tuzak: yol **yoktu** (`packages/…` ↔ gerçeği `app/packages/…`) **+ `2>/dev/null` hatayı
YUTTU** ⇒ ***boşlukta sıfır*** · zsh **tırnaksız glob** komutu düşürdü.

## 5. SENİN BEDELLE ÖĞRENDİKLERİN — ailenin yedi kuralı senden çıktı
- ***Kaynakta beyanlı olmak, KULLANICIYA beyanlı olmak değildir*** (iki ayrı yüzey, iki ayrı kapı)
- ***Bir öz-testi kopyalamak, koruduğu RİSKİ de devraldığını varsaymaktır***
- **(d) bölme denklemi** — `aday = varılan ⊎ varılamayan`
- ***Bir bölme denetimi, iki tarafı AYNI KAYNAKTAN okuyorsa denetim değil TANIMDIR***
  (⚠️ **kendi maddeni kör yazdın** — gözlem aday listesinden **bağımsız** üretilmeli)
- ***Bir elle liste, KAYNAK olarak yanlıştır ama KONTROL olarak doğrudur*** — silinmez, rütbesi düşürülür
- ***Düzeltilmiş kusur ≠ ölçülüp REDDEDİLMİŞ yol*** (birincisi tekrar edilmez, ikincisine
  **yeniden girilebilir**)
- ***Bayat sevk ≠ eşzamanlı sevk*** — **sevk protokolünü sen değiştirdin** (`[L-307 sonrası]`)
- ⚠️ Ve: ***bir panzehir, taşındığı yerde ölçülmeden uygulanamaz*** — Choreia'nın indeksleme
  çözümünü kopyalasaydın **176** raporlayacaktın; **backtick-korumalı `c[4]`** doğrusu **178**.

## 6. SERT KURALLAR
⛔ `ventures/motion-core/lib/tools` **hiçbir kipte kaynak değil.**
⛔ Kurucuya yalnız beş şey: **harcama · store gönderimi · nihai fiyat · lisans riski · tasarım yönü.**
✅ Motion ailesinde **commit+push+merge kalıcı izinli.**
⚠️ `workspace/` **git deposu DEĞİL** — `DEFTER.md`/`PROGRESS.md` commit'lenemez, ama **yazılır.**
