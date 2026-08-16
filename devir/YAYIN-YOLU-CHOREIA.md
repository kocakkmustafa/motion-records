# 💃 CHOREIA — YAYIN YOLU · TUR 2

> Başlangıç promptu · 2026-08-16 tur-2 · hedef: **App Store'a gönderilmeye hazır Choreia 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir. Kurucuya SORU SORULMAZ.

## 0 · KİMLİK VE YETKİ
Choreia (`com.yulalab.choreia`, bundle `PDRAB4FYBS`). Depo `ventures/choreia/app`, defter
`app/workspace/DEFTER.md`. ✅ commit+push+merge kalıcı izinli · ⛔ SUBMIT (`B7`) · harcama ·
**yeni yazılım kurulumu** (`H-71` — hasat serbest, kurulum kurucu izni).

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → defter son ~15 kayıt (`C-296…C-306+`) → vault notun (`🔄 … Choreia H-70 Roger
   Rabbit + iCloud Fırtınası`) → hüküm **posta kutusu**: `devir/KOORDINATOR-HUKUMLERI.md` — **indeks değil, MAİLBOX'IN
   KENDİSİ**, ve tepesinden aşağı, kendi defterinde `işlendi:` kaydı olmayan her hükmü oku.
   ⚠️ `HUKUM-INDEKSI.md` bir **görüntüdür**, üretildiği andan sonra bayatlar (`L-342` bunu
   canlı yaşadı: indeks `H-71` diyordu, mailbox `H-78`deydi). Sayıya güvenme — `max` oku.
2. Mühür: beklenen HEAD **`a66c0a2`+** (H-70 kapanışı; sonrasında bayat-sayı düzeltmesi commit'i
   olabilir — defterin son kaydından doğrula). Kapılar: 25/25.
3. İlk rapor + aşağıdaki sıra.

## 2 · DURUMUN (ölçülmüş)
- ✅ `H-70` kapalı: RR `needsMovementDescription`a geri · mezar taşı silindi · iki `yet` çıktı ·
  `(b)` yolu (**`step` yok**, `structural-circular` kalır, **şema-vaadi çelişkisi AÇIK**).
- ✅ Launch image gerçek (`C-301`, `stage`+`rose`, kendi temandan) · bounce skorlanıyor ·
  RR/RM `demo-only` kayıtlı · tüketici ölçümü Choreia tarafı: **canlı kusur yok**.
- 🔴 **İkon STOK** — teman `#F0A6BD` kapıdan **geçiyor** (`ΔL 0,493` Ostinato'ya, komşun
  Lissom'la ΔH 7,9° ama ΔL 0,173 ✅). Kapı: `motion-core/workspace/tools/ikon_ayirt_kapisi.py`.
- 🔴 **Listing (`D6`) YOK** — kalan 2/5'in birisin.
- 🔴 Cihaz günü paketin YOK (şema: Ostinato/Gravita; **yapı paylaşılır, içerik paylaşılmaz**).
- ❓ `hh_l2` **belirsiz** — iki okuma devir notunda; **tahminle başlama**, orkestratörle netleştir.
- 🌾 STT **kullanılabilir** (`H-68`): `motion-core/lib/tools/fixture_pipeline/.venv`
  (faster_whisper 1.2.1 + model kurulu). 11 RR adayı + `DEFnniCN7ok` bekliyor. Hasat **rutin**
  (`H-71`) — ama 403 tavanı gerçek: küçük dene, düşerse dur.

## 3 · YOL HARİTAN (sıralı)
1. 🎨 **İkon** — kendi temandan üret, kapıdan geçir, deftere yaz. (⛔ kardeş kopyası yok — zemin
   rengin kontrastı belirler.)
2. 🏪 **Listing (`D6`)** — üç kardeşinki emsal (`listing.json` yapısı); yazınca orkestratöre
   bildir, **yan yana okuma** yapılacak (`H-58`).
3. 📱 **Cihaz günü paketi** (`PAKET.md` + ön-uçuş; Gravita'nın v2 gölgeleme düzeltmesini
   **gerekçesiyle** al).
4. 🔬 `DEFnniCN7ok` transkripsiyon denemesi (aile venv'iyle, uçtan uca bir aday) → başarılıysa
   11 aday sınıflandırmaya → RR mezuniyeti yeniden ölçülür.
5. ❓ `hh_l2` kararı — orkestratörle, iki okumadan biri seçilince.

## 4 · ÇALIŞMA DÜZENİ
Küçük adım → gates → commit → push. **iCloud aralıklı tıkanıyor** (`EINTR`) — pencere kapanırsa
dur-bildir; köprü: `/tmp/motion-icloud-koprusu/choreia/`. ⛔ `brctl`/iCloud ayarına dokunma.
Simülatör: `choreia-hatti`.

## 5 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
Mühür · ölçümle yapılan · açık kalemler adıyla.

## 6 · TUZAK EKİ
- `startable.single` birden fazla elemanda **fırlatır** — `canStart` ayrımını `step` alanı yapar,
  `demoOnlyClass` değil (`M-F-730` — orkestratör bunu karıştırdı, sen az kalsın doğru testi
  bozuyordun).
- Promise-dili kapısı yalnız `demoOnlyReason`/`lockedReason`/`whyPermanent`/`displayName` +
  `honesty.*` tarar; yasak: `yet·soon·will be able·once we·coming` (alanlar `{en:…}` haritası).
- **Mezar taşı ≠ hata deposu** (`H-70`, senin ayrımın): hata defterde yaşar, envanterde değil.
- "Authored step file" ≠ "reference" — iki ayrı artefakt (`hh_rock` emsali).
- Yokluk raporu **kelime+ortam+dizin adıyla** (`H-64/68`).
