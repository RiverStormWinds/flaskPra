# coding:utf-8
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/test',
                       max_overflow=0, pool_size=5)

def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute('select * from shop')
    result = cursor.fetchall()
    print(result)


if __name__ == '__main__':
    # conn = pymysql.connect('127.0.0.1', 'root', 'root', 'test', charset='utf8')
    # cursor = conn.cursor()
    task(1)






