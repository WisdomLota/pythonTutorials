# code to display a message
# message = "Hello world, This is Sandra"
# print(message)
# print(message)
# print(message)
# print(message)

# name = "Lotachukwu"
# age = 23
# print('My name is ' + name + '' + "and I am " + str(age) + '' + 'years old.')
# print('My name is ', name, "and I am ", str(age), 'years old.')
# print(f'My name is {name} and I am {age} years old.')


# Snake case
area_of_a_triangle = 'half base times height'

# Camel case
areaOfATriangle = '234'

# string
name = "lota"
# integer
phone = 90
# float
num = 90.3
# boolean
is_student = True
is_student = False
# list
friends_list = ['lota', 'ella', 'emeka', 'sandra', 'ngozi']
# tuples
friends_tuple = ('lota', 'ella', 'emeka', 'sandra', 'ngozi')
# dictionaries
person = {'name': 'Sandra', 'age': 18, 'city': 'Lagos'}

# x, y, z, p = 1, 20, 78, 89
# x = y = z = 7
# print(x, y, z)

# Arithmetic
# a, b = 45, 6
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a % b)
# print(a//b)
# base = 60
# height = 7
# area_of_a_triangle = (1/2) * base * height
# print(area_of_a_triangle)


# comparison
# a = 45
# b = 45
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# assignment
# age = 23
# age += 2
# age -= 2
# age *= 2
# age /= 3
# print(age)

# logical
# name = 'chiirstie'
# age = 17

# print(name == 'sandra' and age == 18)
# print(name == 'sandra' or age == 18)

# is_student = True
# print(not (is_student))

# if, elif and else

# age = 14
# class_level = 'undergraduate'
# if age >= 18 or class_level == 'undergraduate':
#     print('You are an adult')
# else:
#     print('You are a minor')

score = int(input('Please enter your score in mathematics: '))
if score >= 90:
    print('A grade')
    print('Congrats!')

elif score >= 80:
    print('B grade')

elif score >= 80:
    print('C grade')

else:
    print('You failed')
