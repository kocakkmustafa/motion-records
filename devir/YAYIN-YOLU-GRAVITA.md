# 🤸 GRAVITA — YAYIN YOLU · TUR 2

> Başlangıç promptu · 2026-08-16 tur-2 · hedef: **App Store'a gönderilmeye hazır Gravita 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir. Kurucuya SORU SORULMAZ.

## 0 · KİMLİK VE YETKİ
Gravita (`com.yulalab.gravita`, bundle `H3ULV8LL8F`). Depo `ventures/gravita/app`, defter
`app/workspace/DEFTER.md`. ✅ commit+push+merge kalıcı izinli · ⛔ SUBMIT (`B7`) · harcama ·
gerekçe-kodu seçimi (kurucuda).

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → defter son ~15 kayıt (`G-240…G-254`) → vault notun (`🔄 … Gravita Yayın
   Provası + Gerekçeli-API Kapısı + iCloud Krizi`) → hüküm indeksi (71; yeni: `H-58…71`).
2. Mühür: beklenen HEAD **`d502c07`** (G-254, 252 commit). Kapılar: app 222/222 ·
   engine 175/175 · python 20/20.
3. İlk rapor + aşağıdaki sıra.

## 2 · DURUMUN (ölçülmüş) — cihaz gününe HAZIRSIN
- ✅ **Yayın provası GERÇEK**: `gravita.ipa` 34,9 MB, IPA-içi imza `Apple Distribution` doğrulandı
  (arşiv ≠ IPA dersi senden çıktı, `M-F-678`).
- ✅ İkon `#AA262F` (kilitli referans) · açılış görseli gerçek · listing (`D6`) hazır · kamera-izin
  metni **yapısal bayatlamaz** (`M-F-685` — üçüncü yolu sen buldun).
- ✅ `PAKET.md` (tarihli hazır-mı anlık görüntüsü) + `device_day_preflight.py` **v2** (gölgeleme
  düzeltmesi — profil adayları önce `ProvisionedDevices` taşıyanlara daralır).
- ✅ Aile gizlilik kapısı **senin eserin**, aile katmanında: `motion-core/workspace/tools/
  validate_privacy_manifest_coverage.py` (gerçek arşivi tarar, çift-okumalı, vakum korumalı).
- ✅ Profil: geliştirme 13 Ağu, **4 cihaz** (kurucununki içinde).
- 🔴 **Kamera köprüsü canlılığı hiç ölçülmedi** — cihaz gününün İLK maddesi (aile geneli).

## 3 · YOL HARİTAN (sıralı)
1. 🔗 `run_all_gates.sh` → aile kapısına bağlantı hâlâ istiyorsan **kendi git geçmişinde** yap
   (tur-1'de bilerek beklettin — doğruydu).
2. 📄 **31 hareket / 2 ölçülü** açıklaması: `$readinessClaimWhy`nin kendisi bayatlama uyarısıydı;
   `H-58`in (b) yolu — sayıyı gerçek katalog sayımına bağlayan kapın var (`validate_store_
   listing.py`). Sayı değişirse kapı yakalar; **dokunma, izle**.
3. 📱 **Cihaz günü desteği**: kurucu oturduğunda ön-uçuş v2 + `PAKET.md` yürüyüşü.
4. ⏸️ Sonrası orkestratörden.

## 4 · ÇALIŞMA DÜZENİ
Küçük adım → gates → commit → push (iCloud **aralıklı**; `EINTR` görürsen dur-bildir, köprü:
`/tmp/motion-icloud-koprusu/`). Simülatör: `gravita-hatti`.

## 5 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
Mühür · ölçümle yapılan · açık kalemler adıyla · sınır beyanı ("adıyla" kültürünün en iyi
uygulayıcısı sendin — koru).

## 6 · TUZAK EKİ
- **Arşivin `.app`i ≠ IPA'nın `.app`i** (`M-F-678`) — gönderim imzası IPA'dan okunur.
- **`ios/Pods/` gönderilen yüzey değil** (`M-F-698`): `permission_handler` SPM'den; MediaPipe
  ana Runner'a **statik gömülü** — gerçek sembol sayısı linker sonrası (2/1, 12/3 değil).
- **Profiller iki dizinde** (`M-F-739`) — asıl olan `Xcode/UserData`.
- **"En yeni profil" ≠ "doğru profil"** (`M-F-740`) — Store profili cihaza kurulamaz.
- Vakum testi **+** kapsam beyanı — ikisi ayrı kusur sınıfı (`H-62`, senin ve Ostinato'nun eseri).
- Kural yorumu belirsizse **iki okumayı da ölç** (`M-F-700`) — kategori/çerçeve sorusu Apple'da
  belgelenmemiş; kapın bunu zaten yapıyor.
