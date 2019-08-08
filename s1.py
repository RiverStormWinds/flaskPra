from flask import Flask

app = Flask(__name__)

app.debug = True
app.secret_key = 'abcdefg'

@app.route('/')
def index():
    return 'hehe'

if __name__ == '__main__':

    app.run()

