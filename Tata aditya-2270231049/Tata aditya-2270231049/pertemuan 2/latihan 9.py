# operasi komparasi

#setiap hasil dari operasi komparasi adalah boolean
#>,<,>=,<=,==,!=,is,is not

a = 4
b = 2

#lebih besar dari (>)
print ('========= lebih besar dari (>)')

hasil = a> 3
print (a,'>',3,'=',hasil)
hasil = b>3
print (b,'>',3,'=',hasil)
hasil = b>2
print (b,'>',2,'=',hasil)

#kurang dari (<)
print ('========= lebih besar dari (<)')

hasil = a< 3
print (a,'<',3,'=',hasil)
hasil = b<3
print (b,'<',3,'=',hasil)
hasil = b<2
print (b,'<',2,'=',hasil)

#lebih dari sama dengan (>=)
print ('========= lebih besar dari (=)')

hasil = a>= 3
print (a,'>=',3,'=',hasil)
hasil = b>3
print (b,'>=',3,'=',hasil)
hasil = b>2
print (b,'>=',2,'=',hasil)

#kurang dari sama dengan (<=)
print ('========= lebih besar dari (<=)')

hasil = a<= 3
print (a,'<=',3,'=',hasil)
hasil = b<=3
print (b,'<=',3,'=',hasil)
hasil = b<=2
print (b,'<=',2,'=',hasil)

#sama dengan (==)
print ('========= lebih besar dari (==)')

hasil = a== 3
print (a,'==',3,'=',hasil)
hasil = b==3
print (b,'==',3,'=',hasil)
hasil = b==2
print (b,'==',2,'=',hasil)

#tidak sama dengan (!=)
print ('========= lebih besar dari (!=)')

hasil = a!= 3
print (a,'!=',3,'=',hasil)
hasil = b==3
print (b,'!=',3,'=',hasil)
hasil = b==2
print (b,'!=',2,'=',hasil)


#'is' sebagai komparasi object identify
print ('========= object identify(is)')

x= 5 # object assignment membuat object
y= 5

print ('nilai x =',x,',id=',hex(id(x)))
print ('nilai y =',y,',id=',hex(id(y)))

hasil = x is y
print('x is y =', hasil)


print('========== object identify(is not)')
x = 5 # ini adalah assingment membuat object
y = 5

print ('nilai x =',x,',id=',hex(id(x)))
print ('nilai y =',y,',id=',hex(id(y)))

hasil = x is not y
print('x is y =', hasil)

print('========== object identify(is not)')
x = 5 # ini adalah assingment membuat object
y = 6

print ('nilai x =',x,',id=',hex(id(x)))
print ('nilai y =',y,',id=',hex(id(y)))

hasil = x is not y
print('x is y =', hasil)

