import random

# list -> to string
# letters = ['a', 'b', 'c', 'd']
# print("".join(letters).isalpha())

#  # swap
# letters[0], letters[2] = letters[2], letters[0]
# print(letters)

# mutable
# immutable

numbers = [10, 2, -1, 4]
print(numbers)

numbers[0] = 999  # mutable
numbers.remove(2)
print(numbers)

str1 = "word"
str1 = str1 + "!"  # immutable -- creates a new string
print(str1[4])  # can access, read
# str1[4] = "$"  # ERROR, cannot modify, because its immutable

numbers.insert(2, 444)
print(numbers)

# create an empty grades list
# input grade until got -999, ignore grades not between 0-100
# add each grade to the grades list

'''
grades: list[int] = []
while True:
    grade = int(input("enter grade [-999 to exit]:"))
    if grade == -999:
        break
    if grade < 0 or grade > 100:
        continue
    grades.append(grade)

if len(grades) > 0:
    print('max', max(grades))
    print('min', min(grades))
print('sum', sum(grades))
print('len', len(grades))

import statistics
if len(grades) > 0:
    print(f"avg = {sum(grades) / len(grades):.2f}")
    print('avg statistics', statistics.mean(grades))
'''

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list_both = list1 + list2
print(list_both)
list1.extend(list2)
print(list1)
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1 = list1 + list2

# remove -- values
# pop -- index --> show value
del list1[0]
print(list1)

list1.clear() # -- deletes all items

grades = [90, 99, 80, 70, 100, 100]
backup = grades.copy()  # shallow
grades.clear()
print('grades', grades)
print('backup', backup)

x = 1
y = x
y += 1
print(x)

a = "aaa"
b = "aaa"
b = b + "!"
print(a)
print(b)

#         0   1    2   3   4    5   6
list1 = [90, 80, 100, 55, 90, 100, 90]
print(list1.index(90))  # 0

# find how many times 90 appears
# add all 90 index into a list
# 3
# [0, 4, 6]
indexes = []

#           0   1    2   3   4    5   6
# list1 = [90, 80, 100, 55, 90, 100, 90]
for i in range(len(list1)):  # range(0, 7)
    if list1[i] == 90:
        indexes.append(i)
print(indexes)
print(len(indexes))

index = 0
# list1 = [90, 80, 100, 55, 90, 100, 90]
for number in list1:
    if number == 90:
        indexes.append(index)
    index += 1

#           0   1    2   3   4    5   6
# list1 = [90, 80, 100, 55, 90, 100, 90]
indexes = []
for i, number in enumerate(list1):
    if number == 90:
        indexes.append(i)
print(indexes)
print(len(indexes))

list1 = [4, 4, 4, 4, -9, 12, 4]
print(f'4 appears {list1.count(4)} times.')

# create a list of 50 random grades between 0-100
# using only for and count , calculate how many grades >= 90 there are (without using if)
#   grades = []
#   for i in range(50):
#     new_number = random.randint(0, 100)
#     grades.append(new_number)

grades = []
for i in range(50):
    new_number = random.randint(0, 100)
    grades.append(new_number)

print(grades[:25])
print(grades[25:])
_above_90 = 0
for grade in range(90, 100 + 1):
    _above_90 += grades.count(grade)

_above_90 = 0
while max(grades) > 89:
    _max = max(grades)
    _above_90 += grades.count(_max)
    while _max in grades:
        grades.remove(_max)


