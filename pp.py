pes= ['es teh manis' , 'nasi pecel' , 'sambal bawang']

print("Kakak sudah pesan:") 
for p in range (len(pes)):
    print (p+1,pes[p]) 
while True:
    tanya = input("Apa ada tambahan kak? (y/n)")
    if tanya == "y" :
        ui = input("Tambah apa kak?")
        pes.append(ui)
    elif tanya =="n":
        for p in range (len(pes)):
            print(p+1,pes[p])
        break
    else:
        print ("Error")