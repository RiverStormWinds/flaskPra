# coding:utf-8

import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()


class User(Base):
    __tablename__ = 'users_sql'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)  # datetime.datetime.now()会直接执行这个函数，导致时间永远不变
    extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'email'),
    )

engine = create_engine('mysql+pymysql://root:root@127.0.0.1:3306/test',
                       max_overflow=0, pool_size=5)

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
