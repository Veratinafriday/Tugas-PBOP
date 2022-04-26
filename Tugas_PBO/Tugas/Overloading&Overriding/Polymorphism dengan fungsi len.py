# Polymorphism
# Simple example using len function


print(len("polymorphism"))
print(len([0,1,2,3]))

# '''

# Menggunakan fungsi len
# Output:
# 12 (Tipe Data String)
# 4 (Tipe Data List)
# '''

# Using class
class jerman:
    def ibukota(self):
        print('Berlin adalah ibukota negara Jerman')

class jepang:
    def ibukota(self):
        print('Tokyo adalah ibukota jepang')

negara_1 = jerman()
negara_2 = jepang()

for country in (negara_1, negara_2):
    country.ibukota()