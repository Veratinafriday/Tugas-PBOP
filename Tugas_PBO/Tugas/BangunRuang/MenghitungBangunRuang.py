def menu(): 
    print("Pilih Bangun Ruang")
    print("Masukkan Angka 1-5")
    print("1. Segitiga")
    print("2. Lingkaran")
    print("3. Trapesium")
    print("4. Jajargenjang")
    print("5. Bola")

def Segitiga():
    tinggi = int(input("Masukkan tinggi: "))
    alas = int(input("Masukkan alas: "))
    luas = (alas*tinggi)*1/5
    print("Luas segitiga= ", luas)
def Lingkaran():
    jari = int(input("Masukkan jari-jari: "))
    luas = (jari*jari)*3.14
    print("Luas lingkaran= ", luas)
def Trapesium():
    tinggi = int(input("Masukkan tinggi: "))
    sisiSejajar = int(input("Masukkan sisi sejajar: "))
    luas = (tinggi*sisiSejajar)/2
    print("Luas Trapesium= ", luas)
def JajarGenjang():
    tinggi = int(input("Masukkan tinggi: "))
    alas = int(input("Masukkan alas: "))
    luas = (alas*tinggi)
    print("Luas jajargenjang= ", luas)
def Bola():
    jari = int(input("Masukkan jari-jari: "))
    luas = (4*3.14)*jari
    print("Luas Bola= ", luas)



print("###########################################################")
menu()
pilih = int(input("masukkan pilihan: "))
if pilih == 1:
    Segitiga()
elif pilih == 2:
    Lingkaran()
elif pilih == 3:
    Trapesium()
elif pilih == 4:
    JajarGenjang()
elif pilih == 5:
    Bola()

else:
    print("inputan salah!")