import time

def fun():
    print("Started Executing....")
    time.sleep(2)
    print("Completed Executing....")

st = time.perf_counter()
fun()
fun()
fun()
et = time.perf_counter()

print(f"The total tme taken to execute - {round(et - st, 2)}")




