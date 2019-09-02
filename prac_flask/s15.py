# coding:utf-8
from flask import Flask, current_app, globals, _app_ctx_stack
from flask import globals

app = Flask("flask_01")
app.DEBUG = False

app2 = Flask("flask_02")
app2.DEBUG = False


with app.app_context():  # app.app_context()一定是一个对象
    print(_app_ctx_stack._local.__storage__)
    print(current_app.config['DEBUG'])

    with app2.app_context():
        # 在这个app2里面可以体现stack栈的作用
        # {4599125440: {'stack': [<flask.ctx.AppContext object at 0x104292b00>,
        #                         <flask.ctx.AppContext object at 0x104292b38>]}}
        print(_app_ctx_stack._local.__storage__)
        print(current_app.config['DEBUG'])
