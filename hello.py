from flask import Flask, request
from flask_restful import Api, Resource
from flask import g


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


api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)

