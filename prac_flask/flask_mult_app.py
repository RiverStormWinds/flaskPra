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


# 使用DispatcherMiddleware进行多app路由分发
dm = DispatcherMiddleware(app1, {
    "/sec": app2
})

if __name__ == '__main__':
    # 多app应用是非常low的东西，只是通过类DispatcherMiddleware做了相关的分发，详情见源码
    run_simple("localhost", 5000, dm,)

# Flask处理请求全过程 https://www.cnblogs.com/gaoshengyue/p/8657550.html


