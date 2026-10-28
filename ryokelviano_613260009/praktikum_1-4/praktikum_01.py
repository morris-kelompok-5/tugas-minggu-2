# =================================
# PRATIKUM 1: NESTED IF (EVALUASI KELULUSAN)
# Simpan sebagai: praktikum_01.py
#==================================

kehadiran = int(input("Jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (0-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai Ujian Kurang")
    else:
        print("REMEDIAL - NILAI Ujian Kurang")
else:
    print("TIDAK LULUS - Kehadiran Kurang dari 12")        
