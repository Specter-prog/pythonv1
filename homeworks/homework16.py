# try-except

# 1

try:
    num = int(input('Введите число'))
except ValueError:
    print('Введите ЧИСЛО')

# 2

num = 123
try:
    print(num2)
except NameError:
    print('Такой переменной не существует!')

# 3

num1 = int(input())
num2 = int(input())
try:
    print(num1 / num2)
except ZeroDivisionError:
    print('На ноль делить нельзя')

# 4

# while True:
#     try:
#         num1 = int(input())
#         num2 = int(input())
#     except ValueError:
#         print('Введите ЧИСЛО:')
#     else:
#         print(num1 + num2)
    
# 5

dict1 = {'name':'Erlan', 'age':'15', 'height:':179}
try:
    key = 'weight'
    value = dict1[key]
    print(value)
except:
    print('Такого ключа нет')

# 6

list1 = [1, 2, True, -123, 'text']
try:
    print(list1[7])
except IndexError:
    print('Такого элемента нет')

# 7
try:
    age = int(input())
    if age < 18:
        raise ValueError('Доступ запрещен')
except ValueError:
    print('Некорректный возраст')
else:
    print('Спасибо')
finally:
    print('До свидания')

# 8

try:
    num1 = int(input())
    num2 = int(input())
    print(num1 / num2)
except ValueError:
    print('Error')
except ZeroDivisionError:
    print('Error')

# 9

try:
    num1 = int(input())
    num2 = int(input())
    res = num1 + num2
    if res < 0:
        raise ValueError('сумма не может быть отрицателньой')
except ValueError:
    print('Ошибка')
else:
    print(res)    

# 10

num = 123
text = '3213213'
try:
    text + num
except TypeError:
    print('Unsupported option')

# Comprehension

list_comprehension = [i ** 2 for i in range(1, 10)]
list_comprehension = [i for i in range(1, 20) if i % 2 == 0]
dict_comprehension = {i:i**2 for i in range(1, 5)}

words = ["python", "java", "swift", "golang", "javascript"]
list_comprehension = [i for i in words if len(i) > 5]

words = ["apple", "banana", "cherry"]
list_comprehension = [i.upper() for i in words]