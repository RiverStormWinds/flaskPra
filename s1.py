from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    pass

if __name__ == '__main__':
    # run_simple(host, port, self, **options)
    # ������û�����������ִ��app��__call__����
    # app.__call__
    app.run()

