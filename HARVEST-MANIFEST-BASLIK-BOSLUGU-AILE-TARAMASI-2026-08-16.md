# 🔍 Harvest manifest title/description boşluğu — aile taraması (2026-08-16)

> **Görev:** Choreia'nın kendi harvest kütüphanesinde ölçülmüş bir boşluğun
> (manifests/*.json'da title/description alanı YOK, ama raw/*.info.json
> sidecar'ında VAR) diğer 4 app'te (Lissom, Gravita, JabLab, Ostinato) de
> geçerli olup olmadığını doğrulamak. **Salt-okunur** — `~/motion-harvest/`
> altında veya 5 app'in git deposunda tek bayt değiştirilmedi, taşınmadı,
> silinmedi. Choreia'nın kendisi YENİDEN ölçülmedi (zaten ölçülmüştü); yalnız
> aynı yöntemle tutarlılık spot-check'i yapıldı (aşağıda not edildi).
>
> **Yöntem, kısaca:** her app için `manifests/*.json` okunup `title`/
> `description` alanının durumu (absent/null/empty/present) çıkarıldı; eksik
> olan her kayıt için `raw/<video_id>.info.json` sidecar'ında aynı alan
> arandı. Ayrıca manifest'lerin anahtar-kümesi (key-shape) ve `retrieved_at`
> zaman damgasına göre kronolojik sıralaması çıkarılıp eksik/dolu geçişinin
> zamanla örtüşüp örtüşmediği test edildi. `tool_versions` alanı boşluğun
> bağımlılık-sürümü değişikliğiyle mi yoksa pipeline kod değişikliğiyle mi
> ilgili olabileceğini ayırt etmek için karşılaştırıldı.

---

## ÖZET TABLO

| App | Toplam manifest | Eksik title | Eksik description | Sidecar'da VAR (title / description) | Zamanlama ipucu |
|---|---|---|---|---|---|
| **Lissom** | 73 | 47 | 50 | 47/47 · 45/50 (5 vaka sidecar'da da boş — bkz. not) | **Temiz kesim**: son eksik 2026-07-29T02:03, ilk dolu 03:30 — araya hiç dolu kayıt girmiyor |
| **Gravita** | 35 | 3 | 3 | 3/3 · 3/3 | **Temiz kesim**: son eksik 01:26, ilk dolu 03:47 |
| **JabLab** | 30 | 3 | 5 | 3/3 · 3/5 (2 vaka sidecar'da da boş) | **KARIŞIK**: ilk ~73 dk'da (07-28 22:36–23:49) dolu/eksik İÇ İÇE geçiyor; 07-29T16:30'dan itibaren (bugüne, 08-16'ya kadar, 6 harvest oturumu boyunca) İSTİSNASIZ dolu |
| **Ostinato** | 94 | 41 | 41 | 41/41 · 41/41 | **Temiz kesim, en dar pencere**: son eksik 03:16:02, ilk dolu 03:20:40 (~4,5 dk ara) |
| *(Choreia — spot-check, YENİDEN ÖLÇÜLMEDİ)* | 79 | 14 | 14 | 14/14 · 14/14 | **Temiz kesim** (tutarlı): son eksik 01:01:51, ilk dolu 03:56:30 |

**Ham sayılar bunlar. Yorum/senaryo aşağıda ayrı bölümde — tabloyla karıştırılmasın.**

### Kütüphane boyutu (bağlam için)

| App | manifests | raw video (tam) | raw info.json | landmarks | transcripts |
|---|---|---|---|---|---|
| Lissom | 73 | 73 | 76 | 34 | 20 (+ subs/ 27) |
| Gravita | 35 | 35 | 35 | 27 | — |
| JabLab | 30 | 30 | 34 | 20 | 19 |
| Ostinato | 94 | 94 | 99 | 57 | 57 |

---

## Bulgu 1 — Boşluk 4 app'in 4'ünde de var, sidecar'da neredeyse istisnasız kurtarılabilir

Her app için "title/description eksik" kümesindeki her kayıt tek tek
`raw/<id>.info.json`'a karşı kontrol edildi:

- **Lissom**: title eksik 47/47 sidecar'da mevcut. description eksik 50
  kayıttan 45'i sidecar'da mevcut; **5 kayıt sidecar'da DA boş**
  (`8V3uad4MSaE`, `GL6kBBMtWkY`, `MKY-feF0dDo`, `VoWThqK8tCw`,
  `YECk8R-rVU4` — bunların 3'ünde manifest'te title zaten VAR, yalnız
  description boş; muhtemelen kaynak YouTube videosunun gerçekten
  açıklaması yok, pipeline hatası değil).
- **Gravita**: 3/3 title, 3/3 description — tam kurtarılabilir.
- **JabLab**: title eksik 3/3 sidecar'da mevcut. description eksik 5
  kayıttan 3'ü sidecar'da mevcut; **2 kayıt sidecar'da da boş**
  (`InSkFbZWoBY`, `gA8Se6i8mAI` — ikisinde de manifest'te title VAR).
- **Ostinato**: 41/41 title, 41/41 description — tam kurtarılabilir.

Yani gerçek "pipeline kaybı" oranı (sidecar'da veri var ama manifest'e hiç
girmemiş): Lissom title 47, desc 45 · Gravita 3/3 · JabLab title 3, desc 3 ·
Ostinato 41/41. Sidecar'da da boş olan 7 vaka (Lissom 5, JabLab 2) ayrı bir
kategori — muhtemelen kaynağın gerçekten açıklaması yok, KOPYALAMA hatası
değil.

Choreia manifests/ üzerinde aynı yöntemle spot-check yapıldı (yeniden tam
ölçüm değil): kütüphane genelinde title eksik olan **14** manifest var
(`app` klasöründe text-search'le bulunan 11 adaylık alt-kümeden farklı bir
payda — 11'i "hangi kayıtlar tarandı" sorusuna, 14'ü "kütüphanede kaç tanesi
gerçekten eksik" sorusuna cevap veriyor, birbirleriyle ÇELİŞMİYOR). 14'ünün
14'ü de sidecar'da title/description'a sahip.

## Bulgu 2 — Manifest anahtar-kümesi (key-shape) title'la BİRLİKTE kayboluyor

Eksik-title manifest'lerde yalnız `title`/`description` değil, aynı anda
`rom_mode`, `reference_eligible`, `context_tags`, `context_source`,
`movement` alanları da TAMAMEN YOK (null değil, anahtar hiç yok). Bu, 4
app'in 4'ünde de aynı şekilde gözlendi (choreia'da da aynı — `35sk_G8Vf9o`
örneğinde doğrulandı). Yani bu tek bir alanın unutulması değil, manifest
yazımının daha eski/eksik bir sürümünün ürettiği TEK BİR BLOK'un toptan
yokluğu.

## Bulgu 3 — Zamanlama: 3 app'te temiz kesim, JabLab'da ilk oturumda kısa süre iç içe

`retrieved_at` alanına göre kronolojik sıralamada:

- **Lissom, Gravita, Ostinato, (Choreia)**: eksik-title kayıtların HİÇBİRİ,
  dolu-title kayıtların hiçbirinden SONRA gelmiyor — yani belirli bir ana
  kadar (her app kendi zaman çizelgesinde, hepsi 2026-07-28 gece – 2026-07-29
  sabah erken saatleri arası) yazılan HER kayıt eksik, o andan sonra
  kütüphanenin geri kalanının TAMAMI (haftalarca süren sonraki harvest
  oturumları dahil) dolu. Kesim genişliği (son-eksik → ilk-dolu arası boşluk)
  Ostinato'da yalnızca ~4,5 dakika, Gravita'da ~2s21dk, Lissom'da ~87dk.
- **JabLab**: ilk harvest oturumunun ilk ~73 dakikasında (2026-07-28
  22:36–23:49 UTC) dolu ve eksik kayıtlar İÇ İÇE GEÇİYOR (dolu, eksik, dolu,
  eksik, dolu, dolu, eksik sırasıyla) — yani JabLab'da net bir "önce/sonra"
  çizgisi YOK, o dar pencerede tutarsız/aralıklı davranıyor. Ama
  2026-07-29T16:30'dan itibaren — kütüphanenin geri kalan ÖMRÜ boyunca, bugün
  (2026-08-16, saat 02:16) dahil, 6 farklı `tool_versions`/`harvestRig`
  varyantı ve en az bir feature branch (`feat/d1-gate-tool`) üzerinden
  gelen kayıtlar dahil — İSTİSNASIZ her kayıtta title/description dolu.

`tool_versions` (ytDlp/ffmpeg/openCv/mediapipe) eksik-title ve dolu-title
kayıtlarda 4 app'te de BİREBİR AYNI — yani bu üçüncü-taraf araç sürüm
yükseltmesiyle açıklanmıyor. Bazı (hepsi değil) sonraki manifestlerde bir
`tool_versions.harvestRig` alanı (git sha/branch/dirty/behindOriginMain)
belirmeye başlıyor — harvest pipeline'ının kendisinin git-izlenen, sürümlü
bir kod tabanı olduğunun doğrudan kanıtı, ama bu alanın kendisi title-
düzelmesiyle bire bir aynı anda eklenmemiş (JabLab'da dolu-title
manifestlerin bir kısmında bile hâlâ yok) — yani "title neden düzeldi"
sorusuna bu tek başına kanıt değil, yalnızca DESTEKLEYİCİ bağlam.

**"Recovered from sidecar" veya benzeri bir kurtarma-işareti dili** 4 app'in
hiçbirinin manifest'lerinde bulunamadı (metin taraması yapıldı: "recover",
"sidecar", "backfill", "patched" — çıkan birkaç eşleşme hep videonun kendi
başlığı/açıklamasında geçen "recovery" kelimesiydi [ör. fizik tedavi/spor
toparlanma videoları], pipeline'a ait değildi). Choreia'da da yok. Yani eğer
bir "sidecar'dan kurtarma" adımı gerçekten çalıştıysa bile, manifest'e bunu
belirten bir iz bırakmıyor.

## Bulgu 4 — Orphan tarama: "Anna Shuffle" tipi (tam video + manifest YOK) vaka bulunamadı

4 app'in `raw/`'ında da **tam indirilmiş video dosyası olup manifest'i
olmayan** tek bir kayıt bile yok (0/0/0/0). Bulunan tek "manifest'siz" kayıt
türü — ki bu farklı ve zararsız bir kategori — **yarım kalmış indirmeler**:

- **Lissom**: 3 video_id yalnız `info.json`'a sahip, video hiç indirilmemiş
  (`EriPRTk1ly0`, `Iovy1VVmKLU`, `T7qT6l9npPg`).
- **JabLab**: 4 vaka — 2'si yalnız info.json (`5PtQn5ljHOM`, `d7sPW7fuS_E`),
  2'si kısmi/parça indirme (`6KPs2tFATI0` bir `.f137.mp4.part` ile;
  `r9qEcFzZVDA` bir tam `.f303.webm` video-akışı + yarım kalmış
  `.f251.webm.part` ses-akışı ile — yt-dlp video+ses ayrı çekip birleştirmiş
  olsa gerek, birleştirme hiç tamamlanmamış).
- **Ostinato**: 5 vaka, biri kısmi (`thQ4n8cHkZc` bir `.f137.mp4.part` ile),
  4'ü yalnız info.json.
- **Gravita**: Bu app'te AYRICA `raw-orphaned/` diye ayrı bir karantina
  klasörü var — 9 video (`0KtrNQre5rQ`, `0V7BtcG7E4Y`, `65mNUsGx4XM`,
  `LszCaPOFWHg`, `RClKKQqsvXA`, `WkdXHQ74khI`, `gsNoPYwWXeM`, `mla-gfQVQyA`,
  `zWXToSCaq-Q`) — TAM .mp4 dosyaları ama `.info.json`'ları bile yok, hiç
  manifest'e girmemişler. Ama bu **Choreia'daki "Anna Shuffle" vakasına
  benzeyen, AMA ZATEN BİLİNEN ve ZATEN ele alınmış** bir durum: kendi
  `README.orphans.json`'ına göre 2026-07-30'da karantinaya alınmış
  ("kesintiye uğramış bir indirme turundan kalma… G-057 kütüphane-karışması
  sınıfı, ikisi aslında SQUAT klibi"; karar M-F-171/3). Yani bu YENİ bir
  keşif değil — burada yalnız var olduğu teyit edildi.

Bu görev kapsamında **yeni bir "Anna Shuffle" benzeri vaka bulunmadı**;
yukarıdaki yarım-indirmeler farklı bir mekanizma (indirme tamamlanmadı →
pipeline zaten manifest yazmadı, beklenen davranış) ve bug olarak
görünmüyor.

## Diğer gözlemler

- JabLab'ın harvest'i **hâlâ aktif/canlı** — en son manifest bugünün
  (2026-08-16) saat 02:16'sına ait, `raw/` klasöründe bugüne ait dosyalar
  var. Diğer 3 app'in kütüphaneleri Temmuz sonunda dondu görünüyor.
- `~/motion-harvest/` altında görev kapsamı dışında iki ek klasör var:
  `gravita-squat/` (5 app'in hiçbirine birebir uymayan, muhtemelen Gravita'nın
  squat-özel bir alt-harvest'i, kendi `landmarks-rep-sliced/` alt klasörü
  var) ve üst dizinde tek başına duran `posture-dialect-sweep.json`. İkisi de
  bu görevin kapsamı dışında tutuldu, dokunulmadı, yalnız var olduğu not
  ediliyor.

---

## SENTEZ (yorum — ham sayılardan ayrı)

Çalışan teori **doğrulandı**: bu, Choreia'ya özgü değil, **4 app'in 4'ünde
de** aynı imzayla (title+description+rom_mode+reference_eligible+
context_tags+context_source bloğunun toptan yokluğu, sidecar'da veri
istisnasız mevcut) görünen, **aile çapında paylaşılan bir harvest-pipeline
davranışı**. En güçlü kanıt zamanlama: 4 app'in 4'ünde de (+Choreia
spot-check) eksik kayıtların TAMAMI her app'in kendi harvest tarihçesinin en
erken diliminde (hepsi 2026-07-28 gece – 2026-07-29 sabah erken arası)
toplanıyor; o noktadan sonra —haftalarca süren, JabLab'da bugüne kadar uzanan
sonraki harvest'lerin TAMAMINDA— tek bir eksik kayıt yok. Bu, "aynı hata
kütüphane genelinde rastgele/aralıklı oluyor" senaryosunu değil, "erken bir
noktada düzelen/düzeltilen bir şey" senaryosunu destekliyor.

Tek nüans: bu "düzelme" 3 app'te (Lissom/Gravita/Ostinato, +Choreia) TEK BİR
KESKİN ÇİZGİ gibi görünürken, JabLab'da ilk oturumun ilk ~73 dakikasında kısa
bir iç-içe-geçme penceresi var. Bunun tek bir kesin nedeni bu veri setinden
çıkarılamıyor — kod/pipeline kaynağına bakılmadı (görev kapsamı dışı, salt
veri). "Rastgele/tüm kütüphaneye yayılmış" bir örüntü değil; ama "tek an'da,
tüm ailede senkron düzelen tek bir olay" da değil — en azından JabLab'ın ilk
73 dakikası bunu tam desteklemiyor. Bu ayrım (temiz kesim vs kısa iç-içe-geçme
penceresi) koordinatöre aktarılırken korunmalı.

---

*Bu dosya salt-okunur bir taramanın çıktısıdır; `~/motion-harvest/` veya 5
app'in git depolarında hiçbir şey değiştirilmedi. Ham veriye dönmek isteyen
biri için: her app'te `manifests/*.json` vs `raw/*.info.json` karşılaştırması
video_id bazında tekrarlanabilir.*

---

## EK — TÜKETİCİ ÖLÇÜMÜ: Choreia (2026-08-16, Choreia hattı)

**Soru:** boş alanın (`title`/`description`/`rom_mode`/`reference_eligible`/`movement`)
KENDİSİ değil, onu **okuyan bir kod var mı** — ölçüldü, `tools/*.py`nin tamamı tarandı.

| alan | tüketici | manifest mi sidecar mı | sınıf |
|---|---|---|---|
| `title` | `classify_source.py:meta_text()` | **yalnız sidecar** (`raw/<id>.info.json`) — manifest'in kopyasına HİÇ bakılmıyor | 🟢* |
| `description` | aynı | aynı | 🟢* |
| `rom_mode` | yok | — | 🟢 |
| `reference_eligible` | yok | — | 🟢 |
| `movement` | yok | — | 🟢 |

`rom_mode`/`reference_eligible`/`movement`in TEK geçtiği yer `build_reference.py`nin kendi
YORUMU (satır ~1130) — kod bu alanları OKUMUYOR, kasıtlı (`C-123`: bir salsa videosunun
`reference_eligible:true` manifestiyle hip-hop referansına sızması, fail-open ölçülmüş olay).

`*` **Nüans:** `title`/`description` için 🟢 tam doğru kutu değil — alan hiç OKUNMUYOR değil,
**manifest'teki kopyası hiç okunmuyor, KENDİSİ sidecar'dan doğrudan okunuyor** (aynı bilgi,
farklı/sağlam kaynak). Yani bu tüketici hiçbir zaman manifest'in eksik alanına maruz kalmıyor —
sonuç aynı (canlı kusur yok) ama mekanizma farklı, ikisini aynı kutuya sıkıştırmak yanlış
olurdu.

**Sonuç, Choreia için: 🔴 (canlı kusur) HİÇBİR alanda YOK.** Beş alanın hiçbiri, manifest'teki
eksik kopyasıyla gerçekten okunmuyor — ya hiç tüketici yok, ya tüketici zaten sidecar'dan
okuyor. Backfill Choreia'nın kendi doğruluğu için ACİL DEĞİL; ama iki-kaynaklı
tutarsızlığın kendisi (manifest eksik, sidecar dolu) yine de gerçek ve düzeltilebilir bir
hijyen sorunu — yalnız kimseyi şu an yanıltmıyor.

## EK — TÜKETİCİ ÖLÇÜMÜ: diğer 4 hat (2026-08-17, Ostinato hattı, `H-82`③ görevi)

**Yöntem, Choreia'yla birebir aynı soru:** boş alanların (`title`/`description`/`rom_mode`/
`reference_eligible`/`context_tags`/`context_source`) KENDİSİ değil, onları **manifest'in
kendi kopyasından okuyan bir kod var mı** — her hattın `tools/`/`packages/*/tool` ağacı
tarandı (Python: `.get("title"`/`["title"]` deseni; Dart: `m['title']` deseni). **Salt-okunur**
— hiçbir dosyada tek bayt değiştirilmedi. ⛔ Bu ölçüm bir çare ÖNERMİYOR (`H-82`'nin sınırı) —
karar tek elden orkestratörde.

| Hat | tüketici bulundu mu | manifest mi sidecar mı | sınıf |
|---|---|---|---|
| 🥁 **Ostinato** | `tools/reclassify_rom.py:69-76` | **sidecar** (`raw/<id>.info.json`) — manifest'in kopyasına HİÇ bakmıyor | 🟢 (Choreia'nın 🟢*'ı ile AYNI mekanizma) |
| 🤸 **Gravita** | `tools/reclassify_eligibility.py:121-130` | **manifest** — `(lib/"manifests").glob("*.json")`den `json.loads`, `m.get("title")`/`m.get("description")` doğrudan manifest kopyasından | 🔴 |
| 🌊 **Lissom** | `tools/reclassify_pool.py:97-116` | **manifest** — `MANIFESTS.glob("*.json")`den `json.loads`, `m.get("title", "")`/`m.get("description", "")` doğrudan manifest kopyasından | 🔴 |
| 🥊 **JabLab** | `title`/`description` için **YOK** (repoda taranan hiçbir dosya bu ikisini manifest'ten okumuyor) — ama AYNI blok'un diğer dört alanı için **VAR**: `packages/jablab_engine/tool/segment_punches.dart:194-201` (`_refreshEligibility`), `m['reference_eligible']`/`m['rom_mode']`/`m['context_tags']`/`m['context_source']` — Dart `Map` köşeli-parantez erişimi, eksik anahtarda **`null`** döner (Python `KeyError` gibi patlamaz) | 🔴 (title/desc için 🟢 — ayrı alan çifti, aynı blok) |

### Gravita ve Lissom — aynı sınıf, ikisi de fail-open değil ama SESSİZ

İkisi de `m.get(key, "")`/`m.get(key) or ""` deseniyle eksik alanı **boş string**e düşürüyor,
sonra `rom_mode.classify(title="", description="", transcript=..., ...)` çağırıyor. Transkript
VARSA (`sourcesSeen`e transkript de giriyor) sınıflandırma yine de anlamlı bir sonuç
üretebilir — ama transkriptsiz bir kaynak için bu, sınıflandırıcıyı **kasıtlı fail-closed**
tasarımının (`rom_mode.py`: "ayrım kamerada görünmez, yalnız anlatıda") beslediği metni
sessizce sıfırlamak demek. **Etki alanı ölçüldü, iddia edilmedi:** Gravita'da 3 manifest
(title+desc ikisi de eksik), Lissom'da title-eksik 47 / desc-eksik 50 manifest bu yolun
üzerinden geçerse aynı riske girer — GERÇEKTEN geçtiler mi (bu araçlar o kayıtlara karşı hiç
koşuldu mu) bu görevin kapsamı dışı, ayrı bir ölçüm gerektirir.

### JabLab — farklı alan çifti, ama AYNI blok, ve `null` zaten bir anlam taşıyor

`segment_punches.dart`ın kendi yorumu (satır 211-213) `referenceEligible`ta **YOK ile `false`
AYNI DEĞİLDİR** diyor — yokluk "henüz sınıflandırılmadı" anlamına geliyor kodun kendi
sözleşmesinde. Gap-etkili bir manifest bu fonksiyondan geçerse `m['reference_eligible']` →
`null` döner ve `out['referenceEligible']` bu `null` ile EZİLİR (satır 223: `out.addAll(fresh)`)
— eğer o kaynağın DAHA ÖNCE gerçek bir sınıflandırması varsa (örn. ilk hasat sırasında
üretilmiş), bu "tazeleme" onu sessizce "henüz sınıflandırılmadı" durumuna geri düşürür. Bu
fonksiyon yalnız `--manifests <dir>` bayrağıyla çağrıldığında çalışıyor (opsiyonel yol) —
GERÇEKTEN JabLab'ın 3/5 gap-etkili manifestine karşı çalıştırıldı mı, bu ölçümün kapsamı dışı.

### Sonuç — dört hattın dördü de tarandı, iki farklı sınıf çıktı

🟢 **Choreia + Ostinato:** aynı mekanizma (sidecar'dan doğrudan okuma), canlı kusur yok.
🔴 **Gravita + Lissom:** aynı mekanizma (manifest kopyasından okuma), title/description alanları
için potansiyel canlı maruziyet — gerçekleşti mi (araç o kayıtlara karşı koşuldu mu) ayrı ölçüm
gerektirir. 🔴 **JabLab:** title/description için maruziyet YOK, ama AYNI blok'un
`rom_mode`/`reference_eligible`/`context_tags`/`context_source` dörtlüsü için farklı bir
mekanizmayla (`--manifests` tazeleme yolu) maruz.

*(Bu ek 2026-08-17'de tamamlandı — diğer 4 app'in dördü de tarandı, yukarıdaki tablo nihai.)*
