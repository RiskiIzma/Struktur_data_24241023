# PERULANGAN (LOOP)

#for-loop
#for kondisi
#    aksi

a = 0
a += 1 # a = a + 1
print(a)
a += 1
print(a)
a += 1
print(a)

# PERULANGAN DENGAN LIST
angka_list = [0,1,2,4,8,10]
for i in angka_list:
    print(f"i sekarang -> {i}")
print("ini akhir for 1\n")

# PERULANGAN DENGAN RANGE
angka_range = range(5) # diulang 5 kali

for i in angka_range:
    print(f"i sekarang -> {i}")
print("ini akhir for 2\n")

angka_range= range(1,10) # diulang 9/10
for i in angka_range:
    print(f"i sekarang -> {i}")
print("ini akhir for 3\n")

# TUGAS RANGE PAKE NAMA SENDIRI
nama = "RISKI"
for i in range(len(nama)):
    print(nama[i])