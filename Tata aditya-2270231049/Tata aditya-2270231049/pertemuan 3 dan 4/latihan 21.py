# Halaman 56 Modul, Praktikum Algoritma Pemrograman
# Create by ASLAB ELITS 2022
# Contoh penggunaan Nested Loop
# Catatan: Penggunaan modul pada kondisi mengasumsikan nilai selain nolsebagai False (salah)
i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not (i%j): break
        j = j + 1
    if (j > i/j) : print(i, "is prime")
    i = i + 1