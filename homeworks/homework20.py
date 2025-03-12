# 1

def decorator(func):
    def wrapper():
        print('Выполнение функции...')
        func()
    return wrapper

def text():
    print('text')

text = decorator(text)
text()


# 2

def decorator(func):
    def wrapper(a, b):
        c = func(a, b)
        c = 2 * c
        return c
    return wrapper

@decorator
def summ(a, b):
    c = a + b
    return c

print(summ(2, 3))


# 3

def dec(func):
    def wrap():
        res = ''.join([func(), '!'])
        return res
    return wrap

@dec
def text():
    return 'Congratulations'

print(text())


# 4

def dec(func):
    def wrapper(a, b):
        count = 0
        while count < 3:
            res = func(a, b)
            print(f'Result {count + 1} {res}')
            count += 1
        print('The function is not available anymore.')
    return wrapper

@dec
def summ(a, b):
    return a + b
summ(3, 5)


# 5

def dec(func):
    def wrap(a, b):
        print(f'Arguments: {a}, {b}')
        print(func(a, b))
    return wrap

@dec
def diff(a, b):
    return a - b

diff(3, 7)