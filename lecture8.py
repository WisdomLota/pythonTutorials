# BUILT IN FUNCTIONS

# Data type functions
# x = 'lota'
# print(type(x))


# print(isinstance(10, str))

# frens = ['lota', 'sandra', 'emeka', 'chukwu']
# number_of_items = len(frens)
# print(number_of_items)

# name = 'lotachukwu'
# print(len(name))
# names = ['lota', 'rep', '']
# print(ord(106))
# print(ord(107))
# print(ord('lota'))
# print(ord('lota'))

# name = 'lota'
# for l in name:
#     val = ord(l)
#     print(val)

# ID isn't the same integer value for immutable objects
import sys
password = sys.intern(input('please put in password: '))
password_id = id(password)
print(password_id)
login = sys.intern(input('Please enter your password: '))
login_id = id(login)
print(login_id)
if password_id == login_id:
    print('Welcome!')
else:
    print('incorrectpasword')


# MATHEMATICAL FUNCTIONS
# x = 10
# print(abs(x))

# result = 56/3
# print(round(result, 3))
# numbers = [20, 12, 3]
# print(min(numbers))
# print(sum(numbers))

# print(2**3)
# print(pow(2, 3))

# x = 23
# y = str(x)
# print(type(y))

# fruits = ['apple', 'banana', 'cherry']
# for index, value in enumerate(fruits):
#     print(index, value)

# names = ['lota', 'sandra', 'emeka']
# ages = [23, 24, 25]
# for name, age in zip(names, ages):
#     print(name, age)

# numbers = [34, 12, 56, 15, 1, 90]
# print(sorted(numbers))
# for num in reversed(numbers):
#     print(num)

# fruits = ['apple', 'banana', 'watermelon']
# # for fruit in fruits:
# #     print(fruit)

# count = 0
# while count < len(fruits):
#     print(fruits[count])
#     count += 1
