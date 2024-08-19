# result = ""
# try:
#     # code that might raise an exception
#     num1 = int(input('Enter a number: '))
#     num2 = int(input('Enter another number: '))
#     result = num1 / num2

# except TypeError:
#     print('Please convert input to integer')
# except ZeroDivisionError:
#     print('Cannot divide a number by 0')
# except ValueError:
#     print('Please enter numbers only')
# except Exception as err:
#     print(f"An error occured: {err}")
# finally:
#     print(result)

# x = 10
# if x > 5:
#     raise ValueError('x should not be greater than 5')

def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError('Cannot divide by zero')
        return x / y
    except Exception as err:
        print(f"An error occured: {err}")


print(divide(3, 4))
