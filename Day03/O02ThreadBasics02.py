
# asynchronous execution of code

from threading import Thread, current_thread
import time

def doJob():
    print(f"Going to sleep for 2 secs......{current_thread().name}")
    time.sleep(2)
    print(f"Just woke from sleep.......{current_thread().name}")

st = time.perf_counter()

thrd1 = Thread(target=doJob, name = "th1")
thrd2 = Thread(target=doJob, name = "th2")
thrd3 = Thread(target=doJob, name = "th3")


thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

et = time.perf_counter()

print(f"The total time taken to execute is :{round(et - st, 2)}")
