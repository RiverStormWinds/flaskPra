# coding:utf-8
'''
闪现，基于session实现，flash("zzZtq", category='err')，category意为分类，
将我们需要保存的数据通过flash方法进行保存，然后在另外的地方取出并使用，
当然，闪现的取出是一次性的，因为源码里面使用的是pop方法，取出之后，再次取出便为空值，无法在进行取出了
'''
from flask import Flask, flash, get_flashed_messages, request

app = Flask(__name__)

app.config.from_object("settings.DevelopmentConfig")

app.secret_key = 'abc'


@app.route('/get')  # http://127.0.0.1:5000/get?v=old_boy 简单url传参
def get():
    # 从某个地方获取设置的所有值，并清除
    val = request.args.get('v')
    if val == "old_boy":
        return "hello world"
    msg = {"key": "zzZtq"}
    flash(msg, category='err')
    return "hehe"


@app.route('/put/<string:key>')  # http://127.0.0.1:5000/put/hehe  多段url传参
def put(key):
    val = key
    return key


@app.route('/error')
def error():
    # msg = request.query_string.get('msg')
    data = get_flashed_messages(category_filter=['err'])
    if data:
        msg = data[0]
    else:
        msg = 'empty'
    return "错误信息: %s" % (msg,)


if __name__ == '__main__':
    app.run()

