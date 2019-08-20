from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET', 'POST'])
def index():
    return "user"

