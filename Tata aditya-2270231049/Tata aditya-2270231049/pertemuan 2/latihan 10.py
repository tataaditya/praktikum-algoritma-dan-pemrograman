# operasi logika atau boolean

#not,or,and,xor

#not

print('====NOT====')

a = False
c = not a

print('data a =',a)
print('--------NOT')
print('data c=',c)

#OR (jika salah satu true, maka hasilnya adalah true)
print('====OR====')
a = False
b = False
c = a or b 
print (a,'or',b,'=',c)
a = False
b = True
c = a or b
print (a,'or',b,'=',c)
a = True
b = False
c = a or b
print (a,'or',b,'=',c)
a = True
b = True
c = a or b
print (a,'or',b,'=',c)

#AND ( jika dua buah nilai true, maka hasil true)
a = False
b = False
c = a and b 
print (a,'and',b,'=',c)
a = False
b = True
c = a and b
print (a,'and',b,'=',c)
a = True
b = False
c = a and b
print (a,'and',b,'=',c)
a = True
b = True
c = a and b
print (a,'and',b,'=',c)

#xor ( akan true jika salah satu true, sisanya false)
a = False
b = False
c = a ^ b 
print (a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print (a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print (a,'xor',b,'=',c)