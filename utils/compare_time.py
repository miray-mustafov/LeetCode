import time


def compare_time_of2(f1, f2, *params):
    t0 = time.time()
    for i in range(10000):
        f1(*params)
    t1 = time.time()
    for i in range(10000):
        f2(*params)
    t2 = time.time()
    print(t1 - t0, t2 - t1)
