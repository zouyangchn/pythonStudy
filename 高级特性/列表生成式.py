import os

k = list(range(1, 11))
print(k)
l = []
for x in (range(1, 11)):
    l.append(x * x)
print(l)

# 生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print([x * x for x in (range(1, 11))])

print([x * x for x in (range(1, 11)) if x % 2 == 0])

# 以使用两层循环，可以生成全排列
print([m + n for m in 'abcde' for n in 'ABCDE'])

print([d for d in os.listdir('H:\\')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'a': 'A', 'b': 'B', 'c': 'C'}
for k, v in d.items():
    print(k, '=', v)
# 列表生成式也可以使用两个变量来生成list：
print([k + '=' + v for k, v in d.items()])

l = ['Java', 'Php', 'Python', 'China']
print([s.lower() for s in l])
print([s for s in l])
print([s.upper() for s in l])

l1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [s.lower() for s in l1 if isinstance(s, str)]
print(l2)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [k.lower() for k in L1 if isinstance(k, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
