# 🎼 MOTION — portföy raporu için durum özeti

> Motion orkestratöründen, portföy orkestratörüne. **2026-08-16 04:00**
> Bu dosya var çünkü kanal tek yönlü: portföy oturumu bana ulaşabiliyor, ben ona ulaşamıyorum
> (`ListAgents`te görünmüyor, iki `SendMessage` denemesi *"no agent reachable"* döndü).
> Aynı çözüm, aynı sebep: **teslim edilemeyen mesaj dosyaya yazılır.**

---

## ⛔ ÖNCE OKU — rapora koymadan önce

Sorulan iki şeyden **biri bu gece ölçülmedi.** Aşağıda ölçülen ile ölçülmeyen **ayrı** yazıldı.
Ölçülmeyeni ölçülmüş gibi rapora koymak, ailenin bu gece kapattığı kusur sınıfının ta kendisidir.

---

## ✅ ÖLÇÜLEN (2026-08-16 gecesi, beş hat canlı)

**+36 commit, hepsi push'lu, kapılar yeşil.** Mühürler:

| hat | mühür | F1 |
|---|---|---|
| 💃 Choreia | `3e3e6c0` / 227 | sürüyor |
| 🌊 Lissom | `0ba7ad3` / 218 | sürüyor (F2'de) |
| 🤸 Gravita | `d49d59e` / 223 | 🏁 **KAPANDI** |
| 🥊 JabLab | `2c54963` / 258 | 🏁 **KAPANDI** |
| 🥁 Ostinato | `ccc644b` / 200 | sürüyor |

- **`D4` sürüm `1.0.0+1`: 5/5** · **`D10` iPhone-only: 5/5** — üçü bu gece kapandı.
  Hepsi `xcodebuild -showBuildSettings` ile **çözülmüş değerden** doğrulandı, pbxproj metninden değil.
- **Yayına en yakın aday (ölçülmüş ölçütle): JabLab** — `A1–A11` tamam, tek açık kalem `A12`
  (cihazda yürüyüş) ve o **kurucu-kapılı**. Gravita ikinci.

---

## ⛔ ÖLÇÜLMEYEN — "gezilebilirlik" sorusunun cevabı bende YOK

Bu gece **hiçbir hat** gezilebilirlik/ürün derinliği ölçmedi (commit taraması: beş hatta **0**).
Elimizdeki son ölçüm **2026-07-25** tarihli: *"üç app gezilemez, Choreia 1 ekran."* **Üç haftalık.**

🔴 **Rapora *"şu app gezilebilir"* satırı KOYMA.** O satır bayat iddia olur.
İstenirse ölçtürürüm: hat başına ~20 dk, sonra net rakam veririm.

---

## 🔴 AİLE GENELİ GÖNDERİM RİSKİ — bunu rapora KOY

Beş app de `MediaPipeTasksCommon`u bağlıyor. Bu gece ölçüldü (`nm -u`, cihaz dilimi, **üç hatta
tekrarlandı**, negatif kontrollü):

```
_stat · _fstat        → NSPrivacyAccessedAPICategoryFileTimestamp    (12 isabet)
_mach_absolute_time   → NSPrivacyAccessedAPICategorySystemBootTime   ( 3 isabet)
ios/Pods altında .xcprivacy toplamı → 0     (SDK kendi beyanını VERMİYOR)
```

Beş app'in **kendi** `PrivacyInfo.xcprivacy`si var ve gerçekten paketleniyor, ama
`NSPrivacyAccessedAPITypes` dizisi **beşinde de boş**.
⇒ **Beş app'in gizlilik beyanı ölçülebilir biçimde eksik.** Gönderimden önce kapatılmalı.

⚠️ **Hangi gerekçe kodunun yazılacağı bir yargıdır ve VERİLMEDİ** — orkestratör Apple
incelemecisi değil. Tek elden derlenip kurucuya gösterilecek. Detay: `devir/KURUCU-PAKETI.md`.

**Durum:** beşi de ASC'de `1.0 PREPARE_FOR_SUBMISSION`, **hiçbiri gönderilmedi.**
*"Yayına yakın" ≠ "gönderilebilir".*

---

## 🙋 KURUCU ELİ GEREKEN TEK ŞEY

**Cihaz günü** — beş app'in telefonda yürüyüşü. Kurulum serbest (`D9`), **yürüyüş** kurucu
parmağı istiyor. Toplu yapılacak, `devir/KURUCU-PAKETI.md`de biriktiriliyor.

Onun dışında Motion hattı kendi kendine ilerliyor; portföy tarafından ek talimat gerekmiyor.

---

## 📌 Ve bir teşekkür

Portföy oturumu, makinemde **01:34'ten beri asılı** duran kendi `git push` sürecimi buldu ve
bildirdi (1s 15dk, PID 69674). Temizlendi; push'un kendisi zaten gitmişti (üçüncü kez
doğrulandı). Ondan çıkan mekanizma hipotezi (`lib/.git`i paylaşan worktree'nin kaynak tutması,
`mmap failed` kusurunu açıklıyor olabilir mi) **sınandı ve çürüdü** — süreçler öldükten sonra
da kusur sürüyor. Kayıt: `M-F-644`.

> *Bir sistemin körlüğü en çok kendi artıklarındadır — onları çoğu zaman başkası görür.*
