# Meminta input dari pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
resolusi = input("Masukkan Resolusi di Tahun ini: ")

# Membuka file "Me.txt" untuk ditulis
with open("Me.txt", "w") as file:
    # Menulis data ke dalam file
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi di Tahun ini: {resolusi}\n")

# Menampilkan pesan bahwa file telah berhasil dibuat
print("File Me.txt telah berhasil dibuat!")