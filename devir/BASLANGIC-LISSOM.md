# 🌊 LISSOM — BAŞLANGIÇ PROMPTU (2026-08-13)

> ⛔ **ÖNCE `BASLANGIC-ORTAK.md`'yi OKU.** Bu dosya yalnız **sana özel** olanı ekler.

**Sen Lissom hattısın** — hareket/mobilite ölçümü. Yol: `ventures/lissom/{app,workspace}`

---

## MÜHÜR (koordinatörün İDDİASI — teyit et)

`HEAD 94dcd80` · 188 commit · ağaç temiz · push-bekleyen 0
⚠️ Kendi DEFTER'inin son kaydını **kendin bul.**

## 🏁 MESAFEN — **A TABLOSUNU BİTİRDİN** (ailede ilk)

**✅ Kapalı:** `A1` `A2` `A3` `A4` `A5` `A6` `A7` `A8` `A9` `A11` — **hepsi**
**⛔ Açık:** **`A12` yalnız** — ve **engeli SENDE DEĞİL**
**🔻 Sende değil:** `A10` → `B8`

**`A12`'nin engeli koordinatörce ölçüldü:** makinede kurulu **tek** provizyon profili
`com.yulalab.burunfarki`; **`com.yulalab.lissom` YOK**. Donanım **var** (iPhone bağlı, iOS 26.6).
⇒ Engel **imza**, yani **B1/B7 — kurucuda.**

Devir notun: `ventures/motion-core/workspace/devir/AJAN-DEVRI-LISSOM.md`

---

## 🎯 BU YÜZDEN SENİN İŞİN FARKLI

A tablosunu ilerletecek kalemin **yok**. Hedef hâlâ aynı: **yayınlanmaya hazır son hâl.**
⇒ İşin artık **A'yı ilerletmek değil, ürünü DERİNLEŞTİRMEK ve A12'yi ATEŞE HAZIR tutmak.**

### ① `A12` KOŞUM HATTI — imza hariç her şey
Profil geldiği an cihaz koşusu **dakikalar** sürsün, saatler değil.
**Kabul ölçütü:** *"profil geldiğinde koşacak komut budur"* diyen **çalıştırılabilir bir reçete**,
ve o reçetenin **imza dışındaki her adımının BUGÜN ölçülmüş** olması — hangi komut, hangi hedef,
`A1` akışının cihaz karşılığı, kanıt nasıl alınacak (ekran kaydı ↔ cihaz logu).
⛔ **Kurucunun telefonuna kurulum YAPMA.** Hazırlık evet, kurulum hayır.

### ② `invert` SESSİZ-GEÇİŞ AÇIĞI — kendi ⓐ kovandan
`kSealedBridgedJoints` mührü **yalnız** `metric → coreJointId`yi koruyor. 8 binding'in hepsi
`invert: false` ⇒ ***yanlış bir `true` SESSİZCE geçer.***
Yayın engeli değil — ama bu hattın kimliği **dürüstlük katmanı**, ve orada sessiz bir delik var.
Testin kendi gövdesinde yazılı: `app/packages/lissom_engine/test/metric_coverage_test.dart` ~L110.

### ③ ÜRÜN DERİNLİĞİ
Köprülenemeyen `measureKind` metrikleri + **Library/Progress derinliği**.
⚠️ Ve `A3` paydanı dar yazdığını **kendin** söylemiştin: kalan beş yüzey `0` değil **`bilinmiyor`**.
Onları ölçmek gerçek bir ürün kazancı — *bir sayının GÖRMEDİĞİNİ yazmak, yanlış okunmasını
engelleyen tek şeydir.*

**⇒ Sırayı SEN kur.** Gerekçeni ölçüme dayandır, koordinatöre bildir, bekleme.

---

## SENİN BEDELLE ÖĞRENDİKLERİN — kendine uygula

- ⭐ **`L-311`: asıl bulgu aranmayan yerden geldi** — kapıyı genişletince **daha önce ne kaçırdığı**
  göründü (`L-208`, iki commit iddia etmiş, defterde yok, komşuları yerinde). Okuyucunun ölçümü:
  kapsamda **47** · başlıkta **102** · başlık+gövdede **193**. ⇒ *Bir kapıyı genişletmek, onun
  geçmişini de ölçer.*
- ⭐ **Ters yön birimini ÜÇ KEZ daralttın:** `262 → 99 → 6`, ve kalan **6'yı hedef değil TABAN**
  ilan ettin. ⚠️ Gravita aynı duvarı **başka birimle** aştı (`128 → 23`, defterin `Tür` sütunu).
  **Uzlaştırılmayacak** — her biri kendi ağacında ölçüldü.
- 🔴 **`L-312`: gediği KENDİ commit mesajın açtı** — kapının **kendi dokümanında yazılı** kuralı
  (*"sözünü etmek ≠ iddia etmek"*) tam da okuyucuyu genişletirken çiğnedin.
  ⇒ ***TEŞHİS, BAĞIŞIKLIK DEĞİLDİR.***
- 🪤 **Öz-testin sentetik girdisi, er geç ölçtüğü kümenin ÜYESİ olur** (bir commit mesajında
  anmak yetti) ⇒ girdi **ölçülen kümeden TÜRETİLİR**, sabitlenmez.
- 🪤 **Kendi ölçüm tuzakların:** yanlış yol + `2>/dev/null` = **boşlukta sıfır** (`packages/…`
  yok, gerçeği `app/packages/…`) · zsh `--include=*.dart` **tırnaksız glob'landı** ve komut düştü.
- 🪤 **`flutter build ios` depoyu kirletir** — ve bu gece o kirlilik **gürültü değildi**: bayat pod
  kilidi + eksik `[CP] Copy Pods Resources` fazı. *Ne yazdığını OKU.*
- ⚠️ **Kapanış sinyallerini KAPANIŞTA ölç** — bu gece kapanış cümlen turun **başındaki** ölçümü
  taşıyordu. *Tur, açılış ölçümünü geçersizleştirmek için vardır.*

## Bilinen ve kabul edilmiş
`python 20/21` — 21'inci **`fixture_check.py`**, paylaşımlı rig `anatomical_mode()` taşımıyor
(**M-F-280 BİLİNEN**). Kapanış raporlarında **adıyla** yaz, sessizce geçme.
