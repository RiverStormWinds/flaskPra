# coding:utf-8
from flask import Flask, render_template, g

app = Flask(__name__)

app.debug = True
app.secret_key = 'hwk'


@app.route('/')
def index():
    g.a = 'abc'
    print(g.get('a'))
    return render_template('boot.html')


if __name__ == '__main__':
    app.run()

