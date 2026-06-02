# Sometime you need different data types to interact together. Here we change a str to int:
from datetime import date

birth_year = input('Please enter your birth year: ')
current_age = date.today().year - int(birth_year) # have to change birth_year type to int, so it can be subtracted
print(f'Your current age is {current_age}')