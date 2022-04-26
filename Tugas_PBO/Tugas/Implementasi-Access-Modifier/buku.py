class Buku:
    __kodeBuku = 0
    def _init_(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def kodeBuku(self):
        kodeBuku = int(input('Masukkan kode Buku :'))
        self.__kodeBuku = kodeBuku
    
    def tampil(self):
        print('judul buku :',self.judul)
        self.kodeBuku()
        print('pengarang buku :',self.pengarang)
        print('tahun terbit :',self.tahun_terbit)        
        print('kode buku :',self.__kodeBuku)

buku1 = Buku('5CM','Donny Dhirgantoro',2005)
buku2 = Buku('Laskar Pelangi','Andrea Hirata',2005)
buku3 = Buku('Ayat-Ayat Cinta','Habiburrahman El Shirazy',2004)
buku = [buku1, buku2, buku3]
for i in buku:
    i.tampil()
    print('----------------------')