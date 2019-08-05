# coding:utf-8
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERS = {
    1: {'name': '掌柜坤',
        'age': 18,
        'gender': 'male',
        'text': '名花虽有主，我来松松土'},
    2: {'name': '主城',
        'age': 18,
        'gender': 'male',
        'text': '天若有情天亦老，我违章者须疫苗'},
    3: {'name': '福城',
        'age': 18,
        'gender': 'female',
        'text': 'hehe，我呵呵'}
}

@app.route('/detail/<int:nid>', methods=['GET'])  # method 表示函数支持的方法
def detail(nid):
    info = USERS.get(nid)

    return render_template('detail.html', info=info)


@app.route('/index', methods=['GET'])  # method 表示函数支持的方法
def index():

    return render_template('index.html', user_dict=USERS)


@app.route('/login', methods=['GET', 'POST'])  # method 表示函数支持的方法
def login():
    # source_code: template_folder='templates'  templates为模板位置的文件夹相对目录

    if request.method == "GET":
        return render_template("login.html")
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            return redirect('http://www.luffycity.com')
        return render_template("login.html", error='用户名或密码错误')


if __name__ == '__main__':
    app.run(debug=True)

