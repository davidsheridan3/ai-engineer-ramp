# Error Handling
# age = input('Enter your age: ')
# print('Your age is', age)

# allows user to enter a string, we don't want this

# so we use int():
age = int(input('Enter your age: '))
print('Your age is', age)

# now when a string is entered the user receives an error: ValueError: invalid literal for int() with base 10