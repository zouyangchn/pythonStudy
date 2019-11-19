def power(x, n=2):
    sum = 1
    while n > 0:
        n = n - 1
        sum = sum * x
    return sum


print(power(4, 2))


def enroll(name, gender, age=6, city='beijing'):
    print('name：', name)
    print('gender：', gender)
    print('age：', age)
    print('city：', city)


print(enroll('xiaohong', '男'))
enroll('lily', '女')
enroll('lisa', '女', 7)
enroll('olify', '男', city='上海')


def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc((1, 2, 3, 4, 5)))
print(calc([1, 2, 3, 4, 5]))


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3, 4, 5))
print(calc(*[1, 2, 3, 4, 5]))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('bob', 23, city='shenzheng', gender='M')
extra = {'city': 'beijing', 'job': 'engineer'}
print(extra['city'])
print(extra['job'])
person('lili', 18, city=extra['city'], job=extra['job'])
person('mary', 19, **extra)


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('jak', 23, city='shanghai', addr='chenggong', zipcode=123456)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('jak', 13, city='beijing', job='engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('bob', 23, city='shanghai', job='singer')
extra = ['M', '123@qq.com']
person('liya', 18, *extra, city='shenzheng', job='hhhh')


def person(name, age, *, city='beijing', job):
    print(name, age, city, job)


person('nill', 23, job='java')


def f1(name, age=18, *args, **kw):
    print('name:', name, 'age:', age, 'args:', args, 'kw:', kw)


f1('zera', 23, 'w', 'l', city='beijing', job='singer')


def f2(name, age=18, *args, email, **kw):
    print('name:', name, 'age:', age, 'args:', args, 'email:', email, 'kw:', kw)


f2('zouyang', 25, 'java', 'python', email='123@qq.com', city='shanghai', job='engineer')


def product(*numbers):
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum


def product(*args):
    if len(args) == 0:
        raise TypeError('bad operand type')
    sum = 1
    for n in args:
        sum = sum * n
    return sum


print(product(5))
print(product(5, 6))
print(product(5, 6, 7))
print(product(*(5, 6, 7, 8)))
print(product(5, 6, 7, 9))
