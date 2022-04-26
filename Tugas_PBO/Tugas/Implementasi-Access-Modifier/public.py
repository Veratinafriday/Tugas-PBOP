class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi
Segitiga_besar = Segitiga(100,80)

#akses variabel public: alas, tinggi, dan luas dari luas kelas segitiga
print("alas: ",Segitiga_besar.alas)
print("tinggi: ",Segitiga_besar.tinggi)
print("luas: ",Segitiga_besar.luas)