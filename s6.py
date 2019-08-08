# encoding:utf-8
from flask import Flask

app = Flask(__name__)

app.debug = True
app.secret_key = 'abcdefg'


@app.route('/index', methods=['GET', 'POST'], endpoint='n1', redirect_to='/index2')
def index():
    return 'hello world!'


@app.route('/index2', methods=['GET', 'POST'], endpoint='n2')
def login():
    return '登陆'


if __name__ == '__main__':
    app.run()

