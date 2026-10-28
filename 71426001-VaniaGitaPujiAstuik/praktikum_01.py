# =============================================
#PRAKYIKUM 1: NESTED IF (EVALUASI KELULUSAN)
# Simpan sebagai: praktikum_01.py
# ============================================

kehadiran = int(input("Jumlah kehadiran (1-14):"))
nilai = int(input("Nilai ujiqn (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Memuaskan")
    else:
       print("RMEDIAL - Nilai Ujian Kurang")
else:
        print("TIDAK LULUS - Kehadiran Kurang Dari 12")