# coding:utf-8

"""
三层装饰器：
编写带参数decorator
考察上一节的 @log 装饰器：


def log(f):
    def fn(x):
        print 'call ' + f.__name__ + '()...'
        return f(x)
    return fn
发现对于被装饰的函数，log打印的语句是不能变的（除了函数名）。

如果有的函数非常重要，希望打印出'[INFO] call xxx()...'，有的函数不太重要，希望打印出'[DEBUG] call xxx()...'，这时，log函数本身就需要传入'INFO'或'DEBUG'这样的参数，类似这样：


@log('DEBUG')
def my_func():
    pass
把上面的定义翻译成高阶函数的调用，就是：


my_func = log('DEBUG')(my_func)
上面的语句看上去还是比较绕，再展开一下：


log_decorator = log('DEBUG')
my_func = log_decorator(my_func)
上面的语句又相当于：


log_decorator = log('DEBUG')
@log_decorator
def my_func():
    pass
所以，带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数：


def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print '[%s] %s()...' % (prefix, f.__name__)
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()
执行结果：


[DEBUG] test()...
None
对于这种3层嵌套的decorator定义，你可以先把它拆开：


# 标准decorator:
def log_decorator(f):
    def wrapper(*args, **kw):
        print '[%s] %s()...' % (prefix, f.__name__)
        return f(*args, **kw)
    return wrapper
return log_decorator

# 返回decorator:
def log(prefix):
    return log_decorator(f)
拆开以后会发现，调用会失败，因为在3层嵌套的decorator定义中，最内层的wrapper引用了最外层的参数prefix，所以，把一个闭包拆成普通的函数调用会比较困难。不支持闭包的编程语言要实现同样的功能就需要更多的代码。

"""

'''
def outer():
    x = 1
    y = 2

    def inner():
        print("x = %s"%x)
        print("y = %s"%y)

    print(inner.__closure__)
    return inner

outer()
'''
import random
import time

'''
from urllib.request import urlopen

def index(url):  # url 属于内部变量，此函数也属于闭包函数
    def get():
        return url
    return get

# python = index("http://www.python.org")
# print(python())

baidu = index("http://www.baidu.com")
print(baidu())
'''

'''
#  无参装饰器

import time, random


def outer(func):  # 将index的地址传递给func
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间为%s" % (end_time - start_time))
    return inner


def index():  # 作为函数参数本身传递给装饰器函数
    time.sleep(random.randrange(1, 5))
    print("welcome to index page")


if __name__ == '__main__':

    # outer(index)
    # outer(index)本身是不会打印任何东西的，
    # 因为他的返回值是一个函数(inner)地址，而这个函数(inner)没有被调用
    f = outer(index)
    f()  # 在此进行index()方法的调用
'''


'''
# 有参装饰器

def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
        return res
    return wrapper


@timmer  # 就等同于 home = timmer(home)，事实上是将timmer(home) --> wrapper方法的地址传递给了 home
def home(name):
    time.sleep(random.randrange(1, 3))
    print('welecome to %s HOME page' % name)
    return 123123123123


if __name__ == '__main__':


    # 不使用@语法糖调用方法如下:
    #     home = timmer(home)
    #     s = home('hwk')
    #     print(s)


    # 使用语法糖调用方式如下
    # 使用语法糖@相当于将home = timmer(home)加在了s = home('hwk')之前
    s = home('hewk')
    print(s)
'''

'''
# 多装饰器情景
import time
import random


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('run time is %s' % (stop_time - start_time))
    return wrapper


def auth(func):
    def deco():
        name = 'hewk'
        password = '123'
        if name == 'hewk' and password == '123':
            print('login successful')
            func()  # 函数在此被装饰
        else:
            print('login err')

    return deco


@timmer
@auth
def index():
    time.sleep(1)
    print('welecome to index page')


if __name__ == '__main__':
    index()

'''


'''
# 多层装饰器
def deco1(func):
    print(1)
    def wrapper1():
        print(2)
        func()
        print(3)
    print(4)
    return wrapper1


def deco2(func):
    print(5)
    def wrapper2():
        print(6)
        func()
        print(7)
    print(8)
    return wrapper2


@deco1
@deco2
def foo():
    print('foo')

# 整体相当于deco1(deco2(foo))

if __name__ == '__main__':
    # 执行顺序 5 - 8 - 1 - 4 - 2 - 6 - foo - 7 - 3
    """
    1、修饰器本质上就是一个函数，只不过它的传入参数同样是一个函数。
       因此，依次加了deco1和deco2两个装饰器的原函数foo实际上相当于deco1(deco2(foo))。
    2、明白了第1步后，下面进入这个复合函数。首先执行的是内层函数deco2(foo)。因此第一个打印值是5。
       接下来要注意，在deco2这个函数内定义了一个wrapper2函数，但是并没有类似于wrapper2()的语句，
       因此该函数内的语句并没有立即执行，而是作为了返回值。因此wrapper2内的3条语句作为输入参数传递到了deco1内。
       wrapper2函数内还有一行print(8)，因此第二个打印值为8。
    3、下一步是执行deco1()函数内容。
       与2类似，先打印出1和4，返回值为wrapper1。
       由于更外层没有装饰器，因此接下来就将执行wrapper1内的内容。
       第五个打印值为2。接着执行func()函数，注意此处func()表示的是wrapper2中的内容，
       因此跳到wrapper2中执行。第六个打印值为6。类似的，wrapper2中的func()为foo()，
       因此接着会输出foo。最后，回到wrapper2和wrapper1的最后一行，依次输出7和3。
    4、到这里，整个装饰器的运行过程结束。
"""

    foo()

'''

'''
# 类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):  # 类装饰器是使用__call__方法进行实现的，__call__方法在创建类对象时候就进行调用
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
'''

'''
class Foo(object):
    def __init__(self):
        pass

    def __call__(self, func):
        def _call(*args, **kwargs):
            print('class decorator running')
            return func(*args, **kwargs)

        return _call


class Bar(object):
    @Foo()
    def bar(self, test, ids):
        print('bar')


Bar().bar('aa', 'ids')
'''

'''
import time
from functools import wraps
def log(name):
    def decora(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("name : {0}".format(name))
            print("function runing")
            ts = time.time()
            result = func(*args, **kwargs)
            te = time.time()
            print(" function      = {0}".format(func.__name__))
            print("arguments      = {0} {1}".format(args, kwargs))
            print("   return      = {0}".format(result))
            print("     time      = %.6f sec" % (te - ts))
        return wrapper
    return decora

@log('log')
def sum(x,y):
    return x + y

sum(1,2)

'''

def simple_print(rule, endpoint, func, **options):
    print(rule, endpoint)
    print(func, options)


def route(rule, **options):
    def decorator(func):
        endpoint = options.pop('endpoint', None)
        simple_print(rule, endpoint, func, **options)
        return func
    return decorator


@route('/', endpoint='n1', method=['GET', 'POST'])
def index():
    print('hehe')


if __name__ == '__main__':
    index()





























