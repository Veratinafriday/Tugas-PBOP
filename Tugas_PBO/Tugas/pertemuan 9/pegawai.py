# class gaji:
#     def __init__(self, gaji_bulanan):
#         self.gaji_bulanan = gaji_bulanan
    
#     def total(self):
#         return(self.gaji_bulanan*12)

# class pegawai:
#     def __init__(self, gaji_bulanan, bonus):
#         self.gaji_bulanan = gaji_bulanan
#         self.bonus = bonus
#         self.obj_gaji = gaji(self.gaji_bulanan)
    
#     def hasil_tahunan(self):
#         return "Total" + str(self.obj_gaji.total() + self.bonus) + "Rupiah"

# obj_pegawai = pegawai(2600, 500)
# print(obj_pegawai.hasil_tahunan())

class gaji:
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan*12)

class Pegawai:
    jumlah = 0

    def __init__(self, nama, gaji_bulanan, bonus):
        self.nama          = nama
        self.gaji_bulanan  = gaji_bulanan
        self.bonus         = bonus
        self.obj_gaji      = gaji(self.gaji_bulanan)
        Pegawai.jumlah += 1

    def hasil_tahunan(self):
        return 'Total: ' + str(self.obj_gaji.total() + self.bonus)+ 'rupiah'

    def tampiljumlah(self):
        print('Total pegawai: ', Pegawai.jumlah)
    
    def tampilpegawai(self):
        print(f'''

Nama  : {self.nama}
gaji  : {self.gaji_bulanan}
bonus : {self.bonus}

''')

    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri !=None:
            total = anak + istri
            print('Tunjangan anak + istri = ', total)
        
        else:
            total = istri
            print('Tunjangan istri = ', total)

nama         = str(input('Masukkan nama         : '))
gaji_bulanan = int(input('Input gaji            : '))
bonus        = int(input('Input bonus           : '))
anak         = int(input('Input tunjangan anak  : '))
istri        = int(input('Input tunjangan istri : '))


peg1 = Pegawai(nama, gaji_bulanan, bonus)
peg2 = Pegawai(nama, gaji_bulanan, bonus)
peg1.tampilpegawai()
peg2.tampilpegawai()
peg1.tunjangan(anak, istri)
peg2.tunjangan(istri)

print("Total pegawai  =  %d" % Pegawai.jumlah)
rataGaji = (peg1.gaji_bulanan + peg2.gaji_bulanan)/Pegawai.jumlah
print("Rata-rata gaji = "+ str(rataGaji))


print(peg1.hasil_tahunan())
print(peg2.hasil_tahunan())