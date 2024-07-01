# pr dari kelas terbuka 
# operasi logika & komparasi

# -----0+++++5------8++++11-----
#quest 1


print("--- Quest 1 ---")
ans1 = float (input("masukkan angka \ndiatas 0 \ndan \ndibawah 5 \n= "))
ans2 = float (input("masukkan angka \natas 8 \ndan \ndibawah 11 \n = "))

the1 = ans1 > 0
the2 = ans1 < 5
king1 = the1 and the2

print("Kebenaran angka diatas 0 dan dibawah 5 : ", king1)

the3 = ans2 > 8
the4 = ans2 < 11
king2 = the3 and the4
print("kebenaran angka diatas 8 dan dibawah 11 : ", king2)

the_king = king1 and king2
print("maka hasil dari dua kesimpulan adalah : ", the_king)

print("\n")


#++++0------5+++++8-----11+++++
#quest2
print("--- Quest 2 ---")
ans1 = float (input("masukkan angka \bawah 0 \ndan \ndiatas 5 \n= "))
ans2 = float (input("masukkan angka \nbawah 8 \ndan \natas 11 \n = "))

the1 = ans1 < 0
the2 = ans1 > 5
king1 = the1 or the2

print("Kebenaran angka diatas 0 dan dibawah 5 : ", king1)

the3 = ans2 < 8
the4 = ans2 > 11
king2 = the3 or the4
print("kebenaran angka diatas 8 dan dibawah 11 : ", king2)

the_king = king1 and king2
print("maka hasil dari dua kesimpulan adalah : ", the_king)
