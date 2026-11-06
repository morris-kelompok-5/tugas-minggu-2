# ==================================
# PRAKTIKUM 2 : BILANGAN PRIMA & BREAK
# SIMPAN SEBAGAI : praktikum_02.py
# ==================================

def cek_prima(angka):
    angka = int(input("Masukkan Angka: "))
    is_prima = True # 


    if angka < 2:
        is_prima = False
    else:
        for pembagi in range(2,angka):
            if angka % pembagi == 0 :
                is_prima = False
            break


    if is_prima:
        print(F"{angka} Adalah BILANG PRIMA")
    else:
        print(F"{angka} BUKAN BILANGAN PRIMA")



cek_prima(True)