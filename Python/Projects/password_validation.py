# Regular Expressions

# Password that is at least 8 characters long
# Contains any sort letters, numbers, $%#@
# Has to end with a number
import re

pattern = r'^(?=.*[A-Za-z0-9$%#@]).{8,}\d$'

password = input("Enter password: ")

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")

