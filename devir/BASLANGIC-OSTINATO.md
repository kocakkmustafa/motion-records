# 🥁 OSTİNATO — BAŞLANGIÇ PROMPTU (2026-08-13)

> ⛔ **ÖNCE `BASLANGIC-ORTAK.md`'yi OKU.** Bu dosya yalnız **sana özel** olanı ekler.

**Sen Ostinato hattısın** — müzik/ritim pratiği. Yol: `ventures/ostinato/{app,workspace}`

---

## MÜHÜR (koordinatörün İDDİASI — teyit et)

`HEAD 82610a7` · 185 commit · ⚠️ **1 kirli** · push-bekleyen 0
⚠️ Kendi DEFTER'inin son kaydını **kendin bul.**

🔴 **İlk iş: o 1 kirli kalemi KARARA BAĞLA.** Bu gece bir **kalıntı MUT-A mutasyonu** bulmuştun
(`contributingTakes: 3 → 99`, yarım koşumun geri koymadığı sabotaj) ve geri almıştın.
Kalan kirli **aynı sınıf mı, yeni iş ürünü mü — ölç, sonra seç, ve seçimini YAZ.**
⛔ Sessizce geri alma.

## MESAFEN — 2026-08-13 gecesi ölçüldü

**✅ Kapalı:** `A2` `A5` `A6` (**iki yönde — beş hattın tek doğru A6'sıydı**) `A7` (**5/5**) `A8` `A9` `A11`
**⛔ Açık:** **`A1`** · `A3` · `A4` · `A12`
**🔻 Sende değil:** `A10` → `B8`

Devir notun: `ventures/motion-core/workspace/devir/AJAN-DEVRI-OSTINATO.md`

---

## 🎯 ① SIRADAKİ: `A1` — ve **beklediğinden çok daha yakın**

Kendi ölçümün bunu buldu:
- `lib/app/screens/live_screen.dart:36` → **`PoseSource? source`** ve **`skipCountdown` ZATEN VAR**
- **5 test bunu zaten kullanıyor**, `route_path_test.dart:58` **gerçek `Navigator.push` arkasında**
- `live_screen.dart:182` zaten **`ReviewScreenRoute` push ediyor**

⇒ ***Oturum→sonuç bacağı CİHAZSIZ, üretim kodu değişmeden yürünebilir.***

**Kabul ölçütü:** tek yürüyüş, **taze kurulumdan**, tanıkla: onboarding **gerçek dokunuşlarla**
→ ders seçimi → **oturum** → **sonuç yüzeyi**. Ve **simülatörde AÇ, ELLE YÜR, ekran görüntüsü al.**

⚠️ **Ama kendi ölçümün ikinci bir duvarı da gösterdi ve bunu unutma:**
`verify_end_to_end_session.py` kendi docstring'inde *"Ostinato'nun henüz Dart RUNTIME motoru yok…
`replay_check.py`nin AYNI `evaluate()` mantığı (JSON ruleset semantiğinin **Python yansıması**)…
READY fazı STUB'lanır"* diyor, ve `grep -rn "PhaseStateMachine" packages lib` → **0 isabet**.
⇒ ***Bir cihaz koşusu bu bacağı ÖLÇEBİLİR ama KURAMAZ.*** UI yürüyüşü ile motor gerçeği
**iki ayrı iddia** — hangisini kapattığını **adıyla yaz.**

## ② `A3` + `A4` — sayılar sende hazır, eksik olan ARTEFAKT
Bu gece ölçtün: `A3` **28 = 15 iş sunan ⊎ 13 adıyla boş ⊎ 0 çıkmaz**, sessiz oranı **%0**
(13/13'ü `lockedReason`/`demoOnlyReason` **ve** `unblockedBy` taşıyor). `A4` payda 13.
⚠️ **A3 paydan 3 varılamayan ekranı KAPSAMIYOR** — bunu koru, `0` yazma.

🔻 **Ve taksonomi artık ÖLÇÜT DOSYASINDA TANIMLI** — senin bulduğun **`E` = `awaiting-capability`**
kovası **kabul edildi ve yazıldı** (10 `locked` kaleminin ≥4'ü *veri değil ALET* eksiği:
`hands_and_wrists` *"a missing measurement TOOL, not a missing threshold"*).
⇒ Artık eşleme değil **ÖLÇÜM** yapabilirsin; bu gece verdiğin `A 0 · A′ 10 · B 0 · C 0 · D 3`
**senin okumandı** çünkü ölçecek metin yoktu — şimdi var.

## ③ `O-117` katlama-altı bulgusu — **hüküm verildi**
Şerit **375×812'de katlamanın altında**. **Bu tasarım yönü DEĞİL, ERİŞİLEBİLİRLİK kusuru:**
- ✅ **Yetkin var:** var olan giriş kapısını **ulaşılabilir kılmak**, ve **375×812'de ölçülen bir
  testle** kanıtlamak
- ⛔ **Yetkin yok:** görsel tasarımı değiştirmek, kavramsal olarak taşımak, yeni bileşen icat etmek
> *Bir öğenin görünür olması tasarım kararıdır; VARILABİLİR olması bir ölçüm kalemidir.*

## `A12` — donanım VAR, engel İMZA
`flutter devices` → gerçek iPhone **bağlı**, ama `xctrace` onu **"Devices Offline"** altında
listeliyor, ve `com.yulalab.ostinato` profili **yok** ⇒ **B1/B7, kurucuda.**
⛔ Kurucunun telefonuna kurulum yapma; **reçeteyi imzaya kadar hazırla.**
📌 Var olan tüm kanıt **simülatör** ve `docs/evidence/README.md` bunu **adıyla** yazıyor
(*"Kaynak SAHTE ve ekranın en üstünde öyle yazıyor"*) — bu dürüstlük korunacak.

---

## SENİN BEDELLE ÖĞRENDİKLERİN — kendine uygula

- ⭐ **`A11-iOS`'i çözerken ÜÇ hipotezini üst üste çürüttün** (pin · bayat `build/ios` · hook
  koşmamış) ve dördüncüde buldun: **`.dart_tool` önbelleği**. **Depoda sıfır dosya değişti**
  ⇒ ürün kusuru değil **ORTAM** kusuru, taze klon/CI hiç görmezdi.
  > *Bir hipotezi çürütmek, doğrusunu bulmanın yolu — ve üç çürütme bir tahminden ucuzdur.*
- ⭐ **Koordinatörün iCloud uyarısını ÇÜRÜTTÜN:** `git fsck` **exit 0**, `.git` **sağlam**;
  bozulan **çalışma ağacıydı** (`.mutA-log 2.jsonl` çakışma kopyası). ⇒ Aile hafızasındaki
  *"iCloud `.git`'i bozuyor"* **bu vakada geçerli değildi.** Ayrım kayda geçti.
- ⭐ **Kalıntı mutasyon:** `git diff --stat` **996 satır**, `-w` ile **2** ⇒ ***bir farkın
  büyüklüğü, onu gösteren aracın ayarı kadardır.***
- 🪤 **Kendi iki alet tuzağın:** `grep -c '^   ⛔'` → *"3 kapı kırmızı"* okudun, oysa o üç satır
  yürüyüş testinin **(c) varılamayan** çıktısıydı (doğru desen `BAŞARISIZ$` → **0**) ·
  arka plan bildirimi **exit 0** dedi, gerçek `flutter build` çıkışı **1**'di
  (`date`'in kodu) ⇒ ***bir sarmalayıcının çıkış kodu, sardığı şeyin sonucu değildir.***
- 🪤 **`return const SettingsScreen();`** — desen `const`/`new` atlamıyorsa **parametresiz bir kök
  yüzeyi HİÇ görünmez.**
- 🪤 **"Sabotaj inmedi"nin BEŞİNCİ yolu sende ölçüldü: KORUMA ÇİFT** — iki desen birbirinin
  yedeğiyse **tek mutasyon çapayı kıramaz.**
- 🪤 **`A8` md5 ayrışması kusur DEĞİL** — Xcode XML plist'i **binary**'ye çeviriyor.
- 🔴 **Sözleşme (c)'de açık bir kusur bıraktın, adıyla:** `gen_screen_candidates.py:88` deseni
  `widget.source ?? CameraPoseSource()` satırındaki **YEDEĞİ** zorunlu bağımlılık sanıyor ⇒
  üç sebebin **biri doğru** (`SetupCheck`), **ikisi yanıltıcı** (`Live` · `Review`).
  ***Yanlış bir sebep, sebepsizlikten daha kötüdür: denetimi doğrulanmış gösterir.***
  `A1` turunda kendiliğinden çözülebilir — çözülürse **söyle**.
- 🔴 **Aile kuralı, sana da:** *metin tarayan bir kapı YORUMLARI kodla aynı sayar.* **35 python
  kapın** var — fırsat bulduğunda bu gözle ölç, ayrı tur açma.

## ⛔ KOORDİNATÖRE GİDEN
`B8` ikon · `A12` imza · **`B2` sürüm ayrışması:** `pubspec.yaml` → **`version: 1.0.0+1`**,
oysa B2 *"5 hattın 4'ünde `0.1.0+1`"* diyor — **sen o dördün dışındasın**, ASC tarafı ölçülmedi.
