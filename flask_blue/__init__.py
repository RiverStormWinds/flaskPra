from flask import Flask

app = Flask(__name__)

from flask_blue.views.account import account
from flask_blue.views.order import order
from flask_blue.views.user import user

app.register_blueprint(account)
app.register_blueprint(order)
app.register_blueprint(user)

