# Fallback canlılık reçetesi — "tetiklendiği ÖLÇÜLÜR, varlığı VARSAYILMAZ"

**Aile kuralı M-F-184/1.** Beşinci canlılık sorusunun ("kapıya soran var mı")
fallback-sınıfı hâli. Yazan: JabLab oturumu (J-073→J-077 vakası).
Kapsam: `unclassified_*`, `noVerdict`, `refusalReason`, `pending`, `WRONG_*`,
"bilmiyorum/göremiyorum" — **sözlük-dışı girdi için ayrılmış her sınıf.**

---

## 1. Kural

> Bir fallback sınıfının VAR olması, tanımadığı girdinin ORAYA DÜŞTÜĞÜ
> anlamına gelmez. Fallback'in tetiklendiği **ölçülmedikçe dekoratiftir** —
> ve dekoratif bir fallback, ürün dokümanında "kapsam dışını dürüstçe
> işaretliyoruz" diye görünür.

Kod incelemesi bunu yakalamaz: sınıf kod tabanında DURUYOR, testlerde
sentetik girdiyle tetikleniyor bile olabilir. Yakalayan tek şey, **sözlük-dışı
GERÇEK girdiyi hattan geçirip fallback sayacına bakmak.**

## 2. Fallback'in ölü olmasının İKİ AYRI yolu

JabLab vakası ikisini de gösterdi ve **ayırt etmek zorunlu** — çünkü ürün
dokümanına yazılacak cümle farklı, kullanıcıya verilen zarar farklı:

| # | mekanizma | gözlem imzası | kullanıcıya zararı |
|---|---|---|---|
| **A** | **Yanlış-sınıflama.** Girdi en yakın MODELLENMİŞ sınıfa tamamlanıyor. | fallback sayacı 0, **modellenmiş sınıf sayaçları YÜKSEK** | **YANLIŞ** geri bildirim — ve rakam ekranda doğru görünür |
| **B** | **Görünmezlik.** Girdi hiç deneme/hüküm yoluna girmiyor. | fallback 0, **modellenmiş sayaçlar da ~0, abort/red sayacı 0** | **SESSİZ** eksik — kullanıcı "bugün az çalıştım" sanır |

A ile B'yi karıştırmak kolay ve pahalı: ilk turumda JabLab'ın davranışını A
sandım, ölçüm B çıktı (aşağıda §5). **Ayırt eden sayı `abort`/red sayacıdır.**

## 3. Reçete — 5 adım

### Adım 1 — Sözlüğü ve fallback'i İSİMLE yaz
Modellenmiş sınıflar (config'den, hafızadan DEĞİL) + fallback sınıfının adı +
fallback'e girişin kod yolu. Bir sınıfın config'de olması modellenmiş
sayılmaz; faz/kural tanımı olmalı.

### Adım 2 — Sözlük-dışı GERÇEK girdi bul
Sentetik girdi Adım 4'te işe yarar ama **tek başına yeterli değildir**:
sentetik girdi fallback'e girer, çünkü onu fallback'e girecek şekilde
kurarsın. Gerçek girdi şartı: **hattın kapılarını (güven, görünürlük,
faz-tetiği) gerçek bir kayıt gibi zorlamalı.**

Gerçek girdi yokken sonuç "fallback tetiklendi" DEĞİL, "sentetikte
tetiklendi" diye yazılır.

### Adım 3 — ÜÇ sayacı birlikte oku
```
fallback_count          → fallback'e düşen
modelled_counts{}       → her modellenmiş sınıfın tamamlanma sayısı
rejected_count          → abort / red / düşük-güven / "hüküm yok"
```
Ayrıca **girdi yoğunluğuna göre normalize et**: "24,8 dakikada 6 olay" ile
"6 olay" farklı iki cümle. Beklenen yoğunluğu KAYNAKTAN türet (bir kanca
dersi onlarca kanca içerir), tahminden değil.

**Teşhis tablosu:**

| fallback | modellenmiş | red | teşhis |
|---|---|---|---|
| > 0 | — | — | ✅ fallback CANLI |
| 0 | **yüksek** | ~0 | 🔴 **A: yanlış-sınıflama** |
| 0 | ~0 | ~0 | 🔴 **B: görünmezlik** |
| 0 | ~0 | **yüksek** | 🟡 red yolu yiyor — fallback'e hiç sıra gelmiyor (ayrı kusur) |
| — | **düşük ama > 0** | **yüksek** | 🟠 **C: GRANÜLERİTE UYUŞMAZLIĞI** — aşağıda |

### 🟠 C — "kapı POPÜLASYON düzeyinde tutar, GRANÜLERİTESİ iddiasıyla uyuşmaz"

**Aile kuralı M-F-209/1 · yazan: Gravita oturumu (G-103 vakası).**

A ve B'nin ikisi de değil. Kapı ÇALIŞIYOR — girdinin ezici çoğunluğunu
reddediyor — ama **uygulandığı birim ile iddia edilen birim FARKLI.** Gravita'da
kimlik kapısı KARE başına değerlendiriliyor; kapalı kare atlanıp `return`
ediliyor ve **çevrim durumu OLDUĞU GİBİ KALIYOR.** Sonuç: bir "tekrar",
aralarında yüzlerce kapısız kare olan iki kapı-açık parçadan **birleştirilebilir.**
Kapı hiç yanlış karar vermedi; yalnız kararı kare hakkındaydı, iddia tekrar
hakkında.

**Ayırt eden sayı: boşluk-içeren-olay PAYI** — ve payı KENDİSİ ölçülmeli, bayrak
olarak değil. Gravita ölçümü bunu net gösterdi:

| ölçüm | sözlük-dışı | pozitif kontrol | ayırma gücü |
|---|---|---|---|
| boşluk içeren olay ORANI (ikili bayrak) | %36 (9/25) | %19,6 (19/97) | 1,8× |
| boşluk PAYI **medyan** | 0,000 | 0,000 | **ayırmıyor** |
| boşluk PAYI **p90** | **0,832** | **0,123** | **6,8×** |
| boşluk PAYI **maks** | 0,864 | 0,894 | **ayırmıyor** |

Üç ders birden:
1. **İkili bayrak zayıf ayırıcı, PAY güçlü.** "Boşluk var mı" 1,8×; "ne kadar
   boşluk" 6,8×.
2. **Medyan da maks da ayırmıyor — KUYRUK ayırıyor.** Olayların çoğu her iki
   popülasyonda temiz (medyan 0), en kötü tek olay ikisinde de benzer (maks
   ~0,87). Eşik bir gün konacaksa **kuyruk istatistiğinden** konur; ortalamaya
   bakan bir eşik hiçbir şey görmez.
3. **Kontrolde de çıkması belirleyici.** %19,6 → bu sözlük-DIŞINA özgü değil,
   **hattın genel granülerite açığı.** Yalnız sözlük-dışını ölçen bir tur bunu
   "sözlük-dışı sorunu" sanardı; pozitif kontrol (M-F-194) o yanlış teşhisi
   önledi.

**Zorlama ERTELENİR, DAMGA konur (M-F-209/1 hükmü, seçenek c).** İki zorlama
seçeneği de erken:
* *kapı kapanınca çevrimi sıfırla* → G-054 sınıfı: gerçek seansta kadraj dışına
  çıkan TEK kare tekrarı iptal eder, kullanıcı sıfır-sayım + sıfır-geri-bildirim
  durumunda kalır;
* *pay eşiği* → eşik ÖLÇÜLMÜŞ dağılımdan gelmek zorunda ve gerçek-olay ↔
  birleştirilmiş-olay iki popülasyonu henüz yok.

Üçüncü yol yapısal ve EŞİKSİZ: **olayın kendisine pay damgası** (Gravita:
`Rep.identityGapShare`, rapor-only). Sayım cömert DIŞ sınır kalır, kalite
çizgisi KAYDIN İÇİNDE beyan edilir — `unmeasuredUnits` dürüstlük deseninin
olay düzeyi. Eşik, cihaz-günü göz-doğrulamaları iki popülasyonu biriktirince
ölçülmüş ayrışmadan türetilir.

**Adım 4'e ek beklenti (C sınıfı için):** damganın kapı hep-açıkken **SIFIR**
kaldığını da sına (M-F-194 pozitif ikizi). Gürültü üreten bir damga, yarın
eşiğin o gürültüden türetilmesi demektir.

### Adım 4 — ZORUNLU test: negatif girdi fallback'e DÜŞMELİ
Reçetenin kalıcı kısmı. Sentetik veya kırpılmış gerçek girdiyle,
regresyon olarak:

```
test('sözlük-dışı girdi FALLBACK'e düşer, en yakın sınıfa TAMAMLANMAZ', () {
  final out = pipeline.run(outOfVocabularyInput);
  expect(out.fallbackCount, greaterThan(0),
      reason: 'fallback tetiklenmiyor → dekoratif');
  for (final c in modelledClasses) {
    expect(out.countOf(c), 0,
        reason: '$c olarak TAMAMLANDI — yanlış-sınıflama (mekanizma A)');
  }
});
```

İki beklenti birlikte olmak zorunda: yalnız birincisi A'yı kaçırır, yalnız
ikincisi B'yi "başarı" sayar.

### Adım 5 — Bulguyu ürün metnine geçir
Fallback ölüyse, o sınıfa dayanan **her kullanıcıya-görünen cümle yanlıştır.**
Ölçülen mekanizmaya göre yaz — ve ölçülenden fazlasını söyleme:

* A ise: "yanlış sayıyor" (ölçülmüşse)
* B ise: "görmüyor" — *"sayıyor ama sınıflandırmıyor"* demek B'de FAZLA
  İDDİADIR
* Kilit/kapsam gerekçesi varsa sınıf adı da düzeltilir
  (JabLab: `technique-coverage` → `technique-misclassified` → **`technique-invisible`**)

## 4. Ground truth kapısı (bu turun en pahalı dersi)

Fallback canlılığı **olay etiketi olmadan** ölçülebilir (sayaçlar yeter).
**İmza/ayrım ölçümü ölçülemez.** JabLab'da bu ikisini karıştırdım: "kanca
videosu"ndaki FSM olaylarını kanca sanıp jab'la kıyasladım; olaylar muhtemelen
eğitmenin arada attığı gerçek jab'lardı, yani "jab'ı jab'la" kıyaslamış oldum.

> **"X videosu" ≠ "X olayı".** Sınıf-karşılaştırması yapan her ölçüm
> olay-başı ground truth ister. Yoksa sonuç "ayrım yok" değil, **"ölçüm
> yapılmadı"**dır.

Ucuz ara adım: fallback ölçümünün verdiği zaman damgalarını insan gözüyle
doğrulamak (JabLab'da 6 damga = dakikalar).

## 5. Vaka: JabLab `unclassified_strike` (J-073 → J-077)

**Adım 1.** Modellenmiş: `jab` · `cross`. Fallback: `unclassified_strike`
(fazları `GUARD_READY → STRIKE_WINDOW → GUARD_RECOVERED`). **hook/uppercut
modellenmiş DEĞİL.**

**Adım 2.** Gerçek sözlük-dışı girdi: `pVvOF2kQuIQ` — 24,8 dakikalık
**lead-hook öğretim videosu**, %99,5 tespit, %40,6 hüküm verilebilir.

**Adım 3.** Ölçüm:
```
fallback (unclassified_strike) : 0
modellenmiş                    : {jab: 3, cross: 3}   ← 1488 saniyede 6
red / abort                    : 0
```
Yoğunluk normalizasyonu belirleyici oldu: bir kanca dersi onlarca kanca içerir;
6 olay "kancalar jab sayılıyor" ile bağdaşmaz. **0 abort** ise kancanın
`GUARD_READY→EXTENSION` geçişini hiç tetiklemediğini gösteriyor →
**mekanizma B: görünmezlik.**

İlk turda bunu **A** olarak raporladım (fallback 0 + modellenmiş sayaç > 0
gördüm, yoğunluğa ve abort'a bakmadım). Teşhis tablosunun üçüncü kolonu
(`red`) tam bu hatayı önlemek için var.

**Adım 5.** Ürün metni iki kez düzeltildi: en eski gerekçe *"unclassified'a
düşüyor, sayabiliriz ama yargılayamayız"* (fallback tetiklendiği
VARSAYILMIŞTI) → benim *"jab diye yanlış sayılıyor"* (mekanizma yanlış) →
**"görmüyor"**. Disiplin dürüstlük bloğundaki `notMeasured` satırı da
düzeltildi.

**Ders:** en eski gerekçe bir kod incelemesinden doğmuştu — `unclassified_strike`
config'de duruyordu ve kimse tetiklendiğini ölçmemişti. Kural bu boşluk için.

## 6. Aileye uygulama kuyruğu (koordinatör yayar)

| app | fallback sınıfı | Adım 2'de sözlük-dışı gerçek girdi ne olur |
|---|---|---|
| Choreia | `WRONG_FOOT` · `noVerdict` | kütüphanede olmayan bir dans stili/adım |
| Gravita | `refusalReason` · kimlik kapısı → `skippedFrames` | ✅ ölçüldü — 27 gerçek kalça-hareketliliği videosu → **sınıf C** (G-103). ⚠️ `unclassified` sınıfı Gravita'da YOK ve olmaması kusur değil: ürün "bu hangi hareket?" diye sormaz, kullanıcı dersi seçer. `refusalReason` ise bugün ÜRETİMDE ERİŞİLEMEZ (tek canlı hareket `derived`) — "canlı" yazılmadı |
| Ostinato | `pending` retleri | sözlükte olmayan akor/enstrüman/ses kaynağı |
| JabLab | `unclassified_strike` | ✅ ölçüldü — hook (mekanizma B) |

Her app sonraki motor-dokunuşunda kendi fallback'ini bu reçeteyle ölçer ve
Adım 4 testini kalıcı bırakır. **Sayaç okumadan "fallback'imiz var" cümlesi
kurulmaz.**

## ZEYİL (2026-08-04, M-F-249 — Ostinato O-027/O-028 vakasıyla)

1. **A/B teşhisi GİRDİ-BAŞINADIR, toplama uygulanmaz.** Ölçülmüş vaka:
   "fallback canlı, 46,5× ayırma" toplamı DOĞRUYDU — ama %100-reddedilen tek
   nota ile %97-yanlış-etiketlenen Bb'yi ortalayıp sağlıklı bir %53 üretiyordu.
   Toplam-teşhis en kötü vakayı en iyisiyle örter; tablo girdi-başına kurulur,
   toplam yalnız ÖZETTİR.
2. **Aday-kümesi ≠ kabul-kümesi.** "Aday kümesini daraltmak en ucuz doğruluk
   kazancı" bilinenleri AYIRMAK için doğru, bilinmeyeni REDDETMEK için tam
   terstir — kazanacak hipotez listede yoksa argmax en yakın hayatta kalana
   zorlanır (Bb→"Dm" %97). Desen: geniş aday şablonu + dar `acceptedNames`
   (Ostinato: 24 aday/8 kabul → yanlış-etiket %65,5→%0,0, tanıma kaybı
   değişmedi). Eşik oynatmak İKAME DEĞİLDİR — ölçülmüş: yanlış-etiketi
   yarılamak gerçek pozitiflerin %61'ini kaybettiriyordu.
3. **İkincil-tahmin (runnerUp sınıfı) da aynı tuzağın müşterisidir:** daraltılmış
   kümede "runnerUp hep X" gözlemi alan gerçeği değil küme artefaktı olabilir
   (M-O-36 düzeltmesi: Em→E7).
