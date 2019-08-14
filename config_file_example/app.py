from flask import Flask, request
from config_file_example.utils.message import send_msgs
app = Flask(__name__)


@app.route('/')
def index():
    data = request.query_string.get('val')
    if data == 'hwk':
        # 发送报警: 短信，邮件
        send_msgs('.....')  # 根据配置文件发送消息


if __name__ == '__main__':
    app.run()

