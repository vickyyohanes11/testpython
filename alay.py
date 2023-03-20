'''
def translate_alay(kalimat):
    nonalay = 'aAiIeEsSgGoOBb'
    alay = '44113355990086'
    hasil = ''
    for karakter in(kalimat):
        if karakter in nonalay:
            idx = nonalay.index(karakter)
            hasil = hasil + alay[idx]
        else:
            hasil = hasil + karakter
    return hasil

kalimat = input("masukkan kalimat : ")
print(translate_alay(kalimat))
'''
'''
nama = "Mawar Melati mekar di taman"
print(nama[-5:])
print(nama[22:])
'''

# def hitung_vokal(kalimat):
#     vokal = 'AaEeIiUuOo'
#     jumlah = 0
#     for karakter in kalimat:
#         if karakter in vokal:
#             jumlah += 1
#     return jumlah

# def hitung_konsonan(kalimat):
#     vokal = 'AaEeIiUuOo'
#     jumlah = 0
#     for karakter in kalimat:
#         if karakter not in vokal and karakter.isalpha():
#             jumlah += 1
#     return jumlah

# def hitung_digit(kalimat):
#     digit = '0123456789'
#     jumlah = 0
#     for karakter in kalimat:
#         if karakter in digit:
#             jumlah +=1
#     return jumlah

# def white_space(kalimat):
#     jumlah = 0
#     for karakter in kalimat:
#         if karakter.isspace():
#             jumlah +=1
#     return jumlah


# kalimat = input("Masukkan Kata : ")
# hasil = hitung_vokal(kalimat)
# hasail2 = hitung_konsonan(kalimat)
# hasail3 = hitung_digit(kalimat)
# hasail4 = white_space(kalimat)
# print(hasil)
# print(hasail2)
# print(hasail3)
# print(hasail4)

# def ubah_format(tanggal):
#     return tanggal[-2:] + '-' + tanggal[5:7] + '-' + tanggal[:4]

# tgl = input("Masukkan tgl : ")
# print(ubah_format(tgl))

def palindrom(kalimat):
    hasil = kalimat.lower()
    balik = hasil[::-1]
    if hasil == balik:
        print("Palindrom")
    else:
        print("Bukan palindrom")

kalimat = input("Masukkan Kalimat :")
palindrom(kalimat)