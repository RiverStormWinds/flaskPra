from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', ])
def index():
    return "hello world"


if __name__ == '__main__':
    app.__call__
    app.run()
