#!/usr/bin/env python3
"""Posta kutusundaki hükümlerin İNDEKSİNİ üretir — İÇERİK KOPYALAMAZ.

NEDEN BÖYLE: bir kural belgesi, kuralların zaten canlı yaşadığı bir kanalın
yanına yazıldığında ikinci bir otorite üretir, ve iki otoriteden biri her zaman
bayattır (`AILE-KURALLARI-ADAY-2026-08-12.md` bunun kanıtı: 91 kayıt geride
kaldı ve kimse fark etmedi). Bu yüzden indeks yalnız İŞARET taşır:
numara, tarih, muhatap, başlık. Hükmün kendisi tek yerde yaşar.

Bayatlığı MEKANİK olarak yakalanabilir: yeniden üret, diff al.
    python3 tools/hukum_index.py > devir/HUKUM-INDEKSI.md
"""
import re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "devir" / "KOORDINATOR-HUKUMLERI.md"
NOISE = re.compile(r"\*\*|`|[\U0001F300-\U0001FAFF☀-➿️]")

def rows():
    for line in SRC.read_text().split("\n"):
        m = re.match(r"^## (H-\d+) · ([0-9-]+) · ([^—]+)—\s*(.*)$", line)
        if m:
            num, date, who, title = m.groups()
            t = re.sub(r"\s+", " ", NOISE.sub("", title)).strip()
            yield int(num[2:]), num, date, re.sub(r"\s+", " ", NOISE.sub("", who)).strip(), t

def main():
    rs = sorted(rows(), key=lambda r: -r[0])
    nums = {r[0] for r in rs}
    gaps = [n for n in range(min(nums), max(nums) + 1) if n not in nums] if rs else []
    print("# 📇 HÜKÜM İNDEKSİ — yalnız işaret, içerik DEĞİL\n")
    print("> ⚠️ **Bu dosya OTORİTE DEĞİLDİR.** Hükmün metni tek yerde yaşar:")
    print("> `devir/KOORDINATOR-HUKUMLERI.md`. Burada yalnız *nerede ne var* yazılıdır.")
    print("> Üretim: `python3 tools/hukum_index.py > devir/HUKUM-INDEKSI.md` — bayatlığı")
    print("> yeniden üretip `diff` alarak **mekanik** olarak yakalayın.\n")
    print(f"**{len(rs)} hüküm** · en yeni `{rs[0][1]}` · numara gediği: "
          f"**{gaps if gaps else 'YOK'}**\n")
    print("| # | tarih | muhatap | konu |")
    print("|---|---|---|---|")
    for _, num, date, who, t in rs:
        print(f"| `{num}` | {date} | {who} | {t} |")

if __name__ == "__main__":
    main()
