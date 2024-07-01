# operasi boolean 

#operasi not (input)
print("--- Operasi Not (input) ---")
a = bool (input("Masukkan nilai true or false : "))
b = bool (input("Masukkan nilai true or false : "))
hasil = not a
hasil1 = not b
print("Hasil dari Not ", a, "adalah", hasil)
print("hasil dari Not ", b, "adalah", hasil1)


#operasi and
print("--- Operasi and ---")
a = True
b = False
hasil = a and a
hasil1 = a and b
hasil2 = b and a
hasil3 = b and b
print(a, "and ", a, "akan menghasilkan nilai = ", hasil)
print(a, "and ", b, "akan menghasilkan nilai = ", hasil1)
print(b, "and ", a, "akan menghasilkan nilai = ", hasil2)
print(b, "and ", b, "akan menghasilkan nilai = ", hasil3)


#operasi or
print("--- Operasi or ---")
a = True
b = False
hasil = a or a
hasil1 = a or b
hasil2 = b or a
hasil3 = b or b
print(a, "or ", a, "akan menghasilkan nilai = ", hasil)
print(a, "or ", b, "akan menghasilkan nilai = ", hasil1)
print(b, "or ", a, "akan menghasilkan nilai = ", hasil2)
print(b, "or ", b, "akan menghasilkan nilai = ", hasil3)


#operasi xor
print("--- Operasi Xor ---")
a = True
b = False
hasil = a ^ a
hasil1 = a ^ b
hasil2 = b ^ a
hasil3 = b ^ b
print(a, "Xor ", a, "akan menghasilkan nilai = ", hasil)
print(a, "Xor ", b, "akan menghasilkan nilai = ", hasil1)
print(b, "Xor ", a, "akan menghasilkan nilai = ", hasil2)
print(b, "Xor ", b, "akan menghasilkan nilai = ", hasil3)


#operasi and 3 variabel
print("--- Operasi Or 3 Variabel ---")
a = True
b = False
hasil  = a or a or a
hasil1 = a or a or b
hasil2 = a or b or b
hasil3 = b or a or a
hasil4 = b or b or a
hasil5 = b or b or b

print(a, "or ", a, "or ", a, "akan menghasilkan nilai = ", hasil)
print(a, "or ", b, "or ", a, "akan menghasilkan nilai = ", hasil1)
print(a, "or ", b, "or ", b, "akan menghasilkan nilai = ", hasil2)
print(b, "or ", a, "or ", a, "akan menghasilkan nilai = ", hasil3)
print(b, "or ", b, "or ", a, "akan menghasilkan nilai = ", hasil4)
print(b, "or ", b, "or ", b, "akan menghasilkan nilai = ", hasil5)
