from flask import Flask, globals, request

app = Flask(__name__)


@app.route('/', methods=['GET', ])
def index():
    return "hello world"


@app.before_request
def before_hello():
    print("hello world")


if __name__ == '__main__':
    # app.__call__
    print(request)
    app.run()

