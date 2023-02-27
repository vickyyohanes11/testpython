'''
def tambah(a,b):
    hasil = a + b
    return hasil

c = tambah(10,5)
print(c)
'''
'''
def print_twice(message):
    print(message)
    print(message)

print_twice("Hello world")
'''
'''
def seleksi_kkn(sks):
    if sks >= 110:
        return True
    else:
        return False

jumlah_sks = int(input("Masukkan jumlah sks :"))

hasil = seleksi_kkn(jumlah_sks)

if hasil == True:
    print("Boleh")
else:
    print("Tidak Boleh")
'''
'''
def tukar(a,b):
    c = a
    a = b
    b = c
    return a,b

a = int(input("Masukkan Bilangan A : "))
b = int(input("Masukkan Bilangan B : "))
print(a)
print(b)
a,b = tukar(a,b)
print(a)
print(b)
'''
''''
def cek_pythagoras (a,b,c):
    hasila = a**2
    hasilb = b**2
    hasilc = c**2
    if hasila + hasilb == hasilc:
        print("Tripel Pythagoras")
        return True
    elif hasila + hasilc == hasilb:
        print("Triple Pyhagoras")
        return True
    elif hasilb + hasilc == hasila:
        print("Triple Pythagoras")
        return True
    else:
        print("Bukan Pythagoras")
        return False

a = int(input("Bilangan 1 : "))
b = int(input("Bilangan 2 : "))
c = int(input("Bilangan 3 : "))

print(cek_pythagoras(a,b,c))
'''

def n_hari_berikutnya(nama_hari,n):
    n = n % 7
    '''
    senin = 0
    selasa = 1
    rabu = 2
    kamis = 3
    jumat = 4
    sabtu = 5
    minggu = 6
    ''' 
    if nama_hari == "senin":
        bobot = 0
    elif nama_hari == "selasa":
        bobot = 1
    elif nama_hari == "rabu":
        bobot = 2
    elif nama_hari == "kamis":
        bobot = 3
    elif nama_hari == "jumat":
        bobot = 4
    elif nama_hari == "sabtu":
        bobot = 5
    elif nama_hari == "minggu":
        bobot = 6
    
    total = (bobot + n) % 7

    if total == 0:
        print("senin")
    elif total == 1:
        print("selasa")
    elif total == 2:
        print("rabu")
    elif total == 3:
        print("kamis")
    elif total == 4:
        print("jumat")
    elif total == 5:
        print("sabtu")
    elif total == 6:
        print("minggu")
    


hari = input("Masukkan nama hari : ")
n = int(input("Berapa hari kemudian "))
print(n_hari_berikutnya(hari,n))







