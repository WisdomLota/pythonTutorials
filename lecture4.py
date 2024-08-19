# if, elif and else statements
# age = 18
# if age >= 18:
#     print("You can vote")
#     print(f'You are {age} years old')
# else:
#     print("You can't vote")

# score = 45
# if score >= 90:
#     print('A grade')
# elif score >= 80:
#     print('B grade')
# elif score >= 70:
#     print('C grade')
# elif score >= 60:
#     print('D grade')
# elif score >= 50:
#     print('E grade')
# else:
#     print('You got an F')

# score = 85
# if score >= 80:
#     print('B grade')
# elif score >= 80:
#     print('C grade')

# cake_ordered = True
# decoration_set = False
# guest_list_finalized = True

# if cake_ordered:
#     print('Cake has been ordered')
#     if decoration_set:
#         print('Decorations are all set')
#         if guest_list_finalized:
#             print("Everything is ready for the party let's celebrate")
#         else:
#             print('Please finalize the guest list')
#     else:
#         print('Please set up the decorations')
# else:
#     print('Please order the cake first')

age = int(input('Please enter your age: '))
country = input('What country are you from? ')

if age >= 18 or country == 'nigeria':
    print(f'You can vote in {country}')
else:
    print('You cannot vote')
