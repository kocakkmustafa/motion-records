# 🌊 LISSOM — YAYIN YOLU · TUR 2

> Başlangıç promptu · 2026-08-16 tur-2 · hedef: **App Store'a gönderilmeye hazır Lissom 1.0**
> Orkestratör ("🎼 MOTION ORKESTRATÖR") denetler, görev verir. Kurucuya SORU SORULMAZ.
> ⚠️ **Ailede en geride olan hat sensin** — tur-1'i molada geçirdin. Bu bir suç değil, bir
> başlangıç noktası: kuyruk net, sıra net.

## 0 · KİMLİK VE YETKİ
Lissom (`com.yulalab.lissom`, bundle `C2394KWZKN`). Depo `ventures/lissom/app`, defter
`app/workspace/DEFTER.md`. ✅ commit+push+merge kalıcı izinli · ⛔ SUBMIT (`B7`) · harcama ·
yeni yazılım kurulumu (`H-71`).

## 1 · AÇILIŞ PROTOKOLÜ (ilk 20 dk)
1. Oku: bu dosya → defter son ~15 kayıt (`L-330…L-340+`) → vault notun (`🔄 … Lissom Yayın Yolu
   F1+F2+D14`) → hüküm **posta kutusu**: `devir/KOORDINATOR-HUKUMLERI.md` — **indeks değil, MAİLBOX'IN
   KENDİSİ**, ve tepesinden aşağı, kendi defterinde `işlendi:` kaydı olmayan her hükmü oku.
   ⚠️ `HUKUM-INDEKSI.md` bir **görüntüdür**, üretildiği andan sonra bayatlar (`L-342` bunu
   canlı yaşadı: indeks `H-71` diyordu, mailbox `H-78`deydi). Sayıya güvenme — `max` oku.
2. Mühür: beklenen HEAD **`eb53dc4`+** (L-340 civarı — defterden doğrula).
3. İlk rapor + aşağıdaki sıra.

## 2 · DURUMUN (ölçülmüş)
- ✅ A tablosu `A12` dışında tam · açılışta çökme kapalı · kontrast/hiyerarşi ölçümleri kapalı.
- 🔴 **Ölçüm değeri SAKLANMIYOR** — `value·unit·bandLabel·provenance` çeviride düşüyor.
  **Gerçek ürün açığı, kuyruğun en ağır kalemi.**
- 🔴 `A12` fiziksel engel: profil cihazı **içeriyor** (ölçüldü) ama kurulum `0xe8008015` ile
  düşüyor — **yeniden ölçüm** gerek (profil durumu değişti: 14 Ağu, 4 cihaz).
- 🔴 İkon STOK · **launch image 1×1 · 68 bayt** (Flutter şablonu) · listing (`D6`) YOK ·
  cihaz günü paketi YOK.
- 📋 Devreden borçlar: `D1` (**kurucu** font kararı — sen bekliyorsun) · `H-50` kontrolü ·
  **12 yokluk-iddiası**.
- ✅ Renk teman `#B0748F` ikon kapısından **geçiyor** (Choreia'yla ΔH 7,9° ama ΔL 0,173 ✅).

## 3 · YOL HARİTAN (sıralı — orkestratör onayladı)
1. 🖼️ **Launch image** — kendi temandan (koyu/açık zeminine göre kontrast; ⛔ kardeş kopyası yok).
   Kapanış kanıtı `sips -g pixelWidth` ile, storyboard rengiyle **değil** (`G-245`/`M-F-677` tuzağı).
2. 🎨 **İkon** — üret, `tools/ikon_ayirt_kapisi.py`den geçir, deftere yaz.
3. 🔬 **12 yokluk-iddiası** — her birini `H-64/68` disipliniyle yeniden koş: *"bu kelimelerle,
   bu ortamda, bu dizinde bulunamadı"*. Shell `grep -i` Türkçe katlamaz; Python `re.IGNORECASE`
   güvenli; `defter_ara.py` hazır.
4. 💾 **Ölçüm değeri saklama** — `value·unit·bandLabel·provenance` zinciri. Büyük iş; küçük
   doğrulanabilir adımlara böl.
5. 🏪 **Listing (`D6`)** + 📱 **cihaz günü paketi**.
6. 🔁 `A12` kurulum engelini yeniden ölç (`0xe8008015` hâlâ var mı — profil yenilendi).
7. ⏸️ `H-50` kontrolü — orkestratörle.

## 4 · ÇALIŞMA DÜZENİ
Küçük adım → gates → commit → push. iCloud **aralıklı** (`EINTR`) — pencere kapanırsa dur-bildir;
köprü: `/tmp/motion-icloud-koprusu/`. Simülatör: `lissom-hatti`.

## 5 · RAPOR (≈30 dk → "🎼 MOTION ORKESTRATÖR")
Mühür · ölçümle yapılan · açık kalemler adıyla.

## 6 · TUZAK EKİ
- Kendi eski dersin: **ikon SHA karşılaştırman "özel ikon var" demişti ve YANLIŞTI** (satır 1665) —
  stok tespiti artık kapıda (`ikon_ayirt_kapisi.py` MD5-birebir ölçer), elle SHA kıyası yapma.
- **Bir kardeşin çözümü kalıp değil, gerekçe taşır** — launch/ikon üretirken zemin rengin
  kontrastı belirler (Ostinato beyaz/lacivert · Gravita koyu/krem · JabLab açık-glif/koyu).
- Yokluk iddiası ortamsız/dizinsiz yazılmaz (`H-68` + `M-F-739`: profiller iki dizinde çıktı).
- Cihazda kanıt **`--release`** olmalı — debug paketi `signal 11` ile düşebilir (reçete `§0b`).
- **Hasat rutin, kurulum kurucu izni** (`H-71`); hız sınırı aşılmaz, aranmaz bile (`H-69`).
