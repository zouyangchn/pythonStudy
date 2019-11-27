import itertools

cs = itertools.cycle('ABC')
print(list(itertools.islice(cs, 0, 30, 1)))

natuals = itertools.count(1);
print(list(itertools.islice(natuals, 0, 30, 1)))
