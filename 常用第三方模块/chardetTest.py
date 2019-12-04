import chardet

# chardet.detect(b'Hello, world!')
# 就可以对其检测编码。用chardet检测编码，只需要一行代码：
s=chardet.detect(b'Hello, world!')
print(s)


d=data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(d))

t=data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(t))