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
# print(user.get('country')) # returns none, no errors :))))
# print(user.get('country', 'France')) # can also use this to set default value if key doesn't exist

# another way to create dicts (dict function)

# user2 = dict(name='John', age=25, city='New York')
# print(user2)

# another way to check if something exists in dictionaries, away from .get()
# print('name' in user) # returns true (exists)
# print('country' in user) # returns false (absent)
#
# # .keys() + .values() + .items()
# print('name' in user.values()) # checks values, therefore ouput is false as 'name' is a key
# print('height'in user.keys()) # checks keys, returns true
# print(user.items()) # grabs keys + values

# .clear()
# user.clear() # emptys dictionary
# print(user) # now empty

# .copy()
# user3 = user.copy()
# print(user.clear())
# print(user3) # the same as user, and still same after .clear as copy = last version saved

# .pop()
print(user.pop('city')) # removes item, prints corresponding value
print(user)

print(user.popitem()) # removes the last item (key:value)
print(user)

# .update()
print(user.update({'name': 'Marcus'})) # updates value, if key doesn't already exist, it adds as a new item
print(user)
