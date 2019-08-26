# coding:utf-8

# class IntAbs(int):  # 将Int类型进行转换为绝对值类型
#     def __new__(cls, integer):
#         # 通过__new__方法进行重写父类int对象的构造方法，在构造完成之后，重写父类的__init__方法
#         if type(integer) == str:
#             integer = ord(integer)
#         else:
#             integer = abs(integer)
#         return super().__new__(cls, integer)
#
#     def __init__(self, integer):
#         # 进行父类的__init__方法重写
#         # super(PositiveInter, self).__init__(integer)
#         int.__init__(integer)
#         self.integer = integer
#
#
# i = IntAbs(-3)
# print(i, i.integer)
#
# a = IntAbs('a')
# print(a)


class IntAbs(int):
    def __new__(cls, integer):
        if type(integer) == str:
            integer = ord(integer)
        else:
            integer = abs(integer)
        return super().__new__(cls, integer)

    def __init__(self, integer):
        self.integer = integer

a = IntAbs('a')
print(a)

b = IntAbs(-3)
print(b, b.integer)

