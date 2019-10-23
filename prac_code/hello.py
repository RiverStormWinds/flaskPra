# coding:utf-8

'''
私有变量的强制访问
class Foo(object):
    def __init__(self):
        self.__a = {"1": "hello world"}


class Obj():
    def __init__(self):
        self.foo = Foo()
        self.foo._Foo__a = {"1": "hello"}

o = Obj()
print(o.foo._Foo__a)
'''

'''
匿名函数排序操作
a_list = [
    (51, 'alex'),
    (32, 'hwk'),
    (443, 'ztq'),
    (4, 'awj'),
    (4, 'bwj'),
    (4, 'dwj')
]

a_list.sort(key=lambda k: (k[0], k[1]))
print(a_list)
'''

# class A(object):
#     pass
#
#
# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         """
#         name代表类的名称；bases代表当前类的父类集合；attrs代表当前类的属性，
#         是狭义上属性和方法的集合，可以用字典dict的方式传入
#         :param name: 代表类的名字
#         :param bases: 代表类的父类集合
#         :param attrs: 代表当前类的属性，是狭义上的属性和方法集合，可以用字典的方式传入
#         :return:
#         """
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
#
# l = MyList()
#
# l.add(1)
#
# print(l)

'''

# 查找并计算self__class__源码
class Foo(object):
    a = "ting_dinasty"
    b = "imagretion"
    def __init__(self):
        pass

    @classmethod
    def test(cls):
        pass

    def show(self):
        print(self.__class__)


f = Foo()
f.show()

'''

class LocalProxy(object):

    __slots__ = ("__local", "__dict__", "__name__", "__wrapped__")


    def __init__(self, temp, name=None):
        # object.__setattr__(self, "_LocalProxy__local", local)
        # object.__setattr__(self, "__name__", name)
        # if callable(local) and not hasattr(local, "__release_local__"):
        #     object.__setattr__(self, "__wrapped__", local)
        self.__local = temp


if __name__ == '__main__':
    l = LocalProxy('hehe')































