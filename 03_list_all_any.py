import random

# create grades with 20 grades between 0-100
grades = []
for i in range(10):
    new_number = random.randint(0, 100)
    grades.append(new_number)

print(grades)

# a- find if there is ANY grade above 90 in the list.
#    i.e.
#    [80, 85, 87, 88, 12, 30, 40] --> False
#    [80, 95, 87, 88, 12, 98, 40] --> True
grades = []
for i in range(10):
    new_number = random.randint(0, 100)
    grades.append(new_number)
print(grades)

any_grades_above_90 = False
for grade in grades:
    if grade > 90:
        any_grades_above_90 = True
        break
print(any_grades_above_90)

#     any(condition for)
print(any(grade > 90 for grade in grades))

# b- find if ALL grades are below equal 90
#    i.e.
#    [80, 85, 87, 88, 12, 30, 40] --> True
#    [80, 95, 87, 88, 12, 98, 40] --> False

# b- find if ALL grades are below equal 90
all_grades_under_90 = True
for grade in grades:
    if grade >= 90:
        all_grades_under_90 = False
        break
print(all_grades_under_90)
print(all(grade <= 90 for grade in grades))

sleeping = [True, True, False, False, True]
print(any(sleep == True for sleep in sleeping))
print(any(sleep for sleep in sleeping))

numbers = [ 2, 4, 8, 10, 200]
print(all(number % 2 == 0 for number in numbers))

numbers = [ 1, 3, 5, 7, 9, 10]
print(all(number % 2 == 1 for number in numbers))

numbers = [ 1, 3, 5, 7, 9]  # find if all are e-zugi
print(all(number % 2 == 1 for number in numbers))
print(all(number % 2 != 0 for number in numbers))
print(not any(number % 2 == 0 for number in numbers))
print(any(number % 2 == 0 for number in numbers) == False)


sleeping = [True, True, False, False, True]
print(any(sleep == False for sleep in sleeping))

print(any(sleeping))  # is 1 at least True
print(all(sleeping))  # is all True




