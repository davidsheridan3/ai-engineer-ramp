# For strings, we can use either simgle or double quotations:
print(type("Hello World"))
print(type('Hello World'))

# We can also use 3 single quotes in a row for LONG STRINGS:
long_string = '''
I went to the shop yesterday.
It was sunny,
so I bought an ice cream.
'''
print(long_string)

first_name = 'David'
surname = 'Sheridan'
fullname = first_name + ' ' + surname
print(fullname)

# String concatenation
print('David' + 'Sheridan') # this runs fine!
# print('David' + 5) # this doesn't run as we can't add an integer to a string!

# Type conversion
number = str(100)
print('David' + number) # converting the integer 100, to string '100', allows us to add it to 'David'

# Escape sequences
weather = 'It's sunny'' # simply doesn't work, python interpreter thinks the string is being ended after t
# so we use double quotes here
weather = "It's sunny"
print(weather)
# But what about:
weather = "It's "kind of" sunny" # breaks again
# so here we can use escape sequences (\):
weather_today = "It's \"kind of\" sunny"
# '\' means next character can be assumed a string
print(weather_today)
# '\n' = new line
# '\t' = tab

