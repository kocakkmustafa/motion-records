# 💃 CHOREIA — BAŞLANGIÇ PROMPTU (2026-08-13)

> ⛔ **ÖNCE `BASLANGIC-ORTAK.md`'yi OKU** — hedef, döngü, yetki, maliyet disiplini,
> ölçüm disiplini ve tuzaklar orada. Bu dosya yalnız **sana özel** olanı ekler.

**Sen Choreia hattısın** — dans eğitmeni uygulaması. Yol: `ventures/choreia/{app,workspace}`

---

## MÜHÜR (koordinatörün İDDİASI — teyit et)

`HEAD 28826f9` · 204 commit · ağaç temiz · push-bekleyen 0
⚠️ Kendi DEFTER'inin son kaydını **kendin bul** (koordinatörün parse'ı iki hatta yanlış çıktı).

## MESAFEN — 2026-08-13 gecesi ölçüldü

**✅ Kapalı:** `A2` `A3` `A4` `A5` `A6` `A7` `A8` `A9` `A11`
**⛔ Açık:** **`A1`** · `A12`
**🔻 Sende değil:** `A10` → **B8** (ikon = tasarım yönü, kurucuda — **dokunma**)

Devir notun: `ventures/motion-core/workspace/devir/AJAN-DEVRI-CHOREIA.md`

---

## 🎯 ASIL MESELE — ve bunu ürün gözüyle oku

Ölçüm: **34 stilden 1'i başlatılabiliyor** (`hip_hop_foundations/hh_l1_bounce`).
Ve `A1` üç parçadan ikisi eksik: seçim ✅ · **oturum ✗** · **sonuç ✗**.

🔴 **Sebep yapısal ve ölçülü:** `SessionStore`a **hiçbir yazma yok** (`git grep` exit 1;
üç dosyada da yalnız **okuma**) ⇒ ***sonuç yüzeyi TANIM GEREĞİ imkânsız.***
Ve yürüyüşte `LiveLessonPage` + `LiveView` `rootBundle` yüzünden hiç çizilmiyor.

⇒ **Doğru sıra ölçüldü: önce YAZMA, sonra YÜZEY.** Yazma yoksa gösterilecek şey de yok.

**Kabul ölçütü (`A1`):** tek yürüyüş, **taze kurulumdan**, `NavigatorObserver` tanıklı:
ilk açılış → onboarding **düğmeyle** → stil seçimi → **oturum** → **sonuç yüzeyi** → **depoya kayıt**.
Ve — ortak çekirdeğin en önemli kuralı — **simülatörde AÇ ve ELLE YÜRÜ, ekran görüntüsü al.**

📌 **Aile referansı (kopyalama, ölçerek uyarla):** Lissom `8843a30` — köprü **yeni desen değildi**,
var olan `sourceOverride`a ulaşamayan `HomeScreen`di; **sabotaj ikizi** var (boş kaynak ⇒
`finish` yok, depo boş). JabLab `0aa7c62` — dört bölük test **tek yürüyüşe** indi ve ⭐ yeni bir
büyüklük çıktı: **varış KİPİ** (`varılan 6 = push 4 + kök 2`).

## İÇERİK GERÇEĞİ — `A4` kapalı ama tabloyu bil

`A 29 · A′ 3 · B 0 · C 0 · D 1` (payda 34−1=33).
- **29'u aylarca sürecek içerik işi** — kapasite meselesi, karar değil
- **`D 1` = `salsa_shines`** — içerik TAM, kablolama TAM, kapatan şey `bpmResolved BLOCKED`.
  ⛔ **Kurucu kalemi** (~10 dk canlı tap). Sen açma; `bpmStatus`a dokunma.
- **`A′ 3`** için `style.json` kablolaması **yetkin** — ama **yalnız referansı İNMİŞ stil için**.
  ⛔ Referansı inmemiş stile `style.json` yazmak **boş bir açılabilir stil** yaratır ve
  standardın kendi cümlesini çiğner: *"sahte/boş kurs asla listelenmez."*

## `A12` — donanım VAR, engel İMZA

`flutter devices` → **`Mustafa Kaan iPhone'u (wireless) · iOS 26.6` bağlı** (ölçüldü).
Engel: `com.yulalab.choreia` provizyon profili **yok** (makinede kurulu tek profil `burunfarki`).
⇒ **B1/B7, kurucuda.** ⛔ Kurucunun telefonuna **kurulum yapma**. Ama `A1` bittiğinde
**cihaz koşum reçetesini imzaya kadar hazırla** — profil geldiği an koşu dakikalar sürsün.

## SENİN BEDELLE ÖĞRENDİKLERİN — kendine uygula

- ⭐ **"Boş bir sayaç sıfır değildir"** — 11 kalemin 11'ine boş dönen sayaç *"hepsi eksik"* değil,
  **komut kurulumu bozuk** demekti.
- 🪤 **0-bayt yer doğrusu:** `templates/app/ios.tmpl/…` dosyaları **0 bayt** (`md5 d41d8cd9…`);
  naif kıyas *"15/15 farklı"* der. **Geçerli referans = taze `flutter create`.**
- ⭐ **(a) ikinci kanalın = MONTAJ NOKTASI.** Ostinato'nun `Scaffold(` kanalı bu ağaca **geçmiyor**
  — ve Gravita'da da geçmedi. ⇒ ***aktarılabilir olan DESEN değil KAVRAMDIR.***
- 🔴 **Aile kuralı, sana da:** *metin tarayan bir kapı YORUMLARI kodla aynı sayar.* 26 python
  kapın var — fırsat bulduğunda bu gözle ölç, **ayrı tur açma.**

## ⛔ KOORDİNATÖRE GİDEN
`B8` ikon · `salsa_shines` canlı tap · `A12` imza · **`motion_camera` gizlilik manifesti pakete
girmiyor** (podspec `resources` beyan etmiyor — **beş app'i birden** ilgilendiriyor, koordinatörde).
