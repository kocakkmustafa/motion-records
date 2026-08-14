# PAYLAŞIMLI KAYITLARIN ÖLÇÜM AYRIMI — 6 kural / 3 kayıt (Lissom, 2026-08-12)

> ⛔ **Hüküm koordinatörde.** Burada yapılan tek şey: her kural için **O KURALA
> AİT** ölçümü kaydın gövdesinden **satır başına okuyarak** ayırmak.
> ⛔ **Kanıt sütunu KOPYALANMADI** — Gravita'nın aracının sessizce aldığı kısayol.

## PAYDA

| ölçüm | değer |
|---|---|
| paylaşımlı kural | **6** (3 kayıt × 2) |
| **ayrılan** | **6** |
| **ayrılamayan** | **0** |
| denetim | `6 + 0 = 6` ✅ |

---

## M-F-524 — 4.2 ↔ 4.3

⚠️ **Bu kayıt gerçekten zordu:** iki ölçüm **uzun gövdenin farklı yerlerinde**
ve **numaralı bölüm yok** — mekanik çıkarımın ikisine aynı diziyi vermesinin
sebebi bu.

| kural | O KURALA AİT ölçüm |
|---|---|
| **4.2** *Bir aracın DUVARI, sorunun duvarı değildir* | `probe_knee_dips` *"kinematik karşılaştırma koşulamıyor, step config yok"* diyor — ama `prepare_take --step hh_running_man --video` **ÇALIŞIYOR** (**17,0 sn** segment · **1,38 sn** periyot). Engel araçtaydı, soruda değil; koordinatörün *"koşulamıyorsa DUR"* dalı bu yüzden **hiç devreye girmedi**. |
| **4.3** *Bir süpürgenin ÖTMESİ, DOĞRU ŞEYE ötmesi demek değildir* | Kimlik süpürmesi (C-225): ilk sayım **11/13**. `KV-sxd_pQ9w`'nin eşleşmesi **YANLIŞ POZİTİF** — eşleşen cümle *kanal tekrarı* hakkındaymış. Gerçek: **12/13**. ⇒ pozitif kontrolün **dördüncü yüzü: isabetin İÇERİĞİ**. |

## M-F-568 — 4.10 ↔ 4.11

📌 Bu kayıt **başlığında iki kuralı da adıyla** taşıyor ve gövdesi **numaralı
bölümlere** ayrılmış ⇒ ayrım kayıtta **zaten vardı**.

| kural | O KURALA AİT ölçüm |
|---|---|
| **4.10** *Karakter kümesiyle tanınma ≠ her kipte tanınma* (JabLab) | `'BİR'.toLowerCase() == 'bir'` → **TRUE** (Dart). Koordinatörün tablosundaki bir satır **Python'undu, Dart'a yapıştırılmıştı**. Düzeltilmiş: **Python** 🔴 yalnız `İ` (`re.I` çalışıyor) · **Dart** 🔴 yalnız `ı`. |
| **4.11** *Kaynağı regex'le okumak üyeyi anlatandan ayıramaz* (Lissom) | `harvest_prescreen` maruz bildirilmişti; kaynak-regex `"zayıf"`/`"görüş"`/`"iki kişi"` bulmuş ve bunlar **DESEN** sanılmıştı. **Introspection'la** ölçünce: eşleşen kümelerde **Türkçe desen SIFIR** — bulunanlar **etiket ve gerekçe** dizeleriydi. **Değişiklik GERİ ALINDI.** |

## M-F-577 — 2.9 ↔ 2.10

📌 Gövde **①/②** diye numaralı ⇒ ayrım kayıtta **zaten vardı**.

| kural | O KURALA AİT ölçüm |
|---|---|
| **2.9** *Savunmanın kaç katmanı olduğunu aşmaya çalışmadan bilemezsin* | Altından geçmeye çalışınca **ÜÇÜNCÜ katman göründü**: `honesty_box.dart`'ın **`notMeasured.length > 0`** assert'i boş listeyle çizdirmiyor ⇒ fixture *"liste dolu ama içinde kapalılık sebebi yok"* biçimine zorlandı. **Üç katman**: `Library.validate` · `honesty_box` assert'i · içerik şeması. |
| **2.10** *Pozitif kontrol, aynısını çalıştırmıyorsa kendi kopyasını doğrular* | Dedektör **ortak fonksiyona** çıkarıldı (`hasNamedReason`) ve **iki yönde** sınandı: gerekçesiz sentetik kart → dedektör **ÇIKMAZ diyor** ✅ · gerekçeli kapalı kart → **SUSUYOR** ✅ (**10 meşru kova** kırmızıya boyanmadı). |

---

## 📌 BULGU: "paylaşımlı" üç kaydın ikisi aslında paylaşımlı DEĞİLDİ

`M-F-568` ve `M-F-577` **başlığında/gövdesinde ayrımı zaten taşıyordu**
(adıyla anılan iki kural · numaralı bölümler). Mekanik çıkarım onları
*"paylaşımlı"* gösterdi çünkü **kayıt kimliğine** bakıyordu, **gövde
yapısına** değil.

> ***Bir kaydın İKİ kural taşıması, o kuralların AYRILMAMIŞ olduğu anlamına
> gelmez — ayrım gövdede olabilir, çıkarıcı ona bakmıyordur.***

**Gerçekten ayrım gerektiren tek kayıt `M-F-524`'tü**: iki ölçüm uzun bir
gövdenin farklı yerlerinde, numaralı bölüm yok. ⇒ *"3 paylaşımlı kayıt"*
sayısı **1**'e iner; ikisi **çıkarıcının kör noktasıydı**.
