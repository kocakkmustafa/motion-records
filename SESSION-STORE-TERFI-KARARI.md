# SessionStore ÇEKİRDEK-TERFİ KARARI (üçler kuralı hakemliği)

**Tarih:** 2026-07-30 · **Hakem:** koordinatör (M-F-183 gereği) · **Kayıt:** M-F-193
**Girdiler:** JabLab `session_store.dart` (J-064, normatif kaynak) · Choreia
delta-sözleşmesi (109 satır) · Gravita delta-sözleşmesi (147 satır, ÖLÇÜMLÜ).
**Çıktı:** `motion_core` `lib/src/session/session_store.dart` (tag `motion_core-v0.9.0`).

## Kararlar (her biri girdisiyle)

1. **Kurucu `File` alır** (Gravita terfi-şartı #1; ölçümle düzeltilen kapsam
   hükmü: "depo saf Dart, kablolama Flutter"). `path_provider` app'te kalır.
2. **Nötr iş-birimi, KAYIT-başına etiket:** `unitsCompleted`/`plannedUnits`/
   `unitLabel` — üç oturumun bağımsız yakınsaması + Gravita'nın ölçümlü kırışı
   (22 repFsm + 8 staticHold + 1 multiPhase AYNI app'te; "3 of 5 reps" ile
   "45 of 60 seconds" aynı ekranda). App-düzeyi etiket İFADE EDEMEZ.
3. **`lessonClass` yazım-anında, AÇIK sözlük:** core stringi olduğu gibi saklar
   (Choreia `demoOnly` · Gravita `measurementOnly` — sözcük app'in, AYRIM
   ailenin). Tek paylaşılan değer `scored`; **en-az-yetki okuma kuralı**
   çekirdekte: `isScoredClass == (lessonClass == 'scored')` — bilinmeyen/boş
   sınıf ASLA skorlanmış okunmaz (Choreia kuralının genellemesi).
4. **`unmeasuredUnits` + `unmeasuredReason?` çekirdekte, varsayılan 0/null**
   (Gravita delta-3; "sessizlik yalandır"): `unitsCompleted` ÖLÇÜLENİ sayar;
   `attemptedUnits = unitsCompleted + unmeasuredUnits` kullanıcının yaptığı
   iştir; `isComplete` ATTEMPTED üzerinden (PRD "ölçülemeyen deneme ilerleme
   düşürmez" — tamamlama bir ÖLÇÜMDÜR, hüküm değil).
5. **staticHold dejenerasyonu: (a) KABUL-ET-VE-BELGELE.** `unitLabel=='second'`
   iken `unitsCompleted≈workedSeconds` bilinçli tekrardır; (b)-türetme
   okuyucuya etikete-göre-dallanan bir alan-varlığı dayatırdı (tek-tip kayıt
   şekli > akıllı sıkıştırma). Tüketici-rehberi: yüzey ikisini bağımsız olgu
   gibi GÖSTERMEZ (türetilebilir bayrak: `unitLabel=='second'`).
6. **Depo değişmezleri AYNEN** (J-064): append-only JSONL · 3.-taraf DB YOK ·
   SATIR-düzeyi şema (`v:2`) · atomik tmp+rename · bozuk-satır geçmişi silmez ·
   yarım son satır götürmez · bilinmeyen `v` atlanır · dosya-yokluğu hata değil ·
   `_readAll` DEĞİŞTİRİLEBİLİR liste · UTC.
7. **v1-mirası:** okuyucu JabLab'ın v1 satırlarını kabul eder
   (`roundsCompleted→unitsCompleted`, `unitLabel:'round'`, `lessonClass:''` →
   en-az-yetki gereği skorlanmamış okunur — JabLab'ın bugünkü yüzeyi zaten
   hüküm göstermiyor, semantik doğru). Tam geçiş JabLab'ın adopte turunda.
8. **ADR-005 köken alanları (analysisConfidence/orientationStrategy/modelSha)
   EKLENMEDİ** — Attempt-düzeyi; SessionRecord seans-düzeyi (Gravita sınırı
   aynen). Attempt-kalıcılığı kamera köprüsüyle gelen AYRI kalem.
9. **Arayüz dar kalır:** `append` / `recent({limit})` en-yeni-önce /
   `workedSecondsFor(lessonId)`. Sorgu ihtiyacı ÖLÇÜLDÜĞÜNDE genişler.

## Adopte sırası
Lissom İLK tüketici (yerel portu yok — doğrudan çekirdekten başlar). JabLab/
Choreia/Gravita kendi doğal turlarında yerel kopyayı silip çekirdeğe pinlenir;
delta-testleri (her app'in kendi arıza-senaryoları) TAŞINIR, silinmez.
