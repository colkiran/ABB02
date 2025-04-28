

def ProdAll(*numbers):
    print("*numbers :", *numbers)       # unpack
    print("numbers :", numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = ProdAll(1, 2, 3, 4, 5)
print(res)

print("-" * 60)

# **kwargs

def extract_details(**detials):
    print(detials)
    for k, v in detials.items():
        print(k, " => ", v)

extract_details(name="Sachin", age=35, runs=120, oppn="WI", venue="Sabina Park")

