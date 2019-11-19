# 装饰器


def now():
    print('2015-3-25')


f = now
f()


# 2015-3-25


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


# 把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
now()

# -*- coding: utf-8 -*-
import functools


def log(test='call'):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('Begain %s %s()' % (test, fn.__name__))

            print(fn(*args, **kw))

            print('end %s %s()\n' % (test, fn.__name__))

            return fn(*args, **kw)

        return wrapper

    return metric
