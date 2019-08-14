# coding:utf-8
from flask import Flask, render_template, request, redirect, session, url_for
from functools import wraps
from datetime import timedelta

app = Flask(__name__)
app.secret_key = '123456'
app.config.update(SECRET_KEY='123456')

USERS = {
    1: {'name': '掌柜坤',
        'age': 18,
        'gender': 'male',
        'text': '名花虽有主，我来松松土'},
    2: {'name': '主城',
        'age': 18,
        'gender': 'male',
        'text': '天若有情天亦老，我为长者续一秒'},
    3: {'name': '福城',
        'age': 18,
        'gender': 'female',
        'text': 'hehe，我呵呵'}
}


def user_login(func):
    @wraps(func)
    # 如果没有@wraps的话，@user_login 装饰的函数本身就是wrapper函数，
    # @app.route(...)装饰的全部就都是以wrapper命名的函数，导致函数名相同的冲突，就会报错
    def wrapper(*args, **kwargs):
        if not session.get('user_info'):
            return redirect(url_for('l1'))
        else:
            print('session --> ', session.get('user_info'))
            result = func(*args, **kwargs)
            return result
    return wrapper


@app.route('/detail/<int:nid>', methods=['GET'])  # method 表示函数支持的方法
@user_login
def detail(nid):
    user = session.get('user_info')
    if user:
        info = USERS.get(nid)

        return render_template('detail.html', info=info)
    else:
        return redirect('/login')


@app.route('/index', methods=['GET'])  # method 表示函数支持的方法
@user_login
def index():
    user = session.get('user_info')
    if user:
        return render_template('index.html', user_dict=USERS)
    else:
        url = url_for('l1')  # url反向生成
        return redirect(url)


@app.route('/login', methods=['GET', 'POST'], endpoint='l1')  # method 表示函数支持的方法,endpoint反向生成url
def login():
    # source_code: template_folder='templates'  templates为模板位置的文件夹相对目录
    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            app.permanent_session_lifetime = timedelta(seconds=5)  # 设置了session超时时间
            return redirect('index')
        return render_template("login.html", error='用户名或密码错误')


if __name__ == '__main__':
    app.run(debug=True)

