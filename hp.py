class Handphone:
    def __init__(self, version, brand, color):
        self.version = version
        self.brand = brand
        self.color = color

    def info(self):
        print(self.brand, self.version, self.color)

phoneversion = input('Enter phone version: ')
phonebrand = input('Enter phone brand: ')
phonecolor = input ('Enter phone color: ')

handphone1= Handphone(phoneversion, phonebrand, phonecolor)
handphone1.info()
