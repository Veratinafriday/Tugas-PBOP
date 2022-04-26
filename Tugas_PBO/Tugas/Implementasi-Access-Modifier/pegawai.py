class pegawai(): #ini adalah class pegawai
    __nama ='' #atribut nama
    __alamat ='' #atribut alamat
    __gaji = '' #atribut gaji
    def __init__(self,nama,alamat):
        self.__nama = nama
        self.__alamat = alamat

    def hitungGaji(self): #method hitungGaji
        upahLembur = 20000 #atribut upahLembur
        gajiPokok = 2000000 #atribut 2 gajiPokok
        jmlLembur = int(input('Total jam lembur : ')) #atribut jam Lembur
        self.__gaji = (upahLembur*jmlLembur)+gajiPokok
    
    def tampilDetail(self): #pembuatan method tampilDetail
        print('--- Menghitung dan menampilkan detail gaji pegawai ---')
        print('nama',self.__nama) #menampilkan atribut nama
        print('alamat',self.__alamat) #menampilkan atribut alamat
        self.hitungGaji()
        print('Total Gaji',self.__gaji) #menampilkan atribut gaji

pgw = pegawai('mikasa ackerman','wall rose')  #objek pertama
pgw.tampilDetail() #pemanggilan method tampildetail
pgw2 = pegawai('saya kisaragi','profektur negano') #objek kedua
pgw2.tampilDetail() #pemanggilan method tampilDetail 