# coding:utf-8
import pymysql
from DBUtils.PooledDB import PooledDB


"""
DBUtils第二种连接处理方式，即建立一个连接池，线程请求过来通过连接池进行分发cursor
"""
POOL = PooledDB(
    creator=pymysql,  # 使用数据库的模块

    maxconnections=6,  # 连接池允许的最大连接数量
    mincached=2,  # 初始化时，连接池至少创建的空闲连接，0表示不创建
    maxcached=5,  # 连接池中对多共享的连接数量，0和None表示全部共享。ps：无用，因为pymysql和MySQLdb等模块的threadsafety都为1，所有值无效，为全部共享
    blocking=True,  # 连接池中如果没有可用连接之后，是否阻塞等待，True表示等待，False表示不等待然后报错

    maxusage=6,  # 一个连接被重复使用的次数，None表示无限次使用
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
