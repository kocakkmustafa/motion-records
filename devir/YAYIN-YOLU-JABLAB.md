# 🥊 JABLAB — YAYIN YOLU
> Başlangıç promptu · 2026-08-16 · hedef: **App Store'a gönderilmeye hazır JabLab 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir, soru cevaplar.
> Kurucuya SORU SORULMAZ — sorular orkestratöre.

## 0 · KİMLİK VE YETKİ
Sen JabLab hattısın: "JabLab: Shadow Training" (ASC 6794715669, `com.yulalab.jablab`).
Depo: `ventures/jablab/app` (defter `app/workspace/DEFTER.md`). **Yetkin:**
commit+push+merge kalıcı izinli. **Dokunmadıkların:** SUBMIT (B7) · harcama · lisans.
İki eski "koordinatör hükmü bekliyor" kalemin (J-251 · J-259) **D18 ile AÇILDI** —
donmuş ağaç o iki kalem için açılır.

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → posta kutusu (işlenmemişlerin: **H-15 · H-17 · H-19…H-27**) →
   kendi DEFTER son ~15 kayıt (J-246…J-260) → `devir/GECE-JABLAB.md` +
   `workspace/DEVIR-2026-08-14-GECE.md`.
2. Mühür: beklenen HEAD `45dd32a` (252, temiz; hat işi mührü `4c20557`/J-260).
3. **Kendi simülatörünü AL (H-15 — sende hâlâ yok):** `xcrun simctl create
   jablab-hatti "iPhone 16" ...` — tüm çağrılar o UDID'e.
4. Kapılar: pre-commit zinciri → taban analyze 0 · app 344/344 · motor 125/125 ·
   tazelik 0.
5. İlk rapor + F1.

## 2 · VİZYON — bitmiş JabLab
"Solo Combat Training": kullanıcı telefonu karşısına koyar, ekipmansız shadow boxing
yaparken köşesindeki antrenör gibi kısa düzeltme alır. Kuzey yıldızı: aynı seans
içinde düzeltme yapabilen kullanıcı oranı — ders tamamlama ilerleme SAYILMAZ.
Analiz tamamen cihaz-üstü: ham video çıkmaz, landmark bile diske yazılmaz.
**V1 kapsamı güvenilirlik bandına kesilmiş:** yumruk olayı+sayım+stance A bandında;
hook/uppercut V1 DIŞI; skorlar K8 kalibrasyonu geçilene dek BANT değil TİRE — ve bu
dürüst tire TASARIMDIR, blokaj değil. 7 disiplin coming_soon (sebepli). D2 gereği
V1 SESSİZ: sesli koçluk yerine görsel düzeltme (vaat metinlerinde "sesli" geçiyorsa
düzelt — H-13 iki yönlü süpürme).
**V1 tanımı (D12):** onboarding → 30 kontrol 0 sessiz → kurs → seans → kamera →
dürüst özet (SAYILARI GÖSTEREN — F2) → kayıt; cihazda kanıtlı; store tam.

## 3 · BUGÜNKÜ GERÇEK (ölçülmüş)
- A tablosu: **A1–A9 + A11 ✅ · tek açık hat kalemi A6-ikinci-yön · A12 cihaz-fiziksel**
  · A10→B8.
- "Bitmiş ürün" ölçütü #4 UÇTAN UCA kanıtlı (J-256: workedSeconds:17 gerçek, landmark
  yok). 5 canlı yalan düzeltildi. Store taslağı YAZILI ve 27 iddiası denetli
  (docs/store/listing.json — ailenin emsali).
- 🔴 Özet ekranı "ürünün en çok sustuğu yüzey": tur/süre diske yazılıyor ekrana
  GEÇMİYOR (J-259); tirenin açıklaması yok (J-251) → **D18 açtı, F2'de kapat**.
- cross referansı 2/3 eğitmen (M-C-04 ≥3) → **D17: hasat turu-1'de 3. bulunamazsa
  Plan B (jab-öncelikli) TETİKLENİR** — süresiz bekleme bitti.
- A6 ikinci yön: ham 109, birim daraltılmadı — kardeş birimler ölçülüp ALINMADI
  (doğruydu); kendi sütunlarından birim türeteceksin.
- Pin `f13bdc9` çifti. curriculum.json paketleniyor ama üretim HİÇ yüklemiyor (J-207).

## 4 · YOL HARİTASI

### F1 — Hüküm borcu + A6 (≈1 gün)
- [ ] H-15: kendi simülatörün (üstte). H-26: defterin karma sayılmalı (birleşik
      kimlikler var: J-105 çift, J-191(devam), J-194b) — tazelik aracını sabotajla sına.
- [ ] H-27: `tool/` içinde `parent /`+`parents[` tara; ⚪ ORTAM YOK sayımı.
- [ ] **A6 ikinci yön:** kendi defterinden ölçülebilir birim türet (öneri: Kapanış
      kanıtı sütunu commit/dosya ANAN kayıtlar = iddialı küme; 109'u onunla daralt;
      taban koyarsan muaflar her koşumda sayıyla + taban sabit). A6'yı KAPAT.
- [ ] H-20/21: kalıcı depolar (seans kaydı + onboarding bayrağı) üçlü sabotaj.
- [ ] D4: pubspec → `1.0.0+1` · D10: `TARGETED_DEVICE_FAMILY=1`.
**Çıkış:** A6 ✅ → A tablosunda tek açık A12 kalır.

### F2 — Özet ekranı + D2 ses süpürmesi (≈1 gün)
- [ ] **J-259:** `_roundsCompleted`/`_workedSeconds` EKRANA (diske zaten yazılıyor);
      J-257 dersi: 17 sn çalışan kullanıcı "0 min" GÖRMEMELİ — yuvarlama iki olguyu
      aynı cümleye indiriyorsa iddiadır; negatif ikiz kapı (gerçek sıfır hâlâ dürüst).
- [ ] **J-251:** tirenin açıklaması — "why a dash?" tek satır gerekçe (K8
      kalibrasyonu yapılmadı; skor uydurmayız). H-24 simetrisi: canlı yüzeyler NASIL
      açıklasın.
- [ ] D2 süpürmesi: "voice/audio/coach says" geçen her vaat cümlesini tara (lib +
      content + assets — H-23 kapsamı) — V1 sessiz; metinler görsel düzeltmeyi
      anlatmalı.
- [ ] Tempo bandı kararı (D18 kapsamı): motor üretiyor, yüzey yok — V1'de özet
      ekranına TEK satır bant göstergesi ekle (skor değil, dürüst bant); kapıyla.
**Çıkış:** özet ekranı konuşuyor; ses vaadi sıfır; kapılar yeşil.

### F3 — cross/Plan B + içerik (≈2-3 gün; D11+D17)
- [ ] **Hasat turu-1:** cross için 3. bağımsız eğitmen avı — sınırlı pencere
      (≤2 hasat oturumu). Bulunursa: referans → cross dersleri tam güce.
      Bulunamazsa: **Plan B tetiklenir** (PRD §2.0): jab-öncelikli daraltma,
      kurs metinleri güncellenir (H-11: dokunulan yüzeyin cümleleri yeniden ölçülür).
- [ ] curriculum.json kararı: üretim hiç yüklemiyor (J-207) → V1'de ya BAĞLA
      (ilerleme kapılarının sağlanabilir alt kümesiyle: 15 kapının 12'si bugün
      sağlanamaz — sağlanamayanları içeren dersleri kilitle-sebepli) ya da PAKETTEN
      ÇIKAR (ölü ağırlık). Ölç, seç, orkestratöre raporla, uygula.
- [ ] Boks numaralandırması (1=jab, 2=cross) içerik açıklaması — foundations
      kursunun ilk dersine tek kart (içerik yazarlığı, library.json'dan türet,
      dizge uydurma yok — J-247 ilkesi).
- [ ] 4 "şeklin kendisi iş" dersinin adıyla-tekniksiz durumu korunur (dürüst).
**Çıkış:** cross yolu KARARA bağlanmış (referans YA DA Plan B uygulanmış);
curriculum kararı uygulanmış.

### F4 — Mağaza yüzeyi (≈1 gün; store taslağın ZATEN VAR — öndesin)
- [ ] D8 ikon: kırmızı zemin + beyaz glif (jab silueti) — 2-3 aday, en iyisi build'e.
- [ ] D6: mevcut `docs/store/listing.json`u `store/`a taşı/tazele (D2 sonrası ses
      iddiası kalmadığını yeniden denetle — 27 iddia denetimini KOŞ) + ekran
      görüntüleri (kendi simülatörün: kurs, öğret perdesi, canlı seans, DÜZELTİLMİŞ
      özet, Why-not sayfası).
- [ ] Android: `key.properties` (keystore orkestratörden, D5); `android_signing`
      kapısı imzalı release'i kabul edecek şekilde kanıt tazele.
**Çıkış:** `store/` tam + ikon bağlı + iki platform imzalı release.

### F5 — Yayın provası
- [ ] Çekirdek turu-1 pini → pin güncelle (dependency_pin_test yeşil).
- [ ] Taze-klon provası (setup_hooks bir kez şart — README'de görünür kıl;
      fetch_pose_model dahil).
- [ ] A12 paketi: `A12-CIHAZ-RECETESI.md` güncel; CİHAZ GÜNÜ bölümün (kablo takılı
      telefon + kameralı gerçek seans + ekran kaydı). Bayat joker profil silme
      önerisi pakete.
- [ ] Final A tablosu ölçümü + rapor.

## 5 · ÇALIŞMA DÜZENİ
Kısa turlar · tek kalem/tur · sık commit · posta kutusu her tur başı · C koşulu
(2 boş tur → dur+bildir) · defter kodla aynı commit'te · token: grep-önce · engel =
park+devam (H-16) · FAIL×2 → orkestratör reçetesi.

## 6 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
```
[JABLAB RAPOR n] tur:n
KAPANAN: ... — kanıt: <SHA + ölçüm özeti>
BULUNAN: ... / SORU: ... / SIRADAKİ: ...
mühür: HEAD <sha> · analyze 0 · 344+125 · tazelik 0
```

## 7 · TUZAK EKİ
1. **FLUTTER_TARGET zehri (SEN buldun, J-246):** Generated.xcconfig bayat stub
   taşıyabilir — yeşil derleme SENİN ürünün olmayabilir; `flutter build ios
   --config-only` ile hedefi ölç.
2. Zehir zinciri (H-19): hedefte sil → clean → symlink geri (`~/jablab_buildout`) →
   run → vtool IOSSIMULATOR.
3. Metin kapısı YORUMU kodla sayar (4.14): yorum-sökülmüş kopyadan + sökücünün
   pozitif kontrolüyle.
4. Test double gerçeğin kuralını uygulamaz (J-240): kalıcılık yalnız gerçek
   dosya+diske yazımla ölçülür.
5. İmza geçti ≠ kurulur; eşleşmiş ≠ bağlı (tunnelState); generic hedef cihaz eklemez.
6. `git grep` İZLENEN içeriği tarar — çalışma ağacı probu görünmez, sahte sıfır.
7. Türkçe: Dart `caseSensitive:false` ı/İ'de kırık; Python `.lower()` kırık ama
   `re.I` sağlam; BÜYÜK kip ASCII'ye düşürür.
8. "Test artefaktı" etiketi gerçek arızayı maskeler (J-248): ortam davranışı ancak
   gerçek arıza OLMADIĞI ölçülerek sahte sayılır.
9. Kapı kendi ürününü engelleyebilir (J-245): af dar tutulur.
10. `--depth 1` klonda tazelik kapısı tasarımı gereği kırmızı; GitHub API 1 MB
    üstünü vermez.
