detik = int(input(" Masukkan detik : "))

hari = detik / 86400
jam =  detik % 86400 / 3600
menit = detik % 86400 % 3600 /60
detik2  = detik % 86400 % 3600 % 60
print(detik,"detik, = ",int(hari),"hari,",int(jam),"jam,",int(menit),"menit,",int(detik2),"detik")
