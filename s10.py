from flask import Flask, render_template
app = Flask(__name__)

app.config.from_object("settings.DevelopmentConfig")

def func1(arg):
    return "<input type='text' value='%s' />" % (arg)


@app.route('/')
def index():
    return render_template('s10index.html', ff = func1)


if __name__ == '__main__':
    app.run()

