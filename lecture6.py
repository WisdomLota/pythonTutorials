# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# print('i am done')

# password = 'stargirl123'
# user_input = input('enter your password: ')
# attempt = 0
# while user_input != password:
#     attempt += 1
#     if attempt <= 3:
#         print('Please enter the right password')
#         user_input = input('enter your password: ')
#     elif attempt > 3:
#         print('Please you have exhausted your chnaces')
#         break


# def message(name, level, age):
#     print(f"Hello {name}, you are in {level} and you are {age} years old.")
#     print(f'Welcome {name}')


# message('lota', 'js2', 15)
# message('ella', 'js3', 18)
# message('emeka', 'ss2', 15)
# message('faruk', 'js2', 15)

# def subtract(a, b, c):
#     result = a - b - c
#     return result


# num = subtract(1, 2, 3)
# final_result = 200 - num
# print(final_result)


for num in range(1, 201):
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not PRIME')
            break
    else:
        print(f'{num} is PRIME.')
