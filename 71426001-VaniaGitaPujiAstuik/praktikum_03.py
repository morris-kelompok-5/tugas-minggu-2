# ==========================================
#PRAKTIKUM 3: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ==========================================

print("== PROGRAM HITUNGAN DERET ARITMATIKA ==")

awal = int(input("Maukkan Suku Pertama (a):"))
beda = int(input("Masukkan Beda Deret   (b)"))

#1. IMPLEMENTASI WHILE: Valibasi input jumalh suku agar harus positif (> 0) 
banyak = int(input("Masukkan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringkat Banyak suku harus lebih dari 0!")
    banyak = int(input("Silakan masukkan ulang Banyak Suku (n): "))

#2. IMPLEMENTASI FOR & AKUMULATOR: Memcetak deret dan menjumlahkan totalnya
suku = awal
tptal = 0 # Celengan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku    # Akumulasikan penjumlahan bertahap
    suku += beda     # Menyimpan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")