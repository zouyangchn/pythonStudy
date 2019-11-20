#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value



#运行单元测试
#一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：

#另一种方法是在命令行通过参数-m unittest直接运行单元测试： python -m unittest mydict_test