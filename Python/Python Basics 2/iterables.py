# Iterable - list, dictionary, tuple, set, string
# Iterated -> one by one check each item in the collection

# Dictionaries
user = {
    'name': 'David',
    'age': 26,
    'country': 'USA',
    'city': 'New York',
    'can swim': True
}

for item in user: # same as .keys()
    print(item) # prints keys, i.e. name, age, country

for item in user.items():
    print(item) # prints key:value pairs

# if we don't want a tuple output for key:value pairs:
for key, value in user.items():
    print(key, value)

for item in user.values():
    print(item) # prints just the values, i.e. David, 26, USA

# Note: .items(), .keys(), .values() allow us to iterate over dictionaries