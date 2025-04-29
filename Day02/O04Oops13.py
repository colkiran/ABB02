
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("getter called....")
        return self.__price

    def set_price(self, val):
        print("setter called......")
        self.__price = val

    def del_price(self):
        self.__price = 0

    price = property(get_price, set_price, del_price)

coke = Product(115)
print(coke.price)
coke.price = 50
print(coke.price)
del coke.price
print(coke.price)
