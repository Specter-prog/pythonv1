'==================== Встроенные функции ==================='
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [0.1, 5.5, 10.8, 0.5]

# zipped = zip(list1, list2, list3)
# # print(list(zipped))
# for i in zipped:
#     print(i)


# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)

# enum = enumerate('hello', 12)
# print(list(enum))
# print(dict(enum))

# for num, elem in enum:
#     print(num, elem)

# map - принимает дугую функцию и последовательность (записывает в новую последователньость результат функции, в которую передается элементы последовательности)

# list1 = ['1', '2', '3', '4']
# mapped = map(int, list1) # (1, 2, 3, 4)
# print(list(mapped))

# def func(x):
#     return x ** 2

# list1 = [123, 312, 352, 12]

# mapped = list(map(func, list1))
# print(mapped)

# print(list(map(lambda x: x ** 2, [1, 2, 3])))

# filter - возвращает генератор с элементами, прошедшими фильтрацию (какое-то условие), принимает функцию и последовательность

# list1 = ['hello', 'hi', '123', '3']
# filtered = filter(str.isdigit, list1) # ('123', '3')
# print(list(filtered))

# print(list(filter(lambda x: x > 0, [23, -3, 2, -5])))
# print(list(filter(lambda x: x > 0, range(5))))

# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая фнукция должна принимать 2 аргумента)

# from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4,]))

# print(reduce(lambda x, y: x + y, ['hi', 'D', 'A', 'hello'])) #hiDAhello



'------------------------- Задачи ---------------------------'

# ZIP

# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']

# # Возведите в квадрат числа из list1
# # Сделайте строки верехним регестром в list2
# # Сделайте dict1 при помощи zip и этих двух листов

# mapped1 = list(map(lambda x: x ** 2, list1))
# mapped2 = list(map(str.upper, list2))
# dict1 = dict(zip(mapped1, mapped2))
# print(dict1)



# # Сложить поэлементно два списка чисел

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]

# list3 = list(zip(list1, list2))
# mapped = list(map(lambda x: x[0] + x[1], list3))
# print(mapped)

# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 3, 3, 0, 5]

# zipped = list(zip(list1, list2))
# print(list((map(lambda x: x[0] == x[1], zipped))))

# print(list((map(lambda x: x[0] == x[1], zip(list1, list2)))))

# print(list((map(lambda x, y: x == y, list1, list2))))

# # filter
# # Оставить в списке только строки большей длиной 5 символов

# print(list(filter(lambda x: len(x) > 5, ['hi', 'hello', 'master'])))

# Из списка слов оставить только те, которые начинаются с гласной буквы

# print(list(filter(lambda x: x[0].lower() in 'аеиуёоэяию', ['яблоко', 'груша', 'Облако'])))


# list1 = ['шалаш', 'ноутбук', 'мам', 'хакер']
# print(list(filter(lambda x: x[::-1] == x, list1)))

# from functools import reduce

# list1 = [12, 2, 3, 4]
# print(reduce(lambda x, y: x * y, list1))

# from functools import reduce

# list1 = ['hacker', 'english', 'calculus', 'guitar']
# print(reduce(lambda x, y: x + y, list1))