
class Player:

    def __init__(self):         # constructor
        print("Player Initialized.......")

    def get_runs(self):
        print("runs scored")

    def __del__(self):
        print("Destructor.......")

sachin = Player()
sourav = Player()
print("Hello World")
sachin.get_runs()
sourav.get_runs()
