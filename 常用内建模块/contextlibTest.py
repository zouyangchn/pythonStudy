


#在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally：
try:
    f = open('test', 'r')
    a=f.read()
    print(a)
finally:
    if f:
        f.close()

#Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为
with open('test' ,'r') as f:
    a=f.read()
    print(a)


# class Query(object):
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print('Begin')
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     a=q.query()
#     #print('Query',a)

from contextlib import contextmanager
class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("hello")
    print("world")

# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。



from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

#closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：1
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

