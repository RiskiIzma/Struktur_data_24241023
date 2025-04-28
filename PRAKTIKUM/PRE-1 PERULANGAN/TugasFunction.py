# variabel gloal untuk menyimpan data mahasiswa
mahasiswa_list = []

def create():
    """Menampilkan nama mahasiswa ke dalam list"""
    nama = input("Menambahkan nama mahasiswa: ")
    mahasiswa_list.append(nama)
    print(f"nama '{nama}' telah ditambahkan")

def read():
    """Menampilkan data mahasiswa"""
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa")
    else:
        print("Daftar Mahasiswa")
        for index , nama in enumerate(mahasiswa_list):
            print(f"{index + 1}. {nama}")

def update():
    """Mengubah nama mahasiswa berdasarkan indeks"""
    read()
    try:
        indeks = int(input("Masukan nomor mahasiswa yang ingin diubah: ")) -1
        if 0 <= indeks < len(mahasiswa_list):
            nama_baru = input("Masukan nama baru")
            mahasiswa_list[indeks] = nama_baru
            print("Nama mahasiswa berhasil diubah.")
        else:
            print("indeks tidak valid")
    except ValueError:
        print("input harus angka")


def delete():
    """Menghapus nama mahasiswa berdasarkan indeks."""
    read()
    try:
        indeks = int(input("Masukkan nomor mahasiswa yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(mahasiswa_list):
            nama_dihapus = mahasiswa_list.pop(indeks)
            print(f"Nama '{nama_dihapus}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus angka.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih aksi (1-5): ")
        
        if pilihan == '1':
            create()
        elif pilihan == '2':
            read()
        elif pilihan == '3':
            update()
        elif pilihan == '4':
            delete()
        elif pilihan == '5':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
