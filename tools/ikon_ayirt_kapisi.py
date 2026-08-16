#!/usr/bin/env python3
"""Aile ikon ayırt-edilebilirlik kapısı  —  H-60

NE ÖLÇER: iki markanın renginin, MAĞAZA IZGARASINDA ayırt edilebilir olup olmadığını.

NEDEN HEX KARŞILAŞTIRMASI DEĞİL: sRGB'de eşit sayısal adımlar eşit ALGISAL adımlar
değildir. #F0A6BD ile #B0748F sayıca uzak görünür, ikisi de gül tonudur. Doğru uzay
OKLCH: L (açıklık) · C (doygunluk) · H (ton açısı).

KAPSAM BEYANI — bu kapının GÖRMEDİĞİ şeyler (H-23: kapatılamayan deliği
kapatılmış göstermek, deliğin kendisinden kötüdür):
  · GLİF/BİÇİM. Kırmızı bir daire ile kırmızı bir boks eldiveni bu kapıda AYNI çıkar,
    gözde ayrıdır. Kapı rengi ölçer, biçimi ölçmez.
  · ORTALAMA renk. 1×1 indirgeme bir ikonu tek sayıya düşürür; iki renkli bir ikonun
    ortalaması iki rengin hiçbiri olmayabilir.
  · Renk körlüğü. Deuteranopia'da kırmızı/yeşil ayrımı bu kapının verdiğinden azdır.
  · Koyu/açık mod. Tek bir varlık ölçülür, iki temadaki görünümü değil.

KURAL (M-F-681'de ölçümle kalibre edildi):
  ΔH >= 60°                     -> AYIRT EDİLİR, başka koşul aranmaz
  ΔH <  60° ise, EK OLARAK:     ΔL >= 0.15  VEYA  ΔC >= 0.08 gerekir
  ikisi de yoksa                -> ÇARPIŞMA

Kalibrasyon dayanağı: Choreia(#F0A6BD) ile Lissom(#B0748F) ΔH=7.9° ile aynı tonda
ama ΔL=0.173 ile açıklıkta ayrık — ve gözle bakınca GERÇEKTEN ayrılıyorlar. Kural
onları GEÇİRMELİ. Gravita(#A11019) ile JabLab vurgusu(#CE2F36) ΔH=1.8 · ΔL=0.073 ·
ΔC=0.027 — hiçbir eksende ayrılmıyorlar, kural onları DÜŞÜRMELİ.

KULLANIM
  python3 tools/ikon_ayirt_kapisi.py                     # aileyi tara
  python3 tools/ikon_ayirt_kapisi.py '#CC7722' choreia   # aday rengi sına
"""
import math
import sys

# --- kilitli aile renkleri: GERÇEK ikonlardan ölçüldü (stok olanlar hariç) ---
# Ölçüm: sips -z 1 1 ile 1×1 indirgeme, 1024×1024 AppIcon'dan. 2026-08-16.
GERCEK_IKONLAR = {
    "gravita": "#AA262F",
    "ostinato": "#252B45",
}
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


def _tara():
    kaynak = [(n, h, "ikon") for n, h in GERCEK_IKONLAR.items()]
    kaynak += [(n, h, "TEMA(tahmin)") for n, h in TEMA_VURGULARI.items()]
    print("=== AİLE İKON AYIRT-EDİLEBİLİRLİK TARAMASI ===\n")
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
    if carpisma == 0:
        print("  ✅ çarpışma yok")
    print(f"\n  toplam çarpışma: {carpisma}")
    return 1 if carpisma else 0


def main():
    if len(sys.argv) == 3:
        aday, hat = sys.argv[1], sys.argv[2].lower()
        tum = dict(GERCEK_IKONLAR, **TEMA_VURGULARI)
        tum.pop(hat, None)
        print(f"=== ADAY {aday} — {hat} için, {len(tum)} kardeşe karşı ===\n")
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
