n = int(input("Masukkan jumlah deret Fibonacci: "))

a, b = 0, 1 # a akan menyimpan angka sekarang , b akan menyimpan angka berikutnya

angka_range = range(n)
for i in angka_range:
    print(f"Fibonacci ke-{i} -> {a}")
    a, b = b, a + b # ini adalah rumus dari fibonacci
