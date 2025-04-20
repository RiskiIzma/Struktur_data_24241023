n = int(input("Masukkan jumlah deret Fibonacci: "))

a, b = 0, 1 # a akan menyimpan angka sekarang , b akan menyimpan angka berikutnya

print("Deret Fibonacci:", end=',')
for i in range(n):
    print(a, end=',')  # Cetak angka Fibonacci ke samping
    a, b = b, a + b     # ini adalah rumus dari fibonacci
