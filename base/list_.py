'=====================List(списки)========================='
# списки - изменяемый, индексируемый, итерируемый тип ланных, предназначенный для хранения любых типов данных в определнном порядке

# list1 = [1, 2, 3, 2.6, [3, 4, 5], 'hi', True, False, None] 
# print(list1[0])
# print(list1[4])
# print(list1[-4])
# print(list1[4])
# print(list1[4][2])

# list2 = list('hello world')
# print(list2) # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# print(list(range(1, 10)))

# range - это функция которая создает последовательность 
# range(start, end(не включительно), step)

# print(list(range(0, 10, 9)))
# [0,1,2,3,4,5,6,7,8,9]
# [0, 2, 4, 6, 8]
# [0, 3, 6, 9]
# [0, 9]

# list2 = [1,2,3,4,5,6,7,8,9,10,11]
# print(list2)
# list2 = list(range(1, 11))
# print(list2)

'===============Методы списков======================'
#append - добавляет элемент в конец списка

# list3 = [9, 12, 'hi']
# list3.append(20)
# print(list3) # [20]
# list3.append('hi')
# print(list3) # [9, 12, 'hi', 20, 'hi']

#pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если индекс не указать то удалит последний элемент

# list4 = ['hi', 'hello', 'katana']
# a = list4.pop(10)
# print(list4)
# print(a)

# list5 = []
# list5.pop()

# remove - удаляет элемент из списка по значению
# list6 = [12, 'bishkek',342,5,6,26,3,56,34,5,3,6,2,6,3,6,45,8,0,0,0,6,4,3,8,'osh',4,5]
# list6.remove('bishkek')
# print(list6)


# list7 = [0, 1,2,4,23,12,4,0,1,6,7,0]
# count_0 = list7.count(0)
# print(count_0) # 3

# list7 = ['hello', 'hello', 'hello']
# print(list7.count('l'))


# index - возвращает индекс первого вхождения принятого элемента

list8 = ['hi', 'hi',True, False, 12, 'hi', 'good', 12, 1,4,0,0,1]
print(list8.index('hi', 2, 5)) # 0


# insert - добавляет элемент в список

list9 = ['hi', 21, 421, 'dr', True]
list9.insert(1, 'hello')
print(list9)

# extend - добавляет элементы принятого списка в первый список, изменяя его

list1 = [1, 2, 3]
list2 = [0, 0, 0]
list1.append(list2) # [1, 2, 3, [0, 0, 0]]
list1.extend(list2) # [1, 2, 3, 0, 0, 0]

list1.extend('str') 
print(list1) # [1, 2, 3, 's', 't', 'r']
list1.extend(123) # error

# reverse - изменяет список расставляя его элементы в обратном порядке
list10 = [1,2,3,4,5,6,7,8]
list11 = [1,2,3,4,5,[6,7,8]]
list10.reverse()
print(list10) # [8,7,6,5,4,3,2,1]
print(list11) # [[6,7,8], 5,4,3,2,1]

# sort - сортирует список, состоящий из элементов одного типа данных
list12 = [23, 34, 1, 4, 1, 0.5, 456, 3, 56, 3, -4]
list12.sort()
print(list12)

list13 = ['a', 'y', 'f', 'hello', 'hi', 'abc', 'A']
list13.sort(reverse=True) # key=
print(list13) 

list14 = [1,2,3]
list14.clear()
print(list14) # []

str1 = 'hello'
list1 = [23, 2, 1, 4, 0]

print(len(str1)) # 5
print(len(list1)) # 6

a = 15
b = 20
a, b = [15, 20]

# name, age, prof = ['Katana', 21, 'Dev']

meshok = ['luk', 'kartoshka', 'ogutec', 'pomidor']

print(meshok[0])
print(meshok[1])
print(meshok[2])
print(meshok[3])

for ruka in meshok:
    print(ruka)



list15 = [True, 'hi', 10, False, -5, 0.5, [1,2,3]]
for i in list15:
    print(i)

# итерация - процесс прохождения по элементам последовательности (итерируемого объекта)

for i in 'hello world':
    print(i.upper()*5)

str1 = 'hello world'
print(str1.split(',')) # ['hello', 'world' ...] str -> list


list1 = ['a', 'b', '12', 'c']
print('*'.join(list1)) # a*b*12*c  list -> str


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)

