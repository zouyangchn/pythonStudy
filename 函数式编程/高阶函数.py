f = abs
print(abs(-10))
print(f(-10))
print(f)
print(abs)


def add(x, y, f=abs):
    return f(x) + f(y)


print(add(add(1, 2), add(2, 3)))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x * x


m = []
for x in map(f, l):
    m.append(x)
    print(m)
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
print(list(map(f, l)))

print(list(map(str, l)))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '123456789')))


def str2int(str):
    def f(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(f, map(char2num, str))


print(str2int('785949'))

l = ['adam', 'LISA', 'barT']


def normalize(name):
    def upFirst(s):
        if isinstance(s, str):
            return s[0].upper() + s[1:].lower()

    return map(upFirst, name)


print(list(normalize(l)))


def prod(l):
    def ff(x, y):
        return x * y

    return reduce(ff, l)


l = [3, 5, 7, 9]
print(prod(l))


def str2float(s):
    def f(x, y):
        return x * 10 + y

    n = s.index('.')
    s1 = s[:n]
    s2 = s[n + 1:]
    return reduce(f, map(int, s1)) + reduce(f, map(int, s2)) / 10 ** len(s2)


print(str2float('123.456'))


# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]


a = [1, 2, 3.4, 5]
print(a)
[1, 2, 3, 4, 5]
print(a[-1])  ###取最后一个元素
[5]
print(a[:-1])  ### 除了最后一个取全部
[1, 2, 3, 4]

print(a[::-1])  ### 取从后向前（相反）的元素
[5, 4, 3, 2, 1]
print(a[2::-1])  ### 取从下标为2的元素翻转读取
[3, 2, 1]

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序,要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
