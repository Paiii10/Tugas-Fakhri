print("Nomor 1")
print("----------------------------------------------------------------")
kendaraan = ["vario", "motor", 150, "pink", 2]
kendaraan.append(19000000)
kendaraan.append("matic")
kendaraan.insert(2, "Honda")
print(kendaraan)

print("----------------------------------------------------------------")
print("Nomor 2")
print("----------------------------------------------------------------")

print("=== Alat hitung luas bangun datar ===")
print("Pilih 1 untuk menghitung luas persegi")
print("Pilih 2 untuk menghitung luas lingkaran")
print("Pilih 3 untuk menghitung luas segitiga")

pilihan = int(input("Masukkan pilihan (1/2/3): "))

match pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s * s
        print(f"luas persegi adalah: {luas}")

    case 2:
        r = int(input("Masukkan Jari-jari lingkaran: "))
        pi = 3.14
        luas = pi * r**2
        print(f"luas lingkaran adalah: {luas}")

    case 3:
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luas = alas * tinggi / 2
        print(f"luas segitiga adalah: {luas}")

    case _:
        print("salah pilih")