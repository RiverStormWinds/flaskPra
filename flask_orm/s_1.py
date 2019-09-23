# coding:utf-8
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/test',
                       max_overflow=0, pool_size=5)

def task(arg):
    conn = engine.contextual_connect()
    with conn:
        cur = conn.execute(
            'select * from test'
        )
        result = cur.fetchall()
        print(result)

# for i in range(20):
#     t = threading.Thread(target=task, args=(i,))
#     t.start()

if __name__ == '__main__':
    task(1)







