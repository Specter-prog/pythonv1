'=================Dict(словари)======================'
# dict - изменяемый, итерируемый, 'неупорядоченный', неиндексируемый тип данных, для хранения данных в парах (ключ:значение)

# user = {
#     'name':'Katana', 
#     'age':21, 
#     'prof':'Dev'
#     }

# print(user['name']) # Katana

# ключами в словаре могут быть только не изменяемые типы данных
# если в словаре есть одинаковые ключи то сохранится последний

# dict1 = {'a':1, 'b':2, 'c': 3, 'a':4}
# print(dict1) # {'a':4, 'b':2, 'c': 3}

# print(dict1['f']) # KeyError 'f'

'=================Создание====================='
# user = {'a':1, 'b':2}

# user = dict([('a', 1), ('b', 2), ('c', 3)])


# list1 = ['ab', 'cd', 'ef']
# dict1 = dict(list1) # {"a":"b", "c":"d", "e":"f"}

# dict1 = {'prof':'dev'}
# dict1['name'] = 'Katana'
# dict1['age'] = 21
# dict1['prof'] = 'artist'
# # {"prof":"artist", "name":"Katana", "age":21}


'===================Методы словаря====================='
# get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение
user = {
    'name':'katana',
    'age':21,
    'prof':'dev'
}
# print(user.get('namsdfsdf', 'Такого ключа нет')) # Такого ключа нет

# pop - удаляет пару по ключу и возвращает значение
# num = user.pop('age') # 21
# print(num)

# popitem - удаляет последнюю пару и возвращает ее
# dict1 = {'a':1, 'b':2}
# num = dict1.popitem() # ('b', 2)
# print(num)

# update - расширяет словарь парами из второго словаря
# dict1 = {1:'a', 2:'b'}

# dict2 = {2:'c', 4:'d'}

# dict1.update(dict2)
# print(dict1) # 


#fromkeys - метод для создания нового словаря, используя список ключей
# dict1= dict.fromkeys('hi', 12)
# print(dict1)

# dict2= dict.fromkeys([10,20,30], 'hello')
# print(dict2)


user = {1:'a', 2:'b'}
# keys - возвращает все ключи - dict_keys([1,2])
# values - возвращает все значения - dict_values(['a','b'])
# items - возвращает все пары - dict_items([(1, 'a'), (2,'b')])
# print(user.keys())
# print(user.values())
# print(user.items())

# print(dir(dict))

'==================Итерирование словарей====================='
user = {
    'name':'katana',
    'age':21,
    'prof':'dev'
}

a, b = 3, 5


for key, values in user.items(): #('name', 'katana')
    print(key, values) 



# вам дан словарь
dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
#dict2 = {1:"a", 2:"b", 3:"c"}

