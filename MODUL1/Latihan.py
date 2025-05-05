# Latihan List, Tuples, Dictionary

# Latihan List
data_mahasiswa = []
jumlah = int(input("Input jumlah mahasiswa: "))
# perulangan untuk memasukkan nama mahasisqa
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nama = input("Nama: ")
    nilai = list(map(int, input("Masukkan 3 nilai dipisahkan spasi: ").split()))
    rata2 = sum(nilai) / len(nilai)
    data_mahasiswa.append([nama, nilai, rata2])
# Tampilkan semua data
print("\nData Mahaiswa:")
print("Nama\tNilai\t\tRata-rata")
for siswa in data_mahasiswa:
    print(f"{siswa[0]}\t{siswa[1]}\t{siswa[2]:.2f}")
# Tampilkan siswa yang lulus
print("\nMahasiswa Lulus (>= 75):")
for siswa in data_mahasiswa:
    if siswa[2] >= 75:
        print(f"{siswa[0]} - {siswa[2]:.2f}")

# Latihan Tuple
matkul_list = []
jumlah = int(input("Input jumlah mata kuliah: "))
for i in range(jumlah):
    print(f"\nMata kuliah ke-{i+1}:")
    kode = input("Kode: ")
    nama = input("Nama: ")
    sks = int(input("SKS: "))
    matkul = (kode, nama, sks)
    matkul_list.append(matkul)
print("\nDaftar Mata Kuliah:")
for m in matkul_list:
    print(m)
total_sks = sum(m[2] for m in matkul_list)
print(f"\nTotal SKS: {total_sks}")

# Latihan Dictionary
data_mahasiswa = {
    "NIM001": {"nama": "Rina", "jurusan": "TI"},
    "NIM002": {"nama": "Budi", "jurusan": "SI"}
}
data_mahasiswa = {}
jumlah = int(input("Jumlah mahasiswa: "))
for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}:")
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")
    data_mahasiswa[nim] = {
        "nama": nama,
        "jurusan": jurusan
    }
print("\nCari data mahasiswa")
cari = input("Masukkan NIM: ")
if cari in data_mahasiswa:
    mhs = data_mahasiswa[cari]
    print(f"Nama: {mhs['nama']}, Jurusan: {mhs['jurusan']}")
else:
    print("Mahasiswa tidak ditemukan.")
print("\nDaftar Seluruh Mahasiswa:")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} → {info['nama']} ({info['jurusan']})")
