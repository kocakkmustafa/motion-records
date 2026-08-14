# Motion Ailesi — LOOP (oturum protokolü)
1. `../VENTURE.md` + PROGRESS son mühür + DEFTER açık maddeler OKU.
2. 🔒 Kod kilidi: kurucu "X'e başlayalım" demediyse bu oturum yalnız hazırlık/doküman işidir.
3. Başlangıç oturumuysa: 00-AILE-MIMARISI → <app>-plan → V0 kapısı → kurucuya kapı sonucu.
4. Kapanışta: /oturum-kapanisi skill'i (devir notu + pano + PROGRESS mühür + gerekirse regen).

## Koordinatör kuyruğu (güncelleme 2026-07-29 — M-F-20 turu sonrası)

✅ TAMAM (2026-07-29 turu; kanıtlar M-F-20..23): bootstrap+lissom dalları main'de ·
JabLab araçları mocore çatısında (fixture v2) · G-010/ADR-001 çekirdekte (M-019
kapalı) · M-F-07 provenance + M-F-08 gecikme-kalibrasyonu + MotionClock + CueGate ·
`motion_core-v0.1.0` tag'i + pin duyurusu · hasat rig'i (`tools/harvest_rig/`) ·
Art.50 paketi (`docs/compliance/` + `tools/art50/`) · M-O-01 yanıtı (M-F-23).

KALAN (tur-4 eklemeleri başta):
0a. **PoseFrame koordinat-uzayı sözleşmesi + piksel-ölçekleme yardımcısı (M-F-30/J-028, P0):** uzay dokümantasyonu + FrameSize-tarzı API çekirdeğe; JabLab'ın app-side kopyası devralınır.
0b. **G-019: yatay-gövde takas-değişmezi tasarımı** (eksen çekimserken StructuralValidator boşluğu; Gravita #9 fixture'ı girdi).
1. **AI-eğitmen T2 pilotu (M-F-15):** Champ (Apache) ile 1 jab + 1 handstand
   referans-iskelet animasyonu → form-denetim raporu kurucuya; T1 iskelet-avatar
   render sözleşmesi (Flutter/Rive) core'a. Ön-şart: hasat rig'inden ilk gerçek
   referans dizileri (app oturumları kaynak listeleri beslesin).
2. **DTW uzun-sekans genişletmesi (M-F-21):** pencereli dakika-ölçekli hizalama +
   kesit-bazlı skor raporu; JabLab-TaiChi + Choreia tüketici.
3. **RhythmEngine onset-event arayüzü (M-F-21):** ses/MIDI/pose kaynak-bağımsız;
   Ostinato metronom-hiza fixture'ları buradan akar.
4. **Rule-set config şemasını mühürle** (Ostinato `ruleset-v0.md` girdi; M-F-23e).
5. Hasat rig'i İLK GERÇEK KOŞUM: app'lerden `queue.txt` kaynak listeleri gelince
   pilot hasat (app-başına 3-5 video) + rig pürüz listesi.
6. M-015 rakip elle-doğrulama takibi · pano/vault güncelliği.

⚠️ ÇALIŞMA KURALI (M-F-22): paylaşımlı ağaçta dal DEĞİŞTİRME; koordinatör işi
`~/motion-worktrees/coordinator-main`'de (main oraya kilitli).
