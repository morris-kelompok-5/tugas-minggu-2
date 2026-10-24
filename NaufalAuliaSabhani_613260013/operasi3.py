
# ======================================================================
# MODUL OPERASI: DEFINISI FUNGSI DENGAN NILAI KEMBALIAN (RETURN)
# ======================================================================

def tambah(a, b):
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b


def kurang(a, b):
    """Mengembalikan hasil pengurangan a - b."""
    return a - b


def kali(a, b):
    """Mengembalikan hasil perkalian a * b."""
    return a * b


def bagi(a, b):
    """Mengembalikan hasil pembagian a / b."""
    if b == 0:
        return "Error: Pembagian oleh nol tidak diperbolehkan"

    return a / b


def cek_ganjil_genap(angka):
    """Mengembalikan teks GANJIL atau GENAP."""
    if angka % 2 == 0:
        return "GENAP"
    else:
        return "GANJIL"


def hitung_deret_aritmatika(awal, beda, n):
    """Menghitung dan mengembalikan total deret aritmatika."""
    total = 0
    suku = awal

    for i in range(n):
        total += suku
        suku += beda

    return total