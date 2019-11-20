



with open('E:\code\python\PycharmProjects\pythonStudy\IO编程\hello.py', 'r') as f:

    print(f.read(3))




#读文件
f = open('/Users/michael/test.txt', 'r')#一般文件
f = open('/Users/michael/test.jpg', 'rb')#二进制文件
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')#指定字符集
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')#错误处理

#需要关闭流
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
#关闭操作等价于
with open('/path/to/file', 'r') as f:
    print(f.read())

#写文件
f = open('/Users/michael/test.txt', 'w')#一般文件
f = open('/Users/michael/test.jpg', 'wb')#二进制文件
f = open('/Users/michael/gbk.txt', 'w', encoding='gbk')#指定字符集
f = open('/Users/michael/gbk.txt', 'w', encoding='gbk', errors='ignore')#错误处理

#需要关闭流
try:
    f = open('/path/to/file', 'w')
    print(f.write())
finally:
    if f:
        f.close()
#关闭操作等价于
with open('/path/to/file', 'w') as f:
    print(f.write())