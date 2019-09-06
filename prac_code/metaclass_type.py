# coding:utf-8

class MyType(type):
    def __init__(self, *args, **kwargs):
        print('init')
        super(MyType, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('call')
        super(MyType, self).__call__(*args, **kwargs)

class Foo(metaclass=MyType):
    # 1. 元类的特点：类就是元类的实例化，所以在创建Foo类的时候，调用了MyType元类的__init__方法
    # 2. 也就是说Foo类就是MyType()，Foo()就是MyType()()也就自动调用了元类MyType的__call__方法，Foo实例化几次，调用几次
    # 3. 所有的继承object的类，其实本身已经是一个对象了，如果我们进行实例化的时候，也就是Foo()的时候，也就要调用元类的__call__方法了
    # 4. 元类__call__方法本质就是调用元类创建的类Foo的__new__方法和__init__方法
    print('Foo')
    pass

obj = Foo()

