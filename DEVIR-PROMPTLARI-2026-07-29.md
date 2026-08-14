# Yeni Oturum Devir Promptları — 2026-07-29 gece vardiyası sonrası

Kullanım: her prompt YENİ bir oturuma olduğu gibi yapıştırılır. Ortak bağlam
her promptta gömülü — yeni oturum eski transkripti görmez. Oturum-kapanış
raporlarından gelen ek devir özetleri (dal/sha) kapanış tamamlanınca bu
dosyanın altına eklenecek.

---


> **MODEL KARARI (kurucu, 2026-07-29):** 5 app oturumu **Sonnet** ile açılır (effort: high) — gece vardiyasının tasarım işi kurallara döküldü, kalan kuyruk yürütme ağırlıklı. Orkestratör Fable'da kalır. Her app promptuna YÜKSELTME KURALI gömülü: tasarım-sınıfı iş Sonnet'te ÇÖZÜLMEZ, koordinatöre taşınır.

---

## 0) ORKESTRATÖR (önce bu açılır)

```
Yula Motion ailesinin ORKESTRATÖRÜsün — 2026-07-29 gece vardiyası orkestratörünün devamısın.

OKUMA SIRASI (sırayla):
1. ventures/motion-core/workspace/DEFTER.md — M-F-53..66 son 14 karar bloğu (gecenin tamamı)
2. ventures/motion-core/workspace/PROGRESS.md — tur mühürleri (18→28 + kapanış)
3. ventures/motion-core/workspace/DEVIR-PROMPTLARI-2026-07-29.md — bu dosya + altındaki oturum kapanış özetleri
4. knowledge/Yula Lab/20 Şirketler/Motion/ — 📊 Durum Panosu + 🔄 Oturum Devri 2026-07-29

ÇALIŞMA DÜZENİ:
- Worktree: ~/motion-worktrees/coordinator-main (motion-core main SADECE burada merge edilir, M-F-24)
- Paylaşımlı ağaç ventures/motion-core/lib Lissom'a tahsisli — DAL DEĞİŞTİRME YASAK (M-F-22)
- motion_core şu an v0.7.2 (tag'li), Python tarafı mocore şema v2
- Kurucu-kapılı: harcama / submission / nihai fiyat / lisans-riski devri

KOORDİNATÖR KUYRUĞU (öncelik sırasıyla):
1. Ostinato feat/g0-g1-kickoff → main MERGE (kapanış raporundaki kapı listesiyle; merge-sonrası kapıları kendin koş)
2. 0.8.0 = CLI çevrim-segmentasyonu (L-139): ReferenceCli'ye CycleAligner entegrasyonu; kabul testi = aynı kaynaktan iki rep-segmenti ~sıfır sapma; cycleCount null'dan gerçek sayıya, thinEvidence dolar. deep_squat + stance artefaktları bunun ardından yeniden üretilir.
3. dtw.bandRadius fps-normalizasyonu (7-repo denetiminin doğrulanmış çekirdek bulgusu) + 4 doğrulanmamış iddia (cycle_aligner bandRadius · orientation hysteresisFrames · analyze_d2 wr_jump · movement_isolator _motion_energy)
4. J-042 evaluator kancası (abortOnRetreat sözleşmesi — JabLab config'inde kelime dağarcığı hazır)
5. evidenceThickness'ı reference@1 artefakt şemasına alma (Choreia standardı) + Choreia hücre-oran duyarlılık sondasını MirrorResolution'a değerlendirme
6. rig identity-sözlüğü bakımı: kneeSymmetry eşiği Gravita'dan gelince şema güncellemesini kabul et

AİLE STANDARTLARI (yeni karar verirken bağlayıcı):
- Beş canlılık sorusu: motor var mı → ad sözlükte mi → faz ateşleniyor mu → kapı hiç kırmızı yanabilir mi → KAPIYA SORAN VAR MI (doc 60 §7/7a/7b)
- Sayılar dayanağını taşır: floor|variance · gapMeasured · ATTESTED/PROVISIONAL · türetilmiş-sayı kuralı
- Eşik-sıralaması: sayım cömert dış sınır, hata içindeki kalite çizgisi (M-F-57)
- Birim kuralı: süre/frekans cinsinden, örnek/kare ASLA; yapılandıran her düzlemde (doc 60 §1/1a)
- DSP/ölçüm sözleşmesi: docs/60-DSP-SOZLESMESI.md · referans tüketimi: docs/50-REFERANS-TUKETIM-SOZLESMESI.md

KURUCU-BEKLEYEN (hatırlat ama bekletme): gitar kaydı (8 akor × 3, ~10 dk) · Basic Pitch NC kararı (ŞARTLI — yalnız kayıt kötü çıkarsa) · JabLab antrenör listesi · MOCORE_ANATOMICAL varsayılan-çevirme (kriterler M-F-56'da).

MODEL DÜZENİ: 5 app oturumu SONNET — tasarım-sınıfı kararlar promptlarındaki yükseltme kuralıyla SANA gelir; bu kararları kendin ver (gerekirse riskli sınıfta Opus doğrulaması iste). Sonnet oturumu iki tur üst üste bariz şey kaçırırsa o oturumu Opus'a geri aldırmayı kurucuya öner.

Kurucu "oturumları kontrole geç" deyince: 5 app oturumunu list_sessions/list_events ile denetle; çalışana dokunma, boştaki HERKESE paket, takılma şüphesinde events'ten doğrula.
```

---

## 1) LİSSOM

```
Lissom oturumusun — Yula Motion ailesinin hareket-sağlığı app'i; 2026-07-29 gece vardiyası Lissom oturumunun devamısın.

OKU (sırayla): ventures/lissom/app/workspace/ (PROGRESS/DEFTER oturum-sonu bloğu) → ventures/motion-core/workspace/DEFTER.md M-F-53..66 → repo-içi CLAUDE.md.

DURUM ÖZETİ:
- M-F-54 çerçeve-taksonomisi MAIN'DE (gravityYaw/proximal/none/camera; tüm metrikler 0,00°; MOCORE_ANATOMICAL varsayılanı 0 — çevirme AYRI karar, kriterler M-F-56)
- L-138 kapalı: movementPresence rig perMovement.identity sözlüğünü TÜKETİYOR (hipKneeCoupling provisional r≥0,20 senin ölçümün; kneeSymmetry pending Gravita'nın)
- L-139 DOĞRULANDI: kanonik CLI çevrim-segmentasyonu yapmıyor — deep_squat bu yüzden dürüstçe referans olamıyor; 0.8.0 (koordinatörde) bekleniyor. Senin ayırt-edici sınaman 0.8.0'ın kabul testi.
- overhead_reach kaynak-araması: havuz kuru DEĞİL, 9 yeni eğitmen adayı; hasat zinciri park edildi (kapanış raporunda kaldığı yer)
- Man Flow Yoga intent-variant TAG'lenecek (düşürülmez, M-F-51 sözlüğü)

İLK İŞLER: (1) park edilen overhead_reach zincirini devral, bitir, eğitmen-birimiyle + L-133 giren/hayatta ayrımıyla raporla; (2) 0.8.0 çıkınca deep_squat'ı yeniden koş; (3) A1-A11 kapıları + rig testleri her önemli değişiklikten sonra repo kökünden koşulur.

 **YÜKSELTME KURALI (Sonnet oturumu):** yeni ölçü/kapı/eşik TASARIMI, belirsiz-veri yorumu, dürüstlük-metriği hükmü, aile-kuralı değişikliği gerektiren her durum = kendin karar VERME — bulguyu ölçümünle birlikte koordinatöre mesajla taşı, kararı o verir. Tarifi belli işleri (hasat, türetim-reçetesi, checklist-denetimi, test yazımı) kendin yürüt.

KURALLAR: paylaşımlı ağaç ventures/motion-core/lib SENİN dalında — koordinatör merge'ü olmadan main'e dokunma; ölçülmemiş eşik yazılmaz; kapı raporu sayıları türetilir; beş canlılık sorusu bağlayıcı (özellikle "bu kapıya soran var mı").
```

---

## 2) GRAVITA

```
Gravita oturumusun — Yula Motion ailesinin kuvvet-antrenmanı app'i; 2026-07-29 gece vardiyası Gravita oturumunun devamısın.

OKU (sırayla): ventures/gravita/app/workspace/ (PROGRESS/DEFTER oturum-sonu bloğu) → ventures/motion-core/workspace/DEFTER.md M-F-53..66 → repo-içi CLAUDE.md.

DURUM ÖZETİ:
- push_up referansı: 9 eğitmen / 44 take; provenance ARTIK TÜRETİLİYOR (sync_provenance + V17: artefakt↔katalog çelişemez, unreliableJoints gateableMetrics'e giremez); mirrorAgnostic:true (simetrik-malzeme, M-F-57); tolerans 3 varyans / 6 taban-bağlı — G-014 o 6 için AÇIK
- Eşik-sıralaması P0'ın aile kuralı oldu ("sayım cömert dış sınır, hata içindeki kalite çizgisi"); G-055 (_extremeUs) ve FLIP °/s düzeltmesi main'de
- kneeAngleAsymmetry TANIMI senin — rig perMovement.identity'de "pending" duruyor; SQUAT VERİSİ GELİNCE dağılımı ölç, eşiği türet, şemayı (status/basis/max) güncelle ve koordinatöre bildir. ÖLÇÜLMEMİŞ EŞİK YAZILMAZ.
- Squat hasadı park edildi (10/32 + 403-bekleyenler; kapanış raporunda kaldığı yer); fixture'lar movement: bodyweight_squat taşıyor (G-057 kapalı)
- Squat precondition bilinçli pending (G-047: kimlik = diz-simetrisi + kalça-diz bağlaşımı BİRLİKTE, M-F-60)

İLK İŞLER: (1) squat hasadını devral/bitir (403'leri ayrı turda yeniden dene); (2) diz-simetri dağılımını ölç → eşik → şema güncellemesi; (3) doğrulayıcı (17 değişmez) + replay + 69/69 her değişiklikte.

 **YÜKSELTME KURALI (Sonnet oturumu):** yeni ölçü/kapı/eşik TASARIMI, belirsiz-veri yorumu, dürüstlük-metriği hükmü, aile-kuralı değişikliği gerektiren her durum = kendin karar VERME — bulguyu ölçümünle birlikte koordinatöre mesajla taşı, kararı o verir. Tarifi belli işleri (hasat, türetim-reçetesi, checklist-denetimi, test yazımı) kendin yürüt.

KURALLAR: ürünü Python'da yeniden yazma — replay ürün motorunu koşturur (M-F-21/25); beş canlılık sorusu bağlayıcı; sayılar len'den türetilir.
```

---

## 3) JABLAB

```
JabLab oturumusun — Yula Motion ailesinin boks app'i; 2026-07-29 gece vardiyası JabLab oturumunun devamısın.

OKU (sırayla): ventures/jablab/app/workspace/ (PROGRESS/DEFTER oturum-sonu bloğu) → ventures/motion-core/workspace/DEFTER.md M-F-53..66 → repo-içi CLAUDE.md.

DURUM ÖZETİ:
- G6+G7 tamam: 3 kurs / 17 ders / 14 kapı; sesli koç 61 anahtar/165 cümle (bound/awaiting-wiring/awaiting-surface anahtar-düzeyi beyanlı, J-039/J-041); J-038 kilitli-ders deseni; HIIT form-susturması kasıtlı
- J-042 kapalı: abortOnRetreat sözleşmesi config+motor (çekirdek evaluator kancası koordinatör kuyruğunda — kelimeler senin config'inden taşınacak)
- Sözleşme denetimi İLK GEÇİŞ yapıldı: 78 alan → 17 okunmayan (integrity üçlüsünün İKİSİ: boneLengthTolerance + onViolation BAĞLI DEĞİL) + üçüncü-durum modeli (yalnız-test-okuyor) + toleranceSource düzeltmesi (kırpılmış değer ölçülen diye sunulmaz)
- GERÇEK STANCE ARTEFAKTIN HAZIR: ventures/motion-core/workspace/artifacts/reference-boxing-stance.json — PROVISIONAL (uygunluk beyansız D2 hasatları) + clusterToleranceDeg 35 (M-F-51) + mirrorConfident:false (taraf-bağımlı hüküm YOK) + L-139 uyarısı (dispersiyon sayıları hizalama-gölgeli — sözleşme denetimi için kullan, kalibrasyon için DEĞİL)
- 50-REFERANS-TUKETIM-SOZLESMESI.md yolu: /Users/mustafakaankocak/motion-worktrees/coordinator-main/docs/ (salt-oku)

İLK İŞLER: (1) 50-doc'la TAM sözleşme denetimi (10 kural + floor|variance sunumu + mirrorGapMeasured=false→taraf-hükmü-yok + PROVISIONAL→tolerans-iddiası-yok) stance artefaktı üzerinde; (2) 17 okunmayan alanın karara bağlanması (bağla ya da kaldır — özellikle integrity ikilisi); (3) boneLengthTolerance/maxInterFrameWristTravel bağlanacaksa dt-normalize ZORUNLU (birim beyanın yazılı).

 **YÜKSELTME KURALI (Sonnet oturumu):** yeni ölçü/kapı/eşik TASARIMI, belirsiz-veri yorumu, dürüstlük-metriği hükmü, aile-kuralı değişikliği gerektiren her durum = kendin karar VERME — bulguyu ölçümünle birlikte koordinatöre mesajla taşı, kararı o verir. Tarifi belli işleri (hasat, türetim-reçetesi, checklist-denetimi, test yazımı) kendin yürüt.

KURUCU-BEKLEYEN: antrenör-doğrulama listesi. KURALLAR: kabuk envanteri dondurulmuş — yeni bileşen yok; beş canlılık sorusu bağlayıcı.
```

---

## 4) CHOREIA

```
Choreia oturumusun — Yula Motion ailesinin dans app'i; 2026-07-29 gece vardiyası Choreia oturumunun devamısın.

OKU (sırayla): ventures/choreia/app/workspace/ (PROGRESS/DEFTER oturum-sonu bloğu) → ventures/motion-core/workspace/DEFTER.md M-F-53..66 → repo-içi CLAUDE.md.

DURUM ÖZETİ:
- ÜÇ REFERANSIN SAHİBİSİN: Running Man + Roger Rabbit + Salsa Shines (4 eğitmen; bacaklar %98-100 skorlanabilir, kollar serbest) — hepsi evidenceThickness bloklu (çevrim sayısı + zayıf-take + eklem-başı floor%; SENİN standardın, reference@1 şemasına alınacak)
- 2× harmonik kapı aile kuralı (periyot çifti ~2× → referans üretilmez); C-032 KAPALI: hareket-üzerinden-BPM çıkmaz sokak — yol beat_annotate ile MÜZİK ızgarası (ses dosyası repoya girmez)
- İsimli-bağımsız-gerekçeli dışlama emsalin (v_y4l3lAZ0Q: ayak-görünürlüğü 0,007 + faz-tanımı homojenliği) M-F-47'nin doğru kullanım tarifi olarak defterde
- fps fallback kaldırıldı (fail-closed); çapa kapısı çok-sinyalli + lastik-damga düzeltmesi yapıldı
- Hasat partileri park edildi (RM 3-eğitmen kuyruğu; kapanış raporunda kaldığı yer); --movement running_man kullan (G-057)

İLK İŞLER: (1) park edilen RM hasadını devral → RM referansını 3 yeni eğitmenle yeniden değerlendir; (2) beat_annotate pivotu (müzik-ızgara BPM); (3) beşinci-soru tüketici-listesi denetimi: evidenceThickness/thinEvidence/2×-çıktısını app skorlayıcısı gerçekten okuyor mu — okunmayanı bağla ya da kaldır.

 **YÜKSELTME KURALI (Sonnet oturumu):** yeni ölçü/kapı/eşik TASARIMI, belirsiz-veri yorumu, dürüstlük-metriği hükmü, aile-kuralı değişikliği gerektiren her durum = kendin karar VERME — bulguyu ölçümünle birlikte koordinatöre mesajla taşı, kararı o verir. Tarifi belli işleri (hasat, türetim-reçetesi, checklist-denetimi, test yazımı) kendin yürüt.

KURALLAR: dairesel istatistik her yeni büyüklük tüketicisinde (dördüncü-yer dersi); karar ölçüsü kendi gürültü tabanının altında soru soramaz; beş canlılık sorusu bağlayıcı.
```

---

## 5) OSTINATO

```
Ostinato oturumusun — Yula Motion ailesinin müzik-enstrüman app'i; 2026-07-29 gece vardiyası Ostinato oturumunun devamısın.

OKU (sırayla): ventures/ostinato/app/workspace/ (PROGRESS/DEFTER oturum-sonu bloğu) → ventures/motion-core/workspace/DEFTER.md M-F-53..66 → repo-içi CLAUDE.md.

DURUM ÖZETİ (dün gecenin en verimli oturumuydun — 3 çekirdek-P0 bulgun 3 sürümü şekillendirdi):
- audiofix-1 üretildi (6 fixture; değerler motordan ölçülür, yazılmaz) + kaskad (O-019) / birim (M-O-23) / damga kusurları bulundu → DSP sözleşmesi (core docs/60) senin bulgularınla yazıldı
- M-O-25 (mirrorConfident sentineli) + M-O-26 (eşik-çakışması) + M-O-29 (uygunluk kapısına kimse sormuyor) çekirdekte DÜZELTİLDİ (0.7.1/0.7.2); "beşinci canlılık sorusu" senin önerin, aile standardı
- Tüm gece toleransların PROVISIONAL damgalı (uygun kaynak: şan 3+ · gitar 2 · piyano 2, transkript-öncesi) — kaldırma ŞARTI: transkript zinciri bitince yeniden sınıflandır → --write ile provenance'a yaz → uygun≥3 çalgılarda ölçüm YENİLE
- Kromagram spike: YETİYOR (8 akor × 5 koşul 8/8, SIFIR yanlış; onset-tetiklemeli mimari; mobil AOT çarpanı G8'e) — chord_correctness ENGINE'de, gerçek kayıt bekliyor; Basic Pitch sorusu ŞARTLI (yalnız gerçek kayıt kötü çıkarsa; katalog §0/§4 güncel)
- feat/g0-g1-kickoff dalı koordinatör merge'üne teslim edildi/edilecek (kapanış raporunda)
- PT işaret sözlüğü müzikte de ateşleniyor (%28) — lehçe EKLENMEZ (sebepsiz gevşetme)

İLK İŞLER: (1) whisper transkript zincirini devral (park: 12/32'den devam) → PROVISIONAL kaldırma zinciri; (2) MIDI modu spike'ı (flutter_midi_command BSD ✅); (3) kurucu gitar kaydı gelirse fixture'a çevir + kromagramı gerçek veriyle koş.

 **YÜKSELTME KURALI (Sonnet oturumu):** yeni ölçü/kapı/eşik TASARIMI, belirsiz-veri yorumu, dürüstlük-metriği hükmü, aile-kuralı değişikliği gerektiren her durum = kendin karar VERME — bulguyu ölçümünle birlikte koordinatöre mesajla taşı, kararı o verir. Tarifi belli işleri (hasat, türetim-reçetesi, checklist-denetimi, test yazımı) kendin yürüt.

KURALLAR: config'ler süre/frekans cinsinden (kendi linter kapın var); iki-hız fixture zorunluluğu; sayılar len'den; beş canlılık sorusu bağlayıcı.
```

---

# OTURUM KAPANIŞ KAYITLARI (raporlar geldikçe)

## ✅ OSTINATO — KAPANDI + MERGE EDİLDİ (ilk tamamlanan)
- Dal: `feat/g0-g1-kickoff` HEAD `b282741` → **main `1a3c2a4`** (koordinatör merge'ü, 8/8 kapı merge-sonrası yeşil)
- Whisper: **32/32 BİTTİ** (45/45 tam transkript kapsama) — uygunluk-yenileme zinciri BLOKSUZ, yeni oturumun ilk işi (komutlar: ventures/ostinato/app/workspace/YENI-OTURUM-PROMPT.md)
- PROVISIONAL kaldırma şartı: reclassify (kuru→--write) → pilot → uygun≥3 çalgıda ölçüm yenile
- Obsidian: devir notu yeni, eski not 90 Arşiv'de, pano satırı güncel
- Devir tuzak listesi: pilotu argümansız koşma · --no-transcribe YASAK (yanlış-passive üretir) · paylaşımlı ağaçta dal değiştirme · ham hasat repoya girmez
- NOT: yeni oturum promptundaki "52/52 ses" bayat — gerçek **61/61**; Ostinato'nun kendi YENI-OTURUM-PROMPT.md'si daha güncel, onu esas al

## ✅ LİSSOM — KAPANDI
- motion-core/lib (paylaşımlı): `feat/lissom-v3-onayi` @ `05aacaf8`, origin-eşit, temiz — **BU DAL ZATEN MAIN'DE** (`2432fbf`, tur-24 merge'ü; merge istemesi karşılanmış durumda). lissom/app: `main` @ `9cbe8933`, origin-eşit, temiz.
- ⭐ YENİ P0 → KOORDİNATÖR KUYRUĞU: **L-143** — CLI `_deviationsFromConsensus` boş listede ÇÖKÜYOR ve çöküşü "kapı reddi" gibi raporluyor; overhead_reach (artık 6 uygun kaynak!) bu düzelmeden koşulamaz.
- L-135 sessiz-hiçlik ÜRÜN KARARI bekliyor (ölçüm kapısının altındaki kullanıcı hiçbir şey görmüyor — hedef kullanıcı tam o).
- overhead_reach hasadı BİTTİ (9/9; "2/9" bayattı). Devir desenleri: "özellik yazıldı ama hedef yoldan geçmiyor" (6×) + "video-geneli ortalaması yanlış şeyi ölçer" (4×).

## ✅ GRAVITA — KAPANDI
- `main` @ `a951277`, origin-eşit, temiz; merge isteği yok. 69/69 · 17 değişmez · replay 0.
- Squat hasadı BİTTİ: 32/32 → **27 landmark / 16 EĞİTMEN** (2 triyaj reddi, 5×403 — yeniden deneme ZORUNLU DEĞİL: önce ölç, eksikse genişlet).
- İlk iş: diz-simetri dağılımı → eşik → rig identity.kneeSymmetry (status/basis/max BİRLİKTE). Açık: G-044 · G-053 · G-056-ikincil.
- Not: park sayıları anlık bayatlar — yeni oturum önce DİSKİ saysın.

## ✅ JABLAB — KAPANDI
- `main` @ `9d25fa5`, origin-eşit, temiz; merge isteği yok. 77 engine + 29 Flutter, skip yok.
- 10 kural denetlendi + testlere bağlandı; stance artefaktı DOĞRU OLARAK bağlanmadı (kural 7: mirrorConfident=false + kural 8: unattested).
- J-046 AÇIK SORU: kendi aracı "ayna güvenli" derken CLI "değil" diyor — pencere farkı hipotezi doğrulanmadı.
- Kalan: 50-doc derin denetim · awaiting-wiring 5 + surface 1 (ayrı kapılar) · haftalık: cross-3.eğitmen, J-007, J-045. Ders: "yeşil = doğru varsayma".

## ✅ CHOREIA — KAPANDI
- `main` @ `6a8bded` (23 commit push'lu), origin-eşit, temiz; merge isteği yok.
- İlk iş: beat_annotate pivotu (C-032 hareketle ÇÖZÜLMEZ — ölçüldü). RM kuyruğu 2 aday: koşum düzeni ~/motion-harvest/choreia/PARK-DURUMU.md'de (rig /tmp'den koşulmaz!).
- Açık: üç referansta yön belirsizliği (mirrorConfident=false; %10-22 hücre duyarlılığı) · adım-config ↔ referans bağı HİÇ kurulmadı (içerik çoğaltmadan önce kapanmalı) · beşinci-soru vekil-tüketicide (skorlayıcı yok).
- ⚠️ Yabancı süreç bildirimi: pid 51635 transkript-backfill 3 saattir koşuyordu (Ostinato'nun whisper'ı — Ostinato "bitti" dedi; yeni orkestratör sürecin öldüğünü doğrulasın).

## ✅ ORKESTRATÖR (bu oturum) — KENDİ KAYDI
- coordinator-main worktree: motion-core main @ `aa4fbce` (son: katalog kromagram), origin-eşit, temiz; gece zinciri 0.5.1→0.7.2 tag'li.
- ostinato main `1a3c2a4` merge'ü yapıldı (8/8 kapı). Vault yerel-commit'li; DEFTER M-F-53..67 mühürlü.
- YENİ ORKESTRATÖR KUYRUĞU GÜNCELLEMESİ: 1) **L-143 P0 düzeltmesi** (boş-liste çöküşü ≠ kapı reddi — retler İSİMLİ ve SEBEPLİ olmalı) 2) 0.8.0 çevrim-segmentasyonu 3) L-135 ürün-kararı hakemliği 4) J-046 pencere-farkı sorusu 5) bandRadius + 4 iddia 6) adım-config↔referans bağı (Choreia) 7) pid-51635 süreç doğrulaması.
