# coding:utf-8
import threading


class Singleton(object):

    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls, *args, **kw):
        if cls in cls.objs:
            return cls.objs(cls)
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs(cls)
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()


s = Singleton()
print(s)
