# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


import functools

int2 = functools.partial(int, base=2)
a = int2('1000000')
print(a)
# 64
b = int2('1010101')
# 85
print(b)
