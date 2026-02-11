import random

# create grades with 20 grades between 0-100
grades = []
for i in range(10):
    new_number = random.randint(0, 100)
    grades.append(new_number)

print(grades)

# a- find if there is ANY grade above 90 in the list
# b- find if ALL grades are below equal 90