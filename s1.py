from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    pass

if __name__ == '__main__':
    # run_simple(host, port, self, **options)
    # 如果有用户请求到来，则执行app的__call__方法
    # app.__call__
    app.run()

