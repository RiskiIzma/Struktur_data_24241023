# variabel gloal untuk menyimpan data siswa
siswa_list = []

def create():
    """Menampilkan nama siswa ke dalam list"""
    nama = input("Menambahkan nama siswa: ")
    siswa_list.append(nama)
    print(f"nama '{nama}' telah ditambahkan")

def read():
    """Menampilkan data siswa"""
    if not siswa_list:
        print("Tidak ada data siswa")
    else:
        print("Daftar siswa")
        for index , nama in enumerate(siswa_list):
            print(f"{index + 1}. {nama}")

def update():
    """Mengubah nama siswa berdasarkan indeks"""
    read()
    try:
        indeks = int(input("Masukan nomor siswa yang ingin diubah: ")) -1
        if 0 <= indeks < len(siswa_list):
            nama_baru = input("Masukan nama baru")
            siswa_list[indeks] = nama_baru
            print("Nama siswa berhasil diubah.")
        else:
            print("indeks tidak valid")
    except ValueError:
        print("input harus angka")


def delete():
    """Menghapus nama siswa berdasarkan indeks."""
    read()
    try:
        indeks = int(input("Masukkan nomor siswa yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(siswa_list):
            nama_dihapus = siswa_list.pop(indeks)
            print(f"Nama '{nama_dihapus}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input harus angka.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Siswa")
        print("2. Tampilkan Siswa")
        print("3. Ubah Siswa")
        print("4. Hapus Siswa")
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
