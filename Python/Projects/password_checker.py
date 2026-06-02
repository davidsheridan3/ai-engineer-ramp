# Goal: print the username, return the hidden password, and say how many characters it is
user_name = input('Please enter your username: ')
password = input('Please enter your password: ')

password_length = len(password)
converted_password = '*' * password_length

print(f'Hey {user_name}! Your password, {converted_password}, is {password_length} characters long.')

