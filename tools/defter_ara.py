#!/usr/bin/env python3
"""Türkçe-güvenli defter araması  —  H-64

NEDEN VAR: `grep -i` Türkçe büyük harfi katlamaz. ASCII katlaması yalnız a-z↔A-Z
bilir; Ç↔ç · Ğ↔ğ · İ↔i · I↔ı · Ö↔ö · Ş↔ş · Ü↔ü çiftlerini TANIMAZ. Defterlerimiz
başlıkları BÜYÜK HARFLE yazıyor ⇒ `grep -i 'açılış'` bir kaydı bulur, `AÇILIŞ`
yazılmış olanı KAÇIRIR.

ÖLÇÜM (2026-08-16): iki satırlık bir dosyada `grep -ic 'açılış'` -> 1, beklenen 2.
Bu yanlış-negatif gerçek bir hükmü kirletti: Choreia'nın C-296 kaydı ("İKON/AÇILIŞ
VARLIKLARININ 25/25'İ HÂLÂ FLUTTER STOĞU", adlı+tarihli+P0) VARDI ama tarama onu
görmedi ve H-59 "kayıt yok" dedi. Choreia düzeltti.

EK TUZAK — 'i' harfinin iki yönü: Türkçe'de I'nın küçüğü 'ı', İ'nin küçüğü 'i'.
Python'un `.lower()`ı Türkçe bilmez ('I'.lower() -> 'i', Türkçe'de 'ı' olmalı).
Bu yüzden katlama ELLE yapılıyor, `.lower()`a güvenilmiyor.

KAPSAM BEYANI — bu aracın GÖRMEDİĞİ şeyler (H-62: vakum testi körleşmeyi yakalar,
doğuştan darlığı yakalamaz; H-23: kapatılamayan deliği kapatılmış göstermek kötüdür):
  · ANLAM. "açılış ekranı" yazan bir kaydı bulur, "mağazada görülecek ilk şey"
    diyeni BULMAZ. Kelime arar, kavram aramaz. (H-58 ② sınıfı.)
  · EŞ ANLAMLI. splash/launch/açılış/karşılama ayrı kelimelerdir; hepsini VERMELİSİN.
  · Kayıt YOKLUĞUNU kanıtlamaz. Bir şey bulunamadıysa "kayıt yok" DEĞİL,
    "bu kelimelerle bulunamadı" denir.

KULLANIM
  python3 tools/defter_ara.py <defter.md> açılış splash launch ikon
  python3 tools/defter_ara.py --hepsi açılış splash    # beş hattın defterinde ara
"""
import re
import sys
from pathlib import Path

# Türkçe büyük/küçük çiftleri — .lower() bunları doğru yapmaz, elle katlıyoruz.
_CIFTLER = {
    "Ç": "ç", "Ğ": "ğ", "İ": "i", "I": "ı", "Ö": "ö", "Ş": "ş", "Ü": "ü",
}
_TERS = {v: k for k, v in _CIFTLER.items()}

DEFTERLER = {
    "choreia": "choreia/app/workspace/DEFTER.md",
    "gravita": "gravita/app/workspace/DEFTER.md",
    "jablab": "jablab/app/workspace/DEFTER.md",
    "lissom": "lissom/app/workspace/DEFTER.md",
    "ostinato": "ostinato/app/workspace/DEFTER.md",
}
VENTURES = Path("/Users/mustafakaankocak/Documents/YULAlab-AI/ventures")


def katla(s):
    """Türkçe-farkında küçültme. 'AÇILIŞ' -> 'açılış', 'IRMAK' -> 'ırmak'."""
    out = []
    for ch in s:
        if ch in _CIFTLER:
            out.append(_CIFTLER[ch])
        else:
            # ASCII küçültme; Türkçe olmayanlar için güvenli
            out.append(ch.lower() if ch.isascii() else ch.lower())
    return "".join(out)


def ara(yol, kelimeler):
    """(satır_no, kelime, satır) üçlüleri döndürür."""
    p = Path(yol)
    if not p.exists():
        return None
    hedefler = [katla(k) for k in kelimeler]
    bulunan = []
    for i, satir in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        kat = katla(satir)
        for orij, hedef in zip(kelimeler, hedefler):
            if hedef in kat:
                bulunan.append((i, orij, satir))
                break
    return bulunan


def _kimlik(satir):
    """Kayıt ID'sini çıkar (| M-F-123 | veya | **C-296** |)."""
    m = re.search(r"\|\s*\*{0,2}([A-Z]-[A-Z]?-?\d+)\*{0,2}\s*\|", satir)
    return m.group(1) if m else "—"


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--hepsi":
        kelimeler = argv[1:]
        if not kelimeler:
            print("kelime ver"); return 2
        toplam = 0
        for hat, rel in sorted(DEFTERLER.items()):
            sonuc = ara(VENTURES / rel, kelimeler)
            if sonuc is None:
                print(f"=== {hat}: DEFTER YOK ({rel}) ==="); continue
            print(f"=== {hat}: {len(sonuc)} satır ===")
            for no, kelime, satir in sonuc[:6]:
                print(f"  {no:>5}  [{kelime}]  {_kimlik(satir):<8} {satir[:110]}")
            if len(sonuc) > 6:
                print(f"        … {len(sonuc)-6} satır daha")
            toplam += len(sonuc)
        print(f"\ntoplam: {toplam} satır")
        print("⚠️ Bulunamadıysa 'kayıt YOK' DEME — 'bu kelimelerle bulunamadı' de.")
        return 0
    sonuc = ara(argv[0], argv[1:])
    if sonuc is None:
        print(f"dosya yok: {argv[0]}"); return 2
    for no, kelime, satir in sonuc:
        print(f"{no:>5}  [{kelime}]  {_kimlik(satir):<8} {satir[:140]}")
    print(f"\ntoplam: {len(sonuc)} satır")
    print("⚠️ Bulunamadıysa 'kayıt YOK' DEME — 'bu kelimelerle bulunamadı' de.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
