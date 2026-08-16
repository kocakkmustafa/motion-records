# 🍎 Gerekçeli-API (required reason API) — BİRİNCİL LİSTE

> **2026-08-16 · orkestratör aldı** · Gravita'nın `①` görevindeki boşluğu kapatır.

---

## ⚠️ ÖNCE KAYNAK — ne olduğu VE ne OLMADIĞI

**Kaynak:** Apple'ın kendi dokümantasyonu, **JSON uç noktasından doğrudan** çekildi:

```
https://developer.apple.com/tutorials/data/documentation/bundleresources/
  app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitype.json
  app-privacy-configuration/nsprivacyaccessedapitypes/nsprivacyaccessedapitypereasons.json
```

🔑 **Gravita'nın erişemediği şeye erişme yolu buydu:** insan-yüzü sayfa JS ile render ediliyor ve
`WebFetch` yalnız başlığı alıyor. Ama Apple'ın SPA'sı `developer.apple.com/tutorials/data/...json`
uç noktasından besleniyor ve **o JSON düz metin dönüyor**. (⚠️ URL şeması değişmiş:
eski `bundleresources/privacy_manifest_files/...` **404**; yenisi `bundleresources/app-privacy-configuration/...`.)

### 🟡 VE SINIRINI ADIYLA YAZIYORUM
Bu liste **birincil kaynaktan** geldi, **ama ham JSON'u kendim okumadım** — `WebFetch`in özetleyici
modeli çıkardı. Yani:

| | durum |
|---|---|
| kaynak | ✅ **birincil** (Apple'ın kendi uç noktası, forum değil) |
| çıkarım | 🟡 **araç-özetli** (ham JSON gözle okunmadı) |

⇒ Gravita'nın forum-türevi listesinden **kesinlikle daha iyi**, ama *"Apple'ın sayfasını satır satır
okudum"* **değil**. Sembol adları **yüksek güvenli**, ancak bir sembol üzerinde **hüküm kurulacaksa**
o sembol ayrıca doğrulanmalı. (`H-61`: atıf yarım taşır · `H-65`: raporu değil kaynağı oku.)

---

## 📋 KATEGORİLER VE SEMBOLLER

### `NSPrivacyAccessedAPICategoryFileTimestamp` — **13 sembol**
```
FileAttributeKey.creationDate            FileAttributeKey.modificationDate
UIDocument.fileModificationDate          URLResourceKey.contentModificationDateKey
URLResourceKey.creationDateKey
getattrlist      getattrlistbulk      fgetattrlist      getattrlistat        ← ⚠️ ÇİFT KATEGORİ
stat             fstat                fstatat           lstat
```

### `NSPrivacyAccessedAPICategorySystemBootTime` — 2 sembol
```
ProcessInfo.systemUptime        mach_absolute_time()
```

### `NSPrivacyAccessedAPICategoryDiskSpace` — **13 sembol**
```
URLResourceKey.volumeAvailableCapacityKey
URLResourceKey.volumeAvailableCapacityForImportantUsageKey
URLResourceKey.volumeAvailableCapacityForOpportunisticUsageKey
URLResourceKey.volumeTotalCapacityKey
FileAttributeKey.systemFreeSize          FileAttributeKey.systemSize
statfs           statvfs              fstatfs           fstatvfs
getattrlist      fgetattrlist         getattrlistat                          ← ⚠️ ÇİFT KATEGORİ
```

### `NSPrivacyAccessedAPICategoryActiveKeyboards` — 1 sembol
```
UITextInputMode.activeInputModes
```

### `NSPrivacyAccessedAPICategoryUserDefaults` — 1 sembol
```
UserDefaults
```

---

## 🔴 VE BUNUN ÖLÇÜMÜMÜZE ETKİSİ — üç somut sonuç

### ① ⚠️ GRAVİTA'NIN ŞÜPHESİ **DOĞRU** ÇIKTI
`getattrlist` · `fgetattrlist` · `getattrlistat` **iki kategoride birden** geçiyor
(FileTimestamp **ve** DiskSpace). Bir isabet **hangi kategoriye** yazılacağı, sembolün kendisinden
değil **kullanım amacından** çıkar ⇒ bu semboller bulunursa **yargı gerektirir**, otomatik
sınıflandırılamaz.

### ② 🔴 `stat`/`fstat` ARANDI — **11 KARDEŞİ ARANMADI**
FileTimestamp'ta 13 sembol var; ölçümde yalnız ikisi tarandı.
**Aranmayanlar:** `lstat` · `fstatat` · `getattrlistat` · `getattrlistbulk` · `fgetattrlist` ·
`getattrlist` · ve beş Foundation anahtarı.

### ③ 🔴 *"DiskSpace: hiçbir yerde"* **DOĞRULANMAMIŞ**
O sonucun geçerli olması için `statfs` · `statvfs` · `fstatfs` · `fstatvfs` · `getattrlist*`
aranmış olmalıydı. Aranmadıysa o sıfır **ölçüm değil sessizliktir** (`H-59` sınıfı).

---

## 🔢 GEREKÇE KODLARI — ⛔ **SEÇİM KURUCUNUN**, burada yalnız envanter

> ⛔ **Ne orkestratör ne hatlar bir kod SEÇMEZ.** Bu liste, kurucunun tartabilmesi için var.

### FileTimestamp
| kod | Apple'ın tarifi |
|---|---|
| `DDA9.1` | Dosya damgalarını **kullanıcıya göstermek**. Cihaz dışına **gönderilemez**. |
| `C617.1` | **App container / app group / CloudKit container** içindeki dosyaların damga-boyut-üstverisi. |
| `3B52.1` | Kullanıcının **özellikle izin verdiği** dosya/dizinler (ör. document picker). |
| `0A2A.1` | **Üçüncü-taraf SDK sarmalayıcısı**. SDK'nın kendi amaçları için kullanılamaz, dışarı gönderilemez. |

### SystemBootTime
| kod | Apple'ın tarifi |
|---|---|
| `35F9.1` | Olaylar arası **geçen süreyi ölçmek** / zamanlayıcı. Dışarı **gönderilemez**. |
| `8FFB.1` | Uygulama içi olaylar için **mutlak zaman damgası** hesaplamak. Damgalar gönderilebilir, **boot time gönderilemez**. |
| `3D61.1` | Kullanıcının gönderdiği **isteğe bağlı hata raporunda**. Belirgin biçimde gösterilmeli. |

### DiskSpace
| kod | Apple'ın tarifi |
|---|---|
| `85F4.1` | Disk bilgisini **kullanıcıya göstermek**. |
| `E174.1` | **Yeterli alan var mı** kontrolü / alan azsa dosya silmek. |
| `7D9E.1` | İsteğe bağlı **hata raporu** içinde. |
| `B728.1` | **Sağlık araştırması** uygulaması, düşük alanın veri toplamayı etkilediğini bildirmek. |

### ActiveKeyboards
| kod | Apple'ın tarifi |
|---|---|
| `3EC4.1` | **Özel klavye uygulaması** aktif klavyeleri belirler. |
| `54BD.1` | **Özelleştirilmiş arayüz** sunmak için. |

### UserDefaults
| kod | Apple'ın tarifi |
|---|---|
| `CA92.1` | **Yalnız uygulamanın kendisine** erişilebilir bilgi. |
| `1C8F.1` | **App Group** üyeleri arasında paylaşılan bilgi. |
| `C56D.1` | **Üçüncü-taraf SDK sarmalayıcısı**. |
| `AC6B.1` | **MDM** yapılandırması (`com.apple.configuration.managed` / `com.apple.feedback.managed`). |

📌 **Gözlem, karar değil:** `permission_handler_apple` kendi manifestinde **`1C8F.1`** (App Group)
seçmiş. Bizim app'lerimizin App Group kullanıp kullanmadığı **ayrı bir olgu** ve ölçülmedi —
eklentinin kendi beyanı **eklentinin** sorumluluğu, ama **kategori-bazlı** yorum geçerliyse bizim
beyanımızı da etkiler. `M-F-700`ün çift-okumalı kapısı tam bunun içindi.

---

## ❓ HÂLÂ AÇIK — bu liste ÇÖZMÜYOR

**Apple'ın gönderim-anı denetimi KATEGORİ bazında mı toplar, ÇERÇEVE bazında mı?**
Yani `Flutter.framework`in FileTimestamp beyanı, aynı kategoriyi kullanan `MediaPipe`i de kapsar mı?
Bu sayfalar **bunu söylemiyor**. Kapı iki okumayı **ayrı ayrı** ölçmeye devam etsin (`M-F-700`).

🔗 Bakılabilecek yer: **TN3183** (*Adding required reason API entries to your privacy manifest*) —
`developer.apple.com/documentation/technotes/tn3183-...`. Henüz okunmadı.
