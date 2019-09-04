# coding:utf-8
from flask import Flask, signals

app = Flask("flask_01")

def func(*args, **kwargs):
    print("触发信号", args, kwargs)

# 到底是信号先执行呢，还是before_first_request先执行呢?
signals.request_started.connect(func)


# 通过阅读源码，是before_first_request先进行执行
@app.before_first_request
def before_first(*args, **kwargs):
    pass


@app.before_first_request
def before_first_2(*args, **kwargs):
    pass


@app.before_request
def before_req(*args, **kwargs):
    return "hehe"


@app.before_request
def before_req_2(*args, **kwargs):
    return "hehe"


@app.route('/', methods=['GET'])
def index():
    print("视图")
    return "hello world"


if __name__ == '__main__':
    app.run()

