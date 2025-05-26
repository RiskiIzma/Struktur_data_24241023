def main():
    # Dictionary untuk menyimpan data mahasiswa
    data_mahasiswa = {}

    # Meminta jumlah mahasiswa
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

    # Input data untuk setiap mahasiswa
    for _ in range(jumlah_mahasiswa):
        nim = input("\nMasukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))

        # List untuk menyimpan (mata kuliah, nilai)
        nilai_mk = []
        for _ in range(jumlah_mk):
            mata_kuliah = input("  Masukkan nama mata kuliah: ")
            nilai = float(input("  Masukkan nilai: "))
            nilai_mk.append((mata_kuliah, nilai))

        # Simpan data ke dictionary
        data_mahasiswa[nim] = {
            "nama": nama,
            "Mata_kuliah": mata_kuliah
        }

    # Daftar seluruh mahasiswa
    print("\n===== DAFTAR SELURUH MAHASISWA =====")
    for nim, data in data_mahasiswa.items():
        print(f"NIM: {nim} - Nama: {data['nama']}")

    # Rekap nilai
    print("\n===== REKAP NILAI MAHASISWA =====")
    for nim, data in data_mahasiswa.items():
        nama = data["nama"]
        nilai_mk = data["nilai_mk"]
        total_nilai = sum(nilai for _, nilai in nilai_mk)
        rata_rata = total_nilai / len(nilai_mk) if nilai_mk else 0

        print(f"\nNIM        : {nim}")
        print(f"Nama       : {nama}")
        print("Nilai MK   :")
        for mk, nilai in nilai_mk:
            print(f"  - {mk}: {nilai}")
        print(f"Rata-rata  : {rata_rata:.2f}")

if __name__ == "__main__":
    main()
