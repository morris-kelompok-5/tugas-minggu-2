kehadiran = int(input("Masukkan jumlah kehadiran: "))
nilai = int(input("Masukkan nilai ujian (0-100): "))

if kehadiran >= 8:
    if nilai >= 80:
        print("Lulus dengan predikat sangat baik")
    elif nilai >= 70:
        print("Lulus dengan predikat baik")
    else:
        print("Lulus dengan predikat cukup")
else:
    print("Tidak lulus karena kehadiran kurang dari 13x")