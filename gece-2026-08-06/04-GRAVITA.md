# 🌙 GECE VARDİYASI — GRAVITA (İNŞA hattı + içerik ölçeği kararı)

> Önce `00-ORTAK-CEKIRDEK.md`'yi oku. Sen o çekirdeğin **<HAT> = Gravita** hâlisin.

## Nerede kaldın (git-doğrulandı)
`app/main = 4c408c0`, 0/0, ağaç temiz · kabuk 61/61 · motor 128/128 · `validate_library`
TEMİZ + 19/19 · `validate_catalog` 0 · replay 8/0.

## 🔴 DURUMUN DÜRÜST TESPİTİ
**Kodda 3 ekran var** (`ProgressView` · `LiveSessionScreen` · `ContentFailureScreen`);
tasarımın 10 ekranından **8'i yok**, navigasyon kabuğu yok. Kullanıcı Home/Library/
Movement page göremiyor. **Önce inşa, sonra yayın.**

## ⚖️ KOORDİNATÖR HÜKMÜ — içerik ölçeği çelişkisi (senin bulgundu, karara bağlıyorum)
Ölçtün: `library.json` **2 hareket** · `content/catalog/` **28 tanımlı ama terfi etmemiş** ·
tasarım **31/9 aile** iddia ediyor.

**HÜKÜM: kullanıcı-gerçeği `library.json`'dır.** Katalog bir *hazırlık havuzudur*, vitrin
değil. Tasarımın 31'i **hedef**, bugünün iddiası değil.
→ Gecenin işi: **katalogdaki hareketleri hak ettikçe `library.json`'a TERFİ ETTİR.**
→ Terfi ölçütü: `precondition.status` çözülmüş + dürüstlük kutusu üretilebiliyor +
  `validate_library` yeşil. **Ölçüm olmadan terfi YOK.**
→ Terfi edemeyen hareket **görünür kalır ama isimli gerekçesiyle** (30/31'i bugün
  `pending` — bu bir eksiklik değil, ölçüm kuyruğu; öyle sun).

## Bu gecenin sırası

### 1️⃣ NAVİGASYON + HOME + LIBRARY (kapsam belgesi: `DESIGN-AHEAD-OF-CODE.md`)
- **Library'nin kritik kısıtı:** kapsam-dışı arama **BOŞ DÖNMEZ** — "leg press" arayan
  kullanıcı boş sonuç değil, **"Why isn't X here?"** sayfasının ilgili bölümünü görür
- 9 hareket ailesi + 5 beceri ağacı görünür

### 2️⃣ MOVEMENT PAGE (9 zorunlu blok)
- ⭐ **Dürüstlük kutusu ÜRETİLİR, elle yazılmaz** — uzunluğu harekete göre değişir,
  **esnek yükseklik ŞART**, ikinci sınıf dipnot gibi görünemez
- **Referans YOK hâli bugün BASKIN hâl** (30/31 `pending`) → onurlu ve tasarlanmış
  olmalı, "boş/hata" gibi değil. **Sahte iskelet-avatar YOK.**

### 3️⃣ İÇERİK KUYRUĞU (asla boş durma)
- **Katalogdaki 28 hareketi terfi ettir** (yukarıdaki ölçütle) — en büyük içerik kazancı
- Terfi edemeyenlerin `precondition.rationale`'ını **isimli ve okunabilir** yap
- "Why isn't X here?" sayfasını `exclusions.json`'dan **üret** — elle yazma

## ⛔ Bu gece YAPMAYACAKLARIN
- **Tek genel skor** (7 bileşen AYRI, asla toplanmaz) · ses/TTS · sahte veri/placeholder grafik
- **Aspirasyonel düğümlere rozet** · ders izlemekle kilit açma
- 5-faz canlı seans modeli → **bana sor** (mevcut 4 hâlle yapısal fark var)
- Kamera önizlemesi: `Texture` preview çekirdekte **ertelenmiş** — sahte görüntü uydurma

## Açık borcun
Cihaz günü · iki-telefon çekimi (squat mod sorusu) · hareket spec'i (tasarımda YOK,
kurucu kuyruğunda) · `identityGapShare` **rapor-only kalır**
