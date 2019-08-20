from flask import Blueprint, render_template

account = Blueprint('account', __name__, url_prefix='/hwk',
                    template_folder='tpls')
# ��ͼ���������Ϊaccount��url_prefix��account��ͼ�����е�url����/hwkǰ׺

@account.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@account.before_request
def process_request(*args, **kwargs):
    print('before_request')

