from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for a in 'ABCDEFG':
    print(a)

print(isinstance('abcdefg', Iterable))
print(isinstance([1, 2, 3, 4], Iterable))
print(isinstance(1234, Iterable))
print(isinstance((1, 2, 3, 4), Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


def findMinAndMax(l):
    if len(l) == 0:
        min = None
        max = None
        return (min, max)
    else:
        min = max = l[0]
        for v in l:
            if min >= v:
                min = v
            if max <= v:
                max = v
        return (min, max)


print(findMinAndMax([]))
print(findMinAndMax([7]))
print(findMinAndMax([7, 1]))
print(findMinAndMax([7, 1, 3, 9, 5]))
