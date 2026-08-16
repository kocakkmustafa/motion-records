#!/usr/bin/env python3
"""Aile ikon ayırt-edilebilirlik kapısı  —  H-60 / H-67 (2026-08-16)

NE ÖLÇER: iki markanın renginin, MAĞAZA IZGARASINDA ayırt edilebilir olup olmadığını.

NEDEN HEX KARŞILAŞTIRMASI DEĞİL: sRGB'de eşit sayısal adımlar eşit ALGISAL adımlar
değildir. #F0A6BD ile #B0748F sayıca uzak görünür, ikisi de gül tonudur. Doğru uzay
OKLCH: L (açıklık) · C (doygunluk) · H (ton açısı).

⚠️ H-67 DÜZELTMESİ (2026-08-16, Ostinato ölçtü): önceki sürüm renkleri ELLE YAZILMIŞ
hex sabitleriyle taşıyordu (`GERCEK_IKONLAR`/`TEMA_VURGULARI`) — H-58/H-65'in kapattığı
TAM sınıf: bir sayı metinde duruyor, gerçekle bağı yok, bir hat ikon yapar yapmaz
BAYATLAR. Şimdi kapı HER koşumda GERÇEK `AppIcon` PNG'lerini okur — elle güncelleme
gerektirmez, olduğu gibi ölçer.

SALT-OKUNUR: yalnız kardeş hatların `AppIcon` PNG'lerini OKUR, hiçbir dosyaya YAZMAZ
(`sips`in ara 1×1 çıktısı sistem geçici dizinine gider, hiçbir venture'a değil).

KAPSAM BEYANI — bu kapının GÖRMEDİĞİ şeyler (H-23: kapatılamayan deliği
kapatılmış göstermek, deliğin kendisinden kötüdür):
  · GLİF/BİÇİM. Kırmızı bir daire ile kırmızı bir boks eldiveni bu kapıda AYNI çıkar,
    gözde ayrıdır. Kapı rengi ölçer, biçimi ölçmez.
  · ORTALAMA renk. 1×1 indirgeme bir ikonu tek sayıya düşürür; iki renkli bir ikonun
    ortalaması iki rengin hiçbiri olmayabilir.
  · Renk körlüğü. Deuteranopia'da kırmızı/yeşil ayrımı bu kapının verdiğinden azdır.
  · Koyu/açık mod. Tek bir varlık ölçülür, iki temadaki görünümü değil.
  · TEMA VURGUSU → İKON tahmini KESİN DEĞİL (Ostinato #5F4CA0 seed'i #252B45 ikonundan
    AYRI çıktı) — bu yüzden tahminler `🔮 ÖNGÖRÜ` etiketiyle işaretlenir, gerçek
    ikonla AYNI kesinlikte sunulmaz.

KURAL (M-F-684'te ölçümle kalibre edildi):
  ΔH >= 60°                     -> AYIRT EDİLİR, başka koşul aranmaz
  ΔH <  60° ise, EK OLARAK:     ΔL >= 0.15  VEYA  ΔC >= 0.08 gerekir
  ikisi de yoksa                -> ÇARPIŞMA

Kalibrasyon dayanağı: Choreia(#F0A6BD) ile Lissom(#B0748F) ΔH=7.9° ile aynı tonda
ama ΔL=0.173 ile açıklıkta ayrık — ve gözle bakınca GERÇEKTEN ayrılıyorlar. Kural
onları GEÇİRMELİ. Gravita(#A11019) ile JabLab vurgusu(#CE2F36) ΔH=1.8 · ΔL=0.073 ·
ΔC=0.027 — hiçbir eksende ayrılmıyorlar, kural onları DÜŞÜRMELİ.

KULLANIM
  python3 tools/ikon_ayirt_kapisi.py                     # aileyi tara (canlı okuma)
  python3 tools/ikon_ayirt_kapisi.py '#CC7722' choreia   # aday rengi sına
"""
import hashlib
import math
import subprocess
import sys
import tempfile
from pathlib import Path

VENTURES = Path("/Users/mustafakaankocak/Documents/YULAlab-AI/ventures")
ICON_REL = "app/ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-1024x1024@1x.png"
HATLAR = ["choreia", "gravita", "jablab", "lissom", "ostinato"]

#: Flutter'ın stok 1024×1024 AppIcon'unun MD5'i — TAZE bir `flutter create`
#: referansından ölçüldü (Flutter 3.41.1, aynı SDK; bkz. ostinato/app/tools/
#: validate_template_assets.py, aynı yöntem, O-158). SDK yükselirse şablonun
#: kendisi değişebilir — bu durumda bir hat GERÇEKTEN stok kalsa bile "gerçek
#: ikon" sanılabilir; `main()`in kendi uyarısı bunu adıyla söyler.
STOK_MD5 = "c785f8932297af4acd5f5ccb7630f01c"

# --- tema vurgu renkleri: ikonu HENÜZ OLMAYAN hatlar için TAHMİN girdisi ---
# ⚠️ Bunlar ikon DEĞİL. Ostinato ikonunu (#252B45) kendi seed'inden (#5F4CA0)
#    ayırdı ⇒ seed'den ikon TAHMİN ETMEK kesin değildir. Uyarı olarak kullanılır.
TEMA_VURGULARI = {
    "choreia": "#F0A6BD",
    "jablab": "#CE2F36",
    "lissom": "#B0748F",
}


def _srgb_to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def hex_to_oklch(h):
    """sRGB hex -> (L, C, H derece). Björn Ottosson OKLab dönüşümü."""
    h = h.lstrip("#")
    r, g, b = (_srgb_to_lin(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    A = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    B = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360


def ton_farki(h1, h2):
    d = abs(h1 - h2) % 360
    return min(d, 360 - d)


def ayirt_edilir_mi(hex1, hex2):
    """(gecti: bool, gerekce: str, olcum: dict) döndürür."""
    L1, C1, H1 = hex_to_oklch(hex1)
    L2, C2, H2 = hex_to_oklch(hex2)
    dH, dL, dC = ton_farki(H1, H2), abs(L1 - L2), abs(C1 - C2)
    olcum = {"dH": dH, "dL": dL, "dC": dC}
    if dH >= 60:
        return True, f"ton {dH:.1f}° ayrık (>=60)", olcum
    if dL >= 0.15:
        return True, f"ton yakın ({dH:.1f}°) ama açıklık {dL:.3f} ayırıyor (>=0.15)", olcum
    if dC >= 0.08:
        return True, f"ton yakın ({dH:.1f}°) ama doygunluk {dC:.3f} ayırıyor (>=0.08)", olcum
    return False, (f"ÇARPIŞMA: ton {dH:.1f}° · açıklık {dL:.3f} · doygunluk {dC:.3f} "
                   f"— HİÇBİR eksende ayrılmıyorlar"), olcum


class HatDurumu:
    """Bir hattın ikon durumu — üç ayrı hâl, üçü de FARKLI anlam taşır
    (H-20 dersi: yokluk/stok/gerçek aynı kutuya düşmemeli)."""
    def __init__(self, hat, hal, hex_renk=None, sebep=None):
        self.hat, self.hal, self.hex, self.sebep = hat, hal, hex_renk, sebep
        # hal: "gercek" | "stok" | "kor"


def oku_ikon_rengi(hat: str) -> HatDurumu:
    """SALT-OKUNUR: yalnız `AppIcon` PNG'sini okur, hiçbir yere yazmaz (`sips`
    çıktısı sistem geçici dizinine gider)."""
    p = VENTURES / hat / ICON_REL
    if not p.exists():
        return HatDurumu(hat, "kor", sebep=f"dosya yok: {p}")
    try:
        raw_md5 = hashlib.md5(p.read_bytes()).hexdigest()
    except Exception as exc:
        return HatDurumu(hat, "kor", sebep=f"okunamadı: {exc}")
    if raw_md5 == STOK_MD5:
        return HatDurumu(hat, "stok", sebep="Flutter stok ikonuyla MD5-birebir")
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / f"{hat}_1x1.png"
        proc = subprocess.run(
            ["sips", "-z", "1", "1", str(p), "--out", str(out)],
            capture_output=True, text=True)
        if proc.returncode != 0 or not out.exists():
            return HatDurumu(hat, "kor", sebep=f"sips başarısız: {proc.stderr[-200:]}")
        try:
            from PIL import Image
            img = Image.open(out).convert("RGB")
            r, g, b = img.getpixel((0, 0))
        except Exception as exc:
            return HatDurumu(hat, "kor", sebep=f"piksel okunamadı: {exc}")
    return HatDurumu(hat, "gercek", hex_renk=f"#{r:02X}{g:02X}{b:02X}")


def _tara():
    print("=== AİLE İKON AYIRT-EDİLEBİLİRLİK TARAMASI (canlı okuma) ===\n")
    durumlar = {hat: oku_ikon_rengi(hat) for hat in HATLAR}

    kor = [d for d in durumlar.values() if d.hal == "kor"]
    if kor:
        print("  ⛔ KÖR OLDUM — bu hatlar için ikon durumu ÖLÇÜLEMEDİ "
              "('çarpışma yok' DEMİYORUZ, göremiyoruz):")
        for d in kor:
            print(f"     {d.hat}: {d.sebep}")
        print()

    kaynak = []
    for hat in HATLAR:
        d = durumlar[hat]
        if d.hal == "gercek":
            kaynak.append((hat, d.hex, "ikon"))
        elif d.hal == "stok":
            print(f"  📦 {hat}: HENÜZ İKON YAPMAMIŞ (stok Flutter ikonu, "
                  f"MD5-birebir) — renk karşılaştırmasına GİRMEZ")
            if hat in TEMA_VURGULARI:
                kaynak.append((hat, TEMA_VURGULARI[hat], "TEMA(tahmin)"))
        # "kor" hâli zaten yukarıda ayrı raporlandı, kaynağa hiç girmez.
    print()

    for n, h, k in sorted(kaynak):
        L, C, H = hex_to_oklch(h)
        print(f"  {n:<9} {h}  L={L:.3f} C={C:.3f} H={H:6.1f}°   [{k}]")
    print()
    carpisma = 0
    for i in range(len(kaynak)):
        for j in range(i + 1, len(kaynak)):
            n1, h1, k1 = kaynak[i]
            n2, h2, k2 = kaynak[j]
            gecti, gerekce, _ = ayirt_edilir_mi(h1, h2)
            if not gecti:
                carpisma += 1
                tahmin = "TEMA" in k1 or "TEMA" in k2
                etiket = "🔮 ÖNGÖRÜ" if tahmin else "🔴 GERÇEK"
                print(f"  {etiket}  {n1} <-> {n2}\n           {gerekce}")
    if carpisma == 0 and not kor:
        print("  ✅ çarpışma yok (ölçülebilen tüm ikonlar arasında)")
    elif carpisma == 0 and kor:
        print("  ⚠️  ölçülebilenler arasında çarpışma yok — ama yukarıdaki "
              "KÖR hatlar hiç değerlendirilmedi, bu 'temiz' anlamına gelmez")
    print(f"\n  toplam çarpışma: {carpisma} · kör: {len(kor)} · "
          f"stok (henüz ikonsuz): {sum(1 for d in durumlar.values() if d.hal == 'stok')}")
    return 1 if (carpisma or kor) else 0


def main():
    if len(sys.argv) == 3:
        aday, hat = sys.argv[1], sys.argv[2].lower()
        canli = {h: d.hex for h, d in
                  ((h, oku_ikon_rengi(h)) for h in HATLAR) if d.hal == "gercek"}
        tum = dict(canli)
        for h, hx in TEMA_VURGULARI.items():
            tum.setdefault(h, hx)
        tum.pop(hat, None)
        print(f"=== ADAY {aday} — {hat} için, {len(tum)} kardeşe karşı (canlı) ===\n")
        kotu = 0
        for n, h in sorted(tum.items()):
            gecti, gerekce, _ = ayirt_edilir_mi(aday, h)
            print(f"  {'✅' if gecti else '🔴'} {n:<9} {h}  {gerekce}")
            kotu += 0 if gecti else 1
        print(f"\n  {'✅ GEÇTİ' if not kotu else f'🔴 {kotu} çarpışma — başka renk seç'}")
        return 1 if kotu else 0
    return _tara()


if __name__ == "__main__":
    sys.exit(main())
