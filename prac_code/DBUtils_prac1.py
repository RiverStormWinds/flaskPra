# coding:utf-8
from DBUtils.PersistentDB import PersistentDB
import pymysql


"""
DBUtils第一种连接处理方式，即为每一个连接过来的线程进行创建数据库的cursor
"""
POOL = PersistentDB(
    creator=pymysql,  # 使用数据库的模块
    maxusage=None,  # 一个连接被重复使用的次数，None表示无限次使用
    setsession=[],  # 开始会话前执行的命令列表，如: ["set datestyle to ...", "set time zone ..."]
    ping=0,  # ping MySQL服务器检查服务是否可用，0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    closeable=False,  # 如果为False时，conn.close()被忽略，无法关闭连接，如果为True，conn.close()则为关闭连接，再次使用pool.connection时候，则会报错
    threadlocal=None,  # 本地线程独享值对象，相当于threading.local()
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='pooldb',
    charset='utf8'
)

def func():
    conn = POOL.connection(shareable=False)
    cursor = conn.cursor()
    cursor.execute('select * from tbl')
    result = cursor.fetchall()
    cursor.close()
    conn.close()


func()
