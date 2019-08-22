from gevent import monkey
monkey.patch_all()

import gevent

import urllib3


def f(url):
    print('GET: %s' % url)
    http = urllib3.PoolManager()
    resp = http.request('GET', url)
    data = resp.data
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'https://www.github.com/'),
])

