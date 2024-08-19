# def function_name(args):
# lambda args: expression

# def addition(x, y): return x + y


# result = addition(67, 89)
# print(result)

# numbers = [2, 4, 3, 1, 5]
# doubled_numbers = list(map(lambda z: z ** 2, numbers))
# print(doubled_numbers)

# numbers = list(range(31))
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# from functools import reduce
# numbers = [2, 4, 3, 1, 5]
# product_of_all_numbers = reduce(lambda x, y: x * y, numbers)
# print(product_of_all_numbers)

students = [('Sandra', 16), ('Emeka', 19), ('Lota', 23),
            ('Femi', 12), ('Mitchell', 15)]

sorted_students = sorted(students, key=lambda x: x[0])
print(sorted_students)
# print(sorted(students))
