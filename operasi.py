# Operasi string di python

# menambahkan karakter
print("---Tambah karakter---")
x = input("Tulis apa aja : ") 
y = input("Tulis apa aja : ")
z = input("Tulis apa aja : ")
data_gabungan = x + " " + y + " " + z
print(data_gabungan, "\n")

# menghitung panjang string
print("---menghitung panjang string---")
print(x, "= dengan jumlah karakter : ", len(x), "\n")

# Mengambil kata khusus di kalimat 
print("---checking---")
xi = input("Tulis kata aja : ")
yi = input("Tulis kata apa aja : ")
f = xi in x
k = yi in x
o = yi not in x

print("kata  ", xi, "dalam ", x, "= ", f)
print("kata  ", yi, "dalam ", x, "= ", k)
print("kata  ", yi, " tidak ada dalam ", x, "= ", o, "\n")

#mengulang kata sebanyak yg ditentukan
print("---Looping---")
print( x * 10)
print("wkwk" * 10, "\n")

#mengambil kata dalam suatu kalimat
print("---Indexing---")
print("kata ke - 1 dalam kalimat ", x, " adalah : ", x[0])
print("kata ke - 2 dari terakhir dalam kalimat ", x, " adalah : ", x[-2])
print("kata ke 1, 3, 5, 7, 9 dalam kalimat ", x, " adalah : ", x[0 : 6 : 2], "\n")

print("---Ascii Code---")

#nilai plus and minus 
print("nilai kata terkecil dalam ", x, " adalah : ", min(x), "\n")
print("nilai kata terbesar dalam ", x, " adalah : ", max(x), "\n")

#find nilai ascicode 
tk = input("ketik 1 kata : ")
zz = ord(tk)
print("nilai kata ", tk, "dalam ascii code adalah : ", zz)

tk = input("ketik 1 kata : ")
zz = ord(tk)
print("nilai kata ", tk, "dalam ascii code adalah : ", zz)