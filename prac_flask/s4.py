from flask import Flask

app = Flask(__name__)

app.debug = True
app.secret_key = 'abcdefg'


'''
def route(self, rule, **options):
    def decorator(f):
        endpoint = options.pop('endpoint', None)
        self.add_url_rule(rule, endpoint, f, **options)
        return f
    return decorator
'''

# 相当于先把('/', method=['GET', 'POST'], endpoint='n1')全部当成参数闭包进decorator(f)这个内层函数里面
# decorator = app.route('/', method=['GET', 'POST'], endpoint='n1')
# @decorator语法糖修饰的index()方法  -->   相当于  index = decorator(index)
# index = decorator(index) 也就是把decorator(func) 进行了调用，即执行了内部函数
'''
def decorator(f):
    endpoint = options.pop('endpoint', None)
    self.add_url_rule(rule, endpoint, f, **options)
    return f
'''
# 最终decorator(func)  return func 方法本身。
# 也就是说，最终的 index = index，index方法自身继续执行，整个过程即增加了路由映射，又与函数本身没有任何关系，绝妙异常


@app.route('/', method=['GET', 'POST'], endpoint='n1')
def index():
    pass


if __name__ == '__main__':
    app.run()

