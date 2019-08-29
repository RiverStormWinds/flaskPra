# coding:utf-8

# import threading

# from threading import get_ident

# def task(arg):
#     v = get_ident()
#     print(v)
#
#
# for i in range(20):
#     th = threading.Thread(target=task, args=(i,))
#     th.start()


before_dict = {}
before_dict.setdefault(None, []).append('hehe')

print(before_dict)