
class Player:

    team : str
    plyrCount :int

class Derived(Player):
    pass

print(Player.__annotations__)
print(Derived.__annotations__)
