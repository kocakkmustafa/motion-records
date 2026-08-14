# 🌙 GECE VARDİYASI — CHOREIA (İNŞA hattı — ailede yayına EN UZAK)

> Önce `00-ORTAK-CEKIRDEK.md`'yi oku. Sen o çekirdeğin **<HAT> = Choreia** hâlisin.

## Nerede kaldın (git-doğrulandı)
`app/main = 469681b`, 0/0, ağaç temiz, 80 Flutter + 16 engine testi yeşil.

## 🔴 DURUMUN DÜRÜST TESPİTİ
**Kodda tek gezilebilir ekran var** (`live_view` + `progress_view`; navigasyon kabuğu YOK).
Kullanıcı uygulamayı açsa **hiçbir yere gidemez.** Yani senin için "yayın hazırlığı" diye
bir iş yok — **önce İNŞA var.** İçerik tarafı da ince: 34 stilin **1'i canlı**,
1 `demoOpen`, 31 `comingSoon`, 1 `onHold` (Hula, kültürel ortaklık şartı).

**Kapsam belgen hazır:** `docs/design/DESIGN-AHEAD-OF-CODE.md` — 13 kalem, bu gecenin
yol haritası. Tasarım `claude.ai/design` projesinde duruyor, MCP ile yeniden import
edilebilir.

## Bu gecenin sırası

### 1️⃣ NAVİGASYON KABUĞU (2-8 arasındaki her şeyin ön koşulu)
Kapsam belgendeki kalem #1. Var olan iki ekranı kırma — `LiveView`/`ProgressView`
giydirilmiş hâlleriyle korunur, üstlerine navigasyon gelir.

### 2️⃣ LIBRARY — tasarımın **en zor problemi**
34 stil sayfası, **1'i puanlıyor.** Soru: *sahte-dolu görünmeden nasıl geniş kapsam
hissi verir?*
- **Üç rozet ayrı çözülmeli:** `live` (skorlanan ders var) · **`demoOpen`** (*açık ama
  puansız* — ailenin en zor rozeti) · `comingSoon` (açılabilir ders yok)
- `onHold` **gerekçesiyle** görünür (Hula) — gizlenmez
- ⛔ **Sahte/boş kurs ASLA listelenmez**, ama kapsam da gizlenmez

### 3️⃣ STİL SAYFASI + DERS SINIFLARI
- **Köken/atıf kutusu = İÇERİĞİN PARÇASI**, dekorasyon değil (Vogue → Siyah/Latino
  LGBTQ+ ballroom · Afrobeats · Bhangra). Küçültülmez, dipnota indirilmez.
- **Üç ders görsel sınıfı:** skorlu · kilitli (sebep **eksik ÖLÇÜMÜN adıyla**) ·
  **demo-only (İKİNCİ SINIF GÖRÜNMEZ** — tam bir ders, yalnız skoru yok)
- Ders akışı 4 adım; **3. adım (beat'le dene) KAPALI** → yeri **boş bırakılır, sahte
  doldurulmaz.** (🥁 BPM tap kurucu-manuel; gelince açılır.)

### 4️⃣ İÇERİK KUYRUĞU (asla boş durma — 1-3 tıkanırsa buraya dön)
- **32 stilin içeriği yok** — en büyük içerik açığı ailede
- Her stil için: tanıtım · köken/atıf · adım sözlüğü · **dürüstlük kutusu**
- ⚠️ **Ölçüm olmadan skorlanan adım ekleme** — `demoOnly` işaretle, gerekçesini yaz
  (K10: *ölçülemeyen hareket elenmez, demo işaretlenir ve nedeni söylenir*)
- Stil sayfası atıf/glossary alanlarının content'te gerçekten var olup olmadığı
  **doğrulanmadı** — önce ölç

## ⛔ Bu gece YAPMAYACAKLARIN
- Ritim/zamanlama puanı (beat ızgarası yok) · ses/TTS · sahte kurs
- Attempt Summary'yi ayrı ekrana taşıma → **bana sor** (C-136: önce öncelik sırası,
  sonra tek-düzeltme, ancak sonra ayrı ekran)

## Açık borcun
İzin kalıcı-ret sim teyidi · stil sayfası atıf/glossary doğrulaması · C-136 üçlüsü
