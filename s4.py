from flask import Flask

app = Flask(__name__)

app.debug = True
app.secret_key = 'abcdefg'


'''
1. decorator = app.route('/', method=['GET', 'POST'], endpoint='n1')
    def route(self, rule, **options):
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

2. @decorator
'''

@app.route('/', method=['GET', 'POST'], endpoint='n1')
def index():
    pass


if __name__ == '__main__':
    app.run()

