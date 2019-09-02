# coding:utf-8

class SqlHelper(object):  # 模拟一个sql连接执行关闭的功能类

    def open(self):
        pass

    def fetch(self):
        pass

    def close(self):
        pass

    def __enter__(self):  # 在__enter__方法中将数据库连接打开并返回SqlHelper对象
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


with SqlHelper() as obj:  # 使用with再类的前面，也就意味着自动执行类的__enter__方法，obj也是__enter__方法的返回值
    obj.fetch()
    # fetch()之后，自动执行类的__exit__方法，我们直接在__exit__方法中进行close()即可完成数据库连接的上下文处理


# 以后如果遇到源码里面有：打开 -- 执行 -- 关闭这个流程的代码，一般都会使用这种with方法进行执行
