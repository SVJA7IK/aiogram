def summa(*args):
    print(sum(args))


summa(1, 2, 3, 3, 442, 13)


def brand(**brands):
    print(brands)
    for x, y in brands.items():
        print(x, ':', y)


brand(a='Apple', s='Samsung')
