# Task 1

10 > 5 and 3 == 3 # True 
5 < 3 or 2 >= 2 # True
not (4 != 4) # True
(2 < 5) and (5 > 10) # False
(7 >= 7) or (3 < 2 and 8 != 8) # True

# Task 2

bool(0) # False
bool(1) # True
bool(-100) # True
bool("") # False
bool(" ") # True
bool(None) # False

# Task 3.1

x = None 
y = None 
print(x is y) # True

# Task 3.2

a = 1000
b = 1000
print(id(a) == id(b)) # True

x = 5
y = 5
print(id(x) == id(y)) # True

# id() - позволяет узгать идентификационный номер значения
# is - сравнивает id, а == сравнивает значения переменных 

# Task 3.3

x = int(input('Введите число:'))
if x > 0:
    print(f'{x} положительное число')
elif x < 0:
    print(f'{x} отрицательное число')
else:
    print('Число равно 0')


