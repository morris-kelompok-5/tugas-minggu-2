# ==========================================
# PROGRAM UTAMA: kalkulator.py
# Aplikasi kalkulator konsol bermenu interaktif
# ==========================================

import operasi3  # Memanggil modul fungsi berpisah

while True:
    print("\n" + "=" * 45)
    print("         APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (Ganjil / Genap)")
    print("3. Hitung Deret Aritmatika (For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks (Nested Loop)")
    print("5. Keluar")
    print("=" * 45)
    
    pilihan = input("Pilih menu (1-5): ")
    
    # ------------------------------------------
    # MENU 5: KELUAR PROGRAM
    # ------------------------------------------
    if pilihan == '5':
        print("\nTerima kasih telah menggunakan Kalkulator Konsol!")
        break
        
    # ------------------------------------------
    # MENU 1: OPERASI ARITMATIKA DASAR
    # ------------------------------------------
    elif pilihan == '1':
        print("\n--- Sub-Menu Operasi Dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")
        
        op = input("Pilih operasi (A/B/C/D): ").upper()
        
        angka1 = input("Masukkan angka pertama: ")
        angka2 = input("Masukkan angka kedua: ")
        
        # Validasi input berupa angka
        if angka1.replace('.', '', 1).isdigit() and angka2.replace('.', '', 1).isdigit():
            a = float(angka1)
            b = float(angka2)
            
            if op == 'A':
                print(f"Hasil: {a} + {b} = {operasi3.tambah(a, b)}")
            elif op == 'B':
                print(f"Hasil: {a} - {b} = {operasi3.kurang(a, b)}")
            elif op == 'C':
                print(f"Hasil: {a} * {b} = {operasi3.kali(a, b)}")
            elif op == 'D':
                print(f"Hasil: {a} / {b} = {operasi3.bagi(a, b)}")
            else:
                print("Error: Pilihan operasi tidak valid!")
        else:
            print("Error: Masukkan angka yang valid!")
            
    # ------------------------------------------
    # MENU 2: CEK SIFAT BILANGAN
    # ------------------------------------------
    elif pilihan == '2':
        print("\n--- Cek Sifat Bilangan (Ganjil / Genap) ---")
        angka_str = input("Masukkan angka bulat: ")
        
        if angka_str.isdigit():
            angka = int(angka_str)
            sifat = operasi3.cek_ganjil_genap(angka)
            print(f"Angka {angka} adalah bilangan {sifat}.")
        else:
            print("Error: Masukkan angka bulat yang valid!")
            
    # ------------------------------------------
    # MENU 3: HITUNG DERET ARITMATIKA
    # ------------------------------------------
    elif pilihan == '3':
        print("\n--- Hitung Deret Aritmatika ---")
        awal_str = input("Masukkan suku awal: ")
        beda_str = input("Masukkan beda antar suku: ")
        n_str = input("Masukkan banyak suku (n): ")
        
        if awal_str.lstrip('-').isdigit() and beda_str.lstrip('-').isdigit() and n_str.isdigit():
            awal = int(awal_str)
            beda = int(beda_str)
            n = int(n_str)
            
            if n <= 0:
                print("Error: Banyak suku (n) harus lebih besar dari 0!")
            else:
                total = operasi3.hitung_deret_aritmatika(awal, beda, n)
                print(f"Total akumulasi deret aritmatika: {total}")
        else:
            print("Error: Masukkan nilai numerik yang valid!")
            
    # ------------------------------------------
    # MENU 4: CETAK TABEL PERKALIAN MATRIKS
    # ------------------------------------------
    elif pilihan == '4':
        print("\n--- Tabel Perkalian Matriks (1 - 3) ---")
        for i in range(1, 4):
            for j in range(1, 4):
                print(f"{i * j}\t", end="")
            print()  # Pindah baris baru setelah inner loop selesai
            
    else:
        print("Error: Pilihan menu tidak valid! Silakan masukkan angka 1-5.")