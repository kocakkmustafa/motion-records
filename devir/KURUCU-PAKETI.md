# 📦 KURUCU PAKETİ — Motion ailesi yayın yolu

> Orkestratör biriktirir, kurucu tek oturuşta yapar. **Sona bırakılmaz, büyür.**
> Açılış: 2026-08-16 02:30 · son güncelleme: 2026-08-16 02:30
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

## 2 · 🔴 CİHAZ GÜNÜ (henüz HAZIR DEĞİL — hatlar reçete üretiyor)

**Durum:** ⏳ beklemede. Beş hat da önce ekran/kapı işlerini kapatıyor.
Hazır olduğunda buraya her hat için: reçete yolu + preflight betiği + beklenen kanıt listesi gelecek.
**Şimdilik yapılacak bir şey YOK.**

---

## 3 · 🎨 İKON ONAYI (`D8`) — henüz HAZIR DEĞİL

**Durum:** ⏳ hatlar 2–3 aday üretecek (tek renk zemin + tek beyaz glif; Choreia mor · Lissom deniz
yeşili · Gravita turuncu · JabLab kırmızı · Ostinato lacivert). Takas hakkı kurucuda.

---

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

### 🔗 VE BUNUN `D1` İLE BAĞI VAR — hiçbir plan dosyasında yazılı değildi
`D1` fontları **paketler** (`allowRuntimeFetching=false`) ⇒ **giden font isteği ortadan kalkar**
⇒ beş manifestin beyanı **değişir**. Yani `D1` bir tipografi kararı değil, aynı zamanda bir
**gizlilik beyanı kararı**. `D1` indikten sonra beş manifest yeniden ölçülecek.

**KURUCUDAN İSTENEN:** onay değil, **bilgi**. Bir itirazın varsa (ör. *"font indirmesi kalsın"*)
şimdi söyle — çünkü `D1` inince beyan da değişiyor.

---

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
