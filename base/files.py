# '============Модули и пакеты============'
# # любой файл с расширением '.py' - модуль

# # пакет - набор модулей (обязательно должен быть файл __init__.py)

# '=============Работа с файлами========='
# # open - функция, которая открывает файл в определенном режиме
# 'режимы'

# # r - read(только для чтения)
# # w - write(только для записи, каждый раз когда вы открываете файл в режиме записи то что было внутри очищается)
# # a - append(только для дозаписи, добавляет в конец)
# # x - создает файл, но если такой есть то выйдет ошибка
# # b - binary (в бинарном виде)

# '------------Read------------'
# file = open('test.txt', 'r')
# # print(file.read())
# # file.seek(0) # перенос каретки на 0 символ
# # print(file.read())
# # print(file.writable())
# # print(file.readable())
# # print(file.read(3))
# # print(file.read(3)) 

# # file.seek(0)
# # print(file.readlines()) # читает каждую строку и возвращает список со строками
# # file.seek(0)
# # print(file.readline())

# # print(file.tell())

# # file.close()
# # print(file.closed)


# print(file.readline(5))
# # print(file.readline(5))


# import random

# list1 = ['Adilet', 'Ali', 'Emir', 'Beknur', 'Zhanuzak', 'Umar', 'Tima', 'Aiperi', 'Laura', 'Kanykei', 'Iskender']

# for i in [1,2,3]:
#     index = random.randint(0,10)
#     print(list1[index])


'--------------------Write----------------------'
# file = open('test.txt', 'w')
# если файла нет - создаст его

# file.write('HELLOWORLD\nPython')

# print(file.writable())
# file.read()
# print(file.readable())

# file.writelines(['hello\n', 'world\n', 'metalabs'])

# file.close()

# write - очищает файл и записывает строки, принимает строку
# writelines - очищает файл и записывает строки, принимает лист со строками 

'----------------append-----------------'
# file = open('test.txt', 'a')

# file.write('\nNew line')
# file.writelines(['sdasd', 'adfgsh])
# file.close()

# write -  дозаписывает строки в конец, принимает строку
# writelines - дозаписывает строки в конец, принимает лист со строками 

'------------Контекстный менеджер----------------'

# file = open('test.txt' 'r')
# file.close()


# with open('test.txt', 'r') as file:
#     print(file.closed)
#     print(file.read())
#     file.read()
# # file.close()
# print(file.closed)
# print('hi')


with (open('test.txt', 'w+') as file1, open('test1.txt') as file2):
    file1.write('hi')
    file1.seek(0)
    print(file1.read())