# coding:utf-8
from flask import Flask, current_app, globals, _app_ctx_stack, g
from flask import globals

app = Flask("flask_01")
app.DEBUG = False

app2 = Flask("flask_02")
app2.DEBUG = False


with app.app_context():  # app.app_context()一定是一个对象
    print(_app_ctx_stack._local.__storage__)
    print(current_app.config['DEBUG'])

    with app2.app_context():
        print(_app_ctx_stack._local.__storage__)
        print(current_app.config['DEBUG'])

