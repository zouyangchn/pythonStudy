from io import StringIO
from io import BytesIO

#StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())



s = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    k=s.readline()
    if k == '':
        break
    print(k)

#BytesIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

a = BytesIO()
a.write('中文'.encode('utf-8'))
print(a.getvalue())

b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
c=b.read()
print(c)