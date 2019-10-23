# coding:utf-8

import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='root',
                 database='test', port=3306, charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)

cursor.execute('select * from shop')

result = cursor.fetchall()

for i in result:
    for k in i:
        print(k, i[k])


