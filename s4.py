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

# �൱���Ȱ�('/', method=['GET', 'POST'], endpoint='n1')ȫ�����ɲ����հ���decorator(f)����ڲ㺯������
# decorator = app.route('/', method=['GET', 'POST'], endpoint='n1')
# @decorator�﷨�����ε�index()����  -->   �൱��  index = decorator(index)
# index = decorator(index) Ҳ���ǰ�decorator(func) �����˵��ã���ִ�����ڲ�����
'''
def decorator(f):
    endpoint = options.pop('endpoint', None)
    self.add_url_rule(rule, endpoint, f, **options)
    return f
'''
# ����decorator(func)  return func ��������
# Ҳ����˵�����յ� index = index��index�����������ִ�У��������̼�������·��ӳ�䣬���뺯������û���κι�ϵ�������쳣


@app.route('/', method=['GET', 'POST'], endpoint='n1')
def index():
    pass


if __name__ == '__main__':
    app.run()

