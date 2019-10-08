# coding:utf-8

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
import models

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/test',
                       max_overflow=0, pool_size=5)

Session = sessionmaker(bind=engine)

# 从连接池获取连接
# session = Session()
session = scoped_session(Session)

# 执行orm操作
obj = models.User(name='alex2', email='alex2@qq.com')
session.add(obj)
session.commit()

# 关闭数据库连接(将连接放回连接池)
session.close()
