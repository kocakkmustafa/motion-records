# 🔴 KURUCU KUYRUĞU — Motion ailesi, 2026-08-12 vardiyası

> M-F-77: kurucuya **YALNIZ beş şey** gider — harcama · store gönderimi · nihai fiyat ·
> lisans riski · tasarım yönü. Aşağıda **KARAR** ve **GÖREV** ayrı tutuldu:
> bir görev bir karar değildir, ama kurucudan zaman ister.

## ⚡ EN UCUZ / EN YÜKSEK GETİRİ

| # | kalem | tür | maliyet | getiri |
|---|---|---|---|---|
| 1 | **`salsa_shines` MÜZİK IZGARASI** — `tools/beat_annotate.py` ile bilinen bir parçaya **canlı tap** | **GÖREV** (karar değil) | **~10 dk** | Choreia'nın **tek `live` stili** açılır; 33 çıkmazın 1'i kapanır |

**🔴 BU KALEM BUGÜN KÜÇÜLDÜ SANILDI, SONRA GERİ ALINDI — hem hat hem koordinatör düzeltti:**

**✅ AYAKTA KALAN ÖLÇÜMLER (değerli, ve C-032'yi keskinleştirdi):**
- İki tur **çelişmiyor**: `89-100 × 2 = 178-200` ⊂ `160-220` **ve** `160-220 ÷ 2 = 80-110` ⊃ `89-100` — **her iki yönde tam kapsama**, hesapla
- Deponun **sayma kuralı var ve doğrulandı** (hip_hop: hasat 88–103 ↔ beyan [85,105] örtüşüyor)
- `beats == len(countLabels)` **7/7** tutuyor — **ama yalnız SAYISAL etiketli adımlarda**

**🔴 GERİ ALINAN İDDİA — *"belirsizliğin tamamı `beats`te, beyan yeter"*:**
- `ss_shine_footwork`in etiketleri **harf** (`["a","b"]`), ve adımın **kendi `phases` dizisi** ne olduklarını söylüyor: **`settle_a · transfer_ab · settle_b`** ⇒ ***`a`/`b` müzikal SAYIM değil, kinematik FAZ.*** Düzeni buraya uzatmak, **hiç gözlenmediği bir kategoriye** taşımak olurdu
- 🔴 **Ve deponun KAPALI kaydı bunu zaten söylüyordu — `DEFTER C-032`:** *"salsa'nın quick-quick-slow'unda **3 adım 4 müzikal vuruşa** yayılıyor; adım hissi ile müzikal vuruş **~2× fark eder**"* · `library.json`: ***"hareket-üzerinden BPM ÇIKMAZ SOKAKTI, ÖLÇÜLDÜ"***
- ⇒ Hasat çevrim/dk × `beats` **tam olarak** *"hareket-üzerinden BPM"*dir, ve **o yol ölçülüp kapatılmıştır**: salsa'da adım↔vuruş oranı **3:4**, temiz tamsayı çarpanı **yok**

> ⚠️ **Canlı tap "beyanı doğrula" DEĞİL, hâlâ "MÜZİK IZGARASINI KUR"** — çünkü hareket o ızgarayı **veremiyor**, ve bu **ölçülmüş** (C-032), varsayılmamış. **Kalem küçülmedi.**

## ⚖️ KARARLAR (M-F-77 kapsamında)

| # | kalem | sınıf | not |
|---|---|---|---|
| 2 | **`google_fonts` duruşu** — paketle mi, çalışma-anında indir mi | tasarım yönü | 🔴 **BUGÜN ÜÇ KEZ AĞIRLAŞTI** — aşağıda |

**🔴 `google_fonts` — artık bir "duruş sorusu" değil, ÜÇ AYRI ŞEYİ birden çözen bir karar:**
1. **Duruş** — paketlenmiş mi, çalışma anında mı indiriliyor (mağaza/gizlilik beyanı buna bağlı)
2. **Test blokajı (Gravita)** — soğuk açılış testi `fonts.gstatic.com` reddinde **sahipsiz zone** hatasıyla düşüyor; sözleşme uygulaması **bölünmüş kapıya** zorlandı
3. 🆕 **Kapı çelişkisi (Ostinato, ölçüldü)** — `validate_runtime_fetch` öz-testi `productionFontApiCalls < 1` bekliyor; **font gömülürse öz-test EXIT=1 verir.** Yani *"paketle"* kararı **bugün bir kapıyı kırmızıya düşürür.**
   > ⚠️ Ve bu **kapının kusuru**, kararın değil: ***bir kapı, kendi ürününün ilerlemesini cezalandırıyorsa o kapı ürünün düşmanıdır*** — kapı **sentetikleştirilecek** (koordinatör hükmü), ve **karardan bağımsız** hâle gelecek.

⇒ **Karar hangi yöne çıkarsa çıksın maliyet ölçüldü**; *"paketle"* derse ① ve ② çözülür, ③ zaten düzeltiliyor.
| 3 | **Android release keystore (5/5)** | güvenlik/gönderim | hiçbir hat üretmedi (kasıtlı) |
| 4 | **`AFTER_APPROVAL` (5/5)** — onayda otomatik yayın | store gönderimi | ölçüldü, **canlı** |
| 5 | **Sürüm ayrışması** `0.1.0+1` ↔ ASC `1.0` (4/5) | store gönderimi | **beyan değil, GÖNDERİM BLOKAJI** |
| 6 | **Store listing metni** | store gönderimi | *ölçülmüş boş* (erişilemez değil) |
| 7 | **İkon 5/5 şablon varsayılanı** | tasarım yönü | md5 kimliğiyle kanıtlı |
| 8 | **JDK/Gradle kalıcı düzeltmesi** | — | ⚠️ **VENTURE-ÖTESİ** (LifeOS + Burun Farkı da etkileniyor) |
| 9 | **`garba` + `twerk_reggaeton`** | tasarım yönü | `ruling: open` |
| 10 | **Cihaz geçişi** — üç hâl gerçek cihazda hiç doğrulanmadı | store gönderimi | *kod-gerçeği var, cihaz-gerçeği yok* |
| 11 | **Workspace VCS** | — | ölçüm turları **git izi bırakmıyor** (bugün kanıtlandı) |

## 📊 BUGÜN "BEYAN"DAN "ÖLÇÜLMÜŞ GERÇEĞE" DÖNEN KALEMLER

- ⑤ *"önizleme mi yapalım"* → **"var olan onay yeterli mi"** (Ostinato ölçtü: kullanıcı **zaten** adlı teşhis alıyor)
- ikon → **md5 kimliğiyle 5/5 birebir**
- store metni → **ölçülmüş boş**
- sürüm → **gönderim blokajı**
- `google_fonts` → **test blokajı**

## 🔴 AÇIK, KURUCUYA GİTMEYEN (koordinatörde)

33 çıkmaz sokağın **32'si içerik işi** (A 29 · A′ 3) — aylar sürer, karar değil **kapasite** meselesi.
`hula` (`ruling: held`) · `4BRd2E8vBic` (kimlik açık kalemi) · çekirdek turu (5/5 sözleşme bekliyor).
