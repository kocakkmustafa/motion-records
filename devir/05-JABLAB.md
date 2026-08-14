# 🥊 JABLAB — DEVİR PROMPTU (2026-08-12 akşamı)

> Yeni oturumsun. **Hiçbir şeyi hatırladığını varsayma — oku ve ölç.**

## 0. KİMSİN · NEREDESİN
`JabLab` = **boks** app'i. Ağaç: `ventures/jablab/{app,workspace}` · defter `workspace/DEFTER.md`
(**son kayıt `J-239`**, **git İÇİNDE** (2026-08-15, `app/workspace/`)) · kod `app/` (git, push'lu).
**Mühür:** `HEAD = 4e64dc7` == upstream · ağaç **temiz** · analyze **0** · app **332/332** ·
motor **125/125** · öz-test **2×0** · tazelik **0** (`A=14 · B=15 · gedik 0` + `C: 239/239/239 ·
çakışma 0`).

## 1. HEDEF — ve yöntem 2026-08-12 akşamı DEĞİŞTİ
🎯 **Hedefin: "yayınlanmaya hazır SON HÂL".** Yolunu **SEN seçersin**; orkestratör **adım sevk
etmez, ÖLÇÜMÜ DENETLER.**
📄 **ÖNCE OKU:** `ventures/motion-core/workspace/YAYIN-HAZIRLIK-OLCUTU.md`
· **A1–A12: SEN** · **B1–B7: KURUCUDA**, ⛔ dokunma · **C: DURMA KOŞULU** (üst üste iki tur
`⛔→✅` yoksa **DUR ve bildir**) · ⚠️ **kapı ancak A'daki bir kalemi doğruluyorsa kurulur.**

🔴 **Neden değişti:** ailede 12 saatte **133 dosya**, **20'si üretim kodu**, ve
*"kullanıcının görebileceği ne değişti?"* → **hiçbir şey.**

## 2. İLK İŞ — MESAFE ÖLÇÜMÜ (tek tur, ⛔ düzeltme YOK)
**A1–A12: `✅` / `⛔` / `bilinmiyor`**, kanıtıyla. ⚠️ ***İkisi aynı kovaya girmez.***

**Bilinen girdiler (teyit et):**
| kalem | bilinen |
|---|---|
| **A1** tam akış | `KATI 6` rota · `türetilen 12 = yürünen 6 ⊎ varılamayan 6` · ⚠️ **ama (b) ayrışması var** (aşağıda) — *"tam akış"* iddian **şu an kanıtsız** |
| **A3** sessiz boş yüzey | ✅ **`30 = 20 iş sunan + 10 ADIYLA BOŞ + 0 ÇIKMAZ`**; boş oranı **%33**, **sessiz oranı %0** — ve mekanizma **yapısal** (`Library.validate` çıkmazı **ifade edilemez** kılıyor) |
| **A5** kapılar | ✅ analyze 0 · 332/332 · 125/125 · öz-test **koşuyor VE engelliyor** (kanıtlandı) |
| **A6** defter | ⚠️ **gedik 0 · çakışma 0 ✅ ama YÖNÜ beyan edilmedi** — ⚠️ *çakışma* ile *ikinci yön* **aynı şey değildir** (biri kimlik çarpışması, öteki **öksüz kayıt**). A6 **iki yön** istiyor ⇒ **ölç** |
| **A7** sözleşme | 🔴 **"5/5 diyemiyorum": 1 tam · 2 kısmi · 3 AYRIŞMA** (aşağıda, **dosya+satır**) |
| **A8** gizlilik manifesti | ⚠️ `J-171`de eklendi ama **ilk hâlde PAKETE GİRMEMİŞTİ** (pbxproj kaynağı RunnerTests hedefine koymuştu) — **paketten teyit et** |
| **A2·A4·A9·A10·A11·A12** | **bilinmiyor** |

## 3. 🔴 SÖZLEŞME AYRIŞMALARI — dosya+satır ile, en yüksek öncelik
Bunlar **A1 ve A7'yi birlikte** bloke ediyor: *"tam akış çalışıyor"* iddiasının **kanıtı** yok.

| madde | ne eksik | nerede |
|---|---|---|
| 🔴 **(b)** | `NavigatorObserver` **YOK**; denklemdeki `walked` **elle yazılmış bir `const Set<String>`**, yürüyüşün çıktısı **DEĞİL**. Gerçek yürüyüş **başka testte** (`reached`) ve ***ikisinin uzlaştığını hiçbir şey sınamıyor*** ⇒ ***(e) ile rütbesi düşürülen elle küme, (b)'nin işini görüyor*** | `reachable_screens_test.dart` **satır 293** (`const walked`) |
| 🔴 **(d)** | **TOTOLOJİ**: `unreachable = derived − walked`, sonra `assert(walked + unreachable == derived)` ⇒ ***tanım gereği hiç ötemez*** (⚠️ **aynı totolojiyi aynı gün envanter betiğinde de buldun**) | satır **315–332** |
| 🔴 **③** | Yürüyüş **bayrak SET EDİLEREK** başlıyor (`JabLabApp(onboarding: seen)`) ve `reached` **`{'onboarding'}` literaliyle TOHUMLANIYOR** ⇒ **karşılamanın çıkışı hiç basılmadı.** Sebep ölçülü: *testler bilerek bölündü ama bölününce yeniden BAĞLANMADI* | satır **108** |
| ⚠️ **(a)** | Koddan türetiliyor ✅ ama **tek kanal**. Kanalın **yapısal** (`Scaffold(` kuran sınıf) ⇒ adlandırma körlüğüne düşmüyor — ama **kendi körlüğün ölçülmemiş**: `Scaffold`unu ortak kabuğa devreden ekran **hiç aday olmaz** | — |
| ⚠️ **(c)** | 6 varılamayan gerekçesiyle duruyor ✅, ama denetim yalnız **uzunluk** sınıyor (`>25 karakter`) ⇒ **altı gerekçenin YALNIZ BİRİ ölçülü**, beşi **beyan** | — |
| ✅ **(e)** | TAM — iki zorunlu şerh birebir yazılı (madde **senin vakandan** doğdu) | — |

**SIRADAKİ ADIM (senin yazdığın):** yürüyüşün `reached`ini **denkleme bağla** → sonra **③'ü yeniden
bağla** → (c)'nin 5 beyan-gerekçesini **kaynaktan ölç** → (a) ikinci kanal.

## 4. DİĞER AÇIK KALEMLER
**ⓐ SENDE:** gezilebilirlik **kör noktası korumasız** (J-206 taraması kapılı değil) ·
**10 B-sınıfı sabit gecikme** · **BÜYÜK KİP Türkçe körlüğü** (⚠️ kapatmanın bedeli **21 meşru siteyi
kırmızıya boyamak** — ölçüldü, **assertion'la kilitli**, kör nokta kapanınca öter).
**ⓑ ORKESTRATÖRDE:** (a)/(c) kapsam kararı · **⑤. katman** ve **`gateable` dar tanımı**
(⛔ *tek ölçülmemiş kalem*, önceki turlardan devir) · olay sayısının **kalıcılığı** (çekirdek turu) ·
`footwork_combo` / M-C-04.
**ⓒ KURUCUDA (6+1):** ikon · cihaz turu · store metin onayı · gönderim yazma erişimi ·
**sürüm/yüzey ayrışması (GÖNDERİM ENGELİ, 5 hattın 4'ünde)** · `google_fonts` gizlilik duruşu ·
**+ `workspace/` sürüm kontrolü DIŞINDA** (4 "kalıcı" hüküm hücresi orada).

**KAPANMIŞ, yeniden açma:** 4 reddedilmiş yolun `Durum` hücresi ✅ (`J-185/186`·`J-175`·`J-060`·
`J-053`, biçim `REDDEDİLDİ (kapalı) — YOL: … · ÖLÇÜM: …`) · `53`ün yeniden kesilmesi ✅
(**elle doğrulanmış 4**; `kapalı 175` ve `korumasız 53` **GERİ ÇEKİLDİ**).

## 5. SENİN BEDELLE ÖĞRENDİKLERİN — ailenin altı kuralı senden çıktı
- ***Türetilmiş bir sayıyı kaynağına karşı denetleyemezsin: aritmetik kimlik bir ÖLÇÜM değildir***
- ***Bir konvansiyon ZAMANLA DEĞİŞİR; onu DAR bir pencerede ölçmek, en yeni hâlini "tek hâl"
  sanmaktır*** (60 başlık ↔ 225: kapsamın **%21**di)
- ***KAPILAR, İKİMİZİN DE YOKKEN ÇALIŞAN TEK DENETİM***
- ***Bir savunmanın kaç KATMANI olduğunu, onu AŞMAYA ÇALIŞMADAN bilemezsin*** (üç katman çıktı)
- ***Bir payda yeniden üretilemiyorsa ölçüm değil, ANIDIR*** — sayacı **dosyaya yazdın**, doğru
- ***İzlenen bir kapı, tetiklenmiyorsa bir BELGEDİR*** (`--self-test` **hiç koşmuyordu**)
- ⚠️ Ve kendi kapanış cümlen: ***bir kuralı en çok savunan hat, onu UYGULAMA ANINDA düşürmeye en
  yakın olandır — çünkü kuralı BİLMEK, onu o an ÇALIŞTIRMAK değildir.*** Bugün seni **beş kez
  KENDİ KAPILARIN** yakaladı, dikkatin değil.
- ⛔ Ve bir ortam kuralı: ***"beklenen kırmızı" olarak CANLI BİR KUSURU fixture yapma*** — kusur
  düzelince **yanlış alarma** dönüşür (ikinizi de vurdu). **Sentetik/davranışsal** yaz.

## 6. SERT KURALLAR
⛔ `ventures/motion-core/lib/tools` **hiçbir kipte kaynak değil.**
⛔ Kurucuya yalnız beş şey: **harcama · store gönderimi · nihai fiyat · lisans riski · tasarım yönü.**
✅ Motion ailesinde **commit+push+merge kalıcı izinli.** ⛔ `--no-verify` **yasak.**
⚠️ `workspace/` **git deposu DEĞİL.**
