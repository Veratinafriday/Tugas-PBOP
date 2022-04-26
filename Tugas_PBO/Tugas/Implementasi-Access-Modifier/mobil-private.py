#seluruh variabel bersifat private
class Mobil():
    def __init__(self,jendela,pintu,mesin) :
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin


    def tampil(self):
        print('merk jendela :',self.jendela)
        print('merk jendela :',self.pintu)
        print('merk jendela :',self.mesin)

Mobil1 = Mobil('Solar Gard', 'Sliding doors (pintu gunting)',' external combustion engine (ICE)')
Mobil1.tampil()