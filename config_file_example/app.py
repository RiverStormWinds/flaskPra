from flask import Flask, request
from config_file_example.utils.message import send_msgs
app = Flask(__name__)


@app.route('/')
def index():
    data = request.query_string.get('val')
    if data == 'hwk':
        # ���ͱ���: ���ţ��ʼ�
        send_msgs('.....')  # ���������ļ�������Ϣ


if __name__ == '__main__':
    app.run()

