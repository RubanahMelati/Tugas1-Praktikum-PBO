# Meminta input dari pengguna untuk tinggi segitiga
height = int(input("Height: "))

# Loop untuk mencetak segitiga
for i in range(1, height + 1):
    # Mencetak spasi untuk membuat segitiga rata kanan
    for j in range(height - i):
        print(" ", end="")
    # Mencetak bintang sesuai dengan baris saat ini
    for k in range(2 * i - 1):
        print("*", end="")
    # Pindah ke baris berikutnya
    print()