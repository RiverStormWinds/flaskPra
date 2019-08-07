from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdefg'

# app.config['debug'] = True  # �����������ʹ��

# app.config.from_pyfile("settings.py")  # �������Ҳ������ʹ��

app.config.from_object("settings.DevelopmentConfig")  # ʹ��settings�ļ��µ�DevelopmentConfig������������
'''
    ����from_object("settings.DevelopmentConfig")��flaskԴ��
        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
'''


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

