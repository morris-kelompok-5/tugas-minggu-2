# =====================================================
# PRAKTIKKUM 3: DERET ARIMATIKA & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# =====================================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret    (b): "))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (>. 0)
banyak = int(input("Masukkan Banyak Suku  (n): "))
while banyak <= 0:
    print("Peringatkan Banyak suku harus lebih dari 01")
    banyak = int(input("Silakan masukkan ulang banyak suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0 #Celengan Akumula

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku  #Akumulasi penjumlahan bertahap
    suku += beda  #Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")