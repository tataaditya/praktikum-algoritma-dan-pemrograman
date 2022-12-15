import sys
total = []

print("--------------------------")
print ("   _______")
print("   /      //")
print("  /      //")
print(" /______//")
print("/______(/")
print("--------------------------")
print("KASIR dallergut")
print("Dallergut: Toko Penjual Mimpi")
print("dimana kami menjual berbagai mimpi dan penyesalan")
print("=================================================")
pembeli = input("Masukan nama Pembeli: ")
alamat = input("Masukan alamat anda :")
nomor_telepon = input("masukan no telp anda :")

import time
tanggal = time.strftime("%d-%m-%y %H:%M:%S")
print(tanggal)
print(type(tanggal))


def daftar_barang():
    print(" No  Nama buku  Harga")
    print("-------------------------------")
    print(" 1  Mimpi indah......12000")
    print(" 2  Mimpi masa depan........15000")
    print(" 3  Memperbaiki buku penyesalan.....10000")
    print("-------------------------------")
    kode = int(input("Masukkan angka barang  : "))
    if kode == 1:
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 12000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 15000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 10000 * jumlah3 
        total.append(total3)
        tanya()
    return

def tanya():
    print("\n-------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------")
    if tanya == "y":
        daftar_barang()
    elif tanya == "t":
        akhir()
    else:
        print("Pilihan yang anda masukan salah!")

def akhir():
   for harga in total:
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)
        print("-------------------------------")
        bayar = int(input("Bayar            :  "))
        kembalian = bayar - totalakhir
        print("Kembalian        : ", kembalian)
        print("-------------------------------")
        print("          Terima Kasih         ")
        print("-------------------------------")

daftar_barang()