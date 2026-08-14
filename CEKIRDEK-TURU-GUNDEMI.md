# Çekirdek Turu — Gündem (2026-08-12 ölçümleriyle)

> **Durum: AÇILMADI.** Ön koşul hazır, ama tur bugün açılmadı — gerekçe §4.
> Kanonik sözleşmeler: `~/motion-worktrees/coordinator-main/docs/`
> ⛔ `ventures/motion-core/lib/tools` hiçbir kipte kaynak değil (19↔32 araç sapması).

## 1. Sıralama ölçütü

***Terfi sırası hatanın ciddiyetiyle değil, KAÇ HATTIN BAĞIMSIZ ÖDEDİĞİYLE belirlenir.***
Ve terfi eden **kilit değil GARANTİ**: sözleşme + isteğe bağlı ortak primitif, **mecburiyet değil**.
Gerekçe (C-195): kilidi zorunlu kılan bir çekirdek API, **gerekmediğini ölçerek kanıtlamış** bir hatta maliyet dayatır.

## 2. Kuyruk

### Önceki vardiyadan (5)
| # | kalem | yayılım | not |
|---|---|---|---|
| 1 | **C-195 kapanış garantisi** | **4/5 + 1 belgeli muafiyet** | Lissom ölçtü, *"bende yok"*, kilit yazmadı — muafiyet terfinin ŞEKLİNİ belirledi |
| 2 | ~~`worldLandmarks`~~ | **0/5 — TERFİ ADAYI DEĞİL** | 🔴 **2026-08-12 DÜZELTMESİ:** `worldLandmark*` **hiçbir ağaçta yok** — kanonik çekirdek **0** (pozitif kontrol `PoseLandmark` **21** dosya, negatif 0) · beş hat da **0**. **Terfi edecek kod YOK** → bu bir *terfi* değil **YENİ ÇEKİRDEK YETENEĞİ TALEBİ**; maliyeti ve kararı bambaşka. Eski *"2/5, delta world %95 ↔ 2D %90"* satırı bir **ölçüm/karşılaştırma bulgusuna** işaret ediyor, mevcut bir uygulamaya değil. ⚠️ **JabLab KARŞI-ÖLÇÜM verdi:** `PoseLandmark` **zaten `z` taşıyor** ama JabLab `.z`yi hiç okumuyor → *"ölçümüm saf 2D, ve bu eksiklik değil SEÇİM"* — 2/5'e üçüncü olarak **eklenmeyi reddetti** (C-195'te Lissom'un rolü) |
| 3 | pencere-koşulu | 🔴 **3/5 DEĞİL: 2 uygulama + 1 KISMİ** | **2026-08-12 düzeltmesi (Lissom kendi payını indirdi):** Gravita **korelasyon** (hip-knee Pearson) · JabLab **oran** (`withValidAnalysisRatio`) · **Lissom ŞEMAYI TAŞIYOR, MOTORU BAĞLAMADI** — bağlantı **bilerek** yarım (gerçek fixture'ı noise-sensitivity'den kırdığı **ölçüldü**, geri alındı; hüküm: *mekanizma, politika değil*). ⛔ Yayılım yazılırken *"Lissom uyguladı"* **denmez.** ⚠️ **ŞEKİL RİSKİ (kısıt #7):** üç hat üç FARKLI koşul türü kullanıyor |
| 4 | `SessionRecord.workedSeconds → int?` | JabLab | **J-161'i ifade edilebilir kılar** — yeni karar değil |
| 5 | kamera önizleme / texture | **2/5, AYNI SINIF** | 🔴 **2026-08-12 DÜZELTMESİ:** *"hiç ölçülmemiş"* **yanlıştı.** JabLab: `Texture(`/`textureId`/`registrar.textures` **0** (poz kontrol `motion_camera\|CameraSession` 9 satır) — **ama yokluk SESSİZ DEĞİL:** `skeleton_overlay.dart:13` `PLACEHOLDER(asset)` + `unblocked by:` işaretçisi taşıyor (kapı: `unblocked by` yoksa exit 1); sınıf **ERTELENMİŞ** (*yapılabilir, biz yapmadık*; yüzey sorumluluğu üstleniyor, tarih vermiyor). ⭐ Ve `skeleton_overlay.dart:17-21` **Gravita'yla hizalanmayı ZATEN kayda geçmiş** (aynı `motion_camera` pini, aynı `registrar.textures` yolu, aynı sınıf) — gerekçesi yazılı: *iki hattın farklı sınıflandırması, tek bir kısıtın iki farklı şeymiş gibi okunmasına yol açardı.* 📌 Çizilen sahte değil: iskelet **gerçek landmark'lardan** çiziliyor, placeholder olan yalnız kamera görüntüsü |

### 2026-08-12'de eklenen (4, hepsi ölçülü)
| # | kalem | yayılım | referans uygulama |
|---|---|---|---|
| 6 | **tutuş-süresi primitifi** | **3/5** | **Gravita `HoldEngine`** (`EngineType.staticHold`, `holdDurationUs`, `minHoldUs`, testli) · Lissom `holdSeconds` · JabLab config'te var, üretici yok |
| 7 | **olay sayısı kalıcılığı** | 2/5 ödedi | 🔴 **2026-08-12 DÜZELTMESİ (Gravita ölçtü):** *"Gravita `repCount` **serileştirilmiyor**"* **YANLIŞTI** — `live_session.dart:154` `unitsCompleted: state.repCount` ile **serileştiriliyor**. Koordinatörün hatası: `repCount` yalnız `*session_record*`/`*session_store*` **dosya-adı deseninde** arandı, gerçek yazım başka dosyadaydı → *kapsam* hatası (M-F-522'nin koordinatördeki tekrarı). ✅ **Eksik olan bir ALAN değil, o alanın NULLABLE olmaması.** Ve ihtiyacın kanıtı Gravita'nın **kendi kodunda yazılı**: `workedSeconds: worked < 0 ? 0 : worked` satırının yanında *"negatif süre yazılmaz… 0 yazmak daha dürüst"* diyor — ***`int?` olsaydı orada `null` yazardı***; bugünkü `0`, *"ölçtüm ve sıfırdı"* ile *"ölçemedim"*i birleştiriyor. → **#4 ile TEK KALEM** |
| 8 | **izin/gizlilik metni kapısı** | **4/5** | Ostinato yazıyor · **Lissom tek temiz hat** |
| 9 | **"dürüst hâl ekranı bir EYLEM taşır"** | **4/5** | Ostinato uygulamış · **üç ayrı şiddet**, aşağı bak |
| **10** | **`SessionRecord` DEĞER + BANT** *(Lissom ⑨)* | **1/5** | 🔴 **2026-08-12: Ostinato bu satırın EKSİK olduğunu ölçtü** — kalemin §2b'de **numarası** vardı, kuyrukta **tanımı yoktu** (`\| 10 \|` 0 isabet, pozitif kontrol `\| 9 \|` → 1). ***Koordinatörün belge kusuru.*** **TANIM:** `BatterySummaryView` → `BatterySummary.from` **ölçülen DEĞER + BANT** istiyor; `SessionRecord` **ikisini de taşımıyor** ⇒ ***özet geçmişten YENİDEN KURULAMIYOR*** ve yüzey bağlanamıyor. Lissom yüzeyi bağlamayı **reddetti** (*"12 testin 1 satırını 'Assessment Battery' başlığıyla sunmak, bataryanın koşulduğunu ima ederdi"*). **#4/#7 ile AYNI DOSYA, aynı değişikliğin üçüncü yarısı** — hattın kendi sözü: *"ayrı kalem sayılmamalı, yayılım 1/5, **ŞİŞİRME**"*. **Gravita: kapsam dışı ama YÜKLÜ** (form notu açıldığı gün birebir Lissom'un durumuna düşer) · **Ostinato: karşı-ölçüm** (`SessionRecord`ı hiç kullanmıyor) |

**#9'un üç şiddeti — tek kelimeye çökertilmez:**
- **Choreia** — gerçek **ölü düğme** (devre dışı kontrol) → kapatıldı
- **Lissom** — düğme **çalışıyor**, kusur *oraya giden yolun yokluğu* → kapatıldı
- **JabLab** — **eksik eylem** (bilgi tam: çıkışı adıyla veriyor + dürüst yedek söylüyor); *"Tekrar dene"nin yokluğu KASITLI ve doğru* (J-079)
- **Gravita** — **ölçülmedi**, kalıcı-ret dalını hiç işlemiyor olabilir

## 2b. Turun HAT BAŞINA getirisi — ölçüldü (2026-08-12), ve turun ZAMANLAMASININ asıl girdisi

| hat | tur ne getiriyor |
|---|---|
| **Lissom** | ⭐ **ÜÇ KAPI AÇIYOR** — ④+⑦+⑩, *"bugün ifade edilemeyen üç olgu"*; ⑥⑧ zaten canlı; ①②③ açmaz |
| **JabLab** | **yetenek verir, KAPI AÇMAZ** — 16/16 kapı tüketicisiz; darboğazı çekirdek değil kendi tüketicisi |
| **Gravita** | ④+⑦ **güçlü destek** (kendi kodunda kanıt yazılı) · ①③⑥ **tasarım şartlı** destek |
| **Ostinato** | ⏳ değerlendirme koşuyor (⚠️ `SessionRecord`ı **hiç kullanmıyor** — ölçüldü; üç kalem onu bağlamayabilir) |
| **Choreia** | ⏳ hasattan dönmedi |
> ***Aynı tur, aynı kalemler, hatlara farklı getiri.*** Turu açma kararı bu tablodan okunur — *"herkes için aynı ölçüde değerli"* varsayımı **ölçümle çürüdü.**

## 2c. Yayılım düzeltmeleri (hatlar kendi paylarını İNDİRDİ)
- **#2 `worldLandmarks`** → **1 ölçülmüş ihtiyaç + 2 karşı-ölçüm**: **Gravita** gerçek (*eşik **world** uzayında türetildi, üründe **2D** uygulanıyor* → %95→**%90**, 27/30, **muhafazakâr yön**: yanlış kabul yok, **3 gerçek tekrar reddediliyor**) · **JabLab + Lissom** karşı-ölçüm (*2D bir **SEÇİM***; `.z` okuma 0).
- **#7 olay sayacı** → kalem **İKİYE ayrılıyor**: `workedSeconds→int?` **3/5** (Lissom+JabLab+Gravita) · **olay sayacı 2/5** (JabLab+Gravita; Lissom'da `repCount`/`eventCount` **0 dosya**).
- **#5 kamera önizleme** → **2/5 aynı sınıf DEĞİL:** JabLab **ERTELENMİŞ** (beyanlı: `PLACEHOLDER(asset)` + `unblocked by:` + kapı) · **Lissom SESSİZ** (hiçbir yüzey yokluğu söylemiyor — *kendi aleyhine bulgu*, kapatma sevk edildi).
- **#10 (yeni, Lissom ⑨)** `SessionRecord` **değer+bant** → yayılım **1/5**, ve hattın kendi sözü: *"ŞİŞİRME; §3.2 mantığıyla #4/#7 ile **aynı dosya, aynı değişikliğin üçüncü yarısı**, ayrı kalem sayılmamalı."*

## 3. Bağlayıcı tasarım kısıtları (hatlardan çıktı, tartışmaya kapalı)

1. ⛔ **Sayaç NULLABLE girer.** `int = 0` olarak eklenirse `unmeasuredUnits`'in sessizliğini **yeni bir alanda** yeniden üretir — *"ölçtük, yoktu"* ile *"hiç izlemedik"* ayırt edilemez hâle gelir, **ve bu sefer beş hat birden devralır.** (JabLab, M-F-519)
2. ⛔ **#4 ve #7 aynı dosyada ve aynı değişikliğin iki yarısı** — ayrı kalem sayılmaz.
3. ⛔ **Terfi eden kilit değil GARANTİ** — üç kez uygulandı (C-195 · izin-metni kapısı · #9).
4. ⛔ **Anahtar/kapsam TÜRETİLİR, elle liste TUTULMAZ.** İki bağımsız vaka: Gravita'nın tek-dosya kapsamı yanlış bulgu üretti · JabLab'ın alan-beyaz-listesi üçüncü yüzeyi kaçırdı.
5. ⛔ **#8'in kapsamı plist ile sınırlı değil** — mağaza listesi + **kapısız `description`** dahil her metin yüzeyi.
6. 🔴 **#1 (C-195) — KAPSAM DARALMA RİSKİ (Gravita) + OSTİNATO DÜZELTMESİ (2026-08-12).** Gravita'nınki **süreç-geneli STATIC**. ⚠️ **Bu satır Ostinato'nunkini *"aynı seans içindeki zorunlu ekran zinciri"* diye yazıyordu — YANLIŞ:** hat ölçtü, `camera_session.dart:60` `Future<void>? _closing;` **girintisiz = ÜST DÜZEY = SÜREÇ-GENELİ**, docstring birebir *"🔒 SÜREÇ-GENELİ KAPANIŞ KİLİDİ"* diyor. Seans-içi zincir onun **TETİĞİ** (yarışın nerede doğduğu), **kilidinin kapsamı değil.** → ***Risk BİR değil İKİ süreç-geneli uygulamaya karşı yazılmalı (Gravita + Ostinato) — yani GENİŞ KAPSAM SEÇİMİ sanıldığından GÜÇLÜ.*** Terfi anında yine de ölçülmeli: Gravita'nın bugün yakaladığı yarışı (kütüphane→seans→geri→seans) dar bir garanti hâlâ yakalıyor mu?
7. 🔴 **#3 (pencere-koşulu) — TEK-ŞEKİL DAYATMA RİSKİ.** Ölçülen tür sayısı **DÖRT**: Gravita **korelasyon** (hip-knee Pearson) · JabLab **oran** (`withValidAnalysisRatio`) · Lissom **tetik** (şema var, motor bağlı değil) · **Ostinato ARDIŞIKLIK** (`_consecutiveOut >= 3`; penceresi **yalnız GÖSTERİM** — 240 kare grafiğe gidiyor, koşul ayrı yerde → *yayılıma eklenmemeli*). ***Çekirdek tek şekli dayatırsa DÖRTTEN ÜÇÜ uyarlanamaz.*** → Primitif ***"pencere içinde BİR KOŞUL değerlendir"*** olmalı, **koşulun TÜRÜ değil.**
8. 🔴 **#6 (tutuş-süresi) — REFERANSIN GÜNCEL SÜRÜMÜ TAŞINMALI (Gravita).** `HoldEngine`e **bugün iki düzeltme indi** (G-179): `required:` **hareketin kendi beyanından türetiliyor** · güven kapısı **izotropik kare değil HAM kare** kullanıyor. ***Terfi bunları taşımazsa çekirdek, kaynağından ZAYIF bir sürüm alır.*** Ayrıca `hold_engine.dart:117-119`'un **fail-closed girişi** (null metrik → `ready=false`) primitifle **birlikte** gitmeli — `tuck_planche`ın sessizce hiç başlamamasının sebebi o: *doğru yön, ama sessiz.*
> 📌 **Ve bunlar KARŞI-ÖLÇÜM DEĞİL (hattın kendi ayrımı):** *"terfiyi zayıflatmak değil DOĞRU KURMAK için — sayıyı şişirmemek adına ayırıyorum: bunlar **tasarım şartı**."*

## 4. Tur neden 2026-08-12'de AÇILMADI

1. Dört hat **kirli ağaçla** yayın-blokajı işindeydi; pin turu beşinin de **temiz ve sakin** olduğu anı ister.
2. **JabLab ölçtü: terfi ona bir YETENEK verir, bir KAPI açmaz** (16/16 kapı tüketicisiz) → en az bir hat için getirisi düşük.
3. **Kuyruk büyüyordu** — tek günde 4 yeni aday. 5 kalem terfi edip ertesi gün 4 kalemlik kuyruk açmak, turu iki kez yapmaktır.

## 5. Turdan önce kapatılması gereken

- [ ] 🔴 **reachability SAYMA KURALI — kalem sanıldığından BÜYÜK (Gravita, 2026-08-12).**
  Başlangıçta soru *"onboarding sayıya dahil mi"* sanılmıştı (2/5 hat şerh düştü, ikisi de cümleyi daralttı). **Gravita'nın kapsam dökümü daha derin bir sorun gösterdi:**
  > *"GEVŞEK sayımım dört sekme gövdesini **4 yüzey** sayıyor ama KATI'da **1 rota**. Lissom/Choreia sekmeleri farklı sayıyorsa **iki sayı aynı şeyi ölçmüyordur** — fark içerik değil **SAYMA KURALI** olur."*
  ⚠️ Yani bugün panoda yan yana duran **Lissom 6/2 · Choreia 5/3 · Gravita 7/4** sayıları **karşılaştırılabilir DEĞİL** — kural yazılmadan kıyaslamak, bu vardiyada gün boyu düzeltilen **birim hatasının AİLE ÖLÇEĞİNDEKİ** hâli olur.
  **Turdan önce her hattan yazılı kural isteniyor (4 soru):** ① sekme = KATI'da kaç, GEVŞEK'te kaç · ② aday envanteri nasıl türetiliyor (desen mi, elle mi) · ③ ölçüm **nereden** başlıyor (kabuk mu, uygulama kökü mü) · ④ onboarding **içeride mi**.
  **📊 3/5 KURAL YAZILDI (2026-08-12) — ve sonuç ilk sanılandan İNCE:**
  · **Sekme ekseni HİZALI:** Gravita (sekme gövdesi GEVŞEK'te 1/tab, KATI'da 0 + kabuk 1) ↔ Lissom (aynı) ↔ JabLab (**sekme YOK**, 4-sekme kabuğu 08-06'da kaldırılmış — ve *"bende yok" cevabı da kuralın parçası*, yoksa okuyan sekmelerin 6'nın içine katlandığını sanar).
  · 🔴 **ENVANTER ekseni AYRIŞIYOR — ve üçü FARKLI YÖNDE yanılıyor:**
    | hat | yöntem | kör noktası |
    |---|---|---|
    | **Gravita** | desenden **türetme** | desene uymayan adı kaçırır · **ulaşılamayanı SAYABİLİR** |
    | **Lissom** | **elle** liste | listeye eklenmemiş ekran görünmez (desen denendi, `FamilyPage`i kaçırdı — L-270) |
    | **JabLab** | elle liste + **yürüyerek kanıt** | ***yalnız UĞRADIĞI yeri bulur*** — ulaşılabilir ama kimsenin basmadığı ekran görünmez (bir kez ölçüldü, boş çıktı, **ama o tarama KAPILI DEĞİL**) |
    | **Ostinato** | **elle yürüyüş** | ***yazarın DENEMEYİ AKLINA GETİRMEDİĞİ kontrol*** |
  ⭐ **Ve kör noktalar FARKLI HIZLARDA büyüyor (Ostinato'nun eklediği ayrım):** *"Benimki yürüyüş büyüdükçe değil, **ÜRÜN büyüdükçe** büyür."* Gravita'nınki desen değiştikçe, Lissom'unki liste bakımı gevşedikçe, JabLab'ınki yürüyüş kapsamı daraldıkça.
  🔴 **OSTİNATO SAYISI DÜZELTİLDİ (2026-08-12):** eski **11** *(08-07)* **hem BAYAT hem KURALSIZDI** — KATI 8 + kamera-arkası 3'ü tek sayıda topluyordu (**GEVŞEK okuma**). Ve aracın yazdırdığı **9** da yazılı kuralla **ÇELİŞİYORDU**: `guide` ve `scored` **AYNI rotaya** gidiyor (`course_screen.dart:100-104`) ama küme iki **DİZGE** gördüğü için 9 sayıyordu → ***ETİKET ≠ ROTA*** (M-F-499'un üçüncü hâli). ✅ Hüküm: sayaç **rota-kimliğine** çevrilecek → **KATI 8**, ve eşik `>= 8` olduğu için ***kapı tam TABANDA, sıfır paylı*** — düşüşün **sebebi** sayının yanında yazılı olacak.
  📌 **ÜÇÜNCÜ gizli dayanak (Ostinato):** `t.pageBack()` **kullanılamıyor** — geri düğmesi standart `BackButton` değil, ürünün kendi `GlassIconButton`'ı (`‹` glifi). ***Aracın varsayılanı ürünün gerçeğini tanımıyordu.***
  📌 Ve Ostinato'nun sayısı **iki yönde de sınır**: GEVŞEK bir **ALT** sınır (aşamaların ekranlara dağılımı sayılmadı) · KATI `requireSubstance` ile **daraltılmış** (*ulaşmak ≠ çalışmak*).
  > ***İki yöntem farklı YÖNDE yanılıyor; hangisinin kullanıldığı yazılmazsa iki sayı kıyaslanamaz.*** (JabLab)
  ⚠️ **KOORDİNATÖR DÜZELTMESİ:** Lissom'un kuralı Gravita'nınkiyle aynı çıkınca *"6/2 ile 7/4 kıyaslanabilir, fark içerik"* denmişti — **eksikti.** Sayılar **sekme ekseninde** hizalı, **envanter ekseninde DEĞİL**; farkın ne kadarının **içerik**, ne kadarının **YÖNTEM** olduğu **ölçülmedi.**
  📌 **Ve iki hat aynı gizli dayanağı BAĞIMSIZ doğruladı:** `find.byType`ın **`skipOffstage: true`** varsayılanı yalnız **görünen** ekranı işaretliyor; `false` olsaydı biriken `Set` alttaki sayfaları da sayıp **şişirirdi** (Lissom Flutter kaynağında, JabLab 1/0/1 tablosuyla). → ***Bir sayının doğru olması yetmez; onu DOĞRU YAPAN BAYRAĞIN ne olduğu yazılı olmalı.***
  ⏳ **Bekleyen: Ostinato** (08-07'nin *"11"*i **bayat**, kural da yok) · **Choreia** (hasattan dönünce).
  ⛔ Tanım değişince **sayı değişecek** → **pano hangi tanımla yazıldığını taşımalı.**
- [ ] **#2 `worldLandmarks`** ve **#5 kamera önizleme** — bu vardiyada hiç ölçülmedi; yayılımları güncel değil.
- [x] **Lissom `reference_equivalence`** — ✅ HAZIR (ölçüldü; kurulacak sanılıyordu, **zaten tamdı**)

## 6. Turun mekaniği

- **Pin beş hatta ortak** → tur **TEK ve KOORDİNELİ**; beş hat da `kirli 0` + `push-bekleyen 0` olmalı.
- Pin `f13bdc9` **TAM-40-SHA** — pub ref'leri **STRING** karşılaştırır, kısa SHA kabul edilmez.
- Her terfi için: **referans uygulama adıyla** + **muafiyet varsa belgesiyle** (Lissom'un `docs/C-195-YARIS-OLCUMU-2026-08-12.md` emsali).
