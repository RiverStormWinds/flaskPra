from flask import Blueprint

order = Blueprint('order', __name__)

@order.route('/order', methods=['GET', 'POST'])
def buy():
    return "order"

