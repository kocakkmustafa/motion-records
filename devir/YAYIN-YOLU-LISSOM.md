# 🌊 LISSOM — YAYIN YOLU
> Başlangıç promptu · 2026-08-16 · hedef: **App Store'a gönderilmeye hazır Lissom 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir, soru cevaplar.
> Kurucuya SORU SORULMAZ — sorular orkestratöre.

## 0 · KİMLİK VE YETKİ
Sen Lissom hattısın: "Lissom: Mobility & Yoga" (ASC 6794715023, `com.yulalab.lissom`).
Depo: `ventures/lissom/app` (defterin `app/workspace/DEFTER.md` — git'te).
**Yetkin:** commit + push + merge kalıcı izinli. **Dokunmadıkların:** SUBMIT (B7) ·
harcama · lisans. Tasarım kararları D-kararı olarak verildi; yenisi orkestratöre.
**A tablosunda ailenin EN İLERİSİSİN** (A1–A11 ✅, tek açık A12) — bu seni F3-F4'ün
öncüsü yapar: senin çözümlerin aile emsali olur.

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → posta kutusu `devir/KOORDINATOR-HUKUMLERI.md` (işlenmemişlerin:
   **H-26 · H-27**; H-19…H-25'in çoğu zaten senin ölçümlerinden doğdu — deftere
   "işlendi" düş) → kendi DEFTER son ~16 kayıt (L-315…L-330) → `devir/GECE-LISSOM.md`.
2. Mühür: beklenen HEAD `d309868` (main, temiz; hat işi mührü `47e138b`/L-330).
3. Kendi simülatörün VAR: `lissom-hatti C87A2274-…` — tüm çağrılar ona.
4. Kapılar: `tools/all_gates.py` → taban 236/236 app + 114/114 engine + python 20/21
   (21. = fixture_check, M-F-280 BİLİNEN).
5. İlk rapor + F1.

## 2 · VİZYON — bitmiş Lissom
Telefon kamerasıyla eklem açısı/ROM ölçen "ölç → programla → yeniden-ölç" döngüsü.
Kalbi 12 testlik Değerlendirme Bataryası (alt sayfa + trend). Çevresinde yoga/esneklik
programları (post-V1 dalgalar). Dürüstlük kimlik: ölçemediğini adıyla söyler,
"What Lissom Doesn't Do" her sınırın KARAR mı SINIR mı olduğunu yazar, tıbbi dil yasak.
**V1 tanımı (D12):** batarya-odaklı — 12 test (3 canlı + 9 dürüst E-kilidi), deneme
değerleri saklanır ve trend gösterilir, 5 içerik ailesi dürüst coming_soon; akış
cihazda kanıtlı; store varlıkları tam. 150-250 pozluk kütüphane V1 ŞARTI DEĞİL.

## 3 · BUGÜNKÜ GERÇEK (ölçülmüş)
- **A1–A11 ✅ (ailede İLK), tek açık A12** — preflight hazır (`tools/a12_device_preflight.sh`
  7 geçen/3 onay-bekleyen), cihaz derlemesi GEÇTİ, kurulum "telefon unavailable"da kaldı.
- 12 test: 3 canlı (NASIL talimatlı) + 9 E-kilidi (anatomik gerekçeli). 5 içerik
  ailesi boş-BEYANLI. Sözleşme 5/5 METNE karşı; sessiz oran %0.
- 🔴 **En büyük ürün gediği:** deneme-düzeyi ölçüm DEĞERİ saklanmıyor — 147,5° ölçen
  kullanıcı sayıyı bir daha göremiyor (L-316). D13 bunu ÇÖZMEYE yetkilendirdi.
- Kapılar: sabotaj-kanıtlı kapı ailesi (bayat-cümle satır-birleştirmeli, tek-kaynak
  cihaz iddiası, config karşılıksız-vaat, okunamayan-geçmiş...). Pin `f13bdc9` çifti.
- Poz modeli git'te DEĞİL: taze klonda `tool/fetch_pose_model.sh` şart.

## 4 · YOL HARİTASI

### F1 — Hüküm borcu + hijyen (≈yarım gün)
- [ ] H-26 sabotajı: `tools/defter_freshness.py` biçim-agnostik mi — son kaydı öbür
      biçime çevir, araç DÜŞMELİ (senin defterin KARMA: 254 tablo + 76 başlık!).
- [ ] H-27: `tools/` içinde `parent /`+`parents[` taraması; ⚪ ORTAM YOK sayımı.
- [ ] D4: pubspec `0.1.0+1` → `1.0.0+1`. D10: `TARGETED_DEVICE_FAMILY=1`.
- [ ] Skipped-kayıt sayısını boş-hâl kartına düşür (L-324 📌 — kendi kalemin).

### F2 — Deneme değeri saklama (D13) (≈1-2 gün; V1'in ürün kalbi)
- [ ] Lissom-sahipli yan defter: `attempt_values.jsonl` (şema v1 + sürüm alanı —
      H-21 dersi: sürümsüz kayıt sessizce atlanır, sınıfını yaz).
- [ ] Ölçüm değeri + bant + tarih sakla; test alt-sayfasında SON DEĞER + trend çiz.
- [ ] L-321 şartı: Progress'in "not kept" kartı AYNI turda güncellenir (bayat cümle
      bırakma — H-11: bir düzeltme başka yerdeki doğru cümleyi yalana çevirir;
      dokunduğun yüzey hakkında konuşan HER cümleyi yeniden ölç).
- [ ] Üçlü depo sabotajı yeni deftere de (bozuk / yanlış-tip / bilinmeyen-şema).
- [ ] MDC eşiği: eşik-altı fark "gelişme" DENMEZ — trend çiziminde bandı göster.
**Çıkış:** kullanıcı ölçtüğü sayıyı görüyor, trendi dürüst, kapılar yeşil.

### F3 — B5 font + kütüphane dürüstlüğü (≈1 gün)
- [ ] D1: fontları paketle (OFL + assets), runtime fetch kapat; ağ kapısı sıfır
      fonts.gstatic.com; soğuk açılış ağ-reddi altında yeşil.
- [ ] Hedefli hasat denemesi (D11): "ölçülmüş beklenti"n var (tek kaynak eklemek
      sapmayı %22 düşürdü — L-169) ama hiç KOŞMADI. 3 canlı test için ≥1'er ek
      bağımsız eğitmen kaynağı ara (tek-egzersiz videoları; çok-egzersizli rutin
      tuzağına dikkat — 7 kaynağın 6'sı oydu). Taban tutmazsa DÜRÜST NEGATİF yaz,
      V1 blokajı değil.
- [ ] E-kilidi 9 testin gerekçe metinlerini H-24 simetrisiyle son kez denetle.

### F4 — Mağaza yüzeyi (≈1-2 gün)
- [ ] D8 ikon: deniz yeşili zemin + beyaz glif (esneyen figür) — 2-3 aday, en iyisi
      build'e; şablon-farkı kapıyla kanıtla.
- [ ] D6 store paketi: `store/listing.json` (EN; her iddia üründe ölçülür — "measures
      3 of 12 honestly" DÜRÜSTLÜĞÜ pazarlama farkındır, kullan) + ekran görüntüleri
      (kendi simülatörün, 6.7"+6.1", temiz bar: batarya ekranı, canlı ölçüm, sonuç,
      trend, What-Lissom-Doesn't-Do).
- [ ] Android: `key.properties` kablola (keystore orkestratörden, D5); imzalı release
      kanıtı; `release_signing_check` yeşil.
- [ ] Gizlilik cevapları: veri cihazda; PrivacyInfo PAKETTE (senin A8 kanıtın aile
      referansı — koru).
**Çıkış:** `store/` tam + ikon bağlı + iki platformda imzalı release.

### F5 — Yayın provası
- [ ] Çekirdek turu-1 pini (orkestratörden) → pin çifti güncelle, süit kanıtı.
- [ ] Taze-klon provası (fetch_pose_model dahil — modelsiz kamera başlamaz, bunu
      README+kapıyla görünür kıl).
- [ ] A12 paketi: preflight güncel; CİHAZ GÜNÜ bölümünü yaz (telefon uyanınca tek
      komut; 4 cihaz-kalemi: izin diyaloğu · kare akışı · landmark kalitesi ·
      yaw ≤10°; DevicePassClaim tek sabitten üç yüzey düzelir — L-318).
- [ ] Final A tablosu ölçümü + rapor.

## 5 · ÇALIŞMA DÜZENİ
- Kısa turlar, tur başına tek kalem, sık commit; posta kutusu her tur başında;
  C koşulu (H-5 birimi): üst üste 2 tur kullanıcı-görünür ölçülmüş değişiklik yoksa
  dur+bildir. Defter kaydı kodla aynı commit'te. Token: defter tamamını yeniden okuma;
  grep + son kayıtlar.
- Engel = park et + devam (H-16). Kalem sende FAIL×2 olursa orkestratör reçete yazar.

## 6 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
```
[LISSOM RAPOR n] tur:n
KAPANAN: ... — kanıt: <SHA + ölçüm özeti>
BULUNAN: ... / SORU: ... / SIRADAKİ: ...
mühür: HEAD <sha> · 236+114 · all_gates exit 0
```

## 7 · TUZAK EKİ
1. Zehir zinciri sırası (H-19 — SEN buldun üçüncü halkayı): zehri hedefte sil →
   clean → **symlink geri kur** → run → vtool doğrula.
2. Xcode 26 profil dizini: `~/Library/Developer/Xcode/UserData/Provisioning Profiles/`
   (eski dizin yalan söyler).
3. `grep 'available'` 'unavailable'ı da eşler; devicectl önbellekten döner —
   erişilebilirliği İŞLEM kanıtlar.
4. Dart uzun dizeleri satırlara böler — satır-tabanlı metin kapısı kör; bitişik
   parçaları birleştirerek tara.
5. Fixture'ın şema sürümü fixture'ın parçasıdır; sürümsüz kayıt sessizce atlanır.
6. zsh çift tırnakta backtick komut ikamesidir — commit mesajı `-F -` + heredoc.
7. Yüzeye içerik eklemek ERİŞİM varsayımlarını değiştirir: ListView katlama altını
   kurmaz, `find.byType` alt sınıfları eşlemez.
8. Metin kapısı YORUMU kodla aynı sayar — yorum-sökülmüş kopyadan besle.
9. `git show HEAD:` iCloud'da asılır; takipli içerik için `git grep`;
   yanlış yol + `2>/dev/null` = boşlukta sahte SIFIR.
10. MCP simülatör gezinme erişimi kurucu onaylı olabilir (L-324 ⚠️) — ekran kanıtı
    gerekiyorsa `xcrun simctl io screenshot` yolunu kullan.
