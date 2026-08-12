# Error Handling
# age = input('Enter your age: ')
# print('Your age is', age)

# allows user to enter a string, we don't want this

# so we use int():
# age = int(input('Enter your age: '))
# print('Your age is', age)

# now when a string is entered the user receives an error: ValueError: invalid literal for int() with base 10

# we can catch the error in an except block, and prompt the user further:

while True:
    try:
        age = int(input('Enter your age: '))
        10/age
    except ValueError:
        print('Please enter a number!')
    except ZeroDivisionError:
        print('Please enter a number greater than 0!')
    else:
        print('Thank you for your time!')
        break

