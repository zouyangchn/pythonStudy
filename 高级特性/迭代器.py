from collections import Iterable, Iterator

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('100', Iterable))
print(isinstance(100, Iterable))
print(isinstance((x for x in range(10)), Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('100', Iterator))
print(isinstance(100, Iterator))
print(isinstance((x for x in range(10)), Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('100'), Iterator))
# print(isinstance(iter(100),Iterator))
print(isinstance(iter((x for x in range(10))), Iterator))
