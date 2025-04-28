
def fun(x):     # x is a local variable
    global a
    print("Hello World")
    print(f"inside fun x :{x}")
    a = 30
    print(f"inside fun a :{a}")

a = 10

print(f"before the function call :{a}")

fun(a)
# print(f"x :{x}")
print(f"after the function call :{a}")

print("-" * 60)
print("-" * 60)
print("-" * 60)

# non local - nested functions

def outerFun():
    gst = "Sachin"          # local variable

    def innerFun():

        nonlocal gst        # only local variables can be converted to nonlocal
        gst += " Tendulkar"
        print("Hello World")
        print(f"Greetings Mr.{gst}")

    # outerFun Scope
    innerFun()
    print(f"gst :{gst}")

outerFun()


print("-" * 60)
print("-" * 60)
print("-" * 60)

def fun1():
    a = 10

def fun2():
    b = 20
    fun1()
    print(a)
    a = 40

fun2()
fun1()
