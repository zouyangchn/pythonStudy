import types


class Animal(object):
    def run(self):
        print('Animal is running...')

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


class Dog(Animal):
    def run(self):
        print('dog is running...')

    def __init__(self):
        pass


class Husky(Dog):
    def run(self):
        print('Husky is running...')

    def __init__(self):
        pass


print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
animal = Animal('dog', 4)
print(type(animal))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

a = Animal('a', 2)
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Husky))

print(type([1, 2, 3]))
print(isinstance([1, 2, 3], (list, tuple)))
print(type((1, 2, 3)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir(123))
print(dir('abc'))
print(len('abc'))
print('abc'.__len__())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.X


obj = MyObject()

print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 12)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
