# from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import current_app, Flask

app1 = Flask("app1")
app2 = Flask("app2")


@app1.route("/index")
def index():
    print(current_app)
    return "app1"


@app2.route("/index2")
def index():
    print(current_app)
    return "app2"


# ʹ��DispatcherMiddleware���ж�app·�ɷַ�
dm = DispatcherMiddleware(app1, {
    "/sec": app2
})

if __name__ == '__main__':
    # ��appӦ���Ƿǳ�low�Ķ�����ֻ��ͨ����DispatcherMiddleware������صķַ��������Դ��
    run_simple("localhost", 5000, dm,)

# Flask��������ȫ���� https://www.cnblogs.com/gaoshengyue/p/8657550.html


