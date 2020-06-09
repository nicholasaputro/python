def volume(rusuk):
    print(f"{rusuk**3} cm^3")
def luas(rusuk):
    print(f"{rusuk*6} cm^2")

rusuk= int(input("Rusuk kubus:")

c = int(input(" Ketik 1 untuk volume \n Ketik 2 untuk luas\n Ketik di sini: "))

if c == 1:
    volume(rusuk)
elif c == 2:
    luas(rusuk)
else:
     print("ERROR")