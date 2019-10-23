from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'abcdefg'
# app.session_interface  -->  app.session_interface从这里进入flask的session源码

app.config.from_object("settings.DevelopmentConfig")


@app.route('/')
def index():
    # flask内置的使用加密cookie来保存数据
    session['k1'] = 'v1'
    session['k2'] = 'v2'
    session.pop('k1')  # session本身就是字典，可以进行字典的相关操作


if __name__ == '__main__':
    app.run()

