# Task 1

num_a = float(20.7)
num_b = int(num_a)
num_c = str(num_a)
print('Число в формате float:', num_a)
print('Число в формате int:', num_b)
print('Число в формате строки:', num_c)

# Task 2

num = float(input('Введите число:'))
division = num % 5, 1
cube = round(num ** 3, 3)
r = round(num)
print('Остаток от деления на 5:', division)
print('Число в кубе:', cube)
print('Округленное число:', r)


# Task 3

num = float(input('Введите дробное число:'))
print('Округление до 1 знака:', round(num, 1))
print('Округление до 2 знаков:',round(num, 2))

# Task 4

from decimal import Decimal

number = input('Введите дробное число:')
number2 = Decimal(number)
res = number2 + number2 + number2 + number2 + number2 + number2 + number2 + number2 + number2 + number2
data = type(res)
print(res)
print(data)