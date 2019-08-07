from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'abcdefg'

# app.config['debug'] = True  # 这种情况不会使用

# app.config.from_pyfile("settings.py")  # 这种情况也不经常使用

app.config.from_object("settings.DevelopmentConfig")  # 使用settings文件下的DevelopmentConfig开发环境配置
'''
    解析from_object("settings.DevelopmentConfig")的flask源码
        module_name, obj_name = import_name.rsplit(".", 1)
        module = __import__(module_name, globals(), locals(), [obj_name])
'''


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

