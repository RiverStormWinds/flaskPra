from flask import Flask, make_response
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route('/')
def index():
    return ('<h1>Hello World</h1>')

@app.route('/user/<name>')
def user(name):
    return ('<h1>Hello, %s!</h1>' % name)

@manager.command
def print_str():
    print('hello world')

@app.route('/set_cookie')
def set_cookie():
    response = make_response('Hello World')
    response.set_cookie('Name', 'Hyman')


if __name__ == '__main__':
    manager.run()

