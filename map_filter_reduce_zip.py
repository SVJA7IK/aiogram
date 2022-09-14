# Map
with open('map_filter_reduce_zip.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        print(a + b)


def f(a, b):
    return a * b


a = map(f, [2, 4, 5], [5, 6, 7])
print(list(a))

b = map(lambda x: x + 15, (2, 4, 5))
print(list(b))


# Filter
def f(a):
    if a % 2 == 0:
        return a


c = filter(f, (2, 4, 5))
print(list(c))


def f(x):
    return x % 2 == 0


c = filter(f, (2, 4, 5, 0, 10, 7))
print(list(c))

c = filter(lambda x: (x % 2 == 0), (2, 4, 5))
print(list(c))


# Reduce
from functools import reduce
print(reduce(lambda a, b: a * b, (50, 57, 89, 12, 100)))


# Zip
a = [1, 2, 3, 4, 5, 6]
b = 'abcdef'
result = zip(a, b)
print(list(result))