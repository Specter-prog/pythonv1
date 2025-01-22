# Task1

list1 = [73, 'text', True, [5, 12, 1], None]
print(list1[0])
print(list1[-1])
print(list1[3][2])

# Task2

list1 = [1, 3, 5, 6, 11, 523]
list2 = list1.append('str')
list3 = list1.pop(list1[1])
list4 = list1.remove(list1[5])

# Task3

list1 = ['apple', 'pear', 'apple', 'banan', 'apple']
print(list1.count('apple'))

list2 = [123, 0, 312312, 0, 342342, 0, 0, 0]
print(list2.count(0))

# Task4

list1 = ['a', 'b', 'c', 1, 2, 3, 'b']
print(list1.index('b', 3, 6))

# Task 5

nested_list = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(nested_list[2][0])
print(nested_list[0][-1])