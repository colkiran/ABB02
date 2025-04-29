
import time
class TimeCalculator:

    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        print("Execution started......")
        start_time = time.perf_counter()
        result = self.fnc(*args, **kwargs)
        end_time = time.perf_counter()
        print("Execution Completed........")
        print(f"Total time taken by the function to execute :{round(end_time - start_time, 2)} seconds")
        return result

@TimeCalculator
def fun(n):
    lst = []
    for i in range(n):
        for j in range(1, i+1):
            lst.append(j ** 3)

print(fun(6500))
