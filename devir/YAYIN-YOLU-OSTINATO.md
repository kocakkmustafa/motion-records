# 🥁 OSTINATO — YAYIN YOLU · TUR 2

> Başlangıç promptu · 2026-08-16 tur-2 · hedef: **App Store'a gönderilmeye hazır Ostinato 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir. Kurucuya SORU SORULMAZ.

## 0 · KİMLİK VE YETKİ
Ostinato (`com.yulalab.ostinato`, bundle `8TLDR695DW`). Depo `ventures/ostinato/app`, defter
`app/workspace/DEFTER.md`. ✅ commit+push+merge kalıcı izinli · ⛔ SUBMIT (`B7`) · harcama ·
⚠️ **hüküm numarası tahsis etme** (`H-67` dersi — numarayı yalnız orkestratör verir).

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → defter son ~15 kayıt (`O-150…O-166`) → vault notun (`🔄 … Ostinato Mağaza
   Yüzeyi + Cihaz Günü`) → hüküm **posta kutusu**: `devir/KOORDINATOR-HUKUMLERI.md` — **indeks değil, MAİLBOX'IN
   KENDİSİ**, ve tepesinden aşağı, kendi defterinde `işlendi:` kaydı olmayan her hükmü oku.
   ⚠️ `HUKUM-INDEKSI.md` bir **görüntüdür**, üretildiği andan sonra bayatlar (`L-342` bunu
   canlı yaşadı: indeks `H-71` diyordu, mailbox `H-78`deydi). Sayıya güvenme — `max` oku.
2. Mühür: beklenen HEAD **`020c611`** (215 commit). Kapılar: **42 kapı** yeşil.
3. İlk rapor + aşağıdaki sıra.

## 2 · DURUMUN (ölçülmüş) — cihaz gününe HAZIRSIN
- ✅ `F1`·`F2`·`F4`·`F5` kapalı · ikon `#252B45` · listing (`D6`) ailede İLK kapanan ·
  cihaz günü paketi ailede İLK · ön-uçuş **v2** (`O-166`, gölgeleme düzeltmesi canlı önce/sonra).
- ✅ `coached_only` yüzeyi **tam doğrulandı** (`M-F-690` — katman eklemeden önce altındaki verinin
  aktığını ölçtün; öncül çürüktü, katman eklenmedi).
- ✅ 42 kapının Türkçe-katlama denetimi: **0 etkilenen** — ve sıfırı sessiz geçmedin.
- ⛔ **`F3` içerik hasadı turu-2: KURUCU-BLOKE** (YouTube ToS, `KURUCU-PAKETI §5c`) — açılmadan
  başlamaz.
- 🔴 Kamera köprüsü canlılığı hiç ölçülmedi — cihaz gününün İLK maddesi (aile geneli).

## 3 · YOL HARİTAN (sıralı)
1. ⏸️ **BEKLE-VE-HAZIR-OL** — yayın yolunda sende bloke iş yok. Orkestratör görev verirse al
   (tur-1'de sana verilenler hep aile-katmanı denetimlerdi: çapraz-liste, katlama, terfi
   taraması — bu profil sürebilir).
2. 📱 **Cihaz günü desteği**: kurucu oturduğunda ön-uçuş v2 + yürüyüş tablon.
3. 🌾 `F3` yalnız kurucu ToS kararı gelirse.

## 4 · ÇALIŞMA DÜZENİ
Küçük adım → gates → commit → push. ⚠️ **Gates 2 dk Bash sınırını aşabilir** (`O-166` kazası):
commit'i `run_in_background`la koştur; SIGTERM yarım-mutasyon bırakırsa **elle temizleme** —
aracın kendi `_heal_if_needed()`ı (özet-doğrulamalı geri yükleme). Simülatör: `ostinato-hatti`.

## 5 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
Mühür · ölçümle yapılan · açık kalemler adıyla · **tutan desenleri de raporla** (`H-58`de sen
öğrettin: bir denetimin çıktısı yalnız kusur değildir).

## 6 · TUZAK EKİ
- Defter **monotonik değil** — tazelik `max(ids)` (`M-F-647`; terfi taramanda kendin doğruladın).
- Kelime-eşleştiren kapının **kapsam beyanı** olsun; anlamı regex'leme (`H-58②`/`H-62` — ikisi de
  senin esrin). Vakum testi **körleşmeyi** yakalar, **doğuştan darlığı** yakalamaz.
- Python `re.IGNORECASE` Türkçe'yi doğru katlar (sen ölçtün, `H-64` daraltıldı); shell `grep -i`
  katlamaz; `.lower()` `I/ı` çiftinde riskli.
- Bir aracın bıraktığı enkaz **aracın kendi onarım yoluyla** temizlenir.
- Eşzamanlı düzenleme: fark et, geri alma, üstüne inşa et, **yalnız kendi dosyanı** stage'le
  (tur-1'de örnek uygulaman buydu).
