from flask import Flask


app = Flask(__name__)

app.config['SERVER_NAME'] = 'oldboyedu.com:3000'

@app.route('/', subdomain='admin')  # subdomain: 指定具体域
def static_index():
    return 'static.you-domain.tld'


@app.route('/dynamic', subdomain='<username>')
def username_index(username):
    return username + ".your-doman.tld"


if __name__ == '__main__':
    app.run()


