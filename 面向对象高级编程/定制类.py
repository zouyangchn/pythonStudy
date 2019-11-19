class Student(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == 'score':
            return 90
        if item == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__

    def __call__(self):
        print('My name is %s' % self.name)


print(Student('bob'))
s = Student('lily')
print(s)
print(s.name)
print(s.score)
# print(s.abc)
print(s.age())
print(s.age)
print(callable(s))
s()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                    a, b = b, a + b
            return L


for n in Fib():
    print(n)

print(Fib()[5])

print(Fib()[0:5])


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
