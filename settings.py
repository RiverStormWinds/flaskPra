class Config(object):  # 相当于用于测试环境，所有的数据进行最基本的配置
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://?memory:'


class ProductionConfig(Config):  # 相当于用于生产环境，对测试环境的数据进行重写
    # DATABASE_URI = 'mysql://user@localhost/foo'  # 正式的数据库
    # SERVER_NAME = 'oldboy.com:5000'
    DEBUG = True

class DevelopmentConfig(Config):  # 开发环境
    DEBUG = True

class TestingConfig(Config):  # 测试环境
    TESTING = True
