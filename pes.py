pes= {'es teh manis': 4 , 'nasi pecel' : 2 , 'sambal bawang': 3}

print("Kakak sudah pesan:")

for key, val in pes.items():
    print(f"{key}nya {val}")

while True:
    tanya = input("Apa ada tambahan kak? (y/n)")
    if tanya == "y" :
        ui = input("Tambah apa kak?")
        iu = int(input(f"Tambah {ui}nya berapa kak?"))
        pes[ui]=iu
    elif tanya =="n":
        break
    else:
        print ("Error")
        continue

print("Saya ulang pesanannya ya kak.")

print("Kakak sudah pesan:")

for key, val in pes.items():
    print(f"{key}nya {val} ")

while True:
    ask = input("Pesanannya sudah benar ya kak? (y/n)")
    if ask != "y":
        ui = input("Kurang apa kak?")
        iu = int(input(f"Tambah {ui}nya berapa kak?"))
        pes[ui] = iu
    elif ask =="y":
        break
    else:
        continue

pp= list(pes.values())
print(f"Baik kak! Mohon ditunggu ya kak pesanannya {sum(pp)} menit.")
