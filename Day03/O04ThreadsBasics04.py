import concurrent.futures
from threading import current_thread
import logging
import time

st = time.perf_counter()
def doJob(secs):
    print(f"Sleeping for {secs} seconds........{current_thread().name}")
    time.sleep(secs)
    print(f"Just woke up from sleep......{current_thread().name}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [6, 5, 4, 3, 2, 1]
    results = [executor.submit(doJob, sec) for sec in secs]

    # for res in concurrent.futures.as_completed(results):
    #     print(res.result())

et = time.perf_counter()

print(f"Completed the task in {round(et - st, 2)}")
