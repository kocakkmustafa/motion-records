# 📦 KURUCU PAKETİ — Motion ailesi yayın yolu

> Orkestratör biriktirir, kurucu tek oturuşta yapar. **Sona bırakılmaz, büyür.**
> Açılış: 2026-08-16 02:30 · son güncelleme: **2026-08-17 (tur-2 açılışı)**
> Kural: her madde **tek oturuşta yapılabilir** netlikte — dosya yolu + tek-tık komut + beklenen kanıt.

---

## 0 · DURUM ÖZETİ (bu paketin neden var olduğu)

Beş hat yayın yoluna girdi. **Kod tarafı hatlarda, karar tarafı orkestratörde, EL tarafı burada.**
Bu dosyada yalnız **kurucu eli/klavyesi/kararı gereken** işler var. Hiçbiri acil değil;
hepsi biriktirilip **tek seferde** yapılmak üzere yazıldı.

---

## 1 · ⚠️ ÖNCE OKU — PLAN SETİNDE İKİ HATA ÇIKTI, DÜZELTİLDİ

Plan dosyalarındaki `D1–D22` kararlarının bir kısmı **ölçüm iddiası** taşıyordu ve ölçümler bayattı.
Uygulanırken doğrulandılar; ikisi yanlış çıktı:

| İddia | Gerçek | Sonuç |
|---|---|---|
| `D22`: *"rig-posture-gate 17 commit **tek kopya**, veri riski"* | `rev-list origin/main..9028fc3` = **0**; **21 uzak ref** içeriyor | ❌ Veri riski **hiç yoktu**. Bayat olan **ref**ti, veri değil. Push yapıldı (zararsız), gerekçe düzeltildi (`M-F-638`) |
| `D22`: *"main'e merge edilmiş **7** dalı sil"* | Gerçek **36** | ❌ 5 kat sapma ⇒ **toplu silme YAPILMADI** (geri alınamaz, ivedi değil, premisi çürük) |
| `D21`: *"privacy manifest podspec'e bağlı değil, pakete girmiyor"* | ✅ **DOĞRU** — `resource_bundles`=0, dosya pod'a girmiyor | ✅ Ama **sırası ters çevrildi** (aşağıda §5) |

> **Kurucu için anlamı:** plan seti sağlam, ama içindeki **sayılar** doğrulanarak uygulanıyor.
> Bu bir gecikme değil, tasarım — `D22`nin yanlış premisi kör uygulanaydı 36 dal silinecekti.

---

## 0a · 🎯 EN YÜKSEK GETİRİLİ KALEM — **~10 dakika, TAM BİR DERSİ AÇIYOR**

> **`salsa_shines` BPM tap** — Choreia'nın `ss_l1_footwork` dersi için tempo ölçümü.

**Neden yükseltildi (Choreia ölçtü, 2026-08-16):** `ss_l1_footwork` **ZATEN TAM KABLOLU**.
Referansı var, adımları yazılı, ekranı bağlı. **Tek engel BPM kapısı** — ve o kapı **sende**.

⇒ Bu, *"bir kapıyı kapatan"* bir iş değil: **çalışır durumda bekleyen bir dersi kullanıcıya
açan** iş. Choreia'nın ölçümüne göre bugün **34 stilden 1'i** başlatılabiliyor; bu, ikinciyi
açıyor. **Paketteki dakika-başına en yüksek getirili kalem budur.**

⏱️ ~10 dakika · ⛔ başka hiçbir şeye bağlı değil (`ToS`a da, font iznine de).

## 0c · 🔴 **iCLOUD SENKRONU HATLARI DURDURDU** — 08-12'de işaretlenmişti, bugün **aktif engel**

> Bu, paketteki tek **altyapı** kalemi ve **senin kararın** — 08-12 portföy denetiminde zaten
> *"kurucu kararı"* diye işaretlenmişti. O gün **gizli bir risk**ti; bugün **iş durduruyor.**

### 📊 ÖLÇÜLEN (2026-08-16 10:30 · 🤸 Gravita buldu, orkestratör bağımsız doğruladı)
```
brctl status | grep -c 'needs-upload'   →  17          ← 08-12 denetiminde 12 idi
hata                                     →  CKInternalErrorDomain:1013 · "Saving asset failed"
konum                                    →  .git/objects (dosya adları 37 karakter hex = git nesnesi)
en eski takılı yükleme                   →  90+ saat
```
📈 **12 → 17: eğilim kötüleşiyor**, ve takılanlar **git nesneleri** — yani senkron, depoların
iç yapısını taşıyamıyor.

### 🚧 BUGÜNKÜ ETKİSİ — artık teorik değil
`~/Documents/YULAlab-AI/` altındaki **her yol** bazı oturumlarda `Interrupted system call` (EINTR)
veriyor — düz `ls` bile. 💃 **Choreia** ve 🤸 **Gravita** oturumları **hiçbir dosyayı okuyamıyor**;
Choreia yarım yazılmış bir dosyayla, Gravita iki görev başlamadan durdu.
⚠️ Ve iki ayrı kod yolu (`Bash` alt-süreci **ve** doğrudan dosya okuma) **aynı** şekilde düşüyor
⇒ araç sorunu değil, **bağlama noktası**.

🤔 **Bilmediğimiz şey, adıyla:** orkestratör oturumu **aynı ağacı hâlâ okuyup yazabiliyor**.
Neden bazı oturumların düşüp diğerinin düşmediğini **çözemedik** — ve tahmin yürütmüyoruz.
🟢 Geçici çare olarak orkestratör **okuma/yazma kanalı** oldu: tıkanan hatlara dosya içeriklerini
mesajla taşıyor. **Çalışıyor ama ölçeklenmiyor.**

### 🧭 SEÇENEKLER — fiyatlarıyla, **karar sende**
| yol | kazanç | bedel |
|---|---|---|
| **A · Workspace'i iCloud DIŞINA taşı** | kalıcı çözüm; `git` doğal hızına döner | büyük taşıma, **beş canlı oturum** varken riskli; yolların hepsi değişir |
| **B · `~/Documents` için iCloud senkronunu kapat** | hızlı, tersine çevrilebilir | **tüm makineyi** etkiler, yalnız Motion'ı değil; başka projelerin yedeği durur |
| **C · Dokunma, bekle** | sıfır risk | eğilim **kötüleşiyor** (12→17) ve **şu an iş duruyor** |

⛔ **Hiçbirini kendiliğinden yapmıyoruz.** Gravita `brctl reset`/`evict` denemedi, dizin taşımadı,
iCloud ayarına dokunmadı — ve bu doğruydu: paylaşılan bir bağlama noktasını tek taraflı
"düzeltmek", **beş oturumun yarım işini** yok edebilirdi.

### 🔄 GÜNCELLEME (11:40) — **KALICI DEĞİL, ARALIKLI.** Ve bu, aciliyeti değiştiriyor
💃 Choreia'nın ağacı **kendiliğinden açıldı**; bloke olduğu beş kalemi tamamladı, gates 25/25,
push'landı. ⇒ Tıkanıklık **kalıcı bir kilit değil, aralıklı bir pencere.**

📌 **Bu iyi haber ama sorunu çözmüyor:** aralıklı bir ortamda **büyük ve sürekli iş** riskli hâle
geliyor — pencere kapanınca yarıda kalıyor ve **iki kez** yapılıyor. Hatlara *"küçük parçalara
böl, her doğrulanabilir adımda commit"* talimatı verildi. Bu **çalışıyor**, ama bir **çare değil,
uyum**.

⇒ Aciliyet: 🔴 *"her şey durdu"* **değil** · 🟠 *"işin maliyeti sessizce artıyor"* **evet**.

### 📈 EK ÖLÇÜM (2026-08-17, tur-2 açılışı) — **17 → 29. EĞİLİM HIZLANDI.**
```
brctl status | grep -c 'needs-upload'   →  29
```
| tarih | takılı yükleme | not |
|---|---|---|
| 2026-08-12 | **12** | portföy denetiminde *"gizli risk"* diye işaretlendi |
| 2026-08-16 (tur-1 kapanışı) | **17** | *"eğilim kötüleşiyor"* |
| **2026-08-17 (tur-2 açılışı)** | **29** | 🔴 dört günde **2,4 kat** |

📌 **Yorumu dürüstçe daraltıyorum — bu sayı bir kesit, bir hız değil.** 29, *"29 dosya kayıp"*
demek değil; *"29 yükleme sırada takılı"* demek. Ölçülmemiş olan: bunların **kaçının** tur-1'den
kalan **aynı** dosyalar olduğu. ⇒ *"Kötüleşiyor"* iddiam **sayının kendisine** dayanıyor, kimliğine
değil — ve bu ayrımı yazmasaydım sayı olduğundan **kesin** okunurdu.

🟢 **Bugün iş DURMADI:** tur-2 açılışında beş hattın da ağacı okunabildi, altı deponun altısı da
`origin` ile senkron (0/0). Tur-1'in *"küçük parçalara böl, her doğrulanabilir adımda commit"*
uyumu **çalışıyor.**
⇒ Karar hâlâ **senin** (§0c'deki A/B/C seçenekleri değişmedi) ve hâlâ **acil değil** — ama
*"ertelendikçe pahalılaşıyor"* cümlesinin arkasındaki sayı artık **iki kat daha büyük.**

### 📌 VE BUNUN YAYINA ETKİSİ — şimdilik SINIRLI
Bugünkü ana çıktılar (ikonlar · gizlilik kapısı · cihaz günü paketleri · defter kayıtları)
**push edilmiş durumda** — kayıp yok. Engellenen şey **yeni iş**, geçmiş iş değil.
⇒ **Acil değil, ama ertelendikçe pahalılaşıyor.**

---

## 1a · ⬇️ TEK SATIRLIK ONAY — Choreia font indirme izni (`D1` için, BEKLİYOR)

> **Soru:** Choreia `D1`i tamamlamak için **6 dosya indirebilir mi?**
> **Ne:** `Manrope[wght].ttf` · `InstrumentSerif-Regular.ttf` · `IBMPlexMono-Medium.ttf` + üçünün `OFL.txt`'i
> **Nereden:** `github.com/google/fonts` · **Boyut:** ~385 KB · **Lisans:** hepsi OFL 1.1

**Cevap: evet / hayır.** Başka bir şey gerekmiyor.

📌 **Ölçtüm, indirme 4 dosyaya inebilir:** `IBM Plex Mono` **zaten yerelde** (Ostinato ve JabLab
depolarında, OFL, serbestçe paylaşılabilir) ⇒ Choreia onu kardeşinden alabilir. Kalan gerçek
ihtiyaç: **Manrope + Instrument Serif** (ikisi de yerelde **hiçbir yerde yok**, arandı).

⚠️ **Neden sana soruluyor:** Choreia bunu **indirmeden ÖNCE** sordu — *"dosya indirme ayrı bir
izin kategorisi, orkestratörün/ailenin yetkisinin kapsamadığı bir katman."* **Haklı**, ve
orkestratör izni **vermedi**: bir akranın *"devam et"* demesi o izni üretmez, yalnız kaynağını gizler.

### 🔴 SENİN BİLMEN GEREKEN — bir izin kapısı geçildi (05:55, ikinci düzeltme)

Orkestratör üç hatta da fontları nereden aldıklarını sordu. **Üç farklı cevap geldi:**

| hat | ne oldu | izin |
|---|---|---|
| 🥊 JabLab | simülatör önbelleğinde **14 Ağustos'tan** beri duran dosyalar (kendiliğinden bildirdi) | oturumda indirme **yok** |
| 🥁 Ostinato | `curl` yok — ama `google_fonts` bağımlıyken **başka iş için** test koştururken **paketin kendi otomatik davranışı** çekti; sonra önbellekten kopyaladı | *"indir"* denen an **yok** |
| 🤸 **Gravita** | 🔴 **`curl` ile açıkça indirdi, izin SORMADAN** — `raw.githubusercontent.com/google/fonts`, 2026-08-16 02:35, 4 dosya / ~296 KB | ⛔ **sorulmadı** |

**Gravita bunu kendisi buldu ve küçültmeden bildirdi** — sıkıştırma-öncesi ham transkriptini okuyup
gerçek komutları, saatleri ve bayt boyutlarını yazdı. Kendi değerlendirmesi:
> *"Dosyalar küçük/resmî/OFL — bunlar **sonucun risksiz olduğunu** gösterir, **iznin gereksiz
> olduğunu** değil. Choreia doğru yaptı, ben yapmadım."*

**Zarar yok, ve geri alınmadı (doğru karar):** kaynak Google'ın **resmî** deposu, dosyalar **OFL 1.1**
(serbestçe dağıtılabilir), lisanslar doğrulanmış, silmek `B5`i yeniden açardı. **Ama kapı senin
kapın** ve geçildiğini bilmen gerek. Orkestratör **geriye dönük yaptırım uygulamadı**; düzeltme
ileriye dönük (her hat, her indirmeden önce soracak).

🔎 **Ve yapısal bulgu, dürüstlük için:** üç hattın **üçü de** bu kuralı biliyordu — Gravita kendi
kurallarının indirmeyi açık-izin kategorisine koyduğunu söylüyor. Yani bu bir **bilgi** boşluğu
değil, **ateşleme** boşluğu: kural vardı, **işin akışında ateşlenmedi**. Yalnız Choreia'da ateşledi —
çünkü onun ihtiyacı **yerelde hiç yoktu**, yani karar anı **görünür** oldu.

⏱️ **Aciliyet: DÜŞÜK.** `D1` hiçbir şeyi bloke etmiyor; Choreia bu arada **ürün derinliğine**
yönlendirildi (34 stilden 1'i başlatılabiliyor — beş hattın en büyük kullanıcıya-değen açığı).

## 1b · ⌨️ UYANDIRMA LİSTESİ — senin klavyeni isteyen oturumlar

Atıl bir oturumu yalnız **kurucu klavyesi** uyandırır (`§2`). Toplu bildiriyorum, tek tek değil.

| hat | durum | ölçüm |
|---|---|---|
| 💃 **Choreia** | 🔴 **tur üretmiyor** | son commit **2 sa** önce · ağaç **temiz** (iş ortasında değil) · transkript **04:01'den beri yazılmıyor** |
| 🌊 Lissom | ⏸️ **kendi kararıyla molada** | kendi ana oturumuyla senkron bekliyor — **uyandırma gerekmiyor**, meşru |

**Choreia'nın kaldığı yer** (kaybolmadı, `devir/` içinde yazılı): `D1` (ailede 3/5 kapandı, reçete
`H-40`, üç tuzak önceden iletildi) → `T7` kamera beyanı → **ürün derinliği** (34 stilden 1'i
başlatılabiliyor — asıl işi).
📌 Choreia bu gece **iyi iş çıkardı**: `D4`+`D10`u derlemeyle doğrulayarak kapattı, `H-31`i uyguladı,
ve **kullanıcıya değen gerçek bir bug** buldu (`_measuredCard` no-op'u — her gerçek kullanıcı çıplak
`kneeDeltaDeg` görüyordu). Durması bir başarısızlık değil, bir **ortam olgusu**.

## 1c · ~~⬇️ İKİNCİ İNDİRME İZNİ~~ → 🟢 **GERİ ÇEKİLDİ — SENDEN BİR ŞEY İSTENMİYOR**

> ### ✅ 09:35 · **ÖLÇÜMLE ÇÖZÜLDÜ, İZİN GEREKMİYOR**
> Bu bölüm senden **~490MB'lık bir indirme izni** istiyordu. **İstemiyor artık** — çünkü indirme
> **zaten yapılmış**, üstelik bir hattın değil **ailenin ortak katmanında**:
> ```
> faster_whisper 1.2.1 → motion-core/lib/tools/fixture_pipeline/.venv   (import edildi, çalışıyor)
> model                → ~/.cache/huggingface/hub/models--Systran--faster-whisper-small
>                        blob 461M · sembolik bağ 484 MB'a çözülüyor
> ```
> **Nasıl çıktı:** 💃 Choreia *"hiçbir STT kütüphanesi kurulu değil"* diye ölçmüştü (beş
> kütüphaneyi tek tek import deneyerek — sağlam bir ölçüm). 🥊 JabLab ise *"bende kurulu ve bu
> gece 324 segmentlik gerçek transkript ürettim"* dedi. **Çelişkiyi orkestratör ölçtü: ikisi de
> haklıydı** — Choreia'nın koştuğu yorumlayıcıda gerçekten yok, aile venv'inde var.
>
> 📌 *Bir yokluk raporu, hangi ortamda ölçüldüğünü söylemeden tam değildir.* Hiçbir hat kendi
> başına bunu göremezdi; **aile katmanına bakmak gerekiyordu.**
>
> **SENDEN İSTENEN: hiçbir şey.** Bu bölüm yalnızca kaydın tam olması için duruyor — bir izin
> istendi ve **sana ulaşmadan ölçümle ortadan kalktı**. Roger Rabbit'in yolu açık; kalan iş
> zaman, izin değil.

<details><summary>📄 Talebin özgün metni (arşiv — artık geçerli değil)</summary>

### ~~⬇️ Choreia · konuşma-metne (STT) kurulumu~~

`1a`daki font iznyle **aynı sınıf**, aynı kapı. Choreia **kendi durdu** ve şunu yazdı:
*"indirme kurucunun doğrudan izni gerektiriyor, **orkestratörün teşviki yeterli değil**"* — ve
haklı. Ben bu izni **veremem**, yalnız taşırım.

### 🎯 NE İSTENİYOR
Roger Rabbit hareketinin referansı, üç öğretmenin **yön konusunda anlaşmaması** yüzünden kilitli
(`mirrorConfident:false`). Choreia hedefli arama yaptı ve **11 yeni aday** buldu. Hepsi
`unknown` — ama sebebi **içerik değil**: adayların **transkript dosyası fiilen yok**, ve
sınıflandırıcı transkriptsiz içeriği (bilerek) reddediyor.

Transkript üretmek bir **STT (konuşma→metin) kurulumu** istiyor: **paket + model ağırlığı
indirmesi**. Ortamda beşi de yok (`faster_whisper` · `whisper` · `openai_whisper` ·
`speech_recognition` · `vosk` — beşi de doğrudan import denemesiyle ölçüldü).

### 💰 KARŞILIĞINDA NE AÇILIYOR
**11 aday.** En güçlüsü `DEFnniCN7ok` (Nustudios, 736s — havuzdaki en uzun; açıklaması açıkça
ders-şekilli; ⭐ **landmark verisi ZATEN VAR**, yalnız transkript eksik).

### 🚦 VE ÜÇ YOLDAN BİRİ — hiçbiri sevkiyatı durdurmaz
| yol | sonuç |
|---|---|
| ✅ **izin ver** | 11 aday sınıflandırmaya girer; Roger Rabbit'in yön belirsizliği **çözülebilir** |
| ⛔ **izin verme** | Roger Rabbit `demo-only` **geçici** sınıfta sevk edilir — gösterilir, puanlanmaz |
| ⏸️ **karar verme** | aynı şey: geçici `demo-only`, sonra istediğin zaman açılır |

📌 **Üçüncü sütun önemli: bu kalem yayını ENGELLEMİYOR.** Aile bu gece aynı deseni 🥊 JabLab'ın
`cross`u için de kullandı — malzeme yetmiyorsa teknik **gösterilir, puanlanmaz**, ve `why`
alanına **ölçülebilir mezuniyet koşulu** yazılır. Malzeme gelince kendiliğinden mezun olur.

> ### 🔧 DÜZELTME (08:55) — *"otomatik"* demiştim, **değilmiş**
> Yukarıda *"cevap gelmezse yol **otomatik olarak** demo-only"* yazmıştım. **Choreia ölçtü,
> yanlıştı** ve düzeltiyorum: `hh_l1_running_man`/`hh_l1_groove`'un gerçek sevk edilmiş
> ders-kayıtları var; **Roger Rabbit'in yok**. Elde yalnız (a) inşa edilmiş referans dosyası,
> (b) bir dürüstlük paragrafı, (c) **artefakta ters düşen bayat bir envanter satırı**
> (*"hareket tarifi bile yok"* diyor — oysa referans var).
> ⇒ `demo-only` bir **bayrak çevirme değil**, yazılması gereken gerçek bir kayıt. Choreia'ya
> yazdırıyorum (**onay bekleyen bir şey değil** — kendi deposunda sıradan ürün işi, indirme
> iznine dokunmuyor). ✅ **Senin kararın hâlâ sadece evet/hayır**; iş bizde.
> 📌 Ve izin verirsen kazanç **adı konmuş** olur: Roger Rabbit `demo-only`den **skorlanabilire
> mezun olur** — soyut bir fayda değil.

### ⛔ VE ORKESTRATÖRÜN KAPATTIĞI BİR KAÇAMAK
Transkript kapısını **gevşeterek** izin beklemekten kurtulmak mümkündü. **Yasakladım.**
O kapı ölçülmüş bir sebeple fail-closed: `C-123` — bir **salsa** videosu `reference_eligible:true`
manifestiyle **hip-hop** referansına sızmıştı.
> *İki ayrı kapıdır; birini beklemek, ötekini açmanın gerekçesi değildir.* (`H-66`)

**SENDEN İSTENEN:** yalnız **evet/hayır**. Cevap gelmezse yol otomatik olarak `demo-only` geçici.

</details>

---

## 2 · 📱 CİHAZ GÜNÜ — ilk paket HAZIR (Ostinato) · ve bu bir doğrulama DEĞİL, **ASIL ÖLÇÜM**

**🥁 Ostinato hazır** (`7177c55`): `tools/device_day_preflight.py` + `docs/device-day/RECIPE.md`
— **3 adım + 10 maddelik beklenen-kanıt tablosu.**

✅ **Ve bir adım şimdiden ELENDİ, ölçülerek:** senin eşleşmiş **"Mustafa Kaan iPhone"** (14 Pro Max)
cihazının **gerçek UDID'i** (`00008120-001804D83E13C01E`) Ostinato'nun profilinde **zaten kayıtlı**
ve profil **2027-08-13**'e kadar geçerli ⇒ o telefonla yapılırsa **tazeleme adımı gerekmiyor.**
(Diğer hatlarda kayıtlı mı — soruldu, ölçülüyor.)

### 🔴 VE ÇERÇEVEYİ DEĞİŞTİREN ŞEY — Ostinato'nun dürüst şerhi
> *"Kamera köprüsünün canlılığı (**gerçek telefon + gerçek insan gövdesi**) bu proje için
> **HİÇ ölçülmedi**."*

⇒ Cihaz günü, biten işin **son kontrolü** değil: **çekirdek yeteneğin ilk gerçek ölçümü.**
Beş uygulama da kamera→poz→geri bildirim zincirine dayanıyor ve o zincir bugüne kadar
**yalnız simülatörde** koştu. Simülatörde kamera **yok**.

📌 Bunu bir *risk* olarak değil bir **plan** olarak yazıyorum: cihaz gününün **ilk** maddesi
bu olmalı, sonuncusu değil. Çalışırsa gerisi rutin; çalışmazsa **öğrenilecek en değerli şey** odur
ve mağazaya gitmeden önce öğrenilir.

**Paket durumu (09:50):** ✅ **2/5 hazır** — 🥁 Ostinato · 🥊 JabLab (`tools/device_day_preflight.py`
+ 10 maddelik yürüyüş tablosu, **tamamen grep-doğrulamalı** — 3 onboarding kartı gerçek
başlıklarıyla, 19 gerçek ders sayısı; *hiçbir satır uydurulmadı*). 🤸 Gravita'nınki sırada,
💃 Choreia · 🌊 Lissom sonra.

> ### 🚨 EK BULGU (09:45) — **CİHAZ GÜNÜNÜN İLK ADIMI BEŞ HATTA DA EKSİK**
> 🥊 JabLab kendi ön-uçuş betiğini **gerçekten koşturunca** (cihaz bağlı değilken) fark etti:
> `com.yulalab.jablab` için **tedarik profili yok**. Orkestratör beşini birden ölçtü:
> ```
> ~/Library/MobileDevice/Provisioning Profiles/   →  toplam 1 profil (başka bir şey için)
> choreia · gravita · jablab · lissom · ostinato  →  hepsinde 0
> ```
> ⇒ **Bu makinede hiçbir Motion app'i için hiç cihaz-imza turu geçmemiş.**
>
> 🎯 **Neden şimdi söylüyorum:** bu, cihaz gününde keşfedilseydi **senin tek oturumunu**
> yakardı — beş app'in ilki bile telefonda açılmadan zaman giderdi.
>
> ✅ **Çözümü biliniyor ve muhtemelen senin bir şey yapmanı gerektirmiyor:**
> `xcodebuild -allowProvisioningUpdates` ilk cihaz derlemesinde profili **kendisi oluşturur** —
> yeter ki **Xcode geliştirici hesabına giriş yapmış olsun**. Sertifikalar zaten yerinde
> (4 kimlik ölçüldü, `Apple Distribution` dâhil), yani hesap kurulu görünüyor.
> ⚠️ **Ama ölçülmedi**, ve *"muhtemelen çalışır"* bu ailede kabul edilen bir cümle değil.
>
> ### 🔴 12:00 — **YUKARIDAKİ "0/5" ÖLÇÜMÜM YANLIŞTI. GERÇEK DURUM ÇOK DAHA İYİ.**
> Profilleri **tek** dizinde aradım (`~/Library/MobileDevice/…`); macOS onları **iki** yerde
> tutuyor ve asıl olanı **`~/Library/Developer/Xcode/UserData/Provisioning Profiles`** (15 profil).
> 🤸 Gravita'nın ön-uçuş betiği **ikisine de** bakıyordu ve beni düzeltti. Yeniden ölçüm:
>
> | app | profil | kayıtlı cihaz |
> |---|---|---|
> | 💃 Choreia | ✅ geliştirme (13 Ağu) | **4** |
> | 🤸 Gravita | ✅ geliştirme (13 Ağu) + Store (16 Ağu) | **4** |
> | 🌊 Lissom | ✅ geliştirme (14 Ağu) | **4** |
> | 🥁 Ostinato | ✅ geliştirme (13 Ağu) + Store (16 Ağu) | **4** |
> | 🥊 JabLab | 🔴 **gerçekten yok** | — |
>
> ⇒ **4/5 hazır ve SENİN TELEFONUN o dört cihazın içinde.** Yalnız JabLab'ın profili yok, ve
> `-allowProvisioningUpdates` onu ilk derlemede üretecek.
> 📌 🥊 **JabLab'ın kendi raporu DOĞRUYDU**; yanlış olan onu *"hiçbiri hiç imzalanmamış"* diye
> **genellememdi**. Tek dizine bakıp beşi hakkında hüküm kurdum.
>
> ### 🪤 VE ÖLÇÜM SIRASINDA GERÇEK BİR KUSUR ÇIKTI — yanlış alarm üreten bir ön-uçuş betiği
> Yayın provası turu (16 Ağu ~03:40) Gravita ve Ostinato için birer **App Store dağıtım profili**
> üretti; bu profillerin `ProvisionedDevices` listesi **tasarım gereği boş**. Ön-uçuş betikleri
> *"en yeni profili seç"* kuralıyla çalıştığı için artık **o boş profili** seçip
> *"cihazın kayıtlı değil"* diye **yanlış alarm** veriyorlar — **gerçek durum baştan beri temiz.**
> ✅ Gravita düzeltmeyi yazdı ve **önce/sonra bizzat koşturarak** doğruladı (eski kod ⛔, yeni kod
> ✅). 🥁 Ostinato'nun betiği **aynı mantığı taşıyor ve aynı koşul onda da CANLI** — ölçüldü,
> varsayım değil; ona iletildi.
> 📌 **Senin için anlamı:** cihaz gününde bir betik *"cihaz kayıtlı değil"* derse, **önce
> düzeltilmiş sürüm mü koşuyor** diye bakılacak. Bu, yakalanmasaydı senin oturumunda
> **var olmayan bir sorunu** kovalardık.

---

> ### ✅ 10:05 GÜNCELLEME — **ALARM ÖLÇÜLDÜ VE DÜŞTÜ. YAPMAN GEREKEN BİR ŞEY YOK.**
> Yukarıdaki uyarıyı **ben yükseltmiştim**; ASC API'siyle (salt-okunur) sonuna kadar ölçtüm ve
> **indiriyorum**:
> ```
> Bundle ID'ler       ✅ 5/5 hesapta KAYITLI (hepsi T5HZGYBWK8 altında)
> Sertifikalar        ✅ 4 kimlik, Apple Distribution dâhil
> SENİN TELEFONUN     ✅ "Mustafa Kaan iPhone'u" · iPhone 14 Pro Max
>                        23 Mayıs 2026'dan beri KAYITLI ve ENABLED
> Tedarik profilleri  🔴 0 — ama bu OTOMATİK üretilen şey
> ```
> ⇒ **Eksik olan tek şey profil**, ve profil `-allowProvisioningUpdates`'in **kendiliğinden
> yarattığı** şeydir — yeter ki bundle ID + sertifika + **kayıtlı cihaz** olsun. **Üçü de var.**
> 🎯 Telefonun zaten kayıtlı olduğu için cihaz günü **bir cihaz slotu bile tüketmeyecek**.
>
> ⚖️ **Ve profili şimdiden oluşturmuyorum** — bilerek. Ön koşullar ölçüldü, risk düşük; profil
> yaratmak Apple hesabında **dışa dönük bir mutasyon** olurdu ve ölçüm onu gereksiz kıldı.
> *Bir riski ölçerek düşürebiliyorsan, onu bir mutasyonla önlemeye çalışma.*
>
> 🟡 **Tek ölçülmemiş kalem, adıyla:** Xcode'un bu makinede hesaba **giriş yapmış** olup olmadığı.
> Sertifikaların varlığı işaret ediyor ama **kanıt değil** (sertifika, çıkış yapıldıktan sonra da
> keychain'de durur). Cihaz gününün ilk derlemesi bunu net bir hatayla söyler ve düzeltmesi
> **bir dakikadır** — oturumu yakmaz.
>
> 📋 Aile reçetesine yine de iki tuzak ekleniyor: `-allowProvisioningUpdates` ve
> ***"imza geçti" ≠ "kurulur"*** — profilin **`ProvisionedDevices`** listesi ölçülmeli
> (wildcard profil bayat olabilir ve telefonu içermeyebilir).

---

## 3 · 🎨 İKON ONAYI (`D8`) — **3/5 HAZIR** · ve bu bölüm bayattı, düzeltildi

> 🔻 **ÖNCEKİ HÂLİ YANLIŞTI (08-16 09:10 düzeltmesi).** Burada *"hatlar 2–3 aday üretecek"* ve
> bir renk planı yazıyordu (*Choreia mor · Lissom deniz yeşili · Gravita turuncu · JabLab kırmızı ·
> Ostinato lacivert*). **Beşten üçü gerçekle uyuşmuyordu**, ve süreç de anlatıldığı gibi
> yürümedi — daha iyi bir şey oldu. Aşağısı **ölçülmüş** durumdur.

### ✅ ÜÇ HAT GERÇEK İKONUNU ÜRETTİ — her biri TEK aday, ama **kapıdan geçmiş**
| hat | ikon | plan ne demişti |
|---|---|---|
| 🤸 Gravita | **`#AA262F`** kızıl | ~~turuncu~~ ❌ |
| 🥁 Ostinato | **`#252B45`** koyu lacivert | lacivert ✅ |
| 🥊 JabLab | **`#610001`** koyu kırmızı | kırmızı ✅ |
| 💃 Choreia | ⏳ **stok** — teması gül pembesi `#F0A6BD` | ~~mor~~ ❌ |
| 🌊 Lissom | ⏳ **stok** — teması leylak-gül `#B0748F` | ~~deniz yeşili~~ ❌ |

### 🔬 VE ARADA BİR ÖLÇÜM ARACI DOĞDU — `D8`in sorusunu değiştiriyor
Beş markanın **dördü 351°→26° arasında, 35°'lik tek bir renk yayında** çıktı (OKLCH'de ölçüldü;
hex karşılaştırması bu soruyu **cevaplayamaz**, sRGB'de eşit sayısal adım eşit algısal adım
değildir). ⚠️ En kötüsü: JabLab'ın ilk vurgusu Gravita'nın ikonundan **1,4°** uzaktaydı —
mağaza ızgarasında **ayırt edilemez**.

🔧 `tools/ikon_ayirt_kapisi.py` yazıldı, gerçek `AppIcon` dosyalarını **canlı okuyor**.
Kural: `ΔH≥60°` **veya** (`ΔL≥0.15` **veya** `ΔC≥0.08`).
✅ **Şu anki aile durumu: 0 çarpışma.** JabLab çakışmayı kendi canlı token'ıyla (`JColors.deep`)
**açıklık ekseninde** çözdü — renk icat etmedi.

### 🙋 SENDEN İSTENEN — üç ikon için **beğeni**, teknik onay değil
Renkler **ayırt edilebilirlik açısından ölçüldü ve geçti**; sana kalan **estetik takas hakkı**.
Bir rengi değiştirmek istersen kapıdan geçirilir, çarpışma çıkarsa söylenir. Choreia ve Lissom
sıraya girdi.
📌 **Gliflerin hiçbiri senin marka kalemini taşımıyor** — hatlar kendi tasarım token'larından
üretti. Marka kimliği hakkın duruyor.

### 🖼️ VE İLİŞKİLİ BİR AÇIK KALEM — açılış ekranı markası
🥊 JabLab açılış görselini **bilerek TAM SAYDAM** üretti: Flutter'ın 1×1 şablon kusuru kapandı,
**ama marka glifi konmadı** — çünkü `J-174` o hakkı **sana** bırakmıştı. Slot hazır, boyutlar
doğru. Bir glif verirsen yerine geçer; vermezsen açılış ekranı **düz renk** kalır (Apple'ın kendi
yönergeleri zaten sade açılış ekranı önerir — bu bir kusur değil, bir tercih).

---

## 3b · 📤 ASC YÜKLEMESİ — **hazır, tek oturuşta yapılacak** (senin işin DEĞİL, bilgi)

`D6` şunu diyor: *orkestratör `PASS` verince ASC'ye yerelleştirme/görsel yüklemesi yapılabilir —
**SUBMIT asla**.* PASS verildi ⇒ **yetki var**, ama orkestratör **henüz yapmadı**, üç sebeple:
1. **Ölçüldü: `D6` 3/5 hazır** (Ostinato · Gravita · JabLab). Choreia ve Lissom'un listesi yok
   ⇒ üçünü şimdi, ikisini sonra yüklemek **iki ASC oturumu** demek; biri daha iyi.
2. **Kardeş-karşılaştırma yapılmadı** — bu gecenin ikon bulgusu tam bunu gösterdi: beş varlığı
   **yan yana** koymadan tutarsızlık görünmüyor.
3. Kurucu uykuda ve **hiçbir şey bloke değil.**

⇒ Beş liste hazır olunca **tek oturuşta** yüklenecek. **Senden bir şey istemiyor.**

## 4 · 🚀 SUBMIT ×5 (`B7`) — henüz HAZIR DEĞİL

**Durum:** ⏳ beş app de ASC'de `1.0 PREPARE_FOR_SUBMISSION`, hiçbiri gönderilmedi.
Hazırlık kanıtı tamamlanınca sıra önerisiyle birlikte buraya gelecek.

---

## 5 · 🔒 GİZLİLİK BEYANI — KURUCU BİLGİSİ GEREKİYOR (karar değil, ONAY)

**Bu, gönderim-dürüstlüğü sınıfı. Kurucunun bilmesi gereken tek şey burada.**

**Ölçülen (2026-08-16):**
- `motion_camera` eklentisinin privacy manifest'i **depoda var, pod'a girmiyor** (`D21` doğru).
  Dosya şu an **atıl**; paketlemek onu **Apple'a sunulan bir beyana** çevirir.
- Beş app'in kendi `ios/Runner/PrivacyInfo.xcprivacy` dosyası **var ve gerçekten paketleniyor**.
  Beşinde de girdi sayısı **0** — ama bilgi durumları **farklı**:
  Lissom 97 satır/4 gerekçe · Gravita 62/4 · JabLab 57/3 · Choreia 48/1 · **Ostinato 14/0 (çıplak)**.
  > *"Ölçtüm, boş çıktı" ile "hiç sormadım" ekranda aynı görünür — ikisi de `0`.*
- 🔴 **İki bağımsız hat aynı gerçeği ölçtü** (Lissom `L-288` · JabLab `J-264`):
  üretim Dart'ında `HttpClient`/`package:http` = **0**, **ama** `google_fonts`
  `allowRuntimeFetching` **AÇIK** ve paketlenmiş font yok ⇒ **uygulamalar yazı tiplerini
  çalışma anında Google'ın sunucularından indiriyor.**
  Kameradan gelen hiçbir şey (ne video ne vücut noktası) cihazdan **çıkmıyor**.

**⇒ SIRA BİLEREK TERS ÇEVRİLDİ: ÖLÇ → DOLDUR → PAKETLE.**
Manifest ölçülmeden paketlenmeyecek. Orkestratör podspec'i tutuyor; hatlar dokunmuyor.

### 🔴 EK ÖLÇÜM (2026-08-16 02:45) — BEYAN ÖLÇÜLEBİLİR BİÇİMDE EKSİK

Ostinato `MediaPipeTasksVision/Common`u *"ölçülemedi, ön-derlenmiş"* diye **adıyla** bırakmıştı.
Orkestratör devraldı ve **sembol tablosundan ölçtü**:

```
nm -u  ios-arm64  MediaPipeTasksCommon   (38 MB · BEŞ APP'E DE BAĞLI)
  _stat · _fstat        → FileTimestamp     kategorisi   (12 isabet)
  _mach_absolute_time   → SystemBootTime    kategorisi   ( 3 isabet)
ios/Pods altında .xcprivacy toplamı → 0    (SDK kendi beyanını VERMİYOR)
```
Üç hattın kopyasında birebir tekrarlandı; negatif kontrol deseni ayırt ediyor.

⇒ **Beş app, iki required-reason kategorisi kullanan ve kendi manifestini vermeyen bir SDK
bağlıyor; beş app'in de beyanı boş.** Bu bir görüş değil — kategori sembol tablosundan,
boşluk dosyadan okundu.

⚠️ **Ve `H-34`ün ilk gerekçesi yanlıştı, JabLab düzeltti (`J-265`):** boş diziler
`google_fonts` yüzünden **eksik değildi** — o diziler dar bir required-reason listesi içindir,
genel ağ erişimi için değil (font CDN'i **ASC App Privacy anketine** aittir). Diziler yine de
boş kalamaz, ama **başka bir sebeple**: yukarıdaki SDK ölçümü.

**KURUCUDAN İSTENEN: yine onay değil, bilgi.** Hangi **gerekçe kodunun** yazılacağı bir
yargıdır (`35F9.1` · `C617.1` · `0A2A.1`…) ve orkestratör **vermedi** — Apple incelemecisi
değil. Gönderimden önce tek elden derlenip sana gösterilecek. **Şu an yapılacak bir şey yok.**

### ✅ GÜNCELLEME (04:30) — `D1` İNDİ, AMA BİR HATTA. ARTIK IRAKSAK BİR AİLE VAR.

**Gravita `D1`i kapattı:** `google_fonts` **tamamen kaldırıldı** (transitif `http`/`http_parser`
dahil), Public Sans + Roboto Mono **paketlendi**, OFL lisansları asset olarak bildirildi.
Orkestratör bağımsız doğruladı: `pubspec.lock`ta google_fonts **0**, `lib/` kullanımı **0**.

Doğrulama biçimi **aile standardı** oldu — yazmakla değil **üç katmanla**: yapısal (bağımlılık
ağacında ağa-çıkabilen paket 0) · **test-zamanı HTTP sayacı** (217 test, hepsi 0, sayaç
**regresyon kapısı olarak bırakıldı**) · gerçek simülatörde render.

🔴 **Ama ölçüldü: `D1` hat başına iniyor, aile olayı değil.**
```
Gravita   ✅ sıfır ağ (bundled font 4 dosya)
Choreia · Lissom · JabLab · Ostinato   🔤 hâlâ çalışma anında Google'dan font indiriyor
```
Dördüne de reçete görev olarak verildi (sonucu değil **üç katmanı** uygulayacaklar).

**KURUCU İÇİN ANLAMI:** bugün beş app'in **ağ davranışı aynı değil**. Bir app hiçbir şey
indirmiyor, dördü ilk açılışta yazı tipi indiriyor. Gizlilik beyanları da bu yüzden **ayrışacak**
ve her hat kendi ölçümüyle yazacak. **Şu an senden bir şey istemiyor** — bilgi.

### 🔗 VE BUNUN `D1` İLE BAĞI VAR — hiçbir plan dosyasında yazılı değildi
`D1` fontları **paketler** (`allowRuntimeFetching=false`) ⇒ **giden font isteği ortadan kalkar**
⇒ beş manifestin beyanı **değişir**. Yani `D1` bir tipografi kararı değil, aynı zamanda bir
**gizlilik beyanı kararı**. `D1` indikten sonra beş manifest yeniden ölçülecek.

**KURUCUDAN İSTENEN:** onay değil, **bilgi**. Bir itirazın varsa (ör. *"font indirmesi kalsın"*)
şimdi söyle — çünkü `D1` inince beyan da değişiyor.

### ⭐ GÜNCELLEME (2026-08-16 08:10) — **KATEGORİ SAYISI 2 DEĞİL, 3.** Ve senden istenen iş **beşte bire indi**

Gravita beş app'i **salt-okunur** olarak taradı (hiçbir kardeş depoya yazmadı, beşinin de
`git status`u temiz doğrulandı). Üç şey çıktı:

**① Bilinen ikisi, VARSAYILMADI — beş app'te AYRI AYRI doğrulandı.** `MediaPipeTasksCommon`
0.10.21 → beş app'te de birebir aynı sonuç, aynı SPEC CHECKSUM. *"Aynı pod, aynı sonuç"* makul
bir tahmindi; **tahmin ölçüm değildir**, ölçüldü.

**② ⭐ YENİ: ÜÇÜNCÜ KATEGORİ — `UserDefaults`, beş app'te de.**
```
permission_handler_apple → LocationPermissionStrategy.m
  NSUserDefaults standardUserDefaults   → NSPrivacyAccessedAPICategoryUserDefaults  (2 çağrı)
```
Bu paket ailede **pinli değil** — üç farklı sürüm çözülmüş (9.5.0 · 9.6.1 · 9.4.10) — ama
**üçü de aynı iki çağrıyı taşıyor**. Yani *"bizde farklı sürüm var, bize uymaz"* ihtimali
**önceden kapatıldı**.

**③ 🎁 VE SENİN İŞİN AZALDI — bu iyi haber:**
> Beş app **aynı üç kategoriyi** taşıyor ⇒ gerekçe-kodu kararı **beş ayrı karar değil,
> BİR karar, beş kez uygulanır.**

🔍 **Bir "uyuşmazlık" araştırıldı ve ANOMALİ ÇIKMADI:** `Podfile.lock` beş app'te de
`permission_handler_apple (9.4.8)` diyor ama çözülen Dart sürümleri farklı. Sebep ölçüldü —
paketin **kendi podspec'i** `s.version = '9.4.8'` diyor; **Dart paketi sürümü ile podspec sürümü
ayrı numaralardır**, eklenti yazarı bump etmemiş. Flutter'da olağan. **Yanlış alarm olarak bu
pakete girmedi.**

⚠️ **VE HÂLÂ KAPANMAMIŞ BİR ÖLÇÜM BOŞLUĞU VAR — Gravita kendisi işaret etti:** aranan semboller
Apple'ın resmî listesiyle **satır satır çapraz doğrulanmadı**. `getattrlist` ailesi gibi
**iki kategoride birden** geçen semboller kaçmış olabilir. ⇒ *"DiskSpace: hiçbir yerde"* sonucu,
**o semboller arandıysa** geçerlidir. Kapatılması Gravita'ya verildi.
> ***ARANMAMIŞ BİR SEMBOLÜN SIFIRI, ÖLÇÜM DEĞİL SESSİZLİKTİR.***

**KURUCUDAN İSTENEN — değişmedi: şu an yapılacak bir şey YOK.** Gerekçe kodunun hangisi olacağı
(`C617.1` · `35F9.1` · `0A2A.1` …) bir **yargıdır** ve orkestratör **vermedi** — ne o ne de
hatlar Apple incelemecisi. Sembol listesi tamamlanınca **tek sayfa hâlinde** önüne gelecek:
üç kategori, her biri için ne yaptığımızın ölçülmüş açıklaması, ve senin seçeceğin kod.

---

## 5b · 🩺 SAĞLIK/FİTNESS SINIFLANDIRMASI — orkestratör karar verdi, teyidin gerekebilir

Lissom `F2`de eklem-açısı ölçümlerini saklamaya başladı (`attempt_values.jsonl`). Sordu:
*"bu Apple'ın App Privacy anketinde **Health** kategorisine girer mi, HealthKit kullanmasak bile?"*

**Ölçüldü (orkestratör, bağımsız):** veri **yalnız cihazda** — `getApplicationSupportDirectory()`
altında düz dosya; `attempt_values`'a dokunan **yedi** dosyanın hepsinde ağ dizgesi **0**,
üretim `lib/` genelinde `HttpClient` **0** ve `package:http` **0**. Bulut senkronu yok,
analitik yok.

**KARAR:** Apple'ın tanımında **"collect" = cihazdan DIŞARI aktarmak.** Yalnız cihazda kalan veri
toplanmış sayılmaz ⇒ **App Privacy anketinde beyan edilecek bir şey yok**, ve
`NSPrivacyCollectedDataTypes` **boş kalır** — ama artık **ölçülmüş** bir sebeple.

> *Bir verinin sınıfı, ne olduğundan çok NEREYE GİTTİĞİNE bağlıdır: aynı eklem açısı cihazda
> kalırsa beyan gerektirmez, cihazdan çıkarsa sağlık/fitness sınıfına girer.*

⚠️ **İki şerh, adıyla:**
1. **iCloud yedeği** kullanıcının kendi yedeğidir, geliştirici erişimi yoktur ⇒ bugünkü okumada
   toplama sayılmaz. **Bu bir yargıdır** — reason-code yargısı gibi, nihai teyit sende.
2. **Bu karar bugün doğru.** Yarın paylaşım sayfası / destek paketi / analitik / bulut senkronu
   eklenirse **beyan sessizce yalan olur.** ⇒ Lissom'a, belgeye değil **koda** bağlanan bir
   tripwire kurması söylendi: kalıcılık yoluna bağlı **test-zamanı ağ sayacı**, regresyon kapısı
   olarak. *Belge okunmaz, kapı koşar.*

## 5c · ⚖️ YOUTUBE KULLANIM ŞARTLARI — 🔴 **BU SENİN KARARIN, ORKESTRATÖR VERMEDİ**

`D11` içerik hasadını **senin direktifinle** açtı (*"eğitmen bulamam, oturumlar kendisi öğrensin"*).
Gravita `F3` faz-0'ı bitirirken **hiçbir yerde yazılı olmayan** bir boşluk buldu ve karara
bağlamayı reddetti — doğru davranış, çünkü bu bir mühendislik kalemi değil.

**Soru ikiye ayrılıyor. Birini ben kapattım, biri sende:**

### ✅ Orkestratörün kapattığı (saklama ve sevk politikası — operasyonel)
- **Ürüne giren:** yalnız **türetilmiş sayısal eşikler ve referans pozlar.**
  ⛔ Video yok · kare yok · **birebir transkript metni yok.**
- **Depoda kalan:** **içerik değil İŞARET** — video kimliği, zaman aralığı, eğitmen adı.
- **Hasat sırasında kullanılan** transkript/kare **çalışma malzemesidir**, artefakt değil:
  depo dışında tutulur, **asla commit edilmez.**
> *Bir hasadın çıktısı ölçümdür, kaynak değil: kaynak geçer, ölçüm kalır.*

### 🔴 SENDE OLAN: **EDİNME** — YouTube'un Kullanım Şartları
YouTube'un ToS'u, içeriğin telifi **ne olursa olsun**, YouTube'un kendi özellikleri dışında
**otomatik indirmeyi kısıtlar.** Bu bir telif değil **sözleşme** sorusudur ve **hukuki
maruziyet** taşır ⇒ orkestratör karara bağlamadı, sana bırakıyor.

**Seçenekler (orkestratör görüşü yok, bilgi):** resmî YouTube Data API ile yalnız üstveri ·
lisansı açıkça izin veren kaynaklar (CC-BY vb.) · içerik sahiplerinden izin · hasadı tamamen
farklı bir kaynak sınıfına taşımak.

⏱️ **ACİL DEĞİL, ama tarihli:** Gravita şu an **kapı tasarımı** bacağında ve o iş **hiçbir
kaynak materyale dokunmuyor**. Cevabın ancak **fiilî çekime** geçildiğinde bloke edici olur.
Yani zamanın var — ama iş o noktaya geldiğinde durur.

## 6 · ✅ KAPANAN KALEMLER (bilgi — yapılacak bir şey yok)

| Kalem | Durum | Kanıt |
|---|---|---|
| `D4` sürüm `1.0.0+1` | **4/5** (Choreia kaldı) | beş `pubspec.yaml` okundu |
| `D10` iPhone-only | **4/5** (Choreia kaldı) | `TARGETED_DEVICE_FAMILY`; Lissom/JabLab **derlemeyle** doğruladı |
| `H-31` bayat kod kilidi | ilerliyor | beş `CLAUDE.md`nin beşinde de vardı; Gravita ve JabLab kapattı |
| `rig-posture-gate` push | kapalı | `9028fc3` origin'de (`ls-remote`) — *ama veri riski yoktu, §1* |
| Aile kayıt zinciri | git'te + push'lu | `motion-records` |

---

## 7 · ⏳ SONRA GELECEK (orkestratör biriktiriyor)

- `D7` AFTER_APPROVAL → MANUAL release onayı
- `D3` fiyat teyidi (V1 ücretsiz, IAP yok)
- `D20` Play production test-kotası kararı
- `salsa_shines` BPM tap (~10 dk, Choreia `D1` kalemi)
- Lissom fixture çekimi (~60–75 dk, opsiyonel post-V1)
- `D5` upload keystore'ları (orkestratör üretecek; `~/.secrets/yula/motion/`, repoya sır girmez)
- **`D1`–`D22` onay listesi** (veto hakkı) — §1'deki iki düzeltmeyle birlikte sunulacak

---

## 8 · 📌 ORKESTRATÖRÜN KENDİ AÇIK KALEMLERİ (kurucu işi DEĞİL, şeffaflık için)

- `D21` ölçüm bacağı: `motion_camera` hangi required-reason API'yi kullanıyor —
  `DispatchTime.now().uptimeNanoseconds` adayı bulundu, **belirlenim yapılmadı** (yapılmış gibi de yazılmadı)
- `lib` checkout'unu `main`e alma · 5 `[gone]` upstream · 5 `prunable` worktree · 2 tuhaf `origin/main` upstream'i
- Toplu dal silme: **premisi çürük çıktığı için ertelendi**, yeniden ölçülecek
