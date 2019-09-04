# coding:utf-8
from blinker import signal

a = signal("a")
b = signal("a")

if a is b:
    print("True")

