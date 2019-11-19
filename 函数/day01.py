print('hello world!')
print('i\'m ok.')
print('i\'m learning\npython')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(r'''hello,\n
world!''')
age = 22
if age >= 18:
    print('adult')
else:
    print('teenager')

a = 123
print(a)
a = 'abc'
print(a)
x = 2
x = x + 2
print(x)

f = 'ABC'
g = f
f = 'XYZ'
print(g)
print(f)
PI = 3.14
print(PI)
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(10 % 3)

a = 123
print('n =', a)
a = 456789
f = a / 100
print('f=', a / 100)
print(ord('a'))
print(chr(66))
print('\u4e2d\u6587')
print(1 + 3)
s1 = 72
s2 = 85
print('小明的成绩提升了', (s2 - s1) / s1 * 100, '%')
r = (s2 - s1) / s1 * 100
print('小明的成绩提升了：%.1f%%' % r)
s3 = 61
s4 = 95
r = (s4 - s3) / s3 * 100
print('去年{0}的成绩为{1}，今年{2}的成绩为{3},成绩提升了{4:.2f}%'.format('小明', s3, '小明', s4, r))
print('去年 %s 的成绩是 %d ,今年的成绩是 %d ,今年的成绩比去年提高了 %d %%' % ('小明', s3, s4, r))
l = [['apple', 'google', 'microsoft'], ['java', 'php', 'python'], ['adam', 'bart', 'lisa']]
print(l[0][0])
print(l[1][2])
print(l[2][2])

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

birth = input('birth:')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')

h = 1.75
w = 80.5
bmi = w / (h * h)
if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('feipang')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')
