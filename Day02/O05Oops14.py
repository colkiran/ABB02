
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("getter called.....")
        return self.__price

    @price.setter
    def price(self, val):
        print("setter called.....")
        self.__price = val

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.price = 0

slice = Product(75)
print(slice.price)
slice.price = 130
print(slice.price)
del slice.price
print(slice.price)
