from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'abcdefg'
# app.session_interface  -->  app.session_interface���������flask��sessionԴ��

app.config.from_object("settings.DevelopmentConfig")


@app.route('/')
def index():
    # flask���õ�ʹ�ü���cookie����������
    session['k1'] = 'v1'
    session['k2'] = 'v2'
    session.pop('k1')  # session��������ֵ䣬���Խ����ֵ����ز���


if __name__ == '__main__':
    app.run()

