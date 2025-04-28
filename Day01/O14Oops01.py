
class Player:           # pascal casing

    def getruns(self):
        print("runs scored.....")

sachin = Player()
sachin.getruns()

print("-" * 60)
print(type(sachin))

print("-" * 60)
print(f"isinstance(sachin, Player)) :{isinstance(sachin, Player)}")
print(f"isinstance(sachin, object)) :{isinstance(sachin, object)}")
print(f"isinstance(sachin, str)) :{isinstance(sachin, str)}")


