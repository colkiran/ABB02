
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if val < 0:
            raise ValueError ("Price cannot be negative.....")
        self.__price = val

    def del_price(self):
        self.__price = 0


import sys
try:
    pepsi = Product(120)
    print(pepsi.get_price())
    pepsi.set_price(85)
    print(pepsi.get_price())
    pepsi.del_price()
    print(pepsi.get_price())
except:
    print("Exception caught......")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])