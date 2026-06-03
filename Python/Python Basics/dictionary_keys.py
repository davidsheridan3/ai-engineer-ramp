# Keys need to be immutable (cannot change), therefore cannot be a list
# 99% of the time we use something descriptive, like a string
# Also, keys have to be unique.... if a key is repeated, previous value is overwritten

# dictionary = {
#     '123': [1,2,3],
#     '123': 'hello'
# }
#
# print(dictionary['123']) # output = 'hello'

''' To access a key and to see if it even exists (to prevent getting any errors):
lets use .get() method!!! '''

user = {
    'name': 'John',
    'age': 25,
    'sex': 'male',
    'height': 70,
    'city': 'New York'
}

# print(user['country']) # program fails! we don't want this. we want our code to runnnnn
print(user.get('country')) # returns none, no errors :))))
print(user.get('country', 'France')) # can also use this to set default value if key doesn't exist

# another way to create dicts (dict function)

user2 = dict(name='John', age=25, city='New York')
print(user2)
