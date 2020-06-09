a = int(input("Angka pertama: "))
b = int(input("Angka kedua  : "))
c = int(input(" Ketik 1 untuk penjumlahan \n Ketik 2 untuk pengurangan \n Ketik 3 untuk perkalian \n Ketik 4 untuk pembagian \n Ketik di sini: "))
if c == 1:
    print(a + b)
elif c == 2:
    print(b - a)
elif c == 3:
    print(a* b)
elif c == 4:
    print(b/a)
else:
     print("ERROR")