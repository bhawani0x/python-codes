import threading
import time


def func(sec):
    time.sleep(sec)


time1 = time.process_time()

t1 = func(5)
t2 = func(5)

time2 = time.process_time()
print(time2-time1)