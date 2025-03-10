dict1 = {'+':lambda x, y: x + y, '-':lambda x, y: x - y, '*':lambda x, y: x * y, '/':lambda x, y: x / y}
while True:
    x = int(input('Enter a first number:'))
    y = int(input('Enter a second number:'))
    operation = input('+, -, *, /\n')
    if operation in dict1:
        try:
            print(dict1[operation](x, y))
        except ZeroDivisionError:
            print('Error')