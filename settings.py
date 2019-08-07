class Config(object):  # �൱�����ڲ��Ի��������е����ݽ��������������
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://?memory:'


class ProductionConfig(Config):  # �൱�����������������Բ��Ի��������ݽ�����д
    DATABASE_URI = 'mysql://user@localhost/foo'  # ��ʽ�����ݿ�


class DevelopmentConfig(Config):  # ��������
    DEBUG = True

class TestingConfig(Config):  # ���Ի���
    TESTING = True
