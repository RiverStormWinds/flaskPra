# coding:utf-8
import time, threading

'''
# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

from functools import wraps
from functools import partial

def func(a1, a2, a3):
    print(a1, a2, a3)


new_func = partial(func, 444)

new_func(999, 222)
'''


# 偏函数：就是利用老函数重新构造一个新函数，在partial(func, 444) func是老函数，444是老函数第一个参数
# new_func是新函数，构造出来的新函数调用起来就直接可以传递老函数的第二各参数直接调用运行即可


def f1(x):
    return x + 1


def f2(x):
    return x + 10

func_list = [f1, lambda x:x-1]

func_list.append(f2)

for i in func_list:
    print(i)


























