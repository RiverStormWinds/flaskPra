# coding:utf-8

class FuncFile(object):
    def __init__(self):
        pass

    def cs(self):
        print('hello world')


func_file = FuncFile()


def run():
 while True:
    cs=input('请输入要访问的URL：')
    #hasattr利用字符串的形式去对象（模块）中操作（寻找）成员
    if hasattr(func_file,cs):            #判断用户输入的URL是否在func_file模块中
        getattr(func_file,cs)()       #有则将func_file模块下的cs函数赋值
        # func()                           #等同于执行func_file模块下的cs函数
    else:
        print('404')#定义错误页面
run()

