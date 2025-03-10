names = ['Nikita', 'Katana', 'Toma']
ages = [25, 30, 35]
names_ages = dict(zip(names, ages))
print(names_ages)

# 2

text = 'python'
new_text = enumerate(text, 1)
for i in new_text:
    print(i)

# 3

numbers = ["10", "20", "30", "40"]
print(list(map(int, numbers)))

# 4

words = ["apple", "banana", "cherry", "dog", "elephant"]
print(list(filter(lambda word: word.startswith('d'), words )))

# 5

numbers = [1, -2, 3, -4, 5, -6]
pos_numbers = list(filter(lambda num: num > 0, numbers))
square_numbers = list(map(lambda num: num ** 2, pos_numbers))
print(square_numbers)

# 6

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

students_grades = list(zip(students, scores))
grade_80 = list(filter(lambda x: x[1] > 80, students_grades))

numbered_list = list(enumerate(grade_80, 1))
print(numbered_list)