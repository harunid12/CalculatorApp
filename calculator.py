import function

print("#"*50)
print("#"*10 + "         Calculator App       " + "#"*10)
print("#"*10 + "   Created By : Ahmad Harun   " + "#"*10)
print("#"*50)
print("")

print("daftar operator")
print("1. Tambah (+)")
print("2. kurang (-)")
print("3. kali   (x)")  
print("4. bagi   (/)")

pilih = int(input("pilih : "))
angka1 = int(input("angka1 : "))
angka2 = int(input("angka2: "))

if pilih == 1:
    function.tambah(angka1, angka2)
elif pilih == 2:
    function.kurang(angka1, angka2)
elif pilih == 3:
    function.kali(angka1, angka2)
elif pilih == 4:
    function.bagi(angka1, angka2)
else:
    print("input harus benar!!")

print("")
print("#"*50)
print("#"*10 + "         Calculator App       " + "#"*10)
print("#"*10 + "   Created By : Ahmad Harun   " + "#"*10)
print("#"*50)
