# write a decorator to find the time taken by a function to execute
def timeCalc(fnc):

    def helper(n):
        import time
        print("Function execution started......")
        st = time.perf_counter()
        fnc(n)
        et = time.perf_counter()
        print("Function execution completed.......")
        print(f"The total time taken by the function is :{round(et - st, 2)}")

    return helper

@timeCalc
def fun(x):
    lst = []
    for i in range(x):
        for j in range(1, i+1):
            lst.append(j ** 2)

fun(6000)
