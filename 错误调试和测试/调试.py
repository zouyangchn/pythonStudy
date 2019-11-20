
#打印
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)#用print()把可能有问题的变量打印出来看看
    return 10 / n

def main():
    foo('1')

#断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代，如果断言失败，assert语句本身就会抛出AssertionError
    return 10 / n
#程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
#$ python -O err.py（断言的开关“-O”是英文大写字母O，不是数字0。）
def main():
    foo('1')

main()


#logging
#这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。
# 同理，指定level=WARNING后，debug和info就不起作用了
import logging
logging.basicConfig(level=logging.INFO)

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


