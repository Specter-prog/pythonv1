# условные конструкции

# Task 1

time = int(input('Введите часы:'))
if time >= 6 and time <= 11:
    print('Утро')
elif time >= 12 and time <= 17:
    print('День')
elif time >= 18 and time <= 21:
    print('Вечер')
elif time >= 22 or time <= 5:
    print('Ночь')

# # Task 2

price = int(input('Введите цену товара:'))
age = int(input('Введите возраст:'))
if age < 18:
    print('Скидка 10%:', price * 0.9)
elif age >= 18 and age < 60:
    print('Скидки нет:', price)
elif age >= 60:
    print('Скидка 20%:', price * 0.8)

# # Task 3

a = int(input('Введите длину первой стороны треугольника:'))
b = int(input('Введите длину второй стороны треугольника:'))
c = int(input('Введите длину третьей стороны треугольника:'))

if a == b == c:
    print('Треугольник - равносторонний')
elif a == b or b == c or a == c:
    print('Треугольник - равнобедренный')
else:
    print('Треугольник - разносторонний')

# Тернарный оператор 

# Task 1

num = int(input('Введите число:'))
res = 'Четное' if num % 2 == 0 else 'Нечетное'
print(res)

# # Task 2

temp = int(input('Введите температуру:'))
res = 'Холодно' if temp < 15 else 'Тепло'

# Calculator

num1 = int(input('Введите первое число:'))
num2 = int(input('Введите второе число:'))
operation = input('Выберите действие:\n + (сложение) \n - (вычитание) \n * (умножение) \n / (деление) \n // (целочисленное деление) \n % (остаток от деления) \n ** (возведение в степень)')
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/' and num2 == 0:    
    print('Ошибка')
elif operation == '//' and num2 == 0:
    print('Ошибка')
elif operation == '/' and num2 != 0:
    print(num1 / num2)
elif operation == '//' and num2 != 0:
    print(num1 // num2)
elif operation == '%' and num2 == 0:
    print('Ошибка')
elif operation == '%' and num2 != 0:
    print(num1 % num2)
elif operation == '**':
    print(num1 ** num2)
else:
    print('Error')
