# Генератор списка
list = [x for x in range(0, 20) if x % 5 == 0]
print(list)

list = [(i, j) for i in range(1, 21) for j in range(1, 51)]
print(list)

list = [i ** 2 if i > 0 else i ** 3 for i in range(-10, 11) if i % 2 == 0]
print(list)

# Генератор множества
s = [7, 8, 8, -10, -10]
set_set = {i for i in s}
print(set_set)

# Генератор словаря
dictionary = {i: i ** 10 for i in s}
print(dictionary)