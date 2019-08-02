from flask import Flask, request
from flask_restful import Api, Resource
from flask import g
from flask import make_response
from flask import redirect
from flask import abort

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.args['data']
        return {todo_id: todos[todo_id]}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/todo/<string:todo_id>')

@app.before_first_request
def bf_first_request():
    g.string = 'before_first_request'

@app.route('/test')
def test():
    return g.string

@app.route('/res')
def index():
    response = make_response('<h1>this document carries a cookie!</h1>')
    response.set_cookie('answer', '42')

    return response

@app.route('/')
def index2():
    return redirect('/res')


user = {
        '1': {'name': 'hwk'},
        '2': {'name': 'agz'}
        }


def load_user(id):
    return user[id]


@app.route('/user/<id>')
def get_user(id):
    try:
        user = load_user(id)
        return ('<h1>Hello, %s<h1>' % user['name'])
    except:
        abort(404)


@app.route('/set_cookie')
def set_cookie():
    response = make_response('Hello World')
    response.set_cookie('Name', 'Hyman')
    return response


@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('Name')
    return name


if __name__ == '__main__':
    app.run(debug=True)



