class Flower:
    def __init__ (self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

        def info(self):
            print

    def change_flower_name(self,newname):
        self.names= newnames
    def change_flower_petals(self,newnpetals):
        self.petals= newnpetals
    def change_flower_price(self,newprice):
        self.price= newprice

bunga1=Flower("Mawar",6,50000.00)

while True:
    ask =input("Do you want to change something? (y/n)")
    if ask == "n":
        break
    elif ask == "y":
        mana = int(input("Which one do you want to change?\nEnter 1 to change name\nEnter 2 to change petals\nEnter 3 to change price\nNumber: "))
        if mana == 1:
            niunem= input("Enter the name: ")
            bunga1.change_flower_name(niunem)
        elif mana == 2:
            niupet = int(input("Enter the number of petals: "))
            bunga1.change_flower_petals(niupet)
        elif mana == 3:
            niuprais = float(input("Enter the price: "))
            bunga1.change_flower_price(niuprais)
        else:
            print("ERROR")
    else:
        print("ERROR")
