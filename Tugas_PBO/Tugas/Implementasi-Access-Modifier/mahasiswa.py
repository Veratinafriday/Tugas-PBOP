class Mahasiswa:
    __alamat =''
    def __init__(self,nama,nim,prodi,tahun_masuk,alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.tahun_masuk = tahun_masuk
        self.__alamat = alamat
    
    def tampil(self):
        print('Nim :',self.nim)
        print('Nama :',self.nama)
        print('Alamat :',self.__alamat)
        print('Prodi :',self.prodi)
        print('Tahun Masuk :',self.tahun_masuk)
        print('-'*25)

m1 = Mahasiswa('Dinda', '10120531', 'Teknik Elektro', 2021,'Bengkulu')
m2 = Mahasiswa('Agnes', '5210411167', 'Informatika', 2021,'Gunung Kidul')
m3 = Mahasiswa('Bella', '5210411175', 'Informatika', 2021,'Cilacap')
Mahasiswa = [m1,m2,m3]
print('-'*5,' DAFTAR MAHASISWA','-'*5)
for i in Mahasiswa:
    i.tampil()
