
def outerFun(gname):
    gname = gname + " Dravid"

    def innerFun():

        print("Hello World.....")
        print(f"Greetings Mr.{gname}")

    return innerFun

# outerFun("Sachin")
print(f"outerFun.__name__  :{outerFun.__name__}")
print(f"outerFun('Rahul').__name__ :{outerFun('Rahul').__name__}")

print("-" * 60)
outerFun("Rahul")()         # calls the innerFun

print("-" * 60)
inref = outerFun("Rahul")

# after fewlines of code
print("Python Training")
print("Python Training")
print("Python Training")
print("Python Training")
print("Python Training")

print("-" * 60)

inref()                     # calls the innerFun

print("-" * 60)
print("-" * 60)

def add(x, y):
    return x + y

# res = add(10 ,20)
a = add

res = a(30, 40)
print(f"res :{res}")
