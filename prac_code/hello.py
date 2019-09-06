# coding:utf-8


class Foo(object):
    def __init__(self):
        self.__a = {"1": "hello world"}


class Obj():
    def __init__(self):
        self.foo = Foo()
        self.foo._Foo__a = {"1": "hello"}

o = Obj()
print(o.foo._Foo__a)
