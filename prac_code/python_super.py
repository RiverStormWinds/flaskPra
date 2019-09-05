# coding:utf-8

# class A:
#     def add(self, x):
#         y = x + 1
#         print(y)
#
#
# class B(A):
#     def add(self, x):
#         # super() 用法规定: super(type[, object-or-type]) type(类) object-or-type(对象或类) 一般为self
#         super(B, self).add(x)


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print('%s from Parent' % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild, self)首先找到FooChild的父类，然后把类FooChild的对象转换成类FooParent的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar function')
        print(self.parent)


class G:
    def text(self):
        print('g')

class E(G):
    def text(self):
        print('e')

class B(E):
    def text(self):
        print('b')

class F(G):
    def text(self):
        print('F')

class C(F):
    def text(self):
        print('D')

class D(G):
    def text(self):
        print('d')

class A(B,C,D):
    def text(self):
        print('a')


if __name__ == '__main__':
    obj = A()
    print(A.mro())























