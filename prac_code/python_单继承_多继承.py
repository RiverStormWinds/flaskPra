# coding:utf-8

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        return "{X: " + str(self.x) + ", Y: " + str(self.y) + "}"


class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def string(self):
        return "{Width: " + str(self.width) + ", Height: " + str(self.height) + "}"


class Circle(Point, Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)  # 使用父类Point的__init__方法进行Circle自身属性的初始化
        Size.__init__(self, width, height)

    def string(self):
        return "Rectangle's init point is " + Point.string(self) + "; Size is " + Size.string(self)


circle = Circle(3, 2, 5, 7)

print(circle.string())





















