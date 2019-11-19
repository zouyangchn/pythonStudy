from PIL import Image


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# >>> f = lazy_sum(1, 3, 5, 7, 9)
# >>> f
# <function lazy_sum.<locals>.sum at 0x101c6ed90>

# 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()


# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。你可能认为调用f1()，f2()和f3()结果应该是1，4，9，全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

import sys

print(sys.path)

import numpy

print(numpy.str)

im = Image.open("E:\code\python\图片\AMD-Ryzen.jpg")
im.thumbnail((200, 100))
im.save('thumb1.jpg', 'JPEG')
print()
