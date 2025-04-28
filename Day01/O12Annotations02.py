
def greet(gname :str, greet :str = "Hello") -> str:
    return f"{greet} {gname}"

print(greet("Sachin"))
print(greet("Sachin", "Hola"))
print("-" * 60)

def add(a :int, b :int) -> int:
    c = a + b
    return c

print(add(100, 200))
print(add(1.5, 2.9))
print(add("hello", " world"))

print("-" * 60)

def Total_Marks(p : 'Marks in physics', c: 'Marks in chemistry', m :'Marks in maths', b: 'Marks in biology') -> float:
    total = p + c + m + b
    return total

Total_Marks(89, 78, 97, 99)
print(Total_Marks.__annotations__)

