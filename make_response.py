from hello import app

from flask import make_response

@app.route('/res')
def index():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

