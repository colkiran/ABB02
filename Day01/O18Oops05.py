
class Player:

    team = "India"      # class attribute / variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getdetials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Virat",36)
ply1.getdetials()

print("-" * 60)

ply2 = Player("Rohit", 38)
ply2.getdetials()

print("-" * 60)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
ply1.team = "RCB"
print(f"ply1 :{ply1.team}")

print("-" * 60)
print(f"Player :{Player.team}")
print(f"ply2   :{ply2.team}")

print("-" * 60)
print(ply1.__dict__)
# class attributes cannot be modified with objects (ply1) instead it can be modified only using class name (Player)
