# coding:utf-8
'''
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    # c.send(None)  # c.send(None)启动生成器
    c.__next__()  # 由此可见，c.send(None)和c.__next__()是一样的作用
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()  # consumer()是一个生成器
produce(c)  # 将生成器传入produce函数
'''

# 代码解释：c.send(None)之后，生成器consumer接收到send(None)的预激，
# 因为没有c.send(None)发送为None，所以生成器consumer
# 只会执行到n=yield r这一步，但是不会执行n=yield r这一行，完成预激

# 如果没有c.send(None)预激过程，python则会报错：
# can't send non-None value to a just-started generator
# 不能向刚刚启动的生成器发送一个非空的值，也就是说生成器第一步必须进行预激
# 不进行预激则会报错



'''
def consumer():
    r = 0
    for i in range(3):
        yield r
        r = '200 OK' + str(i)


c = consumer()
n1 = c.__next__()
# 生成器第一次进行执行，此时r=0，yield r后，n1得到r(即得到0)，生成器停止运转
print(n1)  # 此次打印n1，0

n2 = c.__next__()
# __next__()再次启动生成器，生成器consumer随即继续运转，得到r='200 OK0'
# 然后进入for循环yield '200 OK0'，随即停止运转，n2拿到'200 OK0'，随即进行打印
print(n2)

n3 = c.__next__()
# __next__()第三次启动生成器，生成器consumer随即又一次运转，得到r='200 OK1'
# 然后进入for循环yield '200 OK1'，随即停止运转，n3拿到'200 OK1'，随即进行打印
print(n3)
'''

# 协程由生成器进行实现，最大特点就是单线程中，正在执行的方法可以随即停止切入到其他方法，
# 不用进行线程切换就实现多个方法同时执行。也被成为微线程

# -----------------------------__next__()和send()区别--------------------------
# 实际上next()和send()作用在一定意义上是相似的，区别是send(*args, **kwargs)可以进行
# 参数传递，但是next()无法进行参数传递，也就是说send(None)和next()作用是一致的


def print_num():
    for i in range(10):
        if i or i==0:
            yield i
        else:
            return

def print_word():
    word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    for j in word_list:
        if j:
            yield j
        else:
            return

def data_print():
    data_num = print_num()
    print(data_num.send(None))

    data_word = print_word()
    print(data_word.send(None))
    i = 0
    while i < 9:
        print(data_num.send(None))  # 协程取值
        print(data_word.send(None))  # 协程取值
        i = i + 1


if __name__ == '__main__':
    data_print()

