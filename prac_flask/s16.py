# coding:utf-8
from flask import Flask, current_app, globals, _app_ctx_stack
from flask import g

app = Flask("flask_01")
app.DEBUG = False


with app.app_context():  # app.app_context()一定是一个对象
    g.kkk = "hehe"
    g.setdefault("jjj", "hehe2")
    print(g.kkk, g.jjj)

