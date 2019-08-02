import threading

localObj = threading.local()

def threadfunc(name):
    localObj.name = name
    print('localObj.name is %s' % name)


if __name__ == '__main__':
    t1 = threading.Thread(target=threadfunc, args=('Hyman',))
    t2 = threading.Thread(target=threadfunc, args=('LiuZhiHui',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


