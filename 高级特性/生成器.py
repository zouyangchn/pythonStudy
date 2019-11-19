l = [x * x for x in range(10)]
print(l)

g = (x * x for x in range(10))
for n in g:
    print(n)
print(g)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)


def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fibg(6)
print(next(f))
print(next(f))
print(next(f))
print("接着循环")
for x in f:
    print(x)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5


o = odd()
print(next(o))
print(next(o))
print(next(o))


# print(next(o))

def fibw(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


w = fibg(6)
while True:
    try:
        x = next(w)
        print('w', x)
    except StopIteration as e:
        print('return', e.value)
        break


# 这就是对杨辉三角的生成方式的理解，一般人（例如我）看就是上一行的数两两相加，
# 然后得到下一行的数再在首尾添个1；这个思路则是认为对上一行的数首尾添0然后再
# 两两相加，再利用下标为-1是最后一个元素的这个python的特点来实现只添加一个0。
# 这个程序对Python的下标运用确实很有启发。
def triangles(max):
    l = [1]
    n = 1
    while n < max:
        yield l
        l.append(0)
        n = n + 1
        l = [l[i - 1] + l[i] for i in range(n)]


a = triangles(100)
for x in a:
    print(x)


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
