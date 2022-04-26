class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa('Dinda', '10120531', 'Teknik Elektro', 2021)
m2 = Mahasiswa('Agnes', '5210411167', 'Informatika', 2021)
m3 = Mahasiswa('Bella', '5210411175', 'Informatika', 2021)

data = [m1, m2, m3]

for i in data:
    print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim}')