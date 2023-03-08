import random
def angka_genrate(bawah,atas):
    angka_komputer = random.randrange(bawah, atas)
    return angka_komputer

angka = angka_genrate(0,100)
print(angka)
tebakan = False
langkah = 6
hasil = False
while tebakan == False:
    if langkah == 0:
        break
    tebakan_user = int(input("masukkan tebakan : "))
    langkah = langkah - 1
    if tebakan_user == angka:
        tebakan = True
        hasil = True
        break
    else:
        if tebakan_user > angka:
            print("Tebakan Anda Terlalu Besar sisa",int(langkah))
        else:
            print("Tebakan Anda Terlalu Kecil",int(langkah))
    print("Tebakan anda masih salah coba lagi")

if hasil == True:
    print("Selamat anda menang sisa langkah", langkah)
else:
    print("Maaf Anda kalah karena kesempatan sudah habis")

    

