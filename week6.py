'''
def pagar_vertikal(n) : 
    for i in range(n):
        print("#")

def pagar_horizontal(n) : 
    for i in range(n):
        print("#", end = " ")


n  = int(input("Masukkan N : "))

pagar_vertikal(n)
pagar_horizontal(n)
'''
'''
def persegi(n):
    for i in range(n):
        #ini diibaratkan di eksekusi terlebih dahulu untuk melakukan perulangan baru diulang diatasnya
        for j in range(n):
          print("*", end = "")
        print()
'''
'''
def segitigakiri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
          print("#")
        print()
'''
'''
def segitigakanan(n):
    for i in range(1,n+1):
        spasi = n - i
        pagar = i
        for j in range(spasi):
          print(" ", end = "")
        for k in range(pagar):
            print("#", end = "" )
        print()
'''

# def kotak(n):
#     for baris in range(n):
#         print("#", end = "")
#     print()
#     for baris in range(n-2):
#         spasi = n - 2
#         print("#", end = "")
#         for kolom in range(spasi):
#             print(' ', end = "")
#         print("#")
#     for baris in range(n):
#         print("#", end = "")
#     print()


# def tandax(n):
#     for baris in range(n):
#         for kolom in range(n):
#             if baris == kolom:
#                 print("#", end="")
#             elif baris+kolom == n - 1:
#                 print("#", end="")
#             else:
#                 print(" ", end = "")
#         print()


# def tandaplus(n):
#     for baris in range(n):
#         for kolom in range(n):
#             if baris == n//2 :
#                 print("#", end = "")
#             elif kolom == n//2:
#                 print("#", end = "")
#             else:
#                 print(" ", end = "")
#         print()


def karpet(n):
    for baris in range(1,(n//2)+1):
        for kolom in range(1,n+1):
            pagar = 2 * baris - 1
            spasi = (n - pagar)//2
            for i in range(spasi):
                print(" ", end= "")
            for i in range(pagar):
                print("#", end= "")
            print()
        
 

n  = int(input("Masukkan N : "))
karpet(n)