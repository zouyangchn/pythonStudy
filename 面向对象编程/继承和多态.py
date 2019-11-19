# 继承和多态
class Animal(object):
    def run(self):
        print('Animal is running ......')


def run_twice(animal):
    animal.run()
    animal.run()


class Dog(Animal):
    def run(self):
        print('Dog is running ......')


class Cat(Animal):
    def run(self):
        print('Cat is running ......')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer(object):
    def run(self):
        print('start...')


animal = Animal()
dog = Dog()
cat = Cat()
tortoise = Tortoise()
animal.run()
run_twice(animal)
dog.run()
run_twice(dog)
cat.run()
run_twice(cat)
run_twice(tortoise)
run_twice(Timer())
