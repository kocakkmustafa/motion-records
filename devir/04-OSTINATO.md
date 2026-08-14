# 🥁 OSTINATO — DEVİR PROMPTU (2026-08-12 akşamı)

> Yeni oturumsun. **Hiçbir şeyi hatırladığını varsayma — oku ve ölç.**

## 0. KİMSİN · NEREDESİN
`Ostinato` = **müzik/ritim** app'i. Ağaç: `ventures/ostinato/{app,workspace}` · defter
`workspace/DEFTER.md` (**son kayıt `O-116`**, **git İÇİNDE** (2026-08-15, `app/workspace/`)) · kod `app/` (git, push'lu).
**Mühür:** `HEAD = 3697b86` == `origin/main` (**SHA'lar birebir**) · ağaç **0 kirli** ·
**34 python kapısı** + **MUT-A 14/14** + pozitif ikiz · `✅ TÜM KAPILAR YEŞİL` (**borusuz** ölçüldü).
Defter **iki yönde taze** (eksik **0** · öksüz **0**), payda **DENKLEM** olarak (`133+51=184`).

## 1. HEDEF — ve yöntem 2026-08-12 akşamı DEĞİŞTİ
🎯 **Hedefin: "yayınlanmaya hazır SON HÂL".** Yolunu **SEN seçersin**; orkestratör **adım sevk
etmez, ÖLÇÜMÜ DENETLER.**
📄 **ÖNCE OKU:** `ventures/motion-core/workspace/YAYIN-HAZIRLIK-OLCUTU.md`
· **A1–A12: SEN** · **B1–B7: KURUCUDA**, ⛔ dokunma · **C: DURMA KOŞULU** (üst üste iki tur
`⛔→✅` yoksa **DUR ve bildir**) · ⚠️ **kapı ancak A'daki bir kalemi doğruluyorsa kurulur.**

🔴 **Neden değişti:** ailede 12 saatte **133 dosya**, **20'si üretim kodu**, ve
*"kullanıcının görebileceği ne değişti?"* → **hiçbir şey.** ***Bir yolun durma koşulu yoktur.***
⚠️ **Sana özel uyarı:** ailenin **en büyük kapı kümesi sende (34)**. Yeni kapı kurma isteğini
**A tablosuna karşı sına** — geçmiyorsa **kurma.**

## 2. İLK İŞ — MESAFE ÖLÇÜMÜ (tek tur, ⛔ düzeltme YOK)
**A1–A12: `✅` / `⛔` / `bilinmiyor`**, kanıtıyla. ⚠️ ***İkisi aynı kovaya girmez.***

**Bilinen girdiler (teyit et):**
| kalem | bilinen |
|---|---|
| **A1** tam akış | `KATI 8` rota, yürüyüş **soğuk açılıştan** · ⚠️ **8 üyenin 2'si rota push'u DEĞİL** (`OnboardingScreen` kök · `LibraryScreen` `setState` takası) — artık `arrival: push\|root` **beyanlı** ve **kök varış 2'ye çapalı** |
| **A2** onboarding | ✅ üç perde **gerçek dokunuşlarla**, bayrak set edilmeden |
| **A5** kapılar | ✅ **34 python** + MUT-A 14/14, öz-testler **koşuyor ve engelliyor** |
| **A6** defter | ✅ **iki yönde** taze, payda **denklem** |
| **A7** sözleşme | ✅ **5/5 METNE karşı** |
| **A12** cihaz | ⛔ **cihaz gerçeği YOK** — bu senin en büyük açığın |
| **A3·A4·A8·A9·A10·A11** | **bilinmiyor** |

## 3. AÇIK KALEMLER — nerede + sıradaki adım
**ⓐ SENDE:**
1. **⑤ kamera önizlemesi ERTELENMİŞ** — hüküm **uygulandı** (*kullanıcı cümlesi YAZILMAYACAK*,
   çünkü ölçüm gösterdi ki kullanıcı **zaten adlı teşhis alıyor**: `framingError` hangi landmark
   eksik diyor · `lowLight` güven eşiğini · `ok` onaylıyor). **Eksik olan GÖRÜNTÜ, ONAY değil.**
   **NEREDE:** kod-gerçeği **var**, **cihaz-gerçeği YOK.** **SIRADAKİ: gerçek cihazda kamera yürüyüşü.**
2. **`LiveScreenRoute` · `SetupCheckScreenRoute` · `ReviewScreenRoute`** hiçbir otomatik yürüyüşle
   **varılamıyor** (kamera sınırı; `ReviewScreenRoute`un kamerası **yok** — kamera gerektiren bir
   ekranın **arkasında**). **SIRADAKİ:** aynı cihaz koşusu.
3. **KATI eşiği tam tabanda `8/8`, SIFIR PAY** — tek rota kaybı kırmızı.
   **SIRADAKİ:** *pay yaratmak değil, payın yokluğunu GÖRÜNÜR tutmak* (zaten her koşumda basılıyor).

**ⓑ ORKESTRATÖRDE:** ⑤'in *"kullanıcı cümlesi yazılmayacak"* hükmü **uygulandı** — teyit orkestratörde ·
gezilebilirlik panosunda **Gravita hiç ölçülmedi** (bu hattı etkilemez, **panoyu** etkiler).

**ⓒ KURUCUDA:** **6 yayın kalemi** · **font duruşu** — ⚠️ ve senin ölçümün onu netleştirdi:
kararı **uygulamak** kapıyı *"beyan tazelenmeli"* diye ötürtür, ki bu ***tasarlanmış karar noktası,
yanlış alarm DEĞİL*** (eski hâl *"tarama ölmüş"* diyordu — **o** yanlış alarmdı ve **gitti**) ·
*"var olan onay yeterli mi"* · ⑫ makine-geneli **JDK** (venture-ötesi).

## 4. SON TURUN KAZANIMI — bozma
📊 **Öz-test sınıf dağılımı: `85 (①3 ②14 ③68)` → `95 (①0 ②15 ③80)`**, öz-testli kapı **9→10.**
⭐ **`①` SIFIRLANDI ve bu bir ELEME değil DÖNÜŞÜM** — üç **durum**-bağımlı kontrol kaldırılmadı,
***özellik-bağımlı YEDİ kontrole çevrildi*** (net **+10**).
> ***Bir kusuru sıfırlamanın iki yolu vardır: SİLMEK ve DÖNÜŞTÜRMEK — ve yalnız ikincisi kapsamı
> büyütür.*** ⚠️ **`①`i sıfırda tut**: yeni bir öz-test yazarken *"bu kontrol bir DURUMA mı yoksa
> bir DAVRANIŞA mı dayanıyor?"* diye sor.

## 5. SENİN BEDELLE ÖĞRENDİKLERİN — ailenin beş kuralı senden çıktı
- ***Bir kapı, bir SONUCU dayatmak yerine KARARSIZLIĞI yasaklayabilir*** (bölme kapısı:
  `user-surface ⊎ source-only`, **üçüncü hâl kırmızı**)
- ***Bir muafiyet ya ölçümünü taşır ya TÜRETİLİR*** (uçuş sınırı: *commit'lenmiş en yüksek
  numaranın üstü uçuştadır*)
- ***Bir "temiz ağaç" sinyali, işin BİTTİĞİNİ değil yalnız FARK OLMADIĞINI söyler*** — ve fark,
  **iş silindiğinde de sıfırdır** (`reset --hard` sessiz kayıp)
- ***Bir sayının doğru olması, ÜYELERİNİN doğru olması değildir*** (hayalet üye:
  `'SettingsScreenRoute'` ≠ `SettingsScreen`)
- ***Bir gereksinimi DÜŞÜREN beyan, kendisi sınırlanmazsa bir KAÇIŞ KAPISIDIR*** (`root` beyanı →
  **kök varış 2'ye çapalandı**, *üçüncüsü beyan değil BULGUDUR*)
- 🆕 ***Sabotaj "inmeme"nin BEŞİNCİ yolu: KORUMA ÇİFT*** (`^O-\d+` + `.match()` birbirinin yedeği ⇒
  tek noktalı mutasyon çapayı **kıramaz**). ⚠️ Ve bunun bulduğu kusur ağırdı:
  `return const SettingsScreen();` → kapı **SESSİZ**, desen `const`/`new` atlamıyordu ⇒
  ***parametresiz bir kök yüzeyi HİÇ görünmezdi.***
- ⛔ Ve bir ortam kuralı: ***sabotajı COMMIT'LEYEREK kurma*** — dosya kopyası al, boz, geri koy;
  `reset --hard` **henüz commit'lenmemiş işi de götürür.**

## 6. SERT KURALLAR
⛔ `ventures/motion-core/lib/tools` **hiçbir kipte kaynak değil.**
⛔ Kurucuya yalnız beş şey: **harcama · store gönderimi · nihai fiyat · lisans riski · tasarım yönü.**
✅ Motion ailesinde **commit+push+merge kalıcı izinli.** ⛔ `--no-verify` **yasak** (kapı seni bir kez
gerçekten durdurdu ve **uydun** — aynen sürdür).
⚠️ `workspace/` **git deposu DEĞİL** (ölçüldü) — DEFTER/PROGRESS **yazılır ama commit'lenemez.**
