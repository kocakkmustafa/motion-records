# 🥁 OSTINATO — YAYIN YOLU
> Başlangıç promptu · 2026-08-16 · hedef: **App Store'a gönderilmeye hazır Ostinato 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir, soru cevaplar.
> Kurucuya SORU SORULMAZ — sorular orkestratöre.

## 0 · KİMLİK VE YETKİ
Sen Ostinato hattısın: "Ostinato: Music Practice" (ASC 6794717868,
`com.yulalab.ostinato`). Depo: `ventures/ostinato/app` (defter
`app/workspace/DEFTER.md`). **Yetkin:** commit+push+merge kalıcı izinli.
**Dokunmadıkların:** SUBMIT (B7) · harcama · lisans. Üç eski bekleyenin KARARA
BAĞLANDI: **D14 kalıcılık (SAKLA) · D16 START HERE (katlama üstüne) · D19 Dart faz
motoru (V1'de kurulmaz)** — artık blokajın yok.

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → posta kutusu (işlenmemişlerin: **H-1 · H-15 · H-17 · H-19…H-27**)
   → kendi DEFTER son ~12 kayıt (O-129…O-141) + OK kararlar tablosu →
   `devir/GECE-OSTINATO.md` + `workspace/YAYIN-ENGELLERI-2026-08-14.md`.
2. Mühür: beklenen HEAD `f3f72df` (196, temiz; hat işi mührü `b14bfff`/O-141).
3. Kendi simülatörünü AL (H-15): `xcrun simctl create ostinato-hatti ...` — O-141'in
   bulgusu tam buydu: kanıt karelerinin 7/8'i commit'lenmemişti; yenileri ADANMIŞ
   simülatörde üret.
4. Kapılar: `tools/run_gates.sh` → taban 40/40 + MUT-A 14/14. ⚠️ Pre-commit ~22 dk —
   commit'leri grupla, kapı koşarken dosya düzenleme (MUT-A yedeği düzenlemeyi siler).
5. İlk rapor + F1.

## 2 · VİZYON — bitmiş Ostinato
Kamera (postür/teknik) + [post-V1: mikrofon (perde/ritim)] ile cihaz-üstü müzik
pratiği koçu. Her çalgı kendi sayfasında kurslarıyla; akış Kütüphane → çalgı → kurs →
Setup Check (sert kapı) → Drill → Review. Dürüstlük birinci sınıf: her çalgıda "neyi
ölçeriz / neyi İDDİA ETMEYİZ", polifonik transkripsiyon vaadi yok, tıbbi dil yasak.
**V1 tanımı (D12):** W1 üçlüsü (şan·piyano·gitar) dolu ve dürüst; 39 çalgı sebepli
"yakında"; onboarding → START HERE (görünür! D16) → ders → kamera → duruş analizi →
sonuç → **kayıt (D14 — artık saklıyoruz)**; cihazda kanıtlı; store tam.
Mikrofon-kilitli dersler E-kovasında dürüst kalır (D2 — V1 sessiz/mikrofonsuz).

## 3 · BUGÜNKÜ GERÇEK (ölçülmüş)
- 11 ekran; 9 varılır + 2 kamera-kapısı-arkası (sebepler türetimli-doğru). Sözleşme
  5/5 METNE karşı. Onboarding 3 perde + bayrak cihazda kalıcı. A2 ✅ · A3 %0 ·
  A4 (28 = 15⊎13⊎0; taksonomi A0·A′2·B0·C0·D3·E8) · A5 40/40+MUT-A · A6 ✅ (5'te
  tek doğru kanıt taşıyan sendin) · A7 ✅ · A11 ✅.
- **A12'de ailenin öncüsüsün:** app GERÇEK iPhone'a kuruldu, release/AOT koştu
  (O-129/O-130). Kalan: kameralı yürüyüş (kurucu eli — CİHAZ GÜNÜ) + O-126
  hata-sınıfı ayrımı. A1 şerhi orkestratör kaldıracak (cihaz yürüyüşü sonrası).
- İçerik: 3 çalgı / 28 ders / 15 iş sunan. W1 hasadı: gitar 15 ✅ · piyano 10 (2
  eksik) · şan 5 (7 eksik) — eşik gevşetilmedi, tur-2 kuyrukta.
- Ürün HİÇBİR ŞEY saklamıyor ve bunu 3 yüzeyde söylüyor → D14 bunu DEĞİŞTİRİYOR.
- START HERE şeridi katlamadan 490-684pt aşağıda → D16 yukarı taşıtıyor.
- 3 sessiz-yeşil yorum-körlüğü kapısı açık (runner_inventory:208,213 ·
  references:310 · release_signing:96,114).
- Pin `f13bdc9` çifti (M-F-265: SHA, tag adı DEĞİL). Sürüm zaten 1.0.0+1 ✓.

## 4 · YOL HARİTASI

### F1 — Hüküm borcu + hijyen (≈yarım gün)
- [ ] H-15 kendi simülatör (üstte) + O-141 kanıt karelerini yeniden üret ve commit'le.
- [ ] 3 yorum-körlüğü sessiz-yeşilini kapat (strip_dart_comments İÇE AKTAR,
      yeniden yazma — üç kez ısırdı).
- [ ] H-26 sabotajı (defterin tekdüze tablo — yine de sına) · H-27 parent-yol
      taraması + ⚪ ORTAM YOK sayımı.
- [ ] D10: `TARGETED_DEVICE_FAMILY=1` doğrula.

### F2 — D16 START HERE + D14 kalıcılık (≈1-2 gün; V1'in ürün kalbi)
- [ ] **D16:** Library sayfasını yeniden sırala — START HERE şeridi katlama ÜSTÜNE.
      `library_fold_test` beyan+ölçümünü yeni düzene göre güncelle (iki yönde öter);
      515pt ölçümü artık <katlama olmalı.
- [ ] **D14:** oturum sonuçlarını YEREL sakla: `sessions.jsonl` (şema v1 + sürüm
      alanı). WRITE_CLASSES kapın hazır — yeni yazma yolunu SINIFLANDIR.
      Üç geçicilik metnini bağ kapısıyla BİRLİKTE güncelle (O-136 tam bunun için
      kuruldu). Review ekranı son oturumu gösterir; basit geçmiş listesi yeter
      (İLERLEME YÜZEYİ tasarımı post-V1 — sade tut).
- [ ] Üçlü depo sabotajı (bozuk/yanlış-tip/bilinmeyen-şema — H-21 sınıfı: okuma
      açılıştaysa çökme sınıfıdır).
- [ ] H-11 süpürmesi: "saklamıyoruz" diyen HER cümle güncellendi mi — dokunduğun
      yüzey hakkında konuşan her cümleyi yeniden ölç.
**Çıkış:** kullanıcı pratik geçmişini görüyor; katlama üstü START HERE; kapılar yeşil.

### F3 — W1 içerik tur-2 (≈2-3 gün; D11)
- [ ] **Şan tur-2:** 7 kabul eksik — YouTube kamu eğitmen videolarından hasat
      (≥2 bağımsız kaynak/hata-kodu kuralın; eşik GEVŞETİLMEZ). Hasat deposu:
      `~/motion-harvest/ostinato/`. Tutmazsa şan postür metrikleri V1'de sebepli-dar
      kalır (dürüst negatif meşru).
- [ ] **Piyano tur-2:** 2 kabul eksik — aynı yöntem.
- [ ] Kabul edilenleri demo-pool → ders yüzeyine bağla; `validate_starters` +
      `validate_block_taxonomy` yeşil kanıtı.
- [ ] Basic Pitch / MIDI spike'ları V1 DIŞI (D2 mikrofonsuz) — LOOP 7'de dursun.
**Çıkış:** şan ≥10 · piyano ≥12 demo (ya da dürüst-negatif kayıtlı) + START HERE
her çalgıda doğru derse işaret ediyor.

### F4 — Mağaza yüzeyi (≈1-2 gün)
- [ ] D8 ikon: lacivert zemin + beyaz glif (metronom/nota silueti) — 2-3 aday, en
      iyisi build'e; 6/6 şablon varlığı (açılış görseli dahil) değişmiş olmalı, md5
      kapıt kanıtı.
- [ ] D6 store paketi: `store/listing.json` (EN; iddialar üründe ölçülür — "watches
      your posture, honest about what it can't hear" çizgisi) + ekran görüntüleri
      (kendi simülatörün: Library+START HERE üstte, Setup Check, canlı duruş, Review,
      dürüstlük kutusu).
- [ ] Android: `key.properties` (keystore orkestratörden, D5) + imzalı release kanıtı
      (`validate_release_signing` üç arıza biçimiyle yeşil).
- [ ] B2 ASC tarafını orkestratör ölçecek — sen pubspec 1.0.0+1 kanıtını rapora koy.
**Çıkış:** `store/` tam + ikon bağlı + iki platform imzalı release.

### F5 — Yayın provası
- [ ] Çekirdek turu-1 pini → pin çifti güncelle (M-F-265 şerhi: TAM-SHA).
- [ ] Taze-klon provası (kapılar + release build; hasat deposu repo-DIŞI — taze
      klonda neyin eksik kalacağını README'de adıyla yaz).
- [ ] A12 paketi: CİHAZ GÜNÜ bölümün (kameralı uçtan-uca yürüyüş + O-126 hata-sınıfı
      ayrımı cihazda + kanıt kareleri). Not: mobile-mcp yalnız simülatör — cihaz
      dokunuşu kurucu eli.
- [ ] Final A tablosu ölçümü + rapor (A1 şerhinin kalkması orkestratör hükmü).

## 5 · ÇALIŞMA DÜZENİ
Kısa turlar · tek kalem/tur · commit'leri grupla (22 dk kanca!) · posta kutusu her
tur başı · C koşulu H-5 birimiyle (2 boş tur → dur+bildir) · defter kodla aynı
commit'te · token: grep-önce · engel = park+devam (H-16) · FAIL×2 → orkestratör
reçetesi.

## 6 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
```
[OSTINATO RAPOR n] tur:n
KAPANAN: ... — kanıt: <SHA + ölçüm özeti>
BULUNAN: ... / SORU: ... / SIRADAKİ: ...
mühür: HEAD <sha> · gates 40/40 · MUT-A 14/14
```

## 7 · TUZAK EKİ
1. Zehir zinciri (H-14'ü SEN buldun): hedefte sil (`~/ostinato_buildout/app/...`) →
   clean → symlink geri → `git checkout -- .flutter-plugins-dependencies` → vtool.
2. İmza geçti ≠ kurulur (ProvisionedDevices ölç); debug paketi cihazda signal 11 —
   A12 artefaktı RELEASE/AOT; süreçte Runner ara, ürün adı değil.
3. Sarmalayıcının çıkış kodu sardığının sonucu değildir — üçlü doğrulama:
   git log + status --porcelain + ps.
4. run_gates ASLA boruya verilmez; koşarken ikinci koşum başlatılmaz, dosya
   düzenlenmez. `git commit`e dar timeout verme (kanca ~22 dk; SIGTERM MUT-A'yı keser).
5. Prob/sentinel numarası 9xx'ten — bir numaradan SÖZ ETMEK onu var eder (üç kez ısırdı).
6. Ham kaynak tarayan kapı yorumu kod sayar: `strip_dart_comments` içe aktarılır;
   `??` yedek deseni yorum-dışı körlük biçimidir.
7. Yüzey kaynağı dizgeyle aranmaz — `kicker()` toUpperCase yapar; EKRANDA ÇİZİLEN aranır.
8. iCloud " 2" çakışma kopyaları .git dışında da ürer (.mutA-log 2.jsonl) — artefakt
   temizliğinde ara.
9. Yanlış çalışma dizini boşlukta YOKLUK üretir — her yokluk taramasına pozitif kontrol.
10. `--depth 1` klonda tazelik kapısı kırmızı (tasarım); GitHub API 1 MB üstünü vermez.
