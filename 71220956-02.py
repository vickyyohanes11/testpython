inch = int(input("Masukkan inputan inch : "))

mile = inch / 63360
yard = inch % 63360 / 36
feet = inch % 63360 % 36 / 12
inch2 = inch % 63360 % 36 % 12

print(inch,"inch = ",int(mile),"mile",int(yard),"yard",int(feet),"feet",int(inch2),"inch")
