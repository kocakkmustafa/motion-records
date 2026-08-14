# 🥊 JABLAB — AJAN DEVRİ (ölçüm ajanı → oturum), 2026-08-13

> **Kurucu kararı:** üretim **OTURUMLARIN**, ajan değil. Bu not, ajanın yaptığı işi
> ve **bıraktığı yeri** kaybolmadan devreder. ⛔ Hiçbir şey sessizce geri alınmadı.

---

## 0. MÜHÜR — nerede duruyor

| şey | durum |
|---|---|
| Depo | `ventures/jablab/app` · dal **`main`** |
| **HEAD** | **`0aa7c62`** — `J-240: (b)+③ birlikte — tanıklı TEK yürüyüş, A1 açıldı` |
| Önceki HEAD | `4e64dc7` (J-237) |
| ⚠️ **PUSH** | **YAPILMADI — `origin/main` hâlâ `4e64dc7`, yerelde 1 commit ileride** |
| Ağaç | temiz (mutasyon kalıntısı **0**, doğrulandı) |
| Kapılar | `analyze` **0** · app **330/330** · motor **125/125** · öz-test **2×0** · tazelik **0** — hepsi commit hook'unda **yeşil koştu** |
| Defter | `J-240` yazıldı · `C: 240/240/240 · çakışma 0` |

### ⚠️ PUSH NEDEN YAPILMADI — karar adıyla
Koordinatör *"tamamlanmışsa gerekçeli commit'le"* dedi; **push demedi**, ve aynı mesajda
üretim yetkisi ajandan alındı. **Commit geri alınabilir, push pratikte alınamaz** ⇒
geri-alınabilir olan seçildi. **Push kararı oturumda/kurucuda.**

### Süit 332 → 330: fark AÇIKLANABİLİR, kayıp DEĞİL
Dört bölük test (`rota 1/6` · `rota 2-6/6` · `gevşek ①` · `gevşek ②`) **iki** teste indi
(`A1 TAM AKIŞ` + `gevşek ①+②`). **−2 = 4−2.** Hiçbir iddia düşmedi; hepsi birleşik
yürüyüşün içinde ve **daha güçlü** hâlde sınanıyor.

---

## 1. A1 BİRLEŞİMİ — nereye geldim: **BİTTİ, YEŞİL, ATEŞLENDİĞİ KANITLI**

Koordinatörün sevki: *`onboarding_test:132`'nin taze yürüyüşünü `reachable_screens_test`inkine
bağla, araya `NavigatorObserver` tanığı tak ⇒ tek iş, üç kalem.* **Yapıldı.**

### Ne yapıldı

**① Tanık dikişi — üretimde tek satır.**
`lib/app/jablab_app.dart` → `JabLabApp.navigatorObservers` (varsayılan **boş liste**).
`MaterialApp` orada kurulduğu için tanık **dışarıdan sarmalanamıyordu**; dikiş
`repository`/`onboarding` ile **aynı emsal**, üretim davranışı değişmedi.

**② Köprü kuruldu — tek `pumpWidget`.**
`test/reachable_screens_test.dart` → `testWidgets('A1 · TAM AKIŞ — taze kurulum →
karşılama → seçim → oturum → SONUÇ')`. Ağaç **bir kez** kuruluyor ⇒ bölünmenin sebebi
olan tuzak (*ikinci `pumpWidget` ikinci ağacı güvenilir kurmuyor*) **geri gelmedi —
var olma sebebi ortadan kalktı.**

**③ ⚠️ KENDİ TUZAĞIM: ikisi de KALKTI (koordinatörün özel uyarısı).**
- `reached = <String>{'onboarding'}` **literali SİLİNDİ** (eski `:109`).
- Bayrak **set edilmiyor**: `seenOverride` **hiç kullanılmıyor** (eski `:115`).
- Yerine: `OnboardingStore(fileOverride:)` + **gerçek geçici dosya**, dosya **yok** ⇒
  ilk-koşu hâli *kurulmuyor, gerçekten öyle*; karşılama **`onboarding-next`e basılarak**
  geçiliyor ve `markSeen()` bayrağı **diske yazıyor** → `flagFile.existsSync()` sınanıyor.
- 🔴 **Ve bir ölçüm buldu:** `seenOverride: false` bunu **ölçemezdi** —
  `OnboardingStore.markSeen` `seenOverride != null` ise **erken dönüyor**
  (`onboarding_store.dart:72`), yani kalıcılık yolu **hiç çalışmazdı**.
  > ***Bir test double, gerçeğin kuralını uygulamaz.***
- ⭐ **Ayrıca eski hâlde HİÇ sınanmayan şey eklendi:** karşılamanın **indiği yer**.
  Eski test yalnız *"`OnboardingPage` findsNothing"* diyordu.
  > ***Bir ekranın kaybolması, bir başkasının geldiği anlamına gelmez.***

**④ ⭐ YENİ BÜYÜKLÜK — VARIŞ KİPİ (aile referansları uygulandı).**
Tanık **adı değil OLAYI** sayıyor (**Ostinato**, M-F-582) ve kök varış **çapalandı**
(`kRootArrivals = 2`, `:88`). Ölçüm:

```
A1 TAM AKIŞ · varılan 6 ekran (push 4 + kök 2) · perde 3 · aşama 4 · tanık: 5 push / 3 pop
```

> **Ostinato'nun bulgusu bu ağaçta da doğrulandı:** `OnboardingPage` ve `SelectPage`
> **aynı kök rotada** yaşıyor — aralarındaki geçiş `_RootState.setState` **takası**
> (`jablab_app.dart`, `_showOnboarding`). Eski toplam-assert bunu **görünmez** kılıyordu.
> Çapa şunun için: ***üçüncü bir kök varış bir BEYAN değil, bir BULGU olsun.***

**⑤ 🪤 KAPI İLK KOŞUMDA BENİ YAKALADI — ve bu kayda değer.**
*"Bu ağaçta rotalar anonim"* diye yazmıştım. Tanık `[/, null, null, null, null]` gösterdi:
**kök rota `/` adını TAŞIYOR**, yalnız 4 gezinme anonim. Varsayım **ölçümle** düzeltildi.
> ***Bir tanığın neye BAKAMAYACAĞI da ölçülür — ve ilk tahmin yanlıştı;
> düzelten şey kapının KENDİSİ oldu.***

**⑥ Denklem yürüyüşe bağlandı — ve (e) korundu.**
`walked` artık **elle `const` değil**, yürüyüşün çıktısı (`walkedClasses`, `:143`).
Elle küme **SİLİNMEDİ** — `knownFloor` (`:481`) adıyla ve **yalnız (e) rolünde** duruyor
(sözleşme (e) silmeyi **yasaklıyor**), üstelik **ikinci bir iş** görüyor: *yürüyüş bir
tabanı atlarsa* öter. **Vakum muhafızı** eklendi: yürüyüş koşmazsa küme boş kalır ve
bölme **vakum-doğru** geçerdi.

### 🔒 Ateşlendiği KANITLANDI — üç mutasyon (hepsi geri alındı)

| # | mutasyon | kapı ne dedi |
|---|---|---|
| **M1** | `navigatorObservers` `MaterialApp`e verilmiyor | *"tanık kök rotayı görmedi (0 push)"* ⇒ **Ostinato'nun "tanımlı ama BAĞLI DEĞİL" kusuru artık yakalanıyor** |
| **M2** | `markSeen()` çağrısı kaldırıldı | *"bayrak diske YAZILMADI"* ⇒ ③'ün kalıcılık yarısı **yük taşıyor** |
| **M3** | A1 yürüyüşü `skip` | *"yürüyüş koşmadı"* **+ denklemin vakum muhafızı** ⇒ bağ **gerçek** |
| **M0/son** | dokunulmamış | **exit 0 — susuyor** |

### 📊 ÖNCE/SONRA (sözleşme raporlama kısıtı 1)
**eski KATI 6 · yeni KATI 6 · FARK 0.** Sebep: **provenans + KİP.**
> ***Sayı değişmedi; sayının NEYLE KANITLANDIĞI değişti*** (elle küme → tanıklı,
> taze kurulumdan yürüyüş) — **ve yeni bir büyüklük doğdu** (push/kök ayrımı).

---

## 2. SIRADAKİ SOMUT ADIM — dosya + satır

### ▶️ ② (d) TOTOLOJİSİ — koordinatör **ikinci seçeneği** seçti
*"Bağımsız kaynaktan oku (`dead_end_test.dart:253-270` deseni); totolojiyi adıyla
işaretlemek bir KAYIT, denetim değil."*

**Yer:** `test/reachable_screens_test.dart`
- `:530` `final Set<String> unreachable = derived.difference(walked);`
- `:547` `expect(walked.length + unreachable.length, derived.length, reason: 'payda TOPLAMIYOR…')` ← **ötemeyen satır**

**⚠️ NÜANS — düzeltmeyi FAZLA GENİŞ yapma (ölçüldü):**
`:531` `expect(unreachable, unreachableWhy.keys.toSet(), …)` **GERÇEK bir denetim** —
ölçülen kümeyi **kayıtlı bir haritaya** karşı sınıyor ve gerçekten ötebilir.
> ***Dosya tamamen kör DEĞİL; ötemeyen şey yalnız TOPLAM-ASSERT'in kendisi.***
Bu ayrım yapılmazsa çalışan bir denetim de sökülür.

**Desen (`dead_end_test.dart:253-270`):** payda `assets/content/library.json`dan
**bağımsız** türetiliyor ve `expect(reachable, expected)` ile denetleniyor. Aynısı burada:
`derived`in *beklenen* büyüklüğünü **ikinci bir kaynaktan** üret, toplamı ona karşı sına.

### ⏸️ (c) — 6 gerekçenin 5'i hâlâ BEYAN
`:520` `unreachableWhy` haritası · `:538` denetim **yalnız uzunluk** (`>25`).
Ölçülü olan tek gerekçe: `CameraHarnessScreen.isAvailable`. Kalan beşi kaynaktan ölç.

### ⏸️ (a) — AYRIŞMA ÖLÇÜLDÜ: **4**
Tek kanal **yapısal** (`Scaffold(` kuran sınıf). Kanalın **göremediği**, ekran-gibi
adlanan sınıflar (ölçüldü, türetim replikası kapının **12** sayısını birebir üretti):

| sınıf | yer | not |
|---|---|---|
| `LibraryPage` | `shell_candidate/library_pages.dart` | dondurulmuş terfi envanteri |
| `ProgressPage` | `shell_candidate/shell_scaffold.dart` | dondurulmuş |
| `SessionSummaryView` | `shell_candidate/live_surface.dart` | dondurulmuş |
| **`SkeletonPreview`** | **`app/skeleton_overlay.dart`** | 🎯 **`app/` ALTINDA — ASIL SORU BU** |

⚠️ İkinci kanal kurulduğu an kapı **4 kalemle kırmızı doğar** ⇒ önce **bu 4'ün hükmü**
gerekiyor (üçü dondurulmuş, biri canlı ağaçta). *Kapsam kararı koordinatörde.*

### ⏸️ A6 — İKİNCİ YÖN = **109** (Gravita'ya verildi, tanım oradan gelecek)
Kapı **tek yönlü**: yalnız `referenced − written` (`tool/defter_freshness.py:353`).
Ölçtüm (hattın **kendi modülünü import ederek**, kopya değil):
`written − referenced` = **109** (238 yazılı − 129 kesişim). Pozitif kontrol: sentetik
öksüz enjekte → **109 → 110** ⇒ **totoloji değil**.

> ⚠️ **ŞERHİM (koordinatör kabul etti, üç hatta da geçerli):** **109'un çoğu MEŞRU** —
> defter kayıtlarının büyük kısmı bulgu/karar, commit üretmez. Kapı ham sayıyı kırmızı
> yaparsa **109 meşru kaydı kırmızıya boyar.** Önce **tanım**, sonra kapı.
> Aile: Lissom **262** · Gravita **128** · JabLab **109** · **referans = Ostinato**
> (A6'sı iki yönlü ve yeşil).

---

## 3. A TABLOSU — ölçülmüş hâl (2026-08-13)

| # | durum | not |
|---|---|---|
| **A1** | ✅ **BU TURDA AÇILDI** | tek yürüyüş, taze kurulum, tanıkla, sonuca kadar |
| **A2** | ✅ | `onboarding_test.dart:132` **+ artık A1'in İÇİNDE** |
| **A3** | ✅ | `30 = 20 + 10 + 0 ÇIKMAZ`; dedektör pozitif kontrollü |
| **A4** | ✅ | payda + işlem basılı. ⚠️ ölçütteki *"A/B/C/D"* **başka hattın birimi** |
| **A5** | ✅ | 6 adım exit 0; öz-testin **engellediği ateşlenerek** görüldü |
| **A6** | 🔴 ⛔ | tek yön; ikinci yön **109** ölçüldü, kapıda yok |
| **A7** | 🔴 **1 tam · 2 kısmi · 1 ayrışma** | (e)✅ (b)**✅ BU TURDA** ③**✅ BU TURDA** · (a)⚠️ (c)⚠️ · **(d)🔴 tek kalan** |
| **A8** | ✅ | paketten `plutil` ile çözüldü, 4 anahtar mevcut |
| **A9** | ✅ | bölme kapısı; üretim `lib/`de ağ API'si 0 |
| **A10** | ⛔ → **B TABLOSUNA TAŞINDI** | **20/20 ikon taze `flutter create` ile birebir.** Koordinatör hükmü: *kurucu direktifi ölçüt metnini yener* ⇒ **hat DOKUNMAZ** |
| **A11** | ✅ | `build ios --release --no-codesign` exit 0, `Runner.app` 46.0MB |
| **A12** | ⛔ ÖLÇÜLEMEDİ | ⚠️ **donanım VAR** (`Mustafa Kaan iPhone'u`, iOS 26.6 bağlı); eksik olan **imza + onay** → kurucuda |

**A7 artık `5/5`e iki madde uzakta: `(d)` ve `(a)`/`(c)` kısmileri.**

---

## 4. AİLE REFERANSLARI — bu turda fiilen kullanılanlar

- **Ostinato (M-F-582)** — tanık **adı değil OLAYI** sayar (`route.settings.name` boş
  olabilir) + kök varış **kimliğe/sayıya çapalanır**. ✅ **İkisi de uygulandı**, ve
  *"adlar boş"* varsayımı **ölçümle düzeltildi** (kök `/` taşıyor).
- **Choreia `_RouteSpy`** — tanığı yürüyüşe bağlar, varışı **boyalı kontrole basarak**
  kanıtlar. ✅ Uygulandı (her `visit()` bir tap'ın ardından).
- **Lissom `_RouteWitness`** — `pushed isNotEmpty` assert'i. ✅ Daha güçlü hâli
  uygulandı: `witness.pushes == 1` **kök rota kontrolü** (tanığın **bağlı** olduğunu
  kanıtlar) + `pops > 0` (akışın **kapandığını** kanıtlar).
- **JabLab `dead_end_test.dart:253-270`** — **kendi ağacındaki** doğru desen; `(d)` için
  koordinatörün seçtiği çözüm.

---

## 5. ⛔ HATTIN DOKUNMADIĞI — güncel

**B tablosu (kurucuda):** B1 keystore · B2 sürüm hizası · B3 store metni/görseller ·
B4 `AFTER_APPROVAL` · B5 `google_fonts` duruşu · B6 fiyat · B7 gönderim
· **+ A10 İKON (bu turda taşındı)** · **+ A12 cihaz turu (imza)**.

📌 **Android release:** `flutter build apk --release` **exit 1 — BİLEREK**.
`ANDROID RELEASE İMZASI YOK — build DURDURULDU (J-215)`; `key.properties` yok, keystore
**B1'de**. Bu **kusur değil, ateşlenmiş bir kapı** — yanlışlıkla "bozuk" diye onarma.

---

## 6. ⚠️ C DURMA KOŞULU — sayaç

- **Tur 1 (ölçüm):** hiçbir kalemi `⛔→✅` yapmadı — ölçütün **E maddesi** bunu emrediyordu.
- **Tur 2 (bu):** **A1 · (b) · ③ → `⛔→✅`.** ✅ **Sayaç SIFIRLANDI.**

---

## 7. GEÇİCİ DOSYALAR

Ölçüm betikleri (**depoya girmedi**, bilerek):
`/private/tmp/claude-501/…/scratchpad/jablab/` — `ikinci_yon.py` (A6 ikinci yön),
`a_korlugu.py` ((a) körlüğü), `oz_test_atesle.py` (A5 öz-test ateşleme),
`mutasyon.sh` (M1-M3), `run_gates.sh`. **Tekrar üretilebilir**; kalıcı değer devirdedir.
