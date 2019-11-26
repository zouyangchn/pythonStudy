import os

print(os.name)
print(os.environ)
print(os.environ.get('COMPUTERNAME' ))
print(os.environ.get('PATH' ))

print(os.path.abspath('.'))

r=os.path.join('E:\code\python\PycharmProjects\pythonStudy\IO编程','test')
print(r)
os.mkdir(r)
os.rmdir(r)

s=os.path.join('E:\code\python\PycharmProjects\pythonStudy\IO编程','hello.py')

t=os.path.split(s)
u=os.path.splitext(s)

print(t)
print(u)

#os.rename('test.text','text.text')
#os.remove('text1.text')
