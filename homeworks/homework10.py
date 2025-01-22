# Main Task

items1 = input('Введите список товаров через запятую:').split(',')
items2 = input('Введите дополнительные товары через пробел:').split()
items1.extend(items2)
print('Ваш список:', items1)

answer = input('Хотите удалить послдений товар:')
if answer == 'да':
    items1.pop()
    print('Ваш список:', items1)
elif answer == 'нет':
    print('Ваш список', items1)

answer2 = input('Хотите развернуть список:')
if answer2 == 'да':
    items1.reverse()
    print('Ваш список', items1)
elif answer2 == 'нет':
    print('Ваш список', items1)

answer3 = input('Хотите отсоритировать список:')
if answer3 == 'да':
    items1.sort()
    print('Ваш список:', items1)
elif answer3 == 'нет':
    print('Ваш список:', items1)

print('Длина списка:', len(items1))

answer4 = input('Хотите очистить список:')
if answer4 == 'да':
    items1.clear()
    print('Ваш список:', items1)
elif answer4 == 'нет':
    print('Ваш список:', items1)
    print('Вашы товары по порядку:')
    for index, item in enumerate(items1, 1):
        print(f' {index}. {item}')

    items1[0], items1[-1] = items1[-1], items1[0]
    print('Ваш обновленный список:', items1)

    print('Ваш объедененный список:', ';'.join(items1))

# Extra tasks

# Task 1

string = input()
vowel_letters = 'аеёэиоуыэюяАЕЁЭИОУЫЭЮЯ'
res = []
for i in string:
    if i in vowel_letters:
        res.append(i)
print(len(res))

# Task 2

numbers = list(map(int, input().split()))
res = []
for digit in numbers:
    if digit % 2 == 0:
        res.append(digit)
print(res)

# Task 3
word = 'python'
text = input()
list1 = []
for i in text:
    if i in word:
        list1.append(i)
    res = ''.join(list1)
    if i not in word:
        i = '_'

