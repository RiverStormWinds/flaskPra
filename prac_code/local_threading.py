# coding:utf-8

import threading

local_values = threading.local()

class Foo:
    def __init__(self):
        self.h = 0

# local_values = Foo()

def func(num):
    local_values.h = num
    import time
    time.sleep(1)
    print(local_values.h, threading.current_thread().name)

for i in range(20):
    t = threading.Thread(target=func, args=(i+1,))
    t.start()

