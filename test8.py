'''print('hello world')
print('saya akan belajar progaming')
print('semoga hasilnya bagus')
'''

bawah=int(input("Masukkan = "))
atas=int(input("Masukkan = "))

if bawah>atas:
    for i in range(bawah,atas-1,-1):
        if i%2==1:
            if i == atas or i == atas+1:
                print(i)
            else:
                print(i, end=", ")
else:
    for i in range(bawah,atas+1):
        if i%2==1:
            if i == atas or i == atas-1:
                print(i)
            else:
                print(i, end=", ")
