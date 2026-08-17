# 📏 MAĞAZA ALAN LİMİTLERİ — aile katmanı, TEK otorite

> **Neden tek dosya:** beş hat aynı tabloyu beş kez yazarsa beş kez bayatlar. Limit değişirse
> **burası** değişir; hatların kapısı **buraya** bakar, kendi kopyasına değil.
> Oluşturma: 2026-08-17 (tur-2, orkestratör) · dayanak: `M-F-748` / `H-78`

---

## ⚠️ ÖNCE PROVENANS — bu sayılar bizim ölçümümüz DEĞİL

Aşağıdaki limitler **platformun belgelediği** değerlerdir; biz onları ölçmedik, **devraldık.**
Gerçek otorite **yükleme anıdır**: ASC ve Play kendi limitlerini kendileri uygular ve
aşan değeri **reddeder**.

> ### ***BU TABLO BİR ÖN-KONTROLDÜR, BİR OTORİTE DEĞİL. TABLO YANILIRSA MAĞAZA HAKLIDIR.***

⇒ Bu yüzden kapı mesajı *"limit aşıldı"* değil, ***"belgelenmiş limiti aşıyor — yükleme
reddedebilir"*** demeli. Bir ön-kontrolün kendini otorite gibi konuşturması, `H-33`ün
(*D-kararları otorite değil iddiadır*) mağaza katmanındaki hâlidir.

📌 Bir limit yanlış çıkarsa: **burayı düzelt, gerekçesini yaz, tarih at.** Hatların kapısı
kendiliğinden düzelir.

---

## 📐 LİMİTLER

### App Store (ASC)
| alan | limit | not |
|---|---|---|
| `appStore/name` | **30** | görünen ad |
| `appStore/subtitle` | **30** | |
| `appStore/promotionalText` | **170** | inceleme olmadan güncellenebilir |
| `appStore/keywords` | **100** | **virgüller dâhil**, tüm dize |
| `description` | **4000** | |

### Google Play
| alan | limit | not |
|---|---|---|
| `playStore/title` | **30** | ⚪ **OPSİYONEL** — yoksa `appStore/name` kullanılır (aşağıya bak) |
| `playStore/shortDescription` | **80** | 🔴 en dar limit — en çok burası taşıyor |
| `description` (full) | **4000** | |

### 🔗 URL ALANLARI — **2026-08-17'de eklendi** (`H-83`; beş listing'in beşinde de yoktu)
| alan | zorunlu mu | not |
|---|---|---|
| `supportUrl` | 🔴 **ZORUNLU** | **Apple bunsuz gönderim kabul etmiyor.** URL'in **gerçekten açılması** gerekir — uydurulmaz. |
| `marketingUrl` | ⚪ opsiyonel | |

⚠️ **Değeri hat SEÇMEZ** — hangi adres olacağı kurucu/altyapı kararıdır (ailede emsal:
`braavolabs.com/support`). Karar gelene kadar alan **boş bırakılmaz, YAZILMAZ**; kapı onu
*"eksik"* diye kırmızı yakar ve bu **doğru** davranıştır.

### 🏷️ `appStore/name` — **ASC'deki CANLI adla eşleşmelidir** (`H-83`)
`listing.json`daki ad, App Store Connect'te o an **yayında olan** adla aynı olmalı; farklıysa bu
bir **iddia farkıdır** ve `$why` ile açıklanır ya da **düzeltilir**. 2026-08-17 ölçümünde
**beşi de ayrışıyordu**; en ağırı 🤸 Gravita (`Rep Counter` ↔ `Skills & Strength` — konumlandırma
farkı, yazım değil).
⛔ **Adı hat değiştirmez** — marka kimliği kurucunun (`KURUCU-PAKETI §3`).

#### ⚖️ `playStore/title` KARARI (orkestratör, 2026-08-17 · `M-F-750`)
**Play başlığı `appStore/name`den türetilir.** Alan listing.json'da **zorunlu değildir**;
yoksa yükleyici `appStore/name`i kullanır.
- 🎯 **Gerekçe ölçüldü:** dört listing'in **üçünde** alan yok (JabLab · Ostinato · Choreia),
  Gravita'da var ve değeri `appStore/name` ile **birebir aynı dize**. `playStore` anahtarını
  okuyan **hiçbir kod yok** (beş depoda tarandı, pozitif kontrollü).
  ⇒ Alan bir **kopya**dır, ve kopya bir **güncelleme borcudur** (`H-58`): ad değişirse iki yer değişmeli.
- ✅ Farklı olmasını **istiyorsan** alan **yazılır ve `$why` taşır** — sessiz sapma yok.
- 🔄 **Geri alınabilir:** karar yanlışsa alan tek satırla geri konur.

---

## 🚪 KAPI SÖZLEŞMESİ — her hat kendi deposunda kurar

Kapı **kalıp değil gerekçe** taşır (`H-74`): aşağısı *ne ölçüleceği*, *nasıl yazılacağı* değil.
Gravita `tools/validate_store_listing.py`, JabLab `test/store_listing_test.dart` kullanıyor —
ikisi de meşru; hat kendi biçimini seçer.

**Ölçülecek üç şey:**
1. **Uzunluk** — yukarıdaki her alan için `len(str)`; aşarsa **KIRMIZI**.
2. **Varlık** — zorunlu alan **eksikse** kırmızı. ⚠️ *"Yok"* ile *"boş"* ayrı yazılır
   (`H-73`: boş bir alan "yok" ile "bakılmadı"yı ayırt ettirmez).
3. **`$` sözleşmesi** — `$` ile başlayan anahtar **gönderilmeyen** kalemdir (gerekçe/metadata).
   Sevk edilen bir alan `$` taşımaz; sevk **edilmeyen** bir blok `$` taşır.
   Emsal: `$ageRating` (`O-157`) — yaş-derecesi anketi **serbest metin almaz**, dolayısıyla
   o blok gönderilen bir alan değildir.

### ⚠️ VE KAPININ KENDİSİ SINANIR (aile standardı, `M-F-652`/`H-62`)
- **pozitif ikiz** — bugünkü doğru metin sessizce geçmeli
- **sabotaj** — limiti 1 karakter aşan metin **yakalanmalı**
- **vakum** — alan/desen **tamamen kaybolursa** kapı sessizce geçmemeli, **kör olduğunu söylemeli**

---

## 📊 2026-08-17 ÖLÇÜMÜ — kapı doğmadan önceki hâl (tarihsel, güncellenmez)

Üç listing yan yana okundu (`H-58`), limitler elle ölçüldü:

| alan | limit | 🤸 Gravita | 🥊 JabLab | 🥁 Ostinato |
|---|---|---|---|---|
| `appStore/name` | 30 | 20 ✓ | 6 ✓ | 8 ✓ |
| `appStore/subtitle` | 30 | **30** ✓ | 22 ✓ | 27 ✓ |
| `appStore/promotionalText` | 170 | 152 ✓ | 142 ✓ | 140 ✓ |
| `appStore/keywords` | 100 | 85 ✓ | 94 ✓ | **100** ✓ |
| `playStore/title` | 30 | 20 ✓ | 🔴 **YOK** | 🔴 **YOK** |
| `playStore/shortDescription` | 80 | 76 ✓ | 76 ✓ | 🔴 **92** |
| `description` | 4000 | 1565 ✓ | 1576 ✓ | 1411 ✓ |

⚠️ **İki alan limitin TAM ucunda** (Gravita subtitle 30/30 · Ostinato keywords 100/100) —
tek karakterlik bir düzenleme onları kırmızıya çevirir. Kapı doğduğunda bu ikisi
**en hassas** kalemler olacak.
