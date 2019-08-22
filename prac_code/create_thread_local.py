# coding:utf-8

import threading
# try:
#     from gevent import getcurrent as get_ident  # 拿到协程的标示符id
# except ImportError:
#     try:
#         from threading import get_ident
#     except ImportError:
#         from _thread import get_ident  # 支持线程
from threading import get_ident

class Local:
    def __init__(self):
        # self.storage = {}
        object.__setattr__(self, 'storage', {})
        # self.get_ident = get_ident
        object.__setattr__(self, 'get_ident', get_ident)

    # def set(self, k, v):
    #     ident = self.get_ident()
    #     origin = self.storage.get(ident)
    #     if not origin:
    #         origin = {k: v}
    #     else:
    #         origin[k] = v
    #     self.storage[ident] = origin

    def __setattr__(self, key, value):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            origin = {key: value}
        else:
            origin[key] = value
        self.storage[ident] = origin

    # def get(self, k):
    #     ident = self.get_ident()
    #     origin = self.storage.get(ident)
    #     if not origin:
    #         return None
    #     return origin[k]

    def __getattr__(self, item):
        ident = self.get_ident()
        origin = self.storage.get(ident)
        if not origin:
            return None
        return origin[item]


local_values = Local()
def task(num):
    # local_values.set('name', num)
    local_values.name = num
    # local_value.name = num 运行时会调用魔法方法，建立'name' = num对应关系(将name视为一个字符串)
    import time
    time.sleep(1)
    print(local_values.name, threading.current_thread().name)


for i in range(20):
    th = threading.Thread(target=task, args=(i,), name="thread%s" % i)
    th.start()



















