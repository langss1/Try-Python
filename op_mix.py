# operasi gabungan antara komparasi dan boolean

# +++ = True
# --- + False

#rentang ++++0----5++++

user_1 = float (input("Masukkan angka \n kurang dari 0 \n atau \n lebih dari 5 \n = "))
log1 = user_1 < 0
log2 = user_1 > 5

print(user_1, "kurang dari 5 bernilai : ", log1)
print(user_1, "lebih dari 10 bernilai : ", log2)

logon = log1 or log2
print("maka kesimpulannya adalah ", logon)


#rentang -----5++++8-----

user_2 = float (input("Masukkan angka \n kurang dari 0 \n dan \n lebih dari 5 \n = "))
log1 = user_2 > 5
log2 = user_2 < 8

print(user_2, "kurang dari 5 bernilai ", log1)
print(user_2, "lebih dari 10 bernilai ", log2)

logot = log1 and log2
print("maka kesimpulannya adalah ", logot)


# atau = maka salah satu benar = benar
# dan = dua - duanya harus benar