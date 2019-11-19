print(1 + 2 + 3 + 4)

# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：
names = ['lily', 'luce', 'mike', 'dana']
for name in names:
    print(name)

# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 幸好Python提供一个range()函数，可以生成一个整数序列
d = range(9)
print(d)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print(list(range(101)))

sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

# 第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    print(n)
    n = n - 2
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
l = ['bart', 'lisa', 'adam', 'mike']
for name in l:
    print('hello,', name, '!')
a = len(l)
while a > 0:
    print('hello,', l[len(l) - a], '!')
    a = a - 1
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

# 在循环中，break语句可以提前退出循环。
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# 在循环中，也可以通过continue语句，跳过当前的这次循环，直接开始下一下次循环，
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
g = {'tina': 12, 'maji': 5, 'gina': 8, 'kely': 29}
print(g['tina'])
print('maji' in g)

d = {}
d['a'] = 'a'
d['b'] = 'b'
d['c'] = 'c'
d['d'] = 'd'
print(d)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
s = set([1, 2, 3, 4, 5])
print(s)
s = set([1, 2, 3, 4, 4, 4, 5, 5, 6, 6])
print(s)
sft = set(['a', 'a', 's', 'e', 'd', 'd', 'w', 'e'])
print(sft)
sft.add('a')
print(sft)
sft.remove('a')
print(sft)

a = ['b', 'c', 'a']
print(a)
a.sort()
print(a)

a = 'abc'
print(a)

print(a.replace('a', 'A'))
print(a)

x = 1
y = [2, 3]
z = (2, 3)
s = {x, z}
print(s)
s = set([1, 2, 3])
# s.add(y)
print(s)
s = {1, 2, 3}
print(s)

print("开始表演")

s = set([1, 2, 3])
print("list")
print(s)
for key in s:
    print(key)

s = set((1, 3, 3))
print("tuple")
print(s)
for key in s:
    print(key)

s = set((1, [2, 3]))
print(s)
print("tuple+list")
print(s)
for key in s:
    print(key)
