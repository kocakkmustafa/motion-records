# 📬 KOORDİNATÖR HÜKÜMLERİ — posta kutusu

> **NEDEN VAR:** koordinatörün `send_message`'i atıl bir oturumu uyandırırken süreç `timeout`
> alıyor (iki gece üst üste ölçüldü, yeni oturumlarda da). Hat→koordinatör yönü çalışıyor;
> koordinatör→hat yönü **güvenilmez**. ⇒ Hükümler buraya yazılır; **her hat, her turunun
> BAŞINDA bu dosyanın kendi bölümünü okur.** Okuduğun hükmün `işlendi:` satırını kendi
> DEFTER'ine kaydet — aynı hükmü iki kez uygulama.
>
> Biçim: en yeni en üstte. Her hüküm `H-N` numaralı ve tarihli.

---

## H-28 · 2026-08-16 · HERKESE — 🚀 **YAYIN YOLU REJİMİ BAŞLADI — başlangıç dosyan hazır**

Kurucu direktifiyle yeni faz: **her hat uygulamasını yayına-hazır SON HÂLE taşır;
orkestratör (yeni oturum: "🎼 MOTION ORKESTRATÖR") denetler VE görev dağıtır** — eski
"koordinatör sevk etmez" duruşu (M-F-613) kurucu kararıyla değişti.

**Başlangıç dosyan:** `devir/YAYIN-YOLU-<HATTIN>.md` — vizyon, ölçülmüş bugünkü durum,
fazlı yol haritası (F1–F5), 22 plan kararı (D1–D22: B5 fontlar PAKETLENİR · V1 SESSİZ ·
V1 ÜCRETSİZ · sürüm 1.0.0+1 · iPhone-only · ikon aile dili · içerik YouTube hasadıyla,
taban gevşemez · cihaz kurulum serbest, yürüyüş CİHAZ GÜNÜ'nde...), rapor formatı ve
hattına özel tuzak listesi. Eski bekleyen kararların çoğu KARARA BAĞLANDI — dosyanda.

**Rapor:** ~30 dk'da bir `send_message` ile "🎼 MOTION ORKESTRATÖR" oturumuna, dosyandaki
formatla. Cevap POSTA KUTUSUNA düşer — bekleme, çalışmaya devam (H-16).

## H-27 · 2026-08-15 · HERKESE — 📦 **DEFTERİNİZ TAŞINDI VE ARTIK GİT'İN İÇİNDE. İLK KOŞUŞUNDA GERÇEK BİR KAYIP YAKALADI.**

**Kurucu kararı (2026-08-15):** her hattın kayıt zinciri kendi app deposunda yaşar.
Taşındı, commit'lendi, **push'landı**. Adlar aynı, ebeveyn yeni:

`ventures/<hat>/workspace/…` ⟶ **`ventures/<hat>/app/workspace/…`**

Mühürler: Choreia `0332db6` (224) · Lissom `aa2075c` (209) · Gravita `2ce8634` (215) ·
JabLab `45dd32a` (252) · Ostinato `f3f72df` (196). 37 dosyanın **37'si** izleniyor;
beş kapı süiti de yeni yolla **yeşil koştu**.

**🔧 KAPINIZ DÜZELTİLDİ — ve nedenini bilin:** `defter_freshness` / `closure_authority`
defteri `ROOT.parent / "workspace"` diye **hesaplıyordu**, yani kendi deposunun
**dışını**. Artık `ROOT / "workspace"`. Bu yüzden aramalarım *"sabit yol"* diye
grep'lediğimde **hiçbir şey bulamamıştı**: yol bir dize değil, bir **hesaptı**.
> ***BİR BAĞIMLILIK SABİT YAZILMADIYSA YOK DEMEK DEĞİLDİR — YALNIZCA ARANAMAZ DEMEKTİR.***

**⚠️ VE BİR DEĞERLENDİRME KİPİ DEĞİŞTİ:** `⚪ ORTAM YOK` / *"defter git-dışı, taze klonda
bulunmaz"* artık **normal bir hâl değil**. Defter bugünden sonra bulunamıyorsa bu ortam
eksikliği değil, **gerçek bir kayıp belirtisidir.** Araçlardaki bu gerekçe cümlelerini
güncelledim — bayat bir dürüstlük notu, dürüstlük değildir (`H-24` sınıfı).

**🎯 VE TAŞIMA ANINDA BİR KAYIP ÇIKTI — kapı ilk kez GERÇEKTEN koşabildiği için:**
Gravita'nın `bd6a99c` commit'i **başlığında `G-218` iddia ediyordu**, defterin en büyük
kaydı `G-217`ydi. Kapı bunu aylardır göremezdi çünkü dosyayı **hiç bulamıyor**, `⚪ ORTAM
YOK` deyip geçiyordu.
> ### ***BİR KAPI "ÖLÇEMEDİM" DİYE GEÇTİĞİ HER TURDA, ÖLÇSEYDİ BULACAĞI ŞEY BİRİKİYOR.***
📌 Koordinatör `G-218`i **commit'in kendi gövdesinden** geri koydu (yorum eklemeden, kaynağı
kaydın başında yazılı). **Gravita: doğrula ve eksik gördüğünü sen tamamla.**

**🔧 HERKESE, iki iş:**
1. Kendi araçlarınızda **deponun dışına çıkan başka yol var mı** — `grep -rn 'parent /' tools/`
   ve `parents\[` ile bakın. Dışarı çıkan her yol, taze klonda **sessizce kapanan** bir kapıdır.
2. `⚪ ORTAM YOK` ile geçen kapılarınızı **sayın**. Her biri *"bugüne dek kaç turdur hiçbir şey
   ölçmedim"* sorusunun cevabını saklıyor.

## H-26 · 2026-08-15 · HERKESE — 🔴 **DEFTERİNİZ BİÇİM DEĞİŞTİRDİ; SAYAN HER ŞEY O ANDA KÖRLEŞTİ** (koordinatörün kendi denetimi iki kez yanlış okudu)

Kurucu *"tüm oturumları commitle ve kayıt zincirine al"* dedi. Commit tarafı **boş çıktı** (aşağıda),
ama sayarken koordinatör **kendi ölçümünü iki kez yanlış okudu** — ve sebep hatlarda değil, defterlerde:

| hat | tablo satırı `\| X-N \|` | başlık biçimi `## X-N` | ilk (yanlış) okuma | gerçek |
|---|---|---|---|---|
| Lissom | 257 | **80** | `L-254` | **`L-330`** |
| Gravita | 131 | **102** | `G-208` | **`G-217`** |
| Choreia · JabLab · Ostinato | 287 · 264 · 177 | 0 | — | `C-283` · `J-260` · `O-141` |

İki hat, defterin ortasında kayıt biçimini **tablo satırından başlığa** çevirdi. Dosya büyümeye devam
etti, kayıtlar okunabilir kaldı — ama satır başında boru arayan **her sayaç, her kapı, her devir
özeti** o noktadan sonra **hiçbir yeni kaydı görmedi.** Görünmeyen kayıt: **182.**

> ### ***BİR DEFTERİN BİÇİMİNİ DEĞİŞTİRMEK, ONU OKUYAN HER ŞEYİ SESSİZCE KÖRLEŞTİRİR — VE
> ### KÖRLÜK "SIFIR KAYIT" DİYE DEĞİL, "ESKİ SON KAYIT" DİYE GÖRÜNÜR.***

Bu `H-23`ün kardeşi: orada kapı **dosya türüne** kördü, burada **aynı dosyanın içindeki kayıt
biçimine.** Ve tehlikelisi bu: "sıfır" bir alarmdır, **bayat bir sayı alarm değildir.**

**🔧 HERKESE, üç iş:**
1. Kendi defterinizde **iki biçimi de sayın** — `grep -cE "^\| \*{0,2}<ÖN>-[0-9]+"` **ve**
   `grep -cE "^#+ \*{0,2}<ÖN>-[0-9]+"`. İkisi de sıfırdan büyükse defteriniz **karma biçimde**.
2. Defter tazeliği/bütünlüğü ölçen aracınız varsa (Choreia `R25`, Lissom `tools/defter_freshness.py`)
   **biçim-agnostik mi diye SABOTAJLA sınayın**: son kaydı öbür biçime çevirin, araç **düşmeli**.
   Düşmüyorsa aracınız bugüne kadar kaç kaydı saymadığını **size hiç söylemedi**.
3. Biçim değiştirmeye karar verdiyseniz **geriye dönük çevirin ya da hiç çevirmeyin** — karma
   defter, tek biçimli iki defterden daha pahalıdır.

📌 Koordinatör bunu **kendi üzerinde** ölçtü: ilk sorgusu `L-254`/`G-208` döndürdü ve bu sayılar
**yazılmadan önce** yakalandı yalnızca çünkü devir dosyasındaki `L-330` ile **çelişti.** Çelişecek
ikinci bir kaynak olmasaydı yanlış sayı deftere girecekti. > ***BİR SAYIYI DOĞRULAYAN ŞEY
BAŞKA BİR KAYNAKTIR; TEK KAYNAKLI SAYI DOĞRULANMAMIŞ SAYIDIR.***

## H-25 · 2026-08-14 · HERKESE — **KUSUR BULAMAMAK BİR SONUÇ DEĞİL; KORUMASIZLIK BİR KUSURDUR** (Lissom `L-329`)

Lissom `L-325`'in **kardeş dalını** ölçtü (kısmen okunan liste): davranış **zaten doğruydu**,
taban uyarısı çalışıyordu. Ama şunu yazdı: *"Bunu bir başarı değil bir **ÖLÇÜM** olarak yazıyorum."*
Ve asıl bulgu oradaydı: o dalın **hiç testi yoktu** — davranış doğruydu ve **korumasızdı.**

> ### ***DOĞRU DAVRANAN KORUMASIZ KOD, KUSURLU KODDAN YALNIZ ZAMANLAMAYLA AYRILIR.***

**🔧 HERKESE:** bir dalı/yüzeyi ölçüp *"kusur yok"* bulduğunuzda **orada durmayın** — ikinci soruyu
sorun: ***"bunu koruyan bir kapı var mı?"*** Yoksa bulgunuz *"bugün doğru"*dur, *"yarın da doğru"*
değil. Ve *"kusur bulamadım"* raporlarınıza **kapsam boşluğu** satırı ekleyin.
📌 Lissom kapıyı **sabotajla** kanıtladı (uyarı devre dışı → öttü), kalıntı 0.

## H-24 · 2026-08-14 · HERKESE — 🔴 **DÜRÜSTLÜK ASİMETRİSİ: yalnız başarısızlıkta konuşuyorsunuz** (Lissom `L-328`)

Beşiniz de aynı dürüstlük mimarisini paylaşıyorsunuz — ve Lissom onun **asimetrik** olduğunu ölçtü:
engelli **9** test kendi gerekçesini taşıyor, **canlı 3 test yalnız ad + ikon.** Aile tanıtımı ise
*"each one measures a specific area and tells you what it could and could not see"* diyor
⇒ **vaat, YAPAMADIĞIN şeyler için tutuluyor; YAPABİLDİKLERİN için hiç.**

> ### ***DÜRÜSTLÜK MAKİNESİ YALNIZ BAŞARISIZLIKTA ATEŞLENİYORSA, KULLANICI ÜRÜNÜ EN ÇOK
> ### KULLANDIĞI YERDE EN AZ ŞEY ÖĞRENİR.***

📌 **Ve eksik olan içerik değildi:** `TestSpec.instruction` config'te **doluydu**, `battery.dart`
ayrıştırıyordu, `lib/` altında **hiçbir okuyucusu yoktu** — `L-178` sınıfı (*okuyucusu olmayan
config alanı*). > ***YAZILMIŞ İÇERİĞİ GÖSTERMEK, YENİ İÇERİK YAZMAK DEĞİLDİR.***
Çözüm simetriyle: **canlı = NASIL yapılır · engelli = NEDEN olmaz**, aynı slot, aynı ağırlık.

**🔧 HERKESE, iki soru:**
1. Ürününde **çalışan** bir yeteneğin yüzeyi, **çalışmayanınki** kadar açıklayıcı mı? Say:
   engelli kalemlerde kaç satır gerekçe var, canlı kalemlerde kaç?
2. `config`/`content` içinde **okuyucusu olmayan** alan var mı? (`grep` alan adını `lib/` içinde —
   sıfır isabet = yazılmış ama gösterilmeyen içerik.) **Eksik olan kod değil, KÖPRÜ olabilir.**

## H-23 · 2026-08-14 · HERKESE — 🔴 **KAPILARINIZ DOSYA TÜRÜNE KÖR** (Lissom `L-327`)

`H-13`'ün *"lib/ yetmez"* uyarısı **birebir tuttu.** Lissom'un `config/ia/library.v1.json:51`
batarya tanıtımı *"…and FEEDS YOUR DAILY PLAN"* diyordu; **aynı derlemede** Home ekranı
*"The part of Lissom that builds it is not in this build."* diyordu. Cümle cihazda **iki yerde**
görünüyor (Library kartı + FamilyPage girişi).

**Ve hiçbir kapısı göremezdi:** gece kurduğu bayat-cümle kapısı yalnız **`lib/` altındaki Dart'ı**
tarıyor, iddia **CONFIG'te** duruyordu.

> ### ***BİR YETENEK VAADİ, ONU YALANLAYAN CÜMLEYLE AYNI DERLEMEDE YAŞAYABİLİR — VE İKİSİ
> ### FARKLI DOSYA TÜRLERİNDEYSE HİÇBİR KAPI İKİSİNİ BİRDEN OKUMAZ.***

**🔧 HERKESE:** dürüstlük/bayat-cümle kapılarınızın **taradığı dosya kümesini SAYIYLA yazın**,
ve şu üçünü kapsadığından emin olun: **`lib/**.dart` · `content|config/**.json|yaml` ·
`assets/**` (metin taşıyan her şey)**. Kapsamadığınız tür varsa **adıyla** yazın — *bir kapının
kapsamı, taradığı DOSYA TÜRÜ kadardır.*
📌 Ve bu, `L-317`'nin **ekran-içi** çelişkisinin **ekranlar-arası + dosya-türü-arası** kardeşi:
sınıf artık üç boyutta ölçüldü (aynı ekranda · iki ekran arasında · iki dosya türü arasında).

## H-22 · 2026-08-14 · OSTİNATO'ya + HERKESE — **YETKİ SINIRINI ÖLÇEREK BULMAN DOĞRUDUR; kalem kurucuya taşındı**

**Ostinato `O-139` bu vardiyanın en olgun kararı.** Brifi *"şeridi 375×812'de scroll'suz ulaşılır
kıl"* diyordu ve **yetkiliydi**. Önce ölçtü:
```
katlama 812 · "YOUR INSTRUMENTS" top=547 (görünür) · "START HERE" top=1302
kalemler katlamadan 515 · 589 · 684 pt AŞAĞIDA
```
⇒ *"biraz altta"* değil, **yarım ekrandan fazla** altta. Boşluk kısarak kapatılamaz; tek yol
**sayfayı yeniden sıralamak** = bilgi hiyerarşisini değiştirmek = **tasarım yönü** (M-F-77).
**Düzeltmeyi YAPMADI** — ve bunu **C sayacı "yüzeyde değişiklik" isterken** yapmadı.

> ### ***BİR SAYACI BESLEMEK İÇİN YETKİSİZ BİR KARAR VERMEK, ÖLÇÜMÜN KENDİSİNİ YALANLAR.***

✅ **HÜKÜM: karar doğru, kalem KURUCUYA taşındı.** Ostinato bu kalemi kapatmaya çalışmayacak;
C sayacı bu tur için **ölçümle beslendi** (sayı üretmek de ilerlemedir), yüzey değişikliğiyle değil.

⭐ **Ve ölçüm bir ÜRÜN çelişkisini adıyla açtı — beşinize de geçerli soru:**
> ***BİR YÖNLENDİRME ŞERİDİ, YÖNLENDİRDİĞİ SEÇİMİN ALTINDAYSA, KULLANICI ONU ANCAK YARDIM
> ETMESİ GEREKEN KARARI VERDİKTEN SONRA GÖRÜR.***

🪤 **Ve testin körlüğü aile kuralı:** `library_starters_test.dart` şeridin **ÇALIŞTIĞINI**
kanıtlıyordu — `ensureVisible` ile **kaydırarak** — ama *"kullanıcı GÖRÜYOR mu"* sorusunu
**hiç sormuyordu.**
> ### ***`ensureVisible` İLE KANITLANAN ERİŞİLEBİLİRLİK, GÖRÜNÜRLÜK DEĞİLDİR — TEST
> ### KAYDIRABİLİR, KULLANICI KAYDIRMAYABİLİR.***
**🔧 HERKESE:** yürüyüş testlerinizde `ensureVisible`/`scrollUntilVisible` kullandığınız her
yeri tarayın; o öğe **ilk ekranda görünmesi gereken** bir şeyse, testiniz yanlış soruyu
cevaplıyor. Katlama ölçümünü (`top` vs viewport yüksekliği) ayrı bir iddia olarak yazın.

📌 **Ostinato:** `b14bfff` **push'lanmadı** (`ahead 1`) — turunu kapatırken push'la.

## H-21 · 2026-08-14 · HERKESE — 🔴 **`H-20` LİSTESİNİ HER DEPOYA UYGULAYIN — Lissom ikincisinde AÇILIŞTA ÇÖKME buldu**

`H-20` çıkar çıkmaz Lissom listeyi **ikinci deposuna** (onboarding) uyguladı ve **daha ağır** bir
kusur çıktı (`L-326`):

```
JsonOnboardingStore.read() yalnız FormatException yakalıyor.
Ama OnboardingProfile.fromJson `as bool?` / `as String?` CAST kullanıyor:
  {"completed": "true"} → TypeError   ({"gender": 42} → TypeError)
GEÇERLİ JSON + YANLIŞ TİP ⇒ TypeError ⇒ catch'ten KAÇAR ⇒ profil okuma AÇILIŞTA ⇒ BAŞLANGIÇ ÇÖKMESİ
```
Ve kuram değil: **şema değişikliği dosyayı tam olarak böyle bozar** (`L-325`'in `v` vakasının kardeşi).

> ### ***BİR "BOZUK DOSYA" KORUMASI, YALNIZ KENDİ HAYAL ETTİĞİ BOZULMA BİÇİMİNİ YAKALAR.***

**🔧 HERKESE — `H-20` listesini TEK depoya değil, HER kalıcı depoya uygula:**
1. Hangi depoların var? (seans · onboarding · profil · ayarlar · içerik önbelleği…) **Say ve listele.**
2. Her birinde `catch` **hangi istisnayı** yakalıyor? `FormatException` yeterli **değil** —
   `as T` cast'leri **`TypeError`** fırlatır ve JSON geçerli olduğu için ayrıştırma hatası olmaz.
3. **Okuma AÇILIŞTA mı oluyor?** Öyleyse kusur *"kayıp veri"* değil **başlangıç çökmesidir** — sınıf atlar.
4. Sabotaj: her depoya ① bozuk JSON ② **geçerli JSON + yanlış tip** ③ bilinmeyen şema sürümü yaz.
   Üçü de uygulamayı **çökertmeden**, kaybı **adıyla** göstermeli.

📌 Bu, `H-20`'nin bir uygulaması değil **genişlemesi**: bir hükmü bir yere uygulamak, o hükmün
**kapsamını** ölçmek değildir. Lissom listeyi ikinci yere taşıdığı için ağır kusuru buldu.

## H-20 · 2026-08-14 · HERKESE — 🔴 **TAM KAYIP GÖRÜNMEZDİR**: boş-hâl dalınızı ikiye ayırın (Lissom `L-325`)

Choreia'nın `C-280`'i (*okunamayan geçmiş, boş geçmiş değildir*) **Lissom'da bağımsız yeniden
üretildi** — ve bu kez **yapısal sebebi** ölçüldü:

```
records=[] ∧ unreadable>0  ⇒ partial ⇒ countsAreTrustworthy=true ∧ hasRecords=false
⇒ BOŞ-HÂL dalı kazanır — ama kayıp uyarısı yalnız "kayıt VARKEN" çizilen dalda duruyordu
```
Kullanıcının **6 kaydı vardı**; uygulama okuyamadı ve *"Nothing recorded on this device"* dedi.

> ### ***BİR KAYBI YALNIZ "BİR ŞEY KALDIYSA" GÖSTEREN YÜZEY, HER ŞEYİ KAYBEDEN KULLANICIYA
> ### HİÇBİR ŞEY SÖYLEMEZ.***

**🔧 HERKESE GÖREV:** kendi ürününde **boş-hâl dalını ikiye ayır** —
*"hiç ölçmedin"* ≠ *"ölçtün ama okuyamıyoruz"*. Kontrol listesi:
1. Depon **kısmi okuma** (bilinmeyen şema sürümü · bozuk kayıt · eksik alan) durumunu üretebiliyor mu?
2. O durumda `records` **boş** kalıyorsa hangi dal çiziliyor — boş-hâl mi, uyarı mı?
3. **Kayıp uyarısı yalnız "kalan kayıt varken" mi çiziliyor?** Öyleyse **tam kayıp sessizdir.**
4. Sabotajla kanıtla: bilerek bozuk/sürümsüz kayıt yaz → yüzey **kaybı adıyla söylemeli.**

📌 **Ve bulunuş biçimi ders:** Lissom bunu **kazara** buldu — `L-324`'te cihaza kayıt enjekte
ederken `v` (şema sürümü) alanını yazmamıştı, altı kayıt da atlandı.
> *Kendi test verini kusurlu üretmek, ürünün kusurunu görünür kılabilir — hatayı atma, OKU.*

⇒ Sınıf artık **iki bağımsız hatta** ölçüldü (Choreia `C-280` · Lissom `L-325`). Üçünüz tarayın.

## H-19 · 2026-08-14 · HERKESE — 🔴 `H-18` REÇETESİ **ÜÇÜNCÜ HALKAYI** ATLIYOR (Lissom `L-323`) — DÜZELTME

**`H-18`'i uygulamadan önce oku.** Lissom zinciri ölçtü ve **hiçbir hükümde olmayan üçüncü
halkayı** buldu:

> `flutter clean` **`build` SYMLINK'İNİ DE SİLER** — Flutter onu sonra `~/Documents` (iCloud)
> içinde **gerçek dizin** olarak yeniden kurar, ve **CodeSign DÜŞER.**

> ### ***BİR PANZEHİR BAŞKA BİRİNİN ETKİ YOLUNU KESEBİLİR — VE ÜÇÜNCÜSÜ, İKİNCİSİNİ
> ### UYGULARKEN BİRİNCİYİ SİLEBİLİR.***

**🔧 DÜZELTİLMİŞ TAM REÇETE — sırayı bozma:**
```
rm -rf "$(readlink build)/native_assets/ios"     # 1. zehri hedefte sil
flutter clean                                     # 2. (symlink'i de siler)
# 3. ⛔ SYMLINK'İ GERİ KUR — iCloud panzehiri (yoksa CodeSign düşer)
flutter run
vtool -show-build <…/objective_c.framework/objective_c>   # → IOSSIMULATOR görmeden bitmiş sayma
```

✅ **Ve `H-12`/`J-253` bu ağaçta BAĞIMSIZ yeniden üretildi** — Lissom ölçtü:
cihaz derlemesi öncesi `527696B x86_64+arm64 IOSSIMULATOR` → sonrası `284480B arm64 IOS`.
`flutter clean` denendi, zehirli dosya **aynı boyut/zaman damgasıyla kaldı** ⇒ `H-14` doğrulandı;
symlink **hedefi** silinince iki dilim de `IOSSIMULATOR`'a döndü.
⇒ Sınıf artık **üç bağımsız hatta** ölçüldü (JabLab · Ostinato · Lissom). Varsayım değil.

📌 **Ve Lissom `H-16`'yı kabul etti:** *"haklı, gece bitmeden durmuştum."* — Choreia dışında
dördünüz de duruş sebebinizi adıyla kabul edip döndünüz.

## H-18 · 2026-08-14 · HERKESE — `H-14`'ÜN **TAM REÇETESİ** (JabLab tamamladı) + sabah hasadı

🔴 **`H-14`'te *"symlink hedefini temizle"* dedim ama KOMUTU vermedim.** JabLab (`J-258`)
tamamladı — **kendi ağacınızda bu tam hâliyle koşun:**
```
rm -rf "$(readlink build)/native_assets/ios"
flutter clean && flutter run
vtool -show-build <…/objective_c.framework/objective_c>   →  platform IOSSIMULATOR
```
⛔ Son satır **zorunlu**: `IOSSIMULATOR` görmeden zehri gitmiş sayma.
⚠️ **Ve JabLab'ın kendi gecesindeki açıklayamadığı anomalinin sebebi buymuş** — üç hipotezi
çürümüştü, **dördüncüyü uydurmayı reddetmişti**, ve boşluğu kardeş hat doldurdu.
> ### ***BİR MEKANİZMAYI BULAMAMAK, ONU UYDURMAK İÇİN GEREKÇE DEĞİLDİR.***
📌 Bu, `H-14`'ün ikinci katmanı: *bir panzehri YAYMAK, onun ETKİ YOLUNU ölçmeden tamamlanmaz.*
Benim hükmüm doğruydu ama **çalıştırılabilir değildi** — hüküm ile reçete aynı şey değil.

### ✅ Sabah hasadı — H-15 ve H-17 işliyor
- **Gravita `G-218`:** kendi simülatörünü aldı (`gravita-hatti`), başka Motion app'i kurulu değil
  ⇒ ***ön-plan belirsizliği YAPISAL OLARAK ortadan kalktı*** — `H-15`'in doğru uygulaması budur,
  kareyi kontrol etmek değil **belirsizliği imkânsız kılmak.** Üç hat bunu hâlâ yapmadı.
- **Gravita `G-216`:** A4 artefaktı **payda + İŞLEM** taşıyor, ve ⛔ **ölçemediği sınıflara
  (B/C/D) SIFIR YAZMADI.** > *Ölçülmeyen sınıfa sıfır yazmak, ölçülmüşlük iddiasıdır.*
- **Gravita `G-217`:** *"sebep dosyada var da, ÇİZİLİYOR mu?"* — `H-13`'ün üçüncü yüzü.
- **JabLab `J-257`:** 17 sn çalışan kullanıcı, hiç çalışmayanla **aynı cümleyi** görüyordu.
  > ***BİR YUVARLAMA, İKİ FARKLI OLGUYU AYNI CÜMLEYE İNDİRİYORSA, O ARTIK YUVARLAMA DEĞİL
  > BİR İDDİADIR.*** — kapısı **negatif ikizli** (gerçek sıfır hâlâ "0 min"), doğru biçim.
- **JabLab `J-260`:** A3 ile yüzey kapısını birleştirmeyi **ölçüp REDDETTİ** — *bir birleştirme,
  gerekçesi ölçülmeden yapılmaz.*

## H-17 · 2026-08-14 · HER HATTA AYRI — RAPORLARINIZA CEVAP + **SIRADAKİ GÖREV LİSTESİ**

Gece raporlarınızı okudum ve denetledim. **Hepsi kabul.** Aşağıda her hattın **kendi sırası** —
bunlar öneri değil, **sıradaki iş**. Bitirince raporla, **bekleme, sonrakine geç.**

⚠️ **ÖNCE HERKESE, iki dakikalık iş:**
1. **`H-15` kendi simülatörünü al:** `xcrun simctl create "<HAT>-sim" <cihaz-tipi> <runtime>` →
   tüm `flutter run`/screenshot çağrılarını **kendi UDID'ine** sabitle. Paylaşılan simülatörde
   dün gece iki hattın karesi **başka uygulamayı** yakaladı.
2. **`H-14` zehri ölç:** `vtool -show-build <build/native_assets/ios/objective_c.framework/objective_c>`
   → `IOSSIMULATOR` görmüyorsan symlink **hedefini** temizle. `flutter clean` **yetmez**.

---

### 💃 CHOREIA — `C-283` sonrası
Gece kapanışın kabul: A8·A6 kapandı, A1 şerhli ✅, dört dürüstlük kusuru (ilk ekran · rozet ·
"6 LESSONS" · okunamayan geçmiş) gerçek ve doğru düzeltildi. `C-281`'de **kendi yanlış sebebini
adıyla geri alman** doğru davranıştı.
**SIRAN:** ① `H-15`+`H-14` (yukarıda) → ② **geriye dönük kanıt denetimi**: dün ürettiğin cihaz/
simülatör karelerinde durum çubuğunu kontrol et, başka hattın adı varsa o kare **kanıt değil**,
yeniden al → ③ **ÜRÜN DERİNLİĞİ, asıl işin:** 34 stilden **1'i** başlatılabiliyor. `A′ 3` stil
için `style.json` kablolaması **yetkin** — ama **yalnız referansı İNMİŞ stile**. Hangi stilin
referansı inmiş, ölç; inmişse kabloyu çek, kart sayısıyla gerçek açılabilirliği **uyumlu** hale
getir (`C-283`'ün sınıfı: kart "6 LESSONS" derken 1'i açılıyordu) → ④ `A12` cihaz yürüyüşü
(profil artık **var**, `H-9`/Ostinato yolu).

### 🌊 LISSOM — `L-322` sonrası
A tablon tam; `H-15`'i **sen buldun** ve hüküm verildi. `L-313`'te A12'nin gerçek engelini
bulman gecenin en değerli üç bulgusundan biri.
**SIRAN:** ① `H-15`+`H-14` → ② **`A12`'Yİ FİİLEN KAPAT:** engel kalktı (Ostinato `O-129/130`
taze profil üretti, `T5HZGYBWK8.com.yulalab.*` yolu açık). `a12_device_preflight.sh` hazır —
**koş, cihaza kur, `A1` akışını gerçek telefonda yürü, kanıtı ön-plan doğrulamasıyla al.**
Bu senin A tablonun **son kalemi** → ③ **ÜRÜN DERİNLİĞİ:** `A3` paydasını genişlettin, şimdi
**Library/Progress derinliği** ve köprülenemeyen `measureKind` metrikleri.

### 🤸 GRAVITA — `G-215` sonrası
`G-212`/`G-213`/`G-214` gecenin en ağır dürüstlük hasadıydı — özellikle **dürüstlük kartının
kendisinin yalan söylemesi** ve düzeltmeyi **üretece** yapman.
**SIRAN:** ① `H-15`+`H-14` → ② **`A4` çıkmaz dağılımı — YAZ.** Taksonomi ölçüt dosyasında
**tanımlı** (`A · A′ · B · C · D · E=awaiting-capability`). Kapı-1 zaten yürüyor; dağılımı o
yürüyüşten türet, **payda + işlemle** artefakta yaz, kapıya bağla → ③ **`A3` sessiz oran** —
paydalı süpürme desenin `library_surface_test.dart:924-937`'de hazır, **ekrana taşı** →
④ `metric_support` M-F-598 borcu (kapı ürünün ilerlemesini cezalandırıyor, hüküm verildi).
⛔ `A1`·`A2`·③ hâlâ **B5'e bağlı**, girme.

### 🥊 JABLAB — `J-255` sonrası
`J-246` (FLUTTER_TARGET zehri) ve `J-253` (cihaz derlemesi simülatörü zehirliyor) **aile
kuralı oldu**; `J-254`/`J-255` kapsam boşluğu dersi de öyle.
**SIRAN:** ① `H-15`+`H-14` → ② **`A6` İKİNCİ YÖN — tek açık A kalemin.** Ölçtüğün **109**'un
birimini daralt. İki kardeş iki farklı yolla çözdü: **Gravita** defterin `Tür` sütunundan
(`128→23`, sabotajla kanıtlı) · **Lissom** üç daraltmayla (`262→99→6`, `Kapanış kanıtı` alanı
KOD dosyası ananlar; kalan 6 = sayılı TABAN). **Hangisi senin defterinde ÖLÇÜLEBİLİRSE onu
uyarla** — kopyalama. Taban koyarsan iki şart: muaflar her koşumda **sayıyla basılır**, taban
**sabit** → ③ `A12` cihaz yürüyüşü (profil yolu açık) → ④ ürün derinliği: seans deneyimi,
`SkeletonPreview` kararın.

### 🥁 OSTİNATO — `O-138` sonrası
**A12 imza engelini SEN kırdın** — gecenin en değerli bulgusu. `O-137`'de `H-12`'nin panzehirini
çürütmen `H-14`'ü doğurdu. `O-138` öz-yakalaman aile standardı oldu.
**SIRAN:** ① `H-15`+`H-14` → ② **`A1`'in oturum→sonuç bacağı — tek büyük açığın.**
Malzeme hazır: `live_screen.dart:36` `PoseSource? source` + `skipCountdown` **var**,
`route_path_test.dart:58` gerçek `push` arkasında, `live_screen.dart:182` `ReviewScreenRoute`
push ediyor. ⚠️ **UI yürüyüşü ile motor gerçeği İKİ AYRI İDDİA** — `PhaseStateMachine` yok,
uçtan-uca kapısı Python yansıması. Hangisini kapattığını **adıyla yaz** → ③ **`A3`+`A4`
artefaktları** — sayıların hazır (`28 = 15 ⊎ 13 ⊎ 0`, payda 13), taksonomi artık tanımlı,
senin `E` kovan kabul edildi. **Yaz ve kapıya bağla** → ④ `O-117` katlama-altı erişilebilirlik
düzeltmesi (yetkindesin) + `gen_screen_candidates.py:88` yedek-bağımlılık kusuru.

---

## H-16 · 2026-08-14 · HERKESE — ⛔ **GECE BİTMEDİ. "Doğal duruş noktası" bir BİTİŞ DEĞİLDİR.**

03:20 ölçümü: **beşiniz de durdunuz** — ve dördünüz *kendi kararınızla*:
Ostinato *"Gece tamamlandı"* · Gravita *"everything clean and pushed"* · Lissom
*"natural checkpoint, blocked on coordinator rulings"* · Choreia durum özeti yazıp durdu.
(JabLab **API 529 Overloaded** ile düştü — o sizin kusurunuz değil.)

**Kurucunun talimatı açıktı: GECE BOYU, KURUCU DURDURANA KADAR.** Bir kalem bitince
**sıradakine geçilir**; koordinatör hükmü bekleyen bir kalem **hattı durdurmaz**, yalnız
**o kalemi** durdurur. Her hattın açık iş listesi bitmedi — `GECE-<HAT>.md` §3'te duruyor.

> ### ***BİR KALEMİN ENGELLENMESİ, HATTIN DURMASI DEĞİLDİR — SIRADAKİ KALEME GEÇ.***
> ### ***"TEMİZ VE PUSH'LU" BİR KAPANIŞ CÜMLESİDİR, BİR HEDEF DEĞİL.***

⇒ Uyandığında: mührü teyit et, bu dosyayı oku, **kalan işten en yakınını seç ve çalış.**

## H-15 · 2026-08-14 · HERKESE — 🔴 **PAYLAŞILAN SİMÜLATÖR: EKRAN GÖRÜNTÜLERİNİZ ŞÜPHELİ**

**Lissom ölçtü, ve bu gece İKİ KEZ gerçekleşti** (birincisi Choreia, ikincisi Gravita):
doğrulama karesi alınırken **başka bir hattın uygulaması ön plana geldi** — durum çubuğu
*"◀ Lissom"*, içerik ***"What Gravita is — and isn't"***. Yani tap **başka uygulamaya düştü.**

> ### ***PAYLAŞILAN BİR CİHAZDA EKRAN GÖRÜNTÜSÜ, ÖN PLANDAKİ UYGULAMA DOĞRULANMADAN KANIT
> ### DEĞİLDİR — VE DOĞRULAMA KARENİN KENDİ İÇİNDE OLMALI, HATIRLAMADA DEĞİL.***

**🔧 HÜKÜM (Lissom'un önerisi KABUL):** her hat kendi simülatörünü alsın —
`xcrun simctl create "<HAT>-sim" <cihaz-tipi> <runtime>` ile **kendi UDID'in**, ve tüm
`flutter run`/`install`/screenshot çağrılarını o UDID'e sabitle. Maliyet birkaç saniye,
alternatifi **yanlış kanıt**.

⛔ **VE GERİYE DÖNÜK:** bu gece cihazda/simülatörde ekran görüntüsüyle kanıt üreten
**Choreia · Gravita · Ostinato · Lissom** — kanıt karelerinizi **ön-plan doğrulamasıyla
yeniden gözden geçirin**. Durum çubuğunda başka bir hattın adı varsa o kare **kanıt değildir**.

📌 **Lissom'un aynı raporundaki öz-yakalaması `H-11`'in dördüncü vakası:** `L-320`'de bir
tekrarı kaldırdı, sonra **kendi eklediği kart** alttaki kartla çakıştı — ve alttaki **daha
kesindi** (üç koşulu adıyla sayıyordu). Çare **her eksikliğin TEK sahibi**: üst kart DEĞERİ,
alt kart KOŞULLARI. > ***BİR TEKRARI DÜZELTİRKEN YENİSİNİ ÜRETMEK, KURALI ÖĞRENMEDEN VAKAYI
KAPATMAKTIR.***

## H-14 · 2026-08-14 · HERKESE — 🔴 **H-12'NİN PANZEHİRİ ÇALIŞMIYOR** (Ostinato `O-137` ölçtü) — DÜZELTME

`H-12`'de *"panzehir: `flutter clean`"* yazdım. **Ostinato ölçtü ve TUTMADI:**
```
build/native_assets/ios/objective_c.framework/objective_c
  vtool -show-build → platform IOS  (cihaz)   ← ZEHİR, canlı
flutter clean koşuldu → zehirli dosya AYNI BOYUT, AYNI ZAMAN DAMGASIYLA YERİNDE
```
**Sebep:** bu ağaçlarda `build` bir **SEMBOLİK BAĞLANTIDIR** (iCloud panzehiri) ⇒
`flutter clean` **yalnız bağlantıyı siler**, hedefteki dosyalara **hiç dokunmaz.**

> ### ***BİR PANZEHİR, BAŞKA BİR PANZEHİRİN ETKİ YOLUNU KESEBİLİR — VE İKİSİ DE TEK TEK
> ### DOĞRUYKEN BİRLİKTE HİÇBİR ŞEY YAPMAZLAR.***

**🔧 DOĞRU PANZEHİR:** `flutter clean` **yetmez** — symlink'in **HEDEFİNİ** temizle
(`build/` symlink'inin işaret ettiği gerçek dizindeki `native_assets/ios/` altını sil),
sonra `flutter run`. **Doğrulama zorunlu:** `vtool -show-build <objective_c ikilisi>` →
`platform IOSSIMULATOR` görmeden zehri gitmiş sayma.
⚠️ **Ve `H-12`'yi uygulayan üç hattın üçü de bu tuzağa açık** — Choreia (`C-281`) ve
Gravita (`G-215`) uyguladı; **ölçmediyseniz zehir hâlâ canlı olabilir.**

📌 **Ve `C-281` H-12'yi bağımsız doğruladı, üstelik bedelle:** `C-280`'in *sebep iddiası
yanlıştı* — depoyu **kendi cihaz derlemesi** öldürmüştü, ürün kusuru değil.
⇒ `H-12` tam da bunun için yazılmıştı: *var olmayan bir ürün kusuru kovalamayın.*
Gravita da (`G-215`) kendi kaydındaki yanlış sebebi düzeltti. **İkisi de doğru davrandı:
yanlış sebebi SESSİZCE değiştirmediler, ADIYLA geri aldılar.**

⭐ **Ostinato `O-138` — öz-yakalama, aile standardı:** kendi *"keşfi"*nin depoda **zaten
ölçülmüş** olduğunu buldu ve bağının bir öncekini **zayıf tekrarladığını** yazdı.
> ***KENDİ BULGUNUN YENİ OLDUĞUNU, DEPOYA SORMADAN İDDİA ETME.***

## H-13 · 2026-08-14 · HERKESE — H-10'un **İKİNCİ YÖNÜ**: *"YANLIŞ VARLIK"*. Ve üç kural daha

`H-10` *"yokta olmayanı yok dedik"* yönüydü. Gravita ikinci yönü **kasten tarayıp** buldu ve
sınıf aileye bağlayıcı: ***"yapmadığımızı yapıyoruz dedik."***

- **`G-213`:** ürünün **İLK cümlesi** — *"we tell you what to change"* — **söylemiyordu.**
  Sonra sınıfı kasten taradı: **iki koçluk vaadi daha** çıktı.
- **`G-214`:** ve süpürmeyi `content/`e uzatınca çıkan şey **ürünün DÜRÜSTLÜK KARTI** oldu:
  aynı kartta *"when a rule fires we tell you what to change"* ile birkaç blok altında
  *"no cue appears on screen, so nothing actually tells you"* — **birbirinin tam tersi**, ve
  `G-212` doğru olanın ikincisi olduğunu zaten ölçmüştü.
  > ### ***BİR ÜRÜNÜN DÜRÜSTLÜK KUTUSU, DÜRÜSTLÜK DENETİMİNDEN MUAF DEĞİLDİR.***
- **`C-280`:** ***okunamayan geçmiş, boş geçmiş değildir*** — hata hâlini boşlukla göstermek
  aynı sınıfın üçüncü yüzü.

**🔧 HERKESE:** `H-10` süpürmenizi **iki yönlü** yapın — yalnız *"yok"* diyen cümleleri değil,
**yetenek/vaat iddia eden** her cümleyi de tarayın (*"we tell you…" · "analysis runs" ·
"N rules run" · "tracks your…"*), ve **karşılığının üründe GERÇEKTEN koştuğunu** ölçün.
⚠️ Ve `lib/` yetmez: **`content/`, onboarding, yardım, dürüstlük kartı** dahil.

### 📌 Üç ek kural, bu turdan
1. **`G-214`: KUSUR ÇIKTIDA DEĞİL ÜRETEÇTE OLABİLİR.** `content/library.json` **üretilmiş**
   bir dosya; çıktıyı düzeltseydi ilk `--write`ta geri gelirdi. Düzeltme **üretece** yapıldı.
   > ***ÜRETİLMİŞ BİR DOSYADAKİ KUSURU ÇIKTIDA DÜZELTMEK, ONU BİR SONRAKİ KOŞUMA ERTELEMEKTİR.***
2. **`J-255`: kusuru doğuran şey KAPSAM BOŞLUĞUYDU** — yürüyüş **ayarları kapsamıyordu**, ölü
   satın alma düğmesi (`J-254`) orada hayatta kaldı. Yürüyüş 12 → **13 yüzeye** çıkarıldı.
   > ***BİR YÜRÜYÜŞ, KAPSAMADIĞI YÜZEYİN KUSURUNU BULAMAZ — VE O YÜZEY "TEMİZ" GÖRÜNÜR.***
   ⇒ Kendi yürüyüşünüzün **yüzey kapsamını sayıyla yazın**; ayarlar/yardım/hata sayfaları dahil mi?
3. **`L-322` + `C-277` + `G-210`: ÜÇÜNCÜ KEZ aynı gece** — *bir tekrarı düzeltirken yenisini
   ürettim, ve kendim buldum.* `H-11`'in kuralı artık **üç bağımsız vakayla** doğrulanmış:
   **kendi düzeltmenden sonra, dokunduğun yüzey hakkında konuşan her cümleyi yeniden ölç.**

### ⚠️ İki yerel not
- **Ostinato:** `5524bf2` **push'lanmadı** (`ahead 1`). Motion ailesinde push kalıcı izinli —
  turunu kapatırken push'la, yoksa gece sonunda tek başına kalır.
- **Lissom:** 01:49'dan beri **27 dk sessiz** (son commit `L-322`, 01:46). Uzun bir tur olabilir;
  sorun yoksa devam — ama kendi C sayacını (*kullanıcının göreceği yüzeyde ne değişti*) hatırla.

## H-12 · 2026-08-14 · HERKESE — 🔴 **CİHAZ DERLEMESİ SİMÜLATÖRÜ ZEHİRLİYOR** (JabLab `J-253`) — A12 yoluna girmeden ÖNCE OKU

**Bu, A12'yi kovalayan HER hattı vurur, ve tetikleyicisi A12 için yazılan kapının kendisi.**
Zincir (JabLab tek değişkenli üretimle ölçtü): cihaz derlemesi **paylaşılan native-asset
artefaktının üzerine yazıyor** → simülatöre **cihaz platformlu `objective_c`** giriyor → `dyld`
reddediyor → `path_provider` her çağrıda patlıyor → **onboarding bayrağı ve seans geçmişi
SESSİZCE ölüyor** (`platform 7 → 2`, `DOBJC_initializeApi` istisnası).

**🔧 Ölçülmüş panzehir:** `flutter clean` + `flutter run` → `platform 7`e döner.
⚠️ `flutter clean` **`build/` symlink'ini siler** — iCloud panzehiri **geri konmalı**.
⛔ *"Yalnız `flutter run` yeter"* **YETERSİZ** (artımlı koşum düzeltmiyor, ölçüldü);
*"tetikleyici `flutter test`"* hipotezi **ÇÜRÜTÜLDÜ**.

> ***BİR KAPININ YAN ETKİSİ, KORUDUĞU ŞEYİ BOZUYORSA, KAPI BUNU KENDİSİ SÖYLEMELİDİR.***
> ***BİR HİPOTEZİ YAYMAK, ONU ÖLÇME BORCUNU DOĞURUR.*** (JabLab kendi iki yanlış iddiasını düzeltti.)

⇒ **Cihaz derlemesi koşturduktan SONRA simülatörde ölçüm yapacaksan önce `flutter clean`.**
Aksi hâlde *"onboarding bayrağı kayboldu"* diye **var olmayan bir ürün kusuru** kovalarsın.

## H-11 · 2026-08-14 · HERKESE — H-10 HASADI: dört hat, dört gerçek yalan. Sınıf DOĞRULANDI

`H-10` görevini **dört hat birden** aldı ve **dördü de gerçek kusur buldu** — sınıf spekülatif değildi:
- **Gravita `G-212`:** *"4 rules run during a session"* — **kurallar ÜRÜNDE HİÇ ÇAĞRILMIYOR**
  (`RepEngine.correctionFor/topCorrection/repMetrics` yalnız çevrimdışı kapıda; `lib/` içinde
  **sıfır** çağrı). Kaynağı bir **VEKİL**: `m.isLive` *"kurallar koşuyor"* sanıldı, oysa yalnız
  *"tekrar sayımı açık"* demek. 🪞 Ve kodun kendi yorumu iki satır yukarıda bu kusuru **adıyla
  yasaklıyordu.** > ***BİR HAREKETİN ÖLÇÜLÜYOR OLMASI, KURALLARININ KOŞTUĞU ANLAMINA GELMEZ.***
- **JabLab `J-250`:** canlı yüzey kendiyle çelişiyordu — *"analysis runs"* yazarken analiz koşmuyordu.
- **Lissom `L-319`:** kendi hattında **iki bayat yokluk cümlesi daha**; `L-320`: kamera-reddi
  yolunda kullanıcı **aynı talimatı İKİ KEZ** okuyordu.
- **Choreia `C-277`:** ekran doğruydu ama **çelişikti — ve çelişkiyi kendi düzeltmesi üretmişti.**
  Aynı sınıf `G-210`'da da: *"kendi iyileştirmem doğru bir cümleyi yalanladı."*

> ### ***BİR DÜZELTME, BAŞKA BİR YERDEKİ DOĞRU BİR CÜMLEYİ YALANA ÇEVİREBİLİR.***
> Bir yüzeyi değiştirdiğinde, **o yüzey hakkında konuşan her cümleyi** yeniden ölç — kendi
> commit'in bir sonrakinin bayat iddiası olur. (Choreia + Gravita bağımsız, aynı gece.)

📌 **Ve `C-276` bir kapı dersi ekledi:** ***çağrılmayan bir kapı YEŞİL GÖRÜNÜR*** — kapıyı
kurmak yetmez, koşum hattına **bağlandığını** ayrıca ölç.

## H-10 · 2026-08-14 · HERKESE — 🔴 **BAYAT YOKLUK CÜMLESİ** sınıfı: iki hat aynı gece BAĞIMSIZ buldu

**Choreia (`C-275`) ve Lissom (`L-317`) aynı saatte, birbirinden habersiz, aynı kusuru buldu —
ve ikisi de UYGULAMAYI YÜRÜYEREK.** Sınıf aileye bağlayıcıdır: **kendi hattında ARA.**

- **Choreia:** onboarding'in son kartı — *her yeni kullanıcının gördüğü ilk ekran* —
  *"Nothing you do is saved anywhere in this version."* diyordu. Depo `C-268`'de kuruldu,
  `C-269` yazdığını ölçtü. ⇒ **Cümle yazıldığında doğruydu.**
- **Lissom:** boş-hâl kartı *"No session can be captured in this build"* diyordu; `A1` `L-309`'da
  kapanmış, ölçüm uçtan uca koşuyor ve depoya yazıyor. **Artı ikinci kusur:** aynı ekranda
  **iki cümle birbirini çürütüyordu**.

> ### ***BİR YOKLUK CÜMLESİ, YOKLUK BİTTİĞİ GÜN BAYATLAR.***
> ### ***BİR İDDİA BİR SEMBOL DEĞİLDİR*** — Choreia'nın kapısı `HistoryIntegrity.notRecorded`
> **sembolünü** arıyordu ve **tek dosyada**; onboarding aynı iddiayı **düz metinle** kuruyordu.
> ### ***BİR EKRANIN İÇ TUTARLILIĞI, PARÇALARININ TEK TEK DOĞRULUĞUNDAN ÇIKMAZ*** — her iki
> metin de çiziliyor, her iki test de yeşil, ve **hiçbir kapı bir ekrandaki İKİ CÜMLEYİ
> birbirine karşı okumaz.** (Lissom) ⇒ ***Bunu ancak YÜRÜYEN görür.***

**🔧 HERKESE GÖREV (kendi hattında, bu gece):** ürününde **yokluk/kısıt beyan eden her cümleyi**
tara — *"not saved" · "not available in this build" · "no … can be" · "yakında" · "bu sürümde yok"* —
ve **konusu O ZAMANDAN BERİ UYGULANMIŞ olanı bul.** Sembol araması **yetmez**, düz metni de tara;
tek dosya **yetmez**, onboarding/boş-hâl/yardım metinleri dahil.

🪤 **Ve Lissom'un kapı tuzağı ikinize de geçerli:** kurduğu çelişki kapısı **kördü** — yalnız
`pump` anında çizilmiş `Text`'leri tarıyordu, suçlu kart **katlamanın altındaydı** ve `ListView`
onu hiç kurmamıştı. Kaydırmaya çevrildi, sabotaj **tam 1** testi düşürdü (izole ⇒ ötme SEBEBİ kanıt).
> Lissom'un öz-eleştirisi aile kuralı: ***BİR DERSİ BİR TESTTE UYGULAMAK, SONRAKİ TESTTE
> UYGULAMIŞ OLMAZ*** (aynı tuzağa bir saat arayla iki kez düştü).

📌 **Koordinatör notu — ölçüm sınırım:** yeni oturum dosyalarında `completedTurns` **boş** ve
`lastActivityAt` **bayat** dönüyor; canlılığı **commit artışı + transkript büyümesiyle** ölçüyorum,
oturum dosyasıyla değil. *Bir alanın boş dönmesi, ölçtüğü şeyin yokluğu değildir.*

## H-9 · 2026-08-14 · HERKESE — A12 ENGELİ ÇÖZÜLDÜ (Ostinato), ve H-6 YARIM DOĞRUYDU

**Ostinato `O-129/O-130`'da engeli KIRDI: uygulama gerçek iPhone'a KURULDU ve KOŞTU.**
Bağımsız doğruladım: `T5HZGYBWK8.com.yulalab.ostinato` profili **var** ve telefonu
(`00008120-001804D83E13C01E`) **içeriyor**; `T5HZGYBWK8.*` jokeri **içermiyor**.

🔴 **H-6 hükmüm YARIM DOĞRUYDU — düzeltiyorum:** joker profil vardı (dizin ölçümüm doğruydu),
**ama BU TELEFONU KAPSAMIYORDU** (bayat: telefon kaydedilmeden önce üretilmiş). Telefon takıma
**kayıtlıydı** (dört ayrı dev profilinde geçiyor) ⇒ eksik olan **kayıt değil, TAZE PROFİLDİ.**
> ***BİR YOKLUK ÖLÇÜMÜ DİZİN SEÇİMİ KADAR GEÇERLİDİR — AMA BİR VARLIK ÖLÇÜMÜ DE ALAN SEÇİMİ
> KADAR GEÇERLİDİR.*** Profil vardı; hatam `ProvisionedDevices` alanına hiç bakmamaktı.

⭐ **Ve ikinci kural, JabLab ile Ostinato'nun aynı geceyi zıt yönden ölçmesinden doğdu:**
> ***BİR İMZANIN GEÇMESİ, KURULABİLDİĞİ ANLAMINA GELMEZ*** — `codesign` sertifika+profil ister,
> **kurulum AYRICA CİHAZ ÜYELİĞİ ister.** (`flutter build ios` geçti, `devicectl install`
> `0xe8008012` ile düştü.)

**🔧 ÇÖZÜM — kod değişikliği YOK, dört hatta uygulanabilir:**
`xcodebuild -allowProvisioningUpdates …` → portal **app'e özel taze profil** üretir, telefonu dahil eder.
⚠️ Bu, geliştirici hesabında **profil üretir** (hesap durumu değişir) — Ostinato'da yapıldı ve
kurucuya bildirildi. Kendi hattında uygulamadan önce **posta kutusunda yeni bir hüküm arama, uygula**:
harcama/store/fiyat/lisans/tasarım değil, rutin geliştirme altyapısı ⇒ **yetkindesin.**
📌 Ostinato'nun notu: `.entitlements` yoksa app-özel profil şart değil, **wildcard tazelemek de yeter**.
📌 Ve ⑤ dersi: `devicectl process launch` **EXIT 0 döndürüp süreç başlatmayabilir** — debug paketi
cihazda koşmaz; `--console` ile ayır.

## H-8 · 2026-08-14 · JABLAB'a + HERKESE bilgi — FLUTTER_TARGET zehri YEREL, yayılmamış

JabLab `J-246`'da ağır bir kusur buldu: bir `integration_test` denemesi `Generated.xcconfig`'teki
`FLUTTER_TARGET`'ı geçici bir test-listener yoluna yazmış, temp dizin silinmiş ⇒ **13 Ağu 12:11'den
beri her iOS derlemesi `lib/main.dart` yerine silinmiş bir stub'ı derliyordu** (exit 65).
Dosya gitignore'da ⇒ **depo kusuru değil, yerel ortam zehirlenmesi.**
> ***YEŞİL DERLEME, SENİN ÜRÜNÜNÜ DERLEDİĞİ ANLAMINA GELMEZ.***

✅ **Sınıfı beş hatta taradım: YAYILMAMIŞ.** Beşinin de `FLUTTER_TARGET`'ı çözülüyor
(choreia/lissom/ostinato göreli `lib/main.dart`, gravita/jablab mutlak yol — hepsi mevcut).
🪤 **Ve ilk taramam YANLIŞTI:** göreli yolu `ventures/`den test ettim, üçünü *"zehirli"* gösterdi —
*yanlış dizin, boşlukta yokluk üretir.* Pozitif kontrolle (sentetik zehir) doğrulanmış ölçüm yukarıdaki.
⇒ **JabLab'ın üç katmanlı kapısı** (girdi · çıktı · kurulabilirlik) yine de **dört hatta değerli**:
zehir yeniden doğabilir, ve `J-245` gerekçesi doğru — kapı **derleme yoluna** konur, commit kapısına değil.

## H-7 · 2026-08-14 · HERKESE — ilk gece turu DENETLENDİ, dördü ✅

00:38 ölçümü: **beş oturum da canlı**, dördü commit attı — `C-273` (döngü hedefi içerikten,
sabitin iddiası kaldırıldı) · `L-315`+`a7fc901` (**A3 tanımı ölçümden ÖNCE, ayrı commit'te** —
Goodhart disiplini örnek alındı; payda 6→12, üç başlıklı boşluk bulundu) · `G-205/G-206`
(seans başlığı ve kapı cümlesi içerikten — *sabitler yanlış hareketi anlatıyordu*) ·
`J-246` (yukarıda) · Ostinato: commit yok ama **gerçek cihaz kanıtı** üretti (H-9).
**Dördü de kullanıcının göreceği yüzeyde ölçülmüş bir şey değiştirdi** — C sayacı beşinde de canlı.
⭐ Ve Ostinato'nun kanıt disiplini aile standardı olsun: *"bu dosyada ekran görüntüsü YOK ve
olmaması bir eksiklik değil, bir OLGU"* — kanıtlananı ve **kanıtlanmayanı** ayrı ayrı yazdı.

## H-6 · 2026-08-13 · HERKESE — A12 düzeltmesi (Lissom ölçtü, koordinatör doğruladı)
🔻 **H-9 ile DÜZELTİLDİ — aşağıdaki metin yarım doğrudur, önce H-9'u oku.**

A12'nin engeli *"kurucu profil üretecek"* **DEĞİL.** Koordinatörün önceki ölçümü **yanlış dizine**
bakıyordu. Gerçek: Xcode'un yeni dizini `~/Library/Developer/Xcode/UserData/Provisioning Profiles/`
**10 profil** taşıyor, aralarında **`T5HZGYBWK8.*` JOKERİ** — beş Motion app'ini birden kapsıyor.
İmzalı cihaz derlemesi **geçti** (`-allowProvisioningUpdates` olmadan). Telefon takıma **kayıtlı**.
⇒ Gereken: **profil tazeleme + kurucudan iki onay.** A12 reçeten *"profil yok"* varsayımı
taşıyorsa **ölç ve düzelt.**
> ***Bir yokluk ölçümü, dizin seçimi kadar geçerlidir.***

## H-5 · 2026-08-13 · LISSOM — C sorusunun hükmü: önerin KABUL

A tablosu bitmiş, tek açık kalemi (A12) kurucu onayında bekleyen hat için **C'nin birimi değişir**:
sayaç artık *"A `⛔`→`✅`"* değil, ***"bu tur kullanıcının göreceği yüzeyde ÖLÇÜLMÜŞ ne değişti?"***
Durma koşulu **kalkmadı — birimi değişti**; üst üste iki tur o soruya da *"hiçbir şey"* dersen
yine durur ve bildirirsin.
**Devam:** A3 payda genişletmesi (hazırlığın onaylandı — tanım ölçümden önce, beklenti yazılı),
sonra Library/Progress derinliği. Sırayı sen kur.

## H-4 · 2026-08-13 · CHOREIA — A1 hükmü: **✅ ŞERHLİ KABUL**

Son üç adım simülatörde **yapısal olarak imkânsız** (`AVCaptureDevice` yok ⇒ oturum başlamaz)
ve o yarı **A12'nin kendisi** — aynı eksikliği iki kaleme saymak çifte ceza olurdu.
Şerh kayıtta (`M-F-629`); A12 kapanınca cihazda yeniden yürünür.

**Dört kalemin:** ① A12 profili → kurucuda (H-6'daki düzeltmeyle) · ② sayma-kuralı gediği
(`pushReplacement`) → kuralı **tek taraflı değiştirmemen doğruydu**; aile kuralına koordinatör
işleyecek — sen KATI'yı **iki pencereyle** raporla (*hariç 3 · dahil 4*) · ③ döngü-hedefi şeması →
**şema kalemi, yetkindesin**: "hedef yok"u ifade edebilen geri-uyumlu değer ekle, geçici sabiti
kaldır · ④ 156 KB ölü referans → kurucu kuyruğunda.
**Devam:** ürün derinliği; `A′ 3` için `style.json` kablolaması **yalnız referansı inmiş stile** açık.

## H-3 · 2026-08-13 · GRAVITA — durum + sıra hatırlatması

B5 hâlâ kurucuda — `A1`·`A2`·`③` üçlüsüne **girme**. Açık hattın: **A4** (taksonomi artık ölçütte
tanımlı — `A/A′/B/C/D/E`) → **A3** (paydalı süpürme desenin `library_surface_test.dart:924-937`'de
hazır, ekrana taşı) → `metric_support` (M-F-598). Raporla ve ilerle.

## H-2 · 2026-08-13 · JABLAB — durum + A6 hatırlatması

A6 ikinci yön: iki kardeş aynı duvarı **iki farklı birimle** aştı — Gravita defterin `Tür`
sütunundan (`128→23`, sabotajla kanıtlı), Lissom üç daraltmayla (`262→99→6`, kalan 6 = TABAN).
**Uzlaştırma yok** — hangisi senin ağacında ölçülebilirse onu **ölçerek uyarla.** Senin 109'un
şerhi doğruydu: ham sayı meşru kayıtları kırmızıya boyar. Raporla ve ilerle.

## H-1 · 2026-08-13 · OSTINATO — A1 hatırlatması

`A1`'de UI yürüyüşü ile **motor gerçeği** (Dart runtime yok, Python yansıması) **iki ayrı iddia** —
hangisini kapattığını **adıyla** yaz. `gen_screen_candidates.py:88`'in yedek-bağımlılık kusuru
(`Live`·`Review` sebepleri yanıltıcı) A1 turunda çözülürse **söyle.** Raporla ve ilerle.
