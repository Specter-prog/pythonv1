#  Task 1

first_name = 'Аман'
last_name = 'Абдылдаев'
res = last_name + ' ' + first_name
print('Привет!\n', 'Меня зовут:', res)

#  Task 2

from math import sqrt

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
num3 = int(input('Введите третье число:'))

print('Квадратный корень из первого числа:', sqrt(num1))
print('Квадратный корень из второго числа:', sqrt(num2))
print('Квадратный корень из третьего числа:', sqrt(num3))

# Task 3

power_1 = pow(3, 4)
power_2 = pow(5, 7, 6)
print('Число 3 в степени 4:\tОстаток от деления числа 5 в степени 7 на 6:')
print(power_1,'\t\t\t',power_2)

# Task 4

number1 = int(input('Введите делимое:'))
number2 = int(input('Введите делитель:'))
print('Целая часть и остаток от деления числа', number1, 'на', number2,':', divmod(number1, number2))