# =========================================
# PRAKTIKUM 3: BILANGAN DERET ARITMATIKA
# =========================================

print ("== PROGRAM BILANGAN DERET ARITMATIKA ==")

awal = int(input("Masukkan bilangan awal (a): "))
beda = int(input("Masukkan beda deret    (b): "))

banyak = int(input("Masukkan banyak bilangan: "))
while banyak <= 0:
    print("Banyak bilangan harus lebih dari 0")
    banyak = int(input("Masukkan banyak bilangan: "))

suku = awal
total = 0

print ("Deret Aritmatika: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku
    suku += beda 

print(f"Jumlah seluruh deret: {total}")