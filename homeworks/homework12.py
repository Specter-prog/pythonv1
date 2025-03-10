# Task 1

dict1 = {'name':'Aruzhan', 'age':'20', 'group':'IS-23'}
print(dict1['name'])
dict1['group'] = 'CS-25'
dict1['hobby'] = 'reading'
print(dict1)

# Task 2

grades = {'math': 90, 'history': 85, 'english': 88}
print(grades.get('math'))
print(grades.get('scince', 'Не найдено'))
print(grades.pop('history'))
print(grades.popitem())

dict2 = {'physycs':92}
grades.update(dict2)
print(grades)

# Task 3

keys = ['name', 'age', 'city']
dict1 = dict.fromkeys(keys, 'unknown')
dict1['name'] = 'Ali'
dict1['age'] = 25
dict1['city'] = 'Almaty'
print(dict1)

# Task 4

names = ['Али', 'Айдана', 'Ермек']
dict1 = {'Али': 3, 'Айдана': 6, 'Ермек': 5}

dict1 = dict.fromkeys(dict1, 'unknown')
dict1['Али'] = 'student'

# Task 5

user_info = {
'name': 'Диана',
'age': 22,
'city': 'Алматы',
'profession': 'дизайнер'
}

for key in user_info.keys():
    print(key)

for value in user_info.values():
    print(value)

for key, value in user_info.items():
    print(key, value)

# Task 6

products = {'apple': 50, 'banana': 30, 'cherry': 60}
for key, value in products.items():
    print(key, value * 1.1)
products['orange'] = 40

for key, value in products.items():
    if value > 50:
        print(key)

