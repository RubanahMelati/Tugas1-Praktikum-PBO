# Meminta input jumlah siswa
jumlah_siswa = int(input("Masukkan jumlah siswa: "))

# Inisialisasi dictionary untuk menyimpan data siswa
data_siswa = {}

# Loop untuk mengisi dictionary dengan data siswa
for i in range(1, jumlah_siswa + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    data_siswa[nama] = nilai

# Menampilkan dictionary yang telah diisi
print("Dictionary =", data_siswa)