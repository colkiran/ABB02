
def funlogger(fnc):

    def helper():
        print("Logged into the service......")
        fnc()
        print("logger channel closed.......")
        print("-" * 60)

    return helper

print("-" * 60)

def normalFun():
    print("I should be called normal......")

funlogger(normalFun)            # no output

print("-" * 60)

funlogger(normalFun)()          # calls helper function

print("-" * 60)

res_fun = funlogger(normalFun)
res_fun()                       # calls helper function

print("-" * 60)

normalFun = funlogger(normalFun)
normalFun()                     # calls helper function

print("-" * 60)
@funlogger          # decorator - basicFun = funlogger(basicFun)
def basicFun():
    print("I should be called BASIC.......")

basicFun()          # calls helper function


