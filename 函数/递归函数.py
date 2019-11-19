print('你好，师姐!')


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(998))


def fact(n, product):
    if n == 1:
        return product
    return fact(n - 1, n * product)


print(fact(998, 1))
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000
0000000000000000000000000
000000000000000000000000


def move(n, a, b, c):
    if n == 1:
        print(a, '---->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(9, 'A', 'B', 'C')
