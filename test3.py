'''suhu = float(input('Masukkan suhu : '))

if suhu < 34:
    print('Mati kedinginan')
elif 34 <= suhu <= 37:
    print('aman')
elif 37 <= suhu <= 40:
    print('Demam')
else:
    print('Mati kepanasan')


'''
'''
bilangan = int(input("Masukkan bilangan :"))

if bilangan > 0 :
    print('Bilangan positif')
elif bilangan < 0 :
    print('Bilangan negatif')
else:
    print('Bilangan NOL')
'''
'''
cigars = int(input("Masukkan jumlah rokok : "))
is_weekend = input('Apakah weekend ? (y/n) : ')

is_weekend = False
if is_weekend == 'y' or is_weekend == 'Y':
    is_weekend = True

if is_weekend == True and cigars >= 40:
    print('sukses')
elif is_weekend == False  and 40 <= cigars <=60:
    print('sukses')
else:
    print('gagal')

'''
'''
nama1 = input('Masukkan nama 1 : ')
nama2 = input('Masukkan nama 2 : ')
nama3 = input('Masukkan nama 3 : ')

panjang1 = len(nama1)
panjang2 = len(nama2)
panjang3 = len(nama3)

if panjang2 < panjang1 > panjang3 :
    print(nama1)
elif panjang1 < panjang2 > panjang3 :
    print(nama2)
else :
    print(nama3)

'''
'''
bil1 = int(input('masukkan bilangan 1 :'))
bil2 = int(input('masukkan bilangan 2 :'))
bil3 = int(input('masukkan bilangan 3 :'))

if bil1 != 13 and bil2 != 13 and bil3 != 13:
    hasil = bil1 + bil2 + bil3
    print(hasil)
elif bil1 !=13 and bil2 != 13 and bil3 == 13:
    hasil = bil1 + bil2
    print(hasil)
elif bil1 != 13 and bil2 == 13 and bil3 != 13:
    print(bil1)
elif bil1 == 13 and bil2 != 13 and bil3 != 13:
    print("0")

'''

ubin1 = int(input('Masukkan jumlah ubin 1 meter : '))
ubin2 = int(input('Masukkan jumlah ubin 5 meter : '))
panjang = int(input('Masukkan panjang yang ingin ditutupi ubin :'))

if ( 1 * ubin1 + 5 * ubin2) >= panjang :
    
