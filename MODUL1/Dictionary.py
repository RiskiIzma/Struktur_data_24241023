# Dictionary
# contoh jika 1 item
aku = {
    "nama": "Adam Bachtiar Maulachela",
    "url": "https://www.fsttundikma.id"
}
nama_dict = {
    "key": "value"
}

# contoh jika lebih dari 1 item
nama_dict = {
    "key1": "value",
    "key2": "value",
    "key3": "value"
}
# membuat dictionary
data = {
    "nama"      : "Riski Izma Perdani",
    "NIM"      : 24241023,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@Riski Izma",
        "twiter"    : '_',
        "instagram" : 'RiskiIzma'
    }
}

# Fungsi atau Method Dictionary
# Mengakses Nilai Dictionary
# mengakses dict menggunakan key
print("Nama Saya adalah %s" % data['nama'])
print("Akun Github saya %s" % data['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIM Saya adalah %s" % data.get('NIM'))

# Mengubah Nilai Item Dictionary
nama_dict['kunci'] = 'Nilai_baru'
# Mengubah nilai item dictionary dict dengan key
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai item dictionary dengan .update
data.update({"sosmed" : {"Instagram" : "riskiizma"}})

# cek hasil perubahan
print(data['sosmed']['Instagram'])

# Menghapus Nilai Item Dictionary
# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)
data.clear()

# Menambahkan item pada dictionary
# membuat dictionary
mahasiswa = {
    "name" : "Riski Izma Perdani"
}

# menambahkan nim
mahasiswa.update({
    "nim" : "24241023"
})

# melihat hasilnya
print(mahasiswa)

# Looping Dictionary
# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

