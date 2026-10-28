def tambah(a, b):
    """mengembalikan hasil penjumlahan a + b"""
    return a + b

def kurang(a, b):
    """mengembalikan hasil pengurangan a - b"""
    return a - b    

def kali(a, b):
    """mengembalikan hasil perkalian a * b"""
    return a * b

def bagi(a, b):
    """ mengembalikan hasil pembagian a / b.   menangani pencegahan error pembagi bernilai nol."""
    
    if b == 0:
        return "Error: Pembagi tidak boleh nol"
    return a / b

def cek_ganjil_genap(angka):
    """memeriksa sifat bilangan ganjil atau genap   menggunakan operator modulus (%)    """

    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitun_deret_aritmatika(awal, beda, deret, n):
    """menghitung total akumulasi deret menggunakan perulangan for  """
    
    total = 0
    suku = awal
    for i in range(n):
        deret.append(suku)
        total += suku
        suku += beda

    return total 
    
