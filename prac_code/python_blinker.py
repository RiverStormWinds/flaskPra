# coding:utf-8
from blinker import signal

# a = signal("a")
# b = signal("a")
# if a is b:
#     print("True")


# 使用.connect(func)方法来订阅一个信号，当信号发布时，该信号的订阅者会执行func。


# 信号的订阅
def subscriber(sender):
    print("Got a signal sent by {}".format(sender))


ready = signal('ready')

ready.connect(subscriber)

def run_send():

    ready = signal('ready')
    ready.send("HWK")

run_send()


# 信号的发布
# class Processor(object):
#     def __init__(self, name):
#         self.name = name

#     def go(self):
#         # 信号再此进行发布
#         ready = signal('ready')
#         ready.send(self)
#         print('Processing')
#         complete = signal('complete')
#         complete.send(self)

#     def __repr__(self):
#         return '<Processor {}>'.format(self.name)


# processor_hwk = Processor("hwk")

# processor_hwk.go()











