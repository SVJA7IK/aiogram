import builtins
print(dir(builtins))

y = 2
def degree(x):
    return y ** x

print(degree(4))

def degree(x):
    y = 2
    return y ** x

print(degree(4))

def degree(x):
    y = 2
    def degree_two():
        return y ** x
    return degree_two()

print(degree(4))

def message(number):
    def print_message():
        return 'Число ' + str(number)
    return print_message()

print(message(78))

def message(x):
    def print_message(y):
        return x, y
    return print_message

d = message(4)
print(d(5))
print(d(8))