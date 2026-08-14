# 🤸 GRAVITA — AJAN DEVRİ (2026-08-13, ölçüm ajanı → oturum)

> **Kurucu kararı:** üretim **oturumların**, ajan değil. Bu not, ajanın ölçtüğü
> ve yaptığı her şeyi oturuma **kayıpsız** devreder.

## 0. MÜHÜR — ölçülmüş, beyan değil

| | |
|---|---|
| **Depo** | `ventures/gravita/app` · **HEAD `5d06d60`** · ağaç **temiz** · push-bekleyen **0** · toplam commit **193** (`rev-list --count HEAD`, G-197 SONRASI ölçüldü) |
| **Kapılar** | `./tools/run_all_gates.sh` → **çıkış 0** · app **175/175** · engine **175/175** · python **15/15** |
| **Defter** | `workspace/DEFTER.md` (git İÇİNDE — 2026-08-15, `app/workspace/`) · son kayıt **`G-197`** |
| **Bu turda commit** | `2eac339` (G-196) · `5d06d60` (G-197) — ikisi de **push'lu** |

⚠️ **İki commit ürün koduna DOKUNMADI** — yalnız `tools/defter_freshness.py`.
Ürün yüzeyi bu turda **değişmedi** ve bu bilinerek böyle.

---

## 1. ⛔ KOORDİNATÖRÜN İKİ VARSAYIMI BAYAT — düzeltiliyor

Kapanış sevki *"A6'da nereye geldin"* ve *"DEFTER `G-195` kusuru **düzeltilmedi**,
adıyla devrediyor"* diyordu. **İkisi de artık doğru değil:**

- **A6 iki yönlü kapı → BİTTİ**, sabotajla kanıtlandı, commit'li, push'lu.
- **`G-195` kayıt kusuru → DÜZELTİLDİ** (`176/176` → `175/175`, silinmeden,
  gerekçesiyle).
- **`G-999` tautolojisi → KAPANDI** (yeri aşağıda, tam satırlarıyla).

> ***Bir devir notunun ilk işi, devredenin bildiğiyle devralanın sandığı
> arasındaki farkı kapatmaktır.***

---

## 2. A1–A12 MESAFE ÖLÇÜMÜ — turun ana çıktısı

| # | durum | özet kanıt |
|---|---|---|
| **A1** | ⛔ **yok** | Uçtan uca akış YOK. `NavigatorObserver` depoda hiç kullanılmıyor (tek isabet `reachability_test.dart:91`, *"denedim ve düştü"* yorumu). Ölçüm **kasıtlı bölünmüş**: kapı-1 `GravitaShell`den başlıyor (`:127`), kapı-2 kabuğa geçmeden duruyor (`onboarding_reach_test.dart:62-65`). **Sebep: B5** |
| **A2** | ⛔ **yarım** | Onboarding var; çıkış **düğmeyle** kanıtlı ama **yalnız ARIZALI depo** dalında (`onboarding_launch_path_test.dart:110-141`, `supportPath: null`). SAĞLAM depoda kabuğa varan iki test de **`markComplete()` ile bayrak set ediyor** (`shell_end_to_end:266→271` · `onboarding_launch_path:68→70`) — A2'nin yasakladığı yol. Payda: 7 `bootGravitaRoot`, yürüyerek kabuğa varan **1**, o da arızalı |
| **A3** | ⛔ **oran yok** | `sessiz oran`/`boş yüzey` → 338 takipli dosyada **0** (pozitif kontrol `sessiz` → 98 dosya). **Şerh:** içerik yüzeyinde **paydalı süpürme VAR** (`library_surface_test.dart:924-937`). Eksik olan: 9 yüzey üstünden **paydalı sessiz-oranı** |
| **A4** | ⛔ **yok** | `çıkmaz sokak` → **1 isabet** (tek çıkmazın *yasaklanması*, sayım değil). A/B/C/D dağılımı ve payda yok |
| **A5** | ✅ | `run_all_gates.sh` **çıkış 0**, borusuz. 175/175 · 175/175 · 15/15 |
| **A6** | ✅ **(bu turda kapandı)** | İki yönlü, sabotaj 5/5, öz-test 7/7 — §3 |
| **A7** | ⛔ **2 tam · 2 kısmi · 1 yok** | metne karşı ilk kez ölçüldü — §4 |
| **A8** | ✅ | `flutter build ios --release --no-codesign` → çıkış 0. `Runner.app/PrivacyInfo.xcprivacy` **pakette**, md5 depo == paket (`aead2c42…`) |
| **A9** | ✅ | `network_claim_audit` çıkış 0 borusuz · öz-test **6/6** · 63/63 paket sınıflandırılmış |
| **A10** | ⛔ **20/20 ŞABLON** → **B tablosuna taşındı** | Android 5/5 + iOS 15/15 Flutter varsayılanıyla birebir. ⛔ **Dokunma** — kurucu direktifi (M-F-77, tasarım yönü) ölçüt metnini yener |
| **A11** | ✅ **iki platform** | iOS `--no-codesign` çıkış 0 · Android `ORG_GRADLE_PROJECT_allowDebugSigning=true flutter build apk --release` çıkış 0 (88.7MB). Düz `flutter build apk` **kasıtlı keystore kapısına** düşüyor = **B1**, A11 değil |
| **A12** | ⛔ **yok, ama DONANIM VAR** | `flutter devices` → **gerçek iPhone bağlı** (`00008120-001804D83E13C01E`, iOS 26.6). Koşum kanıtı 338 dosyada **0**. Ön-girdinin *"donanım yok"* tahmini **YANLIŞTI**. A1'e bağımlı |

---

## 3. A6 — NE YAPILDI, tam yeriyle

### 3.1 `G-999` TAUTOLOJİSİ — tam yeri ve kapanışı

**ESKİ kusur** (`tools/defter_freshness.py`, G-194 hâli, satır **131-134**):
öz-test sentinel'i `git grep -l "G-999"` ile kanıtlıyordu — **ama aranan dizge
aracın KENDİ kaynağındaydı**: satır **25 · 130 · 132 · 134**.

**Ölçüm:** `git grep -l G-999` → **2 dosya**, biri `tools/defter_freshness.py`
**kendisi**. ⇒ `sentinel_in_repo` yarısı **hiçbir koşulda yanlış olamazdı**;
dış fikstür (`docs/KAPI-ENVANTERI.md`) silinse bile **geçerdi**.

> ***Bir denetim iki tarafı aynı kaynaktan okuyorsa TANIMDIR — ve bir tarafını
> KENDİNDEN okuyan denetim, tanımın en sessiz hâlidir.***

**Panzehir (iki parçalı, `5d06d60`'ta canlı):**
1. `SENTINEL_RANGE = range(900, 1000)` — **liste değil ARALIK**; dışlamanın
   çalıştığı **sentetik girdide**, depoya hiç bakmadan kanıtlanıyor (öz-test ④).
2. Dış çapa artık **kendi kaynağını DIŞLAYARAK** aranıyor (öz-test ⑤) ⇒
   fikstür silinirse **öter**. Ölçüldü: ham grep **2**, kendini dışlayan **1**.

### 3.2 İKİ YÖN, İKİ DESEN — ve ham ters yön neden **128 sahte gedik**

| yön | desen | gerekçe |
|---|---|---|
| **EKSİK** (commit→defter) | **ÇAPALI** `^G-NNN` | *"bkz. G-104"* diyen commit G-104'ü **yazmış sayılmamalı** — sözünü etmek ≠ kayıt |
| **ÖKSÜZ** (defter→commit) | **GENİŞ** `\bG-NNN` | gövdedeki anma **bir bağdır** |

**Ölçüm:** çapalı desenle ters yön **128 sahte öksüz**; geniş desenle **23**.
Genişliğin etkisi iki yönde **ZITTIR** — bu yüzden tek desen olamaz.

### 3.3 Ters yönün BİRİMİ — türetildi, elle liste yazılmadı

*"Kod değişikliği İDDİA eden kayıt"* = **defterin kendi TÜR sütunu**:
`görev` iddia eder · `bulgu`/`risk`/`karar`/`ders` **etmez**
(ölçüldü: görev 51 · bulgu 49 · risk 12 · karar 10 · ders 4).

**Sabotajla kanıtlandı:** aynı numara `görev` türüyle → **öttü**;
`bulgu` türüyle → **sustu**. ⇒ birim gerçekten **türden** geliyor, numaradan değil.

**🔒 M-F-588 ÖNCE ölçüldü:** `holding/bin/sensor-defter.py` bu defteri
**venture DIŞINDAN** okuyor (`ventures/*/workspace/DEFTER.md`), satır deseni
`^\|\s*([A-Z]{1,3}-\d+…)\s*\|` ve *"kapalı"*yı **dizge taramasıyla** buluyor.
⇒ Bu kapı biçime **hiçbir alan EKLEMEDİ**, zaten var olanı okudu.

> 📌 **Yan bulgu, düzeltilmedi (holding kalemi):** `sensor-defter.py:60`
> `low = rest.lower()` ile *"kapalı"* arıyor. Python'da `"KAPALI".lower()` →
> `"kapali"` (noktalı i) ≠ `"kapalı"` (noktasız ı). ⇒ **BÜYÜK HARFLE yazılmış
> "KAPALI" kayıtları kapalı sayılmıyor.** Gravita'nın kalemi değil, **adıyla
> devrediyor.**

### 3.4 Bugünün borcu — ADIYLA, gizlenmedi

- **bağı kopuk `görev` 9:** G-010 · 084 · 092 · 093 · 098 · 118 · 122 · 123 · 128
- **türsüz prose 8:** G-167 · 171 · 172 · 173 · 174 · 177 · 179 · 180

Taban **bugün ölçülen sayının kendisi** (G-187'nin `6→7` deseni). **ALT KÜME**
olarak sınanıyor: **büyürse öter, küçülmesi serbest** — ve küçülme
*"⭐ BORÇ ÖDENDİ"* diye **raporlanıyor** (bkz. §3.6).

**⭐ Ters yön ilk koşumda GERÇEK kusur buldu:** `G-179` defterde
*"planche_lean_deg adlandırıldı"* diyor; işin commit'i **var** (`9763da8`) ama
başlığında **numara YOK**. İleri yön bunu **yapısal olarak göremez.**

### 3.5 `DEFTER G-195` kayıt kusuru — **DÜZELTİLDİ**

Beyan **`app 173→176/176`**, ölçüm **175** (JSON reporter: geçen 175 · düşen 0 ·
atlanan 0). **Silinmedi**, gerekçesiyle düzeltildi (`workspace/DEFTER.md`,
G-195 kaydının altında `⚠️ DÜZELTME (G-196)` bloğu).

### 3.6 🪤 G-197 — kendi kapıma M-F-598'i yazdım

G-196'yı commit'ledikten **saniyeler sonra** öz-testim düştü: borç tabanını
**EŞİTLİKLE** sınıyordum, G-196'nın commit **mesajı** G-179'u andı → bağ
kuruldu → borç 8→7 düştü → **iyileşme kırmızı bastı.**

> ***Bir kusuru BAŞKA bir yerde adlandırabilmek, onu KENDİ yazdığında
> tanıyacağın anlamına gelmez — teşhis, bağışıklık değildir.***

> ***Bir kapının girdisi, o kapıyı taşıyan commit'in KENDİSİYSE, kapı kendi
> doğuşuyla durum değiştirir — commit ÖNCESİ yeşil geçerli değildir.***
> ⇒ **Bu araç değişince commit'ten SONRA da koş.**

---

## 4. A7 — sözleşmeye karşı, madde madde (⛔ 2 tam · 2 kısmi · 1 yok)

Canlı sayılar: **KATI 4** · **GEVŞEK 7** · ulaşılamayan **1** · aday **9** ·
soğuk açılış payı **1**. Denklem **7 ⊎ 1 ⊎ 1 = 9** ✓

- **(a) KISMİ** — türetiliyor (`reachability_contract.dart:25-37`), ama
  *"iki bağımsız türetimin uzlaşması"* **YOK**: tek kanal, **ad tabanlı**.
  Şerhin kaynağı **Gravita'nın kendi bedeli** (M-F-575) ve ikinci kanal hâlâ
  kurulmadı. ⚠️ `Directory('lib/app').listSync()` **özyinelemesiz** — bugün
  zararsız (`lib` altında yalnız `lib/app`), alt klasör açılırsa **sessizce**
  eksilir.
- **(b) KISMİ** — yürüyüş gerçek (rota doğrudan çağrılmıyor), ama **tanık
  `NavigatorObserver` DEĞİL**, `canPop()` derinliği. Metnin şerhi (M-F-582)
  *"adı değil OLAYI say"* diyordu; Gravita **tanığı terk etti**. Ayrıca
  KATI'daki **`+1` beyansız kök varış** (`:223`/`:258`) — Ostinato'nun
  `arrival: push|root` çapası burada yok.
- **(c) KISMİ** — ayrı kova ✓, sebep **bugün DOĞRU** (ölçüldü:
  `ContentFailureScreen` yalnız `gravita_app.dart:119` sistem dalından, kullanıcı
  kontrolüyle push eden yer **yok**) ama sebep **ÖLÇÜLMÜYOR** — doc-comment
  düzyazısı, her koşumda türetilmiyor.
- **(d) ✅ TAM** — assert var (`:264-270`), **iki taraf ayrı kaynaktan**, denklem
  **kapılar ARASINDA** (Gravita'nın M-F-578 bedeli ödenmiş), vakum korumalı.
- **(e) ⛔ YOK** — elle küme **silinmiş**, rütbesi düşürülmemiş
  (`reachability_contract.dart:18-19` açıkça *"elle liste YOK"*). **İki zorunlu
  şerhin İKİSİ de yok.** 4 katmanlı, Türkçe-güvenli (`re.IGNORECASE`) pozitif
  kontrolle ölçüldü.
- **③ KISMİ** — kapı-2 uygun (taze dizin, düğmeyle), ama **kanonik sayı
  kabuktan başlıyor**; iki kapıyı birleştiren köprü (§A2) **yok**.

---

## 5. SIRADAKİ SOMUT ADIM — dosya + satır

**① A7 (e) — elle kümeyi geri koy (rütbe düşürerek).** En ucuz `⛔→✅`, tek
dosya, ürün koduna dokunmaz.
- **Dosya:** `ventures/gravita/app/test/support/reachability_contract.dart`
- **Yer:** satır **18-19**'daki *"elle liste YOK"* ifadesinin yerine
  `knownFloor` sabiti + `declaredScreens()`in onu **kapsadığını** sınayan assert
  (`test/reachability_test.dart` içine, `:118` civarına).
- **İki ZORUNLU şerh** (Lissom M-F-577, Ostinato'da yarısı eksikti):
  *"bu küme bir **ALT SINIRDIR, tam envanter DEĞİLDİR**"* ve *"buraya ekleme
  **envanter güncellemesi değil, KONTROLÜN TABANINI yükseltmektir**"*.
- **Çalışan örnek:** Ostinato ve Choreia'daki `knownFloor` / `handWritten`.

**② A7 (a)** ikinci türetim kanalı (YAPI: `Scaffold(` kuran sınıf) — ayrışırsa
kapı ötsün · **(b)** `+1` kök varışın beyanı · **(c)** sebebin koddan türetilmesi.

**③ A4** — `reachability_test.dart` **zaten yürüyor**; çıkmaz sokak o
yürüyüşten türetilebilir. **④ A3** aynı yürüyüşe biner.

**⛔ Açma:** **A2 · A1 · ③** → **B5'e bağlı** (üç panzehirin ikisi zaten
reddedildi, üçüncüsü zinciri koparan bölme). **A10** → B tablosunda, dokunma.
**A12** → A1'e bağımlı, donanım hazır.

---

## 6. REFERANSLAR — nereye bakılacak

| ne | nerede |
|---|---|
| **İki yönlü A6'nın referansı** | `ventures/ostinato/app/tools/defter_freshness.py` — payda **denklemi** (`commit_census()`), **tavan/uçuş** türetimi, `KNOWN_EMPTY` ↔ `PRE_COMMIT_ERA` **ayrı torba** gerekçesi, sentinel `9xx` aralığı |
| **Gravita'nın yeni A6'sı** | `ventures/gravita/app/tools/defter_freshness.py` (`5d06d60`) |
| **Sözleşme metni** | `ventures/motion-core/workspace/GEZILEBILIRLIK-SOZLESMESI.md` |
| **Ölçüt** | `ventures/motion-core/workspace/YAYIN-HAZIRLIK-OLCUTU.md` |
| **Önceki devir** | `ventures/motion-core/workspace/devir/03-GRAVITA.md` |

---

## 7. DEVREDEN AÇIK KALEMLER (yapılmadı, adıyla)

1. **`metric_support` M-F-598 hükmü** — `tools/metric_support.py:141-142`,
   `if "planche_lean_deg" not in named_gaps: fail` **canlı KUSURA dayanıyor**;
   metrik uygulanınca kapı kırmızı olur. Hüküm verildi, **uygulanmadı**.
   Ailenin diğer 4'ü ölçüldü ve **üçü farklı sınıf** çıktı (`knee_angle` sağlıklı ·
   `feet_off_ground`×2 bakım-zorlayıcı · `http` sağlıklı).
2. **`sensor-defter.py:60` Türkçe `.lower()` körlüğü** — holding kalemi (§3.3).
3. **Borç tabanı daraltılabilir:** `G-179` ödendi; `KNOWN_UNLINKED_UNTYPED`
   sabiti hâlâ 8 numara taşıyor (kapı bunu **raporluyor**, kırmızı yapmıyor).
4. **A7 (a) özyineleme sınırı** — `lib/app/` altına klasör açılırsa envanter
   sessizce eksilir.

---

## 8. ÖLÇEMEDİKLERİM — adıyla

- **Cihazda koşum**: donanım bağlı ama koşulmadı (A1 akışı yok; kurulum
  codesign ister). *"Koştu mu"* → **ölçüldü: hayır.** *"Koşarsa ne olur"* →
  **ölçülmedi.**
- **A3/A4'ün gerçek sayıları** — ölçümün **yokluğunu** ölçtüm, değerini değil.
- **Paketteki ikon** — `.app` içindeki ikonu şablona karşı ölçmedim (depo 20/20
  varsayılan olduğu için paket de öyle olmalı, ama bu **çıkarım**).
- **`google_fonts`un cihazdaki gerçek ağ davranışı** — kod düzeyinde uyumlu
  (A9), cihazda paket yakalama yapılmadı.
- **engine 175/175'in kapsamı** — yeşil olduğunu ölçtüm, **neyi kapsadığını** değil.

> ***Bir doğrulamanın kapsamı, doğrulayanın ÇALIŞTIRABİLDİĞİ kadardır.***
