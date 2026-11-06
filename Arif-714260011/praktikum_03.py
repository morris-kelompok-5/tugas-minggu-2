# ==========================================
# PRAKTIKUM 3 : DERET ARIMATIKA & AKUMULATOR
# SIMPAN SEBAGAI : praktikum_03.py
# ==========================================


print("=== PROGRAM HITUNG DERET ARITMATIKA ===")


awal = int(input("MASUKKAN SUKU PERTAMA (A) : "))
beda = int(input("MASUKKAN BEDA DERET (B) : "))


banyak = int(input("MASUKKAN BANYAK SUKU (n): "))

while banyak <= 0:
    print("Peringatan Banyak suku harus lebih dari 0")
    banyak = int(input("SILAKAN MASUKAN ULANG BANYAK SUKU (n)"))


suku = awal
total = 0

print("berisan deret:", end="")
for i in range(banyak):
    print(suku,end=" ")
    total += suku
    suku += beda

print(F"total jumlah seluruh deret = {total}")