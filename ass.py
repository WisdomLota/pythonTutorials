# height_of_triangle = 25
# base_of_triangle = 7
# area_of_triangle = (height_of_triangle*base_of_triangle)/2
# print(area_of_triangle)
# # final_answer = area_of_triangle/2
# # print(final_answer)
# a_number = 78.5
# print(area_of_triangle == a_number)
# formula_b = 'half of base'
# formula_h = 'height'
# print(f'The area of the triangle is {area_of_triangle}')

# student_name = (input('enter your name: '))
# student_class = (input('enter your class: '))
# cut_off_CGPA = 7
# student_CGPA = float(input('enter your CGPA: '))
# if student_CGPA >= cut_off_CGPA:
#     print('you have been promoted to the next class')
# else:
#     print('kindly resit your exams')


# name = 'lota'
# user = input('enter name: ')
# while user != name:
#     print('please enter correct username')
#     user = input('enter name: ')

# print('access granted')


# def calculator(number_1, number_2, sign):

#     if sign == "+":
#         result = number_1 + number_2
#         print(result)
#     elif sign == "-":
#         result = number_1 - number_2
#         print(result)
#     elif sign == "*":
#         result = number_1 * number_2
#         print(result)
#     elif sign == "/":
#         result = number_1 / number_2
#         print(result)

#     else:
#         print('invalid')


# calculator(5, 7, "+")

# for num in range(2, 200):
#     for num_within in range(2, num):
#         if num % num_within == 0:
#             break
#             # print(f'{num} is not PRIME')
#     else:
#         print(f'{num} is PRIME')

product_inventory = {
    'apple': 10,
    'banana': 20,
    'orange': 15,
    "grape": 5
}

# quantity_of_banana = product_inventory['banana']
# print(quantity_of_banana)

# quantity_of_grape = product_inventory.get('banana', 'item not found')
# print(quantity_of_grape)

# for fruit, amount in product_inventory.items():
#     print(f"Fruit: {fruit}, Amount: {amount}")

# list_of_my_keys = product_inventory.keys()
# list_of_my_values = product_inventory.values()
# print(list_of_my_keys)
# print(list_of_my_values)

# print(product_inventory)
new_stock = {'mango': 23, "watermelon": 34}
product_inventory.update(new_stock)
product_inventory['pineapple'] = 90
product_inventory['orange'] = 25

del product_inventory['grape']
removed_item = product_inventory.pop('mango')
print(removed_item)
randomly_removed = product_inventory.popitem()
print(randomly_removed)
print(product_inventory)
