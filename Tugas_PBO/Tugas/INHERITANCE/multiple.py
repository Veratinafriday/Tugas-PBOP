class processor() :
               def __init__(self, processor) -> None:
                              self.processor = processor

class RandomAccessMemory() :
               def __init__(self, detail_ram) -> None:
                              self.ram = detail_ram
class Storage():
               def __init__(self, hdd) -> None:
                              self.hdd = hdd
class Monitor():
               def __init__(self, mntr) -> None:
                              self.monitor = mntr

#child
class Computerpart(processor, Storage, RandomAccessMemory, Monitor) :
               def __init__(self, processor, ram, hdd, mntr) -> None:
                              processor.__init__(self, processor)
                              Storage.__init__(self, hdd)
                              RandomAccessMemory.__init__(self, ram)
                              Monitor.__init__(self, mntr)
this_pc = Computerpart("Intel® Core™ i9-11900H",  "DOMINATOR®  PLATINUM  RGB  32  GB  (2  x  16  GB")
("DDR4  DRAM  3200MHz  C16  Memory  Kit",  "HDD  Toshiba  1  TB",  "Monitor  24  inch  Samsung  S24F350FHE") 
print("\n",
f'''
Saya mempunyai PC/Komputer dengan spesifikasi sebagai berikut :

Processor                     : {this_pc.processor}
RandomAccessMemory            : {this_pc.ram}
Storage                       : {this_pc.hdd}
Monitor                       : {this_pc.mntr}
''')