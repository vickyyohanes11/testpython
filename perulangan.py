'''
for i in range (1,11):
    print(i)
'''
'''
for i in range (1500,20001,50):
    print(i)
'''
'''
for i in range(3,100,3):
    print(i)
'''
'''
for i in range(15,0,-1):
    print(i)
'''
'''
for i in range(15,0,-1):
    if i % 2 == 0:
        print(i,"genap")
    else:
        print(i,"ganjil")
'''
'''
for i in range(1,16):
    if i % 2 == 0:
        print(i,"genap")
    else:
        print(i,"ganjil")
'''
'''
def prima(number):
    pembagi = 0
    for i in range(1,number+1):
        if number % i == 0:
            pembagi = pembagi + 1
    if pembagi == 2 :
        return True
    else:
        return False
    
number = int(input("Masukkan bilangan : "))
batas = int(input("Masukkan bawah : "))

for i in range(number,batas+1):
    hasil = prima(i)
    if hasil:
        print(i)
'''
'''
bilangan = 0
genap = False
while genap == False:
    bilangan = int(input('Masukkan bilangan genap: '))
    if bilangan % 2 == 0:
        genap = True
        print(bilangan, 'yang anda masukkan adalah bilangan genap')
'''
def cetak(a,b):
    if a >= b:
        for i in range(b, a+1):
            print(i)
    else:
        for i in range(a,b+1):
            print(i)
       
    

cetak(5,9)
cetak(18,14)
cetak(8,8)
