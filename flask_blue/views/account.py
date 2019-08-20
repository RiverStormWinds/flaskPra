from flask import Blueprint, render_template

account = Blueprint('account', __name__, url_prefix='/hwk',
                    template_folder='tpls')
# 蓝图对象的名称为account，url_prefix给account蓝图下所有的url加上/hwk前缀

@account.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@account.before_request
def process_request(*args, **kwargs):
    print('before_request')

