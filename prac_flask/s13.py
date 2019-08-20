# coding:utf-8
from flask import Flask, render_template, request, redirect, session, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = '123456'

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


@app.before_request  # 在请求之前拦截请求，并判断是否拥有session，可以省去很多不必要的@user_login装饰器，比较方便
def process_request(*args, **kwargs):
    print("请求之前")
    # print(request.url)
    # print(request.path)
    if request.path == "/login":
        return None
    user = session.get("user_info")
    if user:
        return None
    else:
        return redirect("/login")


@app.after_request  # 这是在请求之后进行相关的操作
def process_response(response):
    print("请求之后")
    return response


@app.errorhandler(404)  # app.errorhandler(404)定制错误信息
def page_not_found(error):
    return 'This page does not exist', 404


@app.route('/detail/<int:nid>', methods=['GET'])  # method 表示函数支持的方法
def detail(nid):
    user = session.get('user_info')
    if user:
        info = USERS.get(nid)

        return render_template('detail.html', info=info)
    else:
        return redirect('/login')


@app.route('/index', methods=['GET'])  # method 表示函数支持的方法
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

