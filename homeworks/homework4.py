# Task 1

print('Hello\nworld\n!')

print('python!\rPY')

# Task 2

name = input('Введите ваше имя:')
age = int(input('Введите ваш возраст:'))
print(f'Меня зовут {name}, мне {age} лет.')
print('Меня зовут {}, мне {} лет.'.format(name, age))
message = 'Меня зовут %s, мне %s лет.'
print(message % (name, age))

# Task 3

full_name = input('Введите ваше имя и фамилию:')
print(full_name.upper())
print(full_name.lower())
print(full_name.swapcase())
print(full_name.capitalize())
print(full_name.title())