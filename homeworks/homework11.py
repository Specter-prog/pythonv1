# Task 1

num = [11, 3, 1, 115, 44, 153, 1213]
for i in num:
    if i % 2 == 0:
        print(i)
        break
else:
    print('No even numbers')


# Task 2

nums = [123, -12441, -1, 341, -542, 76, -761]
count = 0
while count < len(nums):
    if nums[count] < 0:
        count+=1
        continue
    print(nums[count])  
    count += 1

# Task 3

text = 'sahdajksdjkas2jdksajkdja'
count = 0
while count < len(text):
    if text[count].isdigit():
        print(count)
        break
    count += 1
else:
    print('No digits')

# Task 4

list1 = [123, 213213, 5433, 75, 23, -12, -1]
for i in list1:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        break
else:
    print('No such digit')
    
# Task 5

list1 = [2, 3, 47, 87, 92, 44, 162, 91]
summ = 0
for i in list1:
    if i % 2 != 0:
        continue
    summ += i
print(summ)
        


