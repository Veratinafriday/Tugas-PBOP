class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku = Buku('Laskar Pelangi', 'Andrea Hirata', 2005)
print(f'Buku {buku.judul} karangan {buku.pengarang} pertama kali diterbitkan tahun {buku.tahun_terbit}')