x1 = int(input("Masukkan x1 = "))
y1 = int(input("Masukkan y1 = "))
x2 = int(input("Masukkan x2 = "))
y2 = int(input("Masukkan y2 = "))

rumus  = ( x2 - x1)**2 + (y2 - y1)**2
hasil  = rumus ** 0.5
hasil = int(hasil*10)/10
print("Jarak antara titik  adalah",hasil)
