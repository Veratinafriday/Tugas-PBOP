class utama:
    def __init__(self):
        self._a = 2

class Turunan(utama):
    def __init__(self):
        #memanggil konstruktor pada kelas utama
        utama.__init__(self)
        print("memanggil variabel proceted pada class utama: ",self._a)

        #modify the protected variable:
        self.__a = 3
        print("memanggil variabel procted yang dimodifikasi diluar class: ",self._a)


objek1 = Turunan()
objek2 = utama()

#memanggil variabel protected
print("mengakses variabel protected dari objek1: ", objek1._a)
print("mengakses variabel protected dari objek2: ", objek2._a)