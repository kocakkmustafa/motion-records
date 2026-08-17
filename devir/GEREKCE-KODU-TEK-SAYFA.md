# 🔐 GEREKÇE KODU — TEK SAYFA, TEK KARAR, BEŞ APP

> **Kurucu için.** ~30 dakika · **bir karar, beş app'e uygulanır** · beş app **aynı** kategorileri
> taşıyor (ayrı ayrı doğrulandı, varsayılmadı).
> Hazırlayan: orkestratör, 2026-08-17 · dayanak: `M-F-755` (eklenti katmanı) + `G-256` (app katmanı)

---

## ⚖️ ÖNCE SINIR — orkestratör **kodu seçmedi**, seçmeyecek

Aşağıda **ne yaptığımız** yazılı; **hangi gerekçe kodunun** (`35F9.1` · `C617.1` · `0A2A.1` ·
`CA92.1` · `1C8F.1` …) yazılacağı bir **yargıdır** ve o yargı sende. Ne orkestratör ne hatlar
Apple incelemecisi.
⇒ **Senin işin:** her satırın *"ne yapıyoruz"* sütununu Apple'ın kendi gerekçe listesindeki
tanımla eşleştirip **kodu yazmak.** Eşleştirmeyi yapmadım ve **yapılmış gibi de yazmadım.**

---

## 📋 TABLO — kullanılan kategoriler, kanıtıyla

| # | kategori | nereden geliyor | ne yapıyoruz — koddan ölçüldü | kanıt | **senin kodun** |
|---|---|---|---|---|---|
| 1 | **FileTimestamp** | `MediaPipeTasksCommon` (kapalı ikili, **beş app'e de bağlı**) | Poz modelinin **kendi iç dosya erişimi** — model/asset okuma. Bizim kodumuz dosya zamanı **okumuyor**. | `stat` **6** + `fstat` **6** = **12** (arm64) | ⬜ |
| 2 | **SystemBootTime** | `MediaPipeTasksCommon` | Aynı ikilinin iç zamanlaması. | `mach_absolute_time` **3** | ⬜ |
| 3 | **SystemBootTime** | 🔧 **`motion_camera`** — *bizim kendi eklentimiz* | **Çıkarım gecikmesi ölçümü:** bir poz-çıkarım çağrısının başı ve sonu arasındaki süre, mikrosaniye olarak `envelope["infUs"]`e yazılıyor. Saf **uygulama-içi performans** ölçümü; saat okunmuyor, cihaz kimliği türetilmiyor, **cihazdan hiçbir şey çıkmıyor**. | `DispatchTime.now().uptimeNanoseconds`, `MotionCameraPlugin.swift:211` + `:266` | ⬜ |
| 4 | **UserDefaults** | `permission_handler_apple` (**üç sürümün üçü de**: 9.4.10 · 9.5.0 · 9.6.1) | Kamera izni durumunun eklenti tarafından saklanması. | `NSUserDefaults standardUserDefaults`, **2 çağrı yeri** | ⬜ |

### 🟢 VE KULLANILMAYAN İKİ KATEGORİ — *ölçüldü*, varsayılmadı
| kategori | sonuç | kapsam |
|---|---|---|
| **DiskSpace** | **0** | **13/13** sembol arandı (`statfs` ailesi + `getattrlist` ailesi + `volumeAvailableCapacity`…) |
| **ActiveKeyboards** | **0** | **1/1** sembol arandı (`activeInputModes`) |

📌 Bu iki satır **boş bırakılmadı, ölçüldü** — *"aranmamış bir sembolün sıfırı, ölçüm değil
sessizliktir"* (`H-59`). Önceki turda DiskSpace'in **13 sembolünün 13'ü de hiç aranmamıştı**;
bu turda arandı.

---

## 🎯 EN ÖNEMLİ TEK BULGU — sıra **bilerek** ters çevrildi ve doğruymuş

`motion_camera`ın kendi `PrivacyInfo.xcprivacy`si bugün `NSPrivacyAccessedAPITypes`ı
**boş dizi** olarak beyan ediyor. Ama **satır 3**'te ölçüldüğü gibi, o eklenti
**SystemBootTime kullanıyor**.

> ### ***DOSYA BUGÜNKÜ HÂLİYLE PAKETLENSEYDİ, APPLE'A YANLIŞ BİR BEYAN GİTMİŞ OLURDU.***

✅ Paketlenmedi — çünkü `D21` ölçüldü ve sıra **ÖLÇ → DOLDUR → PAKETLE** olarak ters çevrildi.
Podspec `s.source_files = 'Classes/**/*'`; `resources`/`resource_bundles` **yok** ⇒ dosya bugün
**atıl**, Apple'a gitmiyor. Kodu sen seçtikten sonra **önce doldurulacak, sonra paketlenecek.**

---

## ⚠️ SINIRLAR — adıyla, çünkü sıfırla karıştırılmamalı

1. 🔴 **Kapalı ikilideki 8 üst-düzey Swift/Foundation sembolü ÖLÇÜLEMEDİ.**
   (`FileAttributeKey.*` · `URLResourceKey.*` · `UIDocument.fileModificationDate` ·
   `ProcessInfo.systemUptime` · `UITextInputMode.activeInputModes`)
   `nm -u` yalnız **C-linkajını** görür; bu, `MediaPipeTasksCommon`nin kapalı-kaynak olmasının
   **yapısal sonucu**, bu turun eksikliği değil. Kaynağa erişilebilen katmanda aynı 8 sembol
   **tam tarandı** ve sıfır çıktı.
   ⇒ *Bu bir "temiz" değil, bir "**görülemedi**"dir.*
2. 🟡 **Kategori-bazlı mı çerçeve-bazlı mı toplandığı HÂLÂ AÇIK** — Apple belgelemiyor. Bu ölçüm
   onu çözmüyor, **çözmeye çalışmadı**.
3. 🟡 **`MediaPipeTasksVision` bu turda yeniden taranmadı** — önceki ölçüm üç bağımsız hatta
   (Gravita · Choreia · JabLab) **0/0** bulmuştu; bu tur ona **güvendi**, tekrar etmedi.
4. 🟡 **Yalnız gerçek cihaz dilimi** (`ios-arm64`) tarandı — simülatör dilimi değil. *Mağazaya
   giden dilim bu.*
5. 🟡 `permission_handler_apple` **9.6.1**'de FileTimestamp **4 isabet** görünüyor — ölçüldü,
   **`Package.swift` derleme betiğinin yanlış-pozitifi** (çalışma kodunda değil). Bilinen, yeni değil.

---

## ✅ KARARIN NASIL UYGULANIR — senden sonrası bizde

1. Yukarıdaki **4 satırın kodunu** yaz (⬜ sütunu).
2. Gerisi orkestratörde: beş app'in `PrivacyInfo.xcprivacy`si + `motion_camera`ınki doldurulur,
   podspec'e `resource_bundles` eklenir, **paketlenir**, ve paketlendiği **ölçülerek** doğrulanır
   (`Runner.app` içinde manifest sayısı).
3. Beş app **aynı** kategorileri taşıdığı için karar **beş kez uygulanır, bir kez verilir.**

---

*Kaynaklar: `GEREKCELI-API-CAPRAZ-DOGRULAMA-2026-08-17.md` (Gravita, 30/30 sembol, vakum
kontrollü) · `GEREKCELI-API-OLCUMU-2026-08-16.md` · `M-F-755` (motion_camera, pozitif kontrollü) ·
`GEREKCELI-API-BIRINCIL-LISTE.md` (Apple'ın listesi).*
