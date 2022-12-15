# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# +++++++3-------10+++++++

inputuser = float(input("masukan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n"))

# ++++++++3-----------
#memeriksa angka kurang dari 3
iskurangdari = (inputuser < 3)
print("kurang dari 3=",iskurangdari)

# -------10+++++++
#memeriksa angka lebih dari 10
islebihdari = (inputuser > 10)
print("lebih dari 10=",islebihdari)

# +++++++3-------10+++++++

iscorrect = iskurangdari or islebihdari
print("angka yang anda masukan :", iscorrect)

# +++++++3-------10+++++++
#kasus irisan
print("\n,10*","\n")
inputuser = float(input("masukan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n"))

# ++++++++3-----------
# lebih dari 3
islebihdari = inputuser <10
print("lebihdari 10 =",islebihdari)

#-------10+++++++
# lebih dari 3
iskurangdari = inputuser <10
print("kurangdari 10 =",iskurangdari)

# +++++++3-------10+++++++
iscorrect = iskurangdari and islebihdari
print("angka yang anda masukan :", iscorrect)