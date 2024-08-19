# CREATE A LIST
# my_list = [1, 2, 3, 11, 4, 5, 6, 2,  12, 45, 67, 11]
# test_list = [12, 45, 'lota', 'emeka', True, [12, 34, 45], ]


# ACCESSING ITEMS IN A LIST
# fruits = ['apple', 'banana', 'cherry', 'pineapple', 'grapes', 'berries']
# first_fruit = fruits[2]
# print(first_fruit)
# print(fruits[:])

# MANIPULATE ITEMS WITHIN A LIST
# fruits = ['apple', 'banana', 'cherry', 'pineapple', 'grapes', 'berries']
# fruits[2] = 'blueberry'
# print(fruits)

# fruits.append('mangoes')
# fruits.append('oranges')
# print(fruits)

# new_fruits = ['kiwi', 'grapefruits', 'cashew']
# fruits.extend(new_fruits)
# fruits.insert(2, 'Guava')
# print(fruits)


# DELETING/REMOVING ITEMS IN A LIST
# fruits = ['apple', 'banana', 'cherry', 'pineapple', 'grapes', 'berries']
# fruits.remove('cherry')
# del fruits[-1]
# fruits.pop(1)
# fruits.clear()
# print(fruits)


names_of_students = []
i = 0
while i < 10:
    student_name = input('please enter first name: ')
    names_of_students.append(student_name)
    i += 1

print(names_of_students)
