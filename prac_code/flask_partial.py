# coding:utf-8
from flask.globals import _request_ctx_stack
from functools import partial


def _lookup_req_object(name):
    top = _request_ctx_stack.top
    if top is None:
        raise RuntimeError("不存在")
    return getattr(top, name)


class Foo(object):
    def __init__(self):
        self.xxx = "hehe"


_request_ctx_stack.push(Foo())
# print(_request_ctx_stack.top)
req = partial(_lookup_req_object, "xxx")
print(req())
_request_ctx_stack.pop()

 