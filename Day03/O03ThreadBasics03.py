import time
from threading import Thread, current_thread

def doJob(sec, tname):
    print(f"Going to sleep for 2 secs......{tname}")
    time.sleep(sec)
    print(f"Just woke from deep sleep.......{tname}")

st = time.perf_counter()

threads = []

for i in range(50):
    t = Thread(target=doJob, name="th"+ str(i), args=[2, "th" + str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

et = time.perf_counter()

print(f"The total time taken by the task is {et - st}")
