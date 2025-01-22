# Task 1

text = input('Напишите что-то:')
print(text.center(50))
print(text.count('а'))

# Task 2

text = input('Введите что-то:')
print(text.startswith('Привет'))
print(text.endswith('!'))
print(text.isupper())
print(text.islower())

# Task 3

text = input('Введите что-то:')
print('Тольцо цифры:', text.isdigit())
print('Только буквы:', text.isalpha())
print('Только буквы и цифры:', text.isalnum())

# Task 4

text = input('Ввдетие текст:')
print(text.replace(' ', '_'))