
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor.......")

    def getdetails(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fnm, lnm, age):
        print("factory......")
        return cls(f"{fnm} {lnm}", age)          # call the constructor


ply1 = Player("Virat Kholi", 36)
ply1.getdetails()

print("-" * 60)
ply2 = Player.createPlayer("Rohit", "Sharma", 38)
ply2.getdetails()






