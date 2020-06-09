doc = []

def doc():
    for d in doc():
        for key, val in d.items():
            print(f"{key}:{val}")
        print(" ")

def make(nama, umur, spesialitas, namadoktor):
    nama={}
    nama["Nama"]= namadoktor
    nama["Umur"]= umur
    nama["Speciality"]= spesialitas

while True:
    ask = input("Add doctor?(y/n)")
    if ask == "y":
        nama = input("Isi nama dokter: ")
        age = int(input("Isi umur dokter: "))
        spes = input("Isi spesialitas dokter: ")
        make(nama, age, spes, nama)
    elif ask =="n":
        break
    else:
        print("ERROR")
        continue

doc()