def test():
    for i in range(3):
        yield i


a = test()
print(next(a))
print(next(a))
print(next(a))
for i in test():
    print(i)


a = iter("test")
print(next(a))
print(next(a))
print(next(a))
print(next(a))

a = iter("test")
for i in a:
    print(i)

def test_two():
    yield from [1, 2, 3]

for i in test_two():
    print(i)

def test_two():
    yield from [x for x in range(20)]

for i in test_two():
    print(i)


def test_two():
    print("started")
    while True:
        yield 1
        yield 2

a = test_two()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


def test():
    print("started")

    while True:
        x = yield
        print("recv:", x)


a = test()
print(next(a))
print(next(a))
a.send("test")