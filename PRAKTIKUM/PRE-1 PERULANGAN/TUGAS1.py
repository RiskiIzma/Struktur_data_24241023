jumlah_baris = int(input("masukan jumlah baris: "))
angka_range = range(1, jumlah_baris * 2, 2) # range(mulai, berhenti , step) contoh misalnya jumlah_baris = 5 * 2 = 10 - 1 = 9

spasi_awal = jumlah_baris - 1 # misalnya jumlah_baris = 5 maka spasi_awal = 5 - 1 = 4

for i in angka_range:
    print(' ' * spasi_awal + '*' * i)
    spasi_awal -= 1 # jadi spasi awal - 1  = 3,bagaimana bisa kek gitu karena spasi awal sudah ada yaitu 4 