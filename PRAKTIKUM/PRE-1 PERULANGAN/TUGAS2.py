jumlah = int(input("Masukkan jumlah bilangan genap yang ingin ditampilkan: "))  # Minta input dari user

angka_range = range(1, jumlah + 1)  # Misalnya: jika jumlah = 5, maka range(1, 6)

print("Bilangan genap yang ditampilkan:", end=' ')
for i in angka_range:
    print(i * 2, end=',')  # Cetak ke samping, dipisahkan oleh koma
