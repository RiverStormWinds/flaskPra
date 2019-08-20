# coding:utf-8

class E(object):
    def __init__(self, value):
        print("into __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into __new__")
        return super(E, cls).__new__(cls)


# -------------------------------------------------------


class A(object):
    def __init__(self, value):
        print("into A __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into A __new__")
        return object.__new__(cls)  # 第二步


class B(A):
    # 在新式类中，__new__()对当前类进行实例化，并将实例返回
    # 传给了__init__()，__init__()方法是self就是__new__()传过来的。
    # 如果__new__方法没有正确返回cls实例，则__init__方法无法正确执行

    def __init__(self, value):  # 第三步
        print("into B __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into B __new__")
        return super(B, cls).__new__(cls, *args, **kwargs)  # 第一步


# -----------------------------------------------------------


class C(object):
    def __init__(self, value):
        print("into C __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into C __new__")
        return object.__new__(cls)  # 第二步


class D(C):
    # 在新式类中，__new__()对当前类进行实例化，并将实例返回
    # 传给了__init__()，__init__()方法是self就是__new__()传过来的。
    # 如果__new__方法没有正确返回cls实例，则__init__方法无法正确执行

    def __init__(self, value):
        # 第三步未执行，因为__new__(C, *args, **kwargs)传递给__init__()的不是cls类本身，传递进去的是一个错误类C
        # __init__()拿到了错误的C类，无法进行初始化操作
        print("into D __init__")
        self.value = value

    def __new__(cls, *args, **kwargs):
        print("into D __new__")
        return super(D, cls).__new__(C, *args, **kwargs)  # 第一步


if __name__ == '__main__':
    # b = B(10)
    # d = D(10)
    e = E(10)

