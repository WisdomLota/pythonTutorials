password = input('Please put in password: ')
password_id = ""
for letter in password:
    password_letter_ord_value = str(ord(letter))
    password_id += password_letter_ord_value

login = input('Please enter your password: ')
login_id = ''
for letter in login:
    login_letter_ord_val = str(ord(letter))
    login_id += login_letter_ord_val

if password_id == login_id:
    print('welcome')
else:
    print('incorrect')
    
