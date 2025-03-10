# 1

x = '10' + 5
# Выходит ошибка TypeError так как нельзя складывать строки и числа 
# Чтобы её исправить нужно перевести строку '10' в целое число: '10' -> 10
# x = 10 + 5

# 2

numbers = [1, 2, 3]
print(numbers[5])
# IndexError - в списке numbers всего 3 индекса, а мы хотим обратиться к 5 индексу которого не существует
# мы можем обратиться к 1, 2, 3 индексу и ошибки не будет
# numbers = [1, 2, 3]
# print(numbers[0]) 

# 3

age = "25"
print(age / 5)
# TypeError 
# нельзя делить строку на число, нужно перевести строку в число '25' -> 25
# age = 25
# print(age / 5)

# 4
my_dict = {"name": "Alice", "age": 30}
print(my_dict["gender"])

# KeyError
# в словаре my_dict нету ключа gender
# my_dict = {"name": "Alice", "age": 30}
# print(my_dict["name"])

# 5

# for i in range('5'):
# print(i)
# IndentationError
# ошибка табуляции нужно 4 пробела 
# Также возникает ошибка TypeError
# так как в range не может быть строка, только число
# for i in range(5):
    #   print(i)

# 6

value = None
print(value + 10)
# TypeError
# нельзя сложить None и int
# value = 123
# print(value + 10)

# 7

a = 10
b = 0
result = a / b
print(result)

# ZeroDivisionError
# делить на ноль нельзя
# a = 10
# b = 2
# result = a / b
# print(result)