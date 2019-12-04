import itertools

#“无限”迭代器：
#count()
#cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
print(list(itertools.islice(cs, 0, 30, 1)))

natuals = itertools.count(1);
print(list(itertools.islice(natuals, 0, 30, 1)))


#cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
cs='abc'
for c in cs:
    print(c)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for c in ns:
    print(c)


natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
r = itertools.chain('ABC', 'XYZ')
print(list(r))
for c in itertools.chain('ABC', 'XYZ'):
   print(c)



#groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
     print(key, list(group))

print('不区分大小写')
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
     print(key, list(group))

