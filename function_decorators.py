def my_decor(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


def my_func():
    print('Тут основная функция')


my = my_decor(my_func)
my()


def my_decor(func):
    def wrapper(n):
        print('start')
        func(n)
        print('end')

    return wrapper


@my_decor
def my_func(number):
    return print(number ** 2)


my_func(10)

import time


def my_decor(func):
    def my_wr():
        start_time = time.time()
        func()
        print(time.time() - start_time)

    return my_wr


@my_decor
def sp():
    list = [i ** 2 for i in range(10000) if i % 2 == 0]
    print(list)


sp()


@my_decor
def sp():
    list = []
    for i in range(10000):
        if i % 2 == 0:
            list.append(i ** 2)
    print(list)


sp()
