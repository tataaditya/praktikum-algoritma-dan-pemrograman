#format string

#contoh generic
#string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

#boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

#angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

#bulat
angka = 15
format_str = f"bilangan bulat= {angka:d}"
print(format_str)

#bilangan dengan ordo ribuan
angka = 20000000
format_str = f"jutaan = {angka:,}"
print(format_str)

#desimal
angka = 2005.54321
format_str = f"desimal = {angka:3f}"
print(format_str)

#menampillkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

#desimal
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus= {angka_plus:.2f}"

print(format_minus)
print(format_plus)

#menformat persen
persen = 0.045
format_persen =f"persen = {persen:.2%}"
print(format_persen)

#melakukan operqasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5 
format_string = f"harga_total = Rp. {harga*jumlah:,}"
print(format_string)

#format angka lain (binary,octal,hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexa = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)


