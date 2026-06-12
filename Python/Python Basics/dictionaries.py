# Dictionary
dictionary = {
    'a': 'apple', # key:value
    'b': 'banana', # key:value
}

print(dictionary['a']) # outputs value of key 'a'

# unlike lists, dictionaries are unordered: can't access value by index number, only key name

dictionary2 = {
    'a': ['apple', 'banana','kiwi'],
    'b': 'hello',
    'c': True
}

print(dictionary2['a'][1]) # accesses index 1 of list value belonging to key 'a'

# another layer, dictionaries within  a list:
list = [
    {
        'a': ['apple', 'banana','kiwi'],
        'b': 'hello',
        'c': True
    },
    {
        'a': ['1', '2','3'],
        'b': 'hello',
        'c': True
    },
    {
        'a': ['hey', 'hello','bye'],
        'b': 'hello',
        'c': True
    }

]

# to get 'bye' from the last dict in the list:
print(list[2]['a'][2])