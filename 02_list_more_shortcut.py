
[10, 2, -1, 4].index(2) # returns index of value 2 → 1

[1,2,3,3,4].count(3) # returns how many times 3 appears → 2

[1,2,3].append(4) # adds 4 to end → [1,2,3,4]

[1,2,3].remove(2) # removes first 2 → [1,3]

[1,2,3].pop(1) # removes & returns value at index 1 → 2

[1,2,3].insert(1, 99) # inserts 99 at index 1 → [1,99,2,3]

[1,2] + [3,4] # joins lists → [1,2,3,4]

lst = [1,2];
lst.extend([3]) # adds 3 → [1,2,3]

del lst[0] # deletes item at index 0

[1,2,3].clear() # removes all items → []

[1,2,3].copy() # creates shallow copy

"".join(["a","b"]) # joins list to string → "ab"

max([1,5,3]) # largest value → 5
min([1,5,3]) # smallest value → 1
sum([1,2,3]) # total → 6
len([1,2,3]) # number of items → 3

import statistics
statistics.mean([4,5,9,9,9])  # avg


# instead of this
grades = [90, 80, 100, 55, 90]
for i in range(len(grades)):
    print(i, grades[i])

# do this ------->
#          0   1    2   3   4
grades = [90, 80, 100, 55, 90]
for index, value in enumerate(grades):
    print(index, value)
# output:
# 0 90
# 1 80
# 2 100
# 3 55
# 4 90


grades = [90, 75, 100, 55, 90, 60]
# Do the following:

# 1 Print how many times 90 appears
print(grades.count(90))

# 2 Print the index of the first 100
print(grades.index(100))

# 3 Add grade 88 to the end
print(grades.append(88))
grades = grades + [88]
grades.extend([88])

# 4 Insert 50 at index 2
grades.insert(2, 50)

# 5 Remove the first 55
grades.remove(55)
del grades[grades.index(55)]
grades.pop(grades.index(55))

# 6 Remove the grade at index 3 using pop() and print what was removed
grades.pop(3)

# 7 Print the maximum grade
print(max(grades))

# 8 Print the minimum grade
print(min(grades))

# 9 Print the total sum of grades
print(sum(grades))

# A Print how many grades there are
print(len(grades))

# B Make a backup copy of the list
backup = grades.copy()

# C Clear the original list
grades.clear()

# D Print both lists to prove copy worked

# You must use:
# count, index, append, insert, remove, pop, max, min, sum, len, copy, clear

# put the word 'hello'(str) into a list (hint: use list command)
# make the list into str (using join), then upper and put it back into the list
# change the last character to 0
# remove the first character
# make it a string and print
