print("program bangun datar")

print("1.balok")

panjang = int(input("masukkan nilai panjang: "))
lebar = int(input("masukkan nilai lebar: "))
tinggi = int(input("masukkan nilai  tinggi: "))


luas_balok = panjang * lebar * tinggi 

print("luas balok adalah: ", luas_balok)

print("2. \ntabung")

luas_alas_lingkaran = int(input("masukkan alas lingkaran: "))
tinggi = int(input("masukkan nilai tinggi: "))

volume_ling = luas_alas_lingkaran * tinggi

print("nilai volume tabung adalah:", volume_ling)

print("3.limas")

alas = int(input("masukkan nilai alas: "))
tinggi = int(input("masukkn nilai tinggi: "))
volume_1 = alas * tinggi 
print("volume limas adalah:", volume_1)

kursDOLAR = 14000
rupiah = float(input("masukkan uang rupiah: "))
rupToDol = rupiah/kursDOLAR
dolDecimal = round(rupToDol, 2)
print("RP.",rupiah, "==> US$", dolDecimal)



