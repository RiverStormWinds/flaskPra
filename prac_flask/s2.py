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
    @wraps(func)  # 做的事情相当于将wrapper的函数名称改成(func): 传递进来的func
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


# flask的app.before_request和app.after_request相当与django的中间件，两者作用相同
"""
可以添加多个app.before_request和app.after_request
app.before_request是按照顺序进行执行
app.after_request是按照倒序进行执行的
例：
@app.before_request
def request1():
    print('request1')

@app.before_request
def request2()
    print('request2')

@app.after_request
def response1()
    print('response1')

@app.after_request
def response2()
    print('response2)
    
接收到请求的最终打印结果如下：
request1
request2
response2
response1

补充：如果request1执行完成后并没有执行后面的request2，但是所有的response都会执行 
"""


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
            app.permanent_session_lifetime = timedelta(seconds=60)  # 设置了session超时时间
            return redirect('index')
        return render_template("login.html", error='用户名或密码错误')


@app.template_global()
def sb(a1, a2):
    return a1 + a2
# 在template模板中进行使用的方法是 {{sb(1, 2)}}


@app.template_filter()
def db(a1, a2, a3):
    return a1 + a2 + a3
# 在template模板中进行使用的方法是 {{1|db(2, 3)}}


if __name__ == '__main__':
    app.run(debug=True)

