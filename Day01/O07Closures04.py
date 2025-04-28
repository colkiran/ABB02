
def fun(*args):
    print(args)
    # print("*args :", *args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)
fun(10, 20, 30, 40)

print("-" * 60)

def sum(x, y):
    print("sum function called...")
    return x + y

def diff(x, y):
    print("diff function called.....")
    return x - y

def add(*x):
    print("add function called......")
    y = 1
    for i in x:
        y += i
    return y

# HOF - Higher Order Function - any function if it takes a function as an argument or returns a function as reference
def log_details(fnc):
    log_info = "Logging into a service......."

    def innerFun(*args):
        print(log_info)
        print(fnc(*args))           # call back
        print("-" * 60)

    return innerFun

sumlogger = log_details(sum)
difflogger = log_details(diff)

sumlogger(10, 20)
difflogger(30, 12)

addlogger = log_details(add)
addlogger(1, 2, 3, 4, 5)
