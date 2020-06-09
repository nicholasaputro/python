import random
import time

main=['Gunting','Batu','Kertas']

while True:
    kom = main[random.randint(0,3)]
    gas =input ("Suit yuk!\n(Ayuk/ Nope)")
    if gas == "Ayuk":
        print("Aku kasih 3 detik buat mikir!")
        for x in range (3,0,-1):
            print(x)
            time.sleep(1)
        jawaban =  input("Gunting \nBatu \nKertas \nJangan lupa huruf kapital!\nPilihanmu: ")
        if jawaban == kom:
            print("Sehati kita!")
            print(" ")
        elif jawaban == "Gunting":
            if kom == "Batu":
                print("Kasian deh kalah!")
                print(" ")
            elif kom == "Kertas":
                print("Ihh Kamu menang!\nHoki banget!")
                print(" ")
        elif jawaban == "Kertas":
            if kom =="gunting":
                print("Kasian deh kalah!")
            elif kom =="Batu":
                print("Ihh Kamu menang!\nHoki banget")
                print(" ")
        elif jawaban == "Batu":
            if kom == "Gunting":
                print("Ihh Kamu menang!\nHoki banget")
                print(" ")
            elif kom == "Kertas":
                print("Kasian deh kalah!")
                print(" ")
        else:
            print("ERROR")
    elif gas == "Nope":
        print("Thank you for playing!\nBye!")
        break
    else:
        print("Bye")
        break