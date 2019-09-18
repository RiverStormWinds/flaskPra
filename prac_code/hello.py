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

class A(object):
    pass


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        """
        name代表类的名称；bases代表当前类的父类集合；attrs代表当前类的属性，
        是狭义上属性和方法的集合，可以用字典dict的方式传入
        :param name: 代表类的名字
        :param bases: 代表类的父类集合
        :param attrs: 代表当前类的属性，是狭义上的属性和方法集合，可以用字典的方式传入
        :return:
        """
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    def __init__(self):
        pass



l = MyList()

l.add(1)

print(l)































