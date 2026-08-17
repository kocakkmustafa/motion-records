# 🔍 Gerekçeli-API sembol çapraz doğrulaması — TAM 30 sembol, satır satır (2026-08-17, Gravita)

> **Görev kaynağı:** `KOORDINATOR-HUKUMLERI.md` `H-82` (🤸 Gravita'ya) — kendi işaret ettiğim
> boşluğu kapatıyor: `GEREKCELI-API-OLCUMU-2026-08-16.md`'nin "Sınır" bölümü *"aranan semboller
> Apple'ın resmî listesiyle tek tek çapraz doğrulanmadı"* diyordu. Bu dosya o boşluğu kapatır.
> **Salt-okunur** (tek bayt değiştirilmedi) ve **gerekçe kodu SEÇİLMEDİ/ÖNERİLMEDİ** — bu bir
> yargı, kurucu paketine gidiyor.

---

## ÖZET — asıl şüphe YANITLANDI: çift-kategori semboller bu app'in yüzeyinde YOK

`getattrlist` · `fgetattrlist` · `getattrlistat` · `getattrlistbulk` — Apple'ın hem FileTimestamp
hem DiskSpace'te birden listelediği dört sembol — **taranan HİÇBİR yüzeyde ([binary + 3×
`permission_handler_apple` sürümü + kendi `ios/Runner/`] bir tek isabet vermedi.** Kategori-yargısı
gerektiren bir sembol bu app'in gerçek bağımlılık ağacında **bulunmuyor** — `H-82`'nin açtığı soru,
kurgusal değil gerçek bir boşluktu, ama sonucu **sıfır**.

| kategori | Apple listesi (tam) | bu turda YENİ taranan | önceki ölçümde eksikti |
|---|---|---|---|
| FileTimestamp | 13 sembol | **13/13** | 11/13 (yalnız `stat`/`fstat`) |
| SystemBootTime | 2 sembol | **2/2** | 1/2 (yalnız `mach_absolute_time`) |
| DiskSpace | 13 sembol | **13/13** | 0/13 (hiçbiri aranmamıştı — "sessizlik" `H-59` sınıfı) |
| ActiveKeyboards | 1 sembol | **1/1** | 1/1 (zaten tamdı) |
| UserDefaults | 1 sembol | **1/1** | 1/1 (zaten tamdı) |

**30 sembolün 30'u** artık `GEREKCELI-API-BIRINCIL-LISTE.md`'deki listeyle **birebir, satır satır**
karşılaştırıldı.

---

## 1 — YÖNTEM, iki katman ayrı çünkü ayrı sınır taşıyor

### 1a — Kapalı ikili (`MediaPipeTasksCommon.xcframework`, ios-arm64) → **yalnız C-düzeyi**
`nm -u` yalnız **linkleme-anında çözülen C sembollerini** görür (`_stat`, `_getattrlist` vb.).
Apple listesindeki **Swift/Foundation üst-düzey API'ler** (`FileAttributeKey.creationDate`,
`URLResourceKey.*`, `UIDocument.fileModificationDate`, `ProcessInfo.systemUptime`,
`UITextInputMode.activeInputModes`) **kapalı bir ikilide bu yöntemle görünmez** — bunlar
Objective-C çalışma-zamanı çağrılarına (`objc_msgSend` + seçici) derlenir, kendi sembol adlarını
**taşımazlar**. Bu bir **kapsam beyanıdır** (`H-62`): bu 8 üst-düzey sembol bu ikilide **ölçülemedi**,
"sıfır bulundu" değil "bu yöntemle görünmez" — ikisi aynı çıktıyı üretir ama **anlamı farklıdır**.

### 1b — Kaynağa erişilebilir kod (`permission_handler_apple` ×3 sürüm, kendi `ios/Runner/`) → **tam 30 sembol**
Kaynak metinde hem C-düzeyi hem Swift/Foundation üst-düzey semboller **düz metin olarak görünür**
⇒ burada **hiçbir kapsam sınırı yok**, 30 sembolün 30'u da gerçekten arandı.

### Vakum kontrolleri (`H-62`) — her iki katmanda da koştu
- İkili: `nm -u` toplamda **43.792** çözülmemiş sembol döndürdü (boş değil — arama mekanizması ölü değil).
- Kaynak: bilinen bir dize (`import`) `ios/Runner/*.swift`de **2 dosyada** bulundu (arama körleşmemiş).

---

## 2 — SONUÇLAR, sembol sembol

### `MediaPipeTasksCommon` ikili — gerçek cihaz (arm64), C-düzeyi 15/15
```
FileTimestamp (C-düzeyi 8/13):
  stat 6 · fstat 6 · fstatat 0 · lstat 0
  getattrlist 0 · getattrlistbulk 0 · fgetattrlist 0 · getattrlistat 0
SystemBootTime (C-düzeyi 1/2):
  mach_absolute_time 3
DiskSpace (C-düzeyi 4/13, getattrlist ailesi yukarıda tekrar sayılmadı):
  statfs 0 · statvfs 0 · fstatfs 0 · fstatvfs 0
```
`stat`+`fstat` = **12**, önceki ölçümün birleşik `_stat`/`_fstat` sayısıyla (**12**) birebir eşleşti
— aynı ikili, aynı sonuç, bağımsız yeniden koşumla **doğrulandı**, çelişki yok.
`mach_absolute_time` = **3**, önceki ölçümle birebir eşleşti.

**YENİ ölçülen (önceki turda hiç aranmamıştı):** `fstatat` · `lstat` · dört `getattrlist*` ·
dört `statfs` ailesi → **hepsi 0**. `H-59`'un uyardığı *"aranmamışın sıfırı ölçüm değil
sessizliktir"* durumu artık **gerçek bir ölçümle kapatıldı**.

### `permission_handler_apple` — ÜÇ sürümün ÜÇÜ de (aile genelinde çözülen tüm sürümler)
| sembol ailesi | 9.4.10 (JabLab) | 9.5.0 (Gravita·Ostinato) | 9.6.1 (Choreia·Lissom) |
|---|---|---|---|
| FileTimestamp (creationDate/modificationDate/fileModificationDate/getattrlist ailesi/stat ailesi) | 0 | 0 | **4*** |
| SystemBootTime (systemUptime/mach_absolute_time) | 0 | 0 | 0 |
| DiskSpace (volumeAvailableCapacity/systemFreeSize/systemSize/statfs ailesi/getattrlist ailesi) | 0 | 0 | 0 |
| ActiveKeyboards (activeInputModes) | 0 | 0 | 0 |
| UserDefaults (NSUserDefaults\|UserDefaults) | **4** (2 çağrı yeri) | **4** (2 çağrı yeri) | **4** (2 çağrı yeri) |

\* **9.6.1'deki 4 `modificationDate` isabeti doğrulandı ve önceki ölçümle birebir eşleşti:**
`Package.swift:367-368,396-397` — `import PackageDescription` taşıyan Swift Package Manager
**derleme-zamanı** betiği (bir YAML config'in üretilmiş JSON'dan yeni olup olmadığını kontrol
ediyor). **Derlenen uygulama koduna girmez**, yalnız paket çözümlemesi sırasında koşar — önceki
ölçümün doğru gerekçeyle kapsam dışı bıraktığı bulgu, bu turda **bağımsız yeniden doğrulandı**,
yeni bir şey değil.

**Üç sürümün ÜÇÜNDE de**: `getattrlist` ailesi **sıfır**, `stat` ailesi **sıfır**, DiskSpace
ailesinin tamamı **sıfır**. Çift-kategori sembol riski üç sürümde de **doğrulanmış negatif**.

### Kendi `ios/Runner/` (Gravita) — tam 20 sembol, hepsi 0
`PrivacyInfo.xcprivacy`'nin kendi kategori-adı sözlüğü (yanlış-pozitif, önceki turda elendi) dışında
gerçek kod isabeti **yok** — 20 sembolün 20'si de sıfır, önceki ölçümle tutarlı.

---

## 3 — VE BUNUN `H-82`'NİN SORDUĞU SORUYA CEVABI

> *"`getattrlist` gibi iki kategoride birden geçenler kaçmış olabilir."*

**Kaçmadı, çünkü hiç yok.** Taranan üç yüzeyin (kapalı ikili C-düzeyi + üç `permission_handler_apple`
sürümü + kendi kaynak kodu) **hiçbirinde** `getattrlist`/`fgetattrlist`/`getattrlistat`/
`getattrlistbulk` bir kez bile geçmiyor. Kategori-yargısı gerektiren bir sembol **yok** ⇒
Gravita'nın (ve aynı bağımlılıkları taşıyan dört kardeşin) gerekçe-kodu tablosunda bu belirsizlik
**sınıfı devreye girmiyor**.

⚠️ **Ama bu, `H-82`'nin sorduğu soruyu YANLIŞ sordurduğu anlamına gelmez** — soru geçerliydi,
önceki ölçüm gerçekten bu semboller için **hiç aramamıştı** (`H-59` sınıfı sessizlik), şüphe
**haklı bir şüpheydi**. Sonucun sıfır çıkması, sorunun sorulmaması gerektiği anlamına gelmiyor.

---

## 4 — SINIR, adıyla — bu ölçümün YAPMADIĞI/YAPAMADIĞI şeyler

- **Kapalı ikilideki 8 üst-düzey Swift/Foundation sembolü ölçülemedi** (`FileAttributeKey.*`,
  `URLResourceKey.*`, `UIDocument.fileModificationDate`, `ProcessInfo.systemUptime`,
  `UITextInputMode.activeInputModes`) — bu, `MediaPipeTasksCommon`nin kapalı-kaynak bir ikili
  olmasının **yapısal sonucu**, bu turun eksikliği değil. Kaynağa erişilebilen katmanda (permission
  handler + kendi kod) aynı 8 sembol **tam tarandı** ve sıfır çıktı.
- **Kategori-bazlı mı çerçeve-bazlı mı toplandığı sorusu HÂLÂ AÇIK** — Apple belgelemiyor
  (`GEREKCELI-API-BIRINCIL-LISTE.md`'nin kendi açık sorusu), bu ölçüm onu çözmüyor, çözmeye
  çalışmadı.
- **`MediaPipeTasksVision`** bu turda yeniden taranmadı — önceki ölçüm zaten kendi sembol
  tablosunda sıfır bulmuştu (Gravita+Choreia+JabLab bağımsız, 0/0); bu tur onu tekrar etmedi,
  eskisine güvendi.
- **Gerekçe kodu seçilmedi, seçilmeyecek** — bu dosyanın işi değil, kurucu paketine gidiyor.
- **Simülatör dilimi taranmadı**, yalnız gerçek cihaz (`ios-arm64`) — mağazaya giden dilim bu.

---

## Kaynak komutlar (yeniden üretilebilir)

```bash
BIN="ios/Pods/MediaPipeTasksCommon/frameworks/MediaPipeTasksCommon.xcframework/ios-arm64/MediaPipeTasksCommon.framework/MediaPipeTasksCommon"
for s in stat fstat fstatat lstat getattrlist getattrlistbulk fgetattrlist getattrlistat \
         statfs statvfs fstatfs fstatvfs mach_absolute_time; do
  nm -u "$BIN" | grep -Ec "\b_${s}\b"
done

# Kaynak (permission_handler_apple, üç sürüm de ~/.pub-cache/hosted/pub.dev/'de):
grep -rEo "<sembol>" <dizin> --include="*.swift" --include="*.m" --include="*.h" | wc -l
```

**Ölçen:** Gravita hattı, 2026-08-17. Beş depoya da (kendi + `permission_handler_apple`'ın üç
pub-cache sürümü) yalnız OKUMA erişimiyle girildi — kendi deposu dışında hiçbir yazma komutu
çalıştırılmadı.
