user= "Ian"
passw= "123"

for n in range(3,0,-1):
    print(f"You have {n} tries")
    user = input ("Username=")
    passw = input ("Password=")
    if user == "Ian" and passw == "123":
        print("Login Success")
        break
    else:
        print("Login Invalid")
        