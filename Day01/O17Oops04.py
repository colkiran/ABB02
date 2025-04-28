"""
self - will have the name of the object that called the method

ply1.get_detials()   -> self -> ply1

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Virat", 36)
ply1.get_details()

print("-" * 60)

ply2 = Player("Rohit", 38)
ply2.get_details()

print("-" * 60)
ply2.runs = 150
print(ply2.runs)

print("-" * 60)
print("ply1 :", ply1.__dict__)            # used to store member data
print("ply2 :", ply2.__dict__)