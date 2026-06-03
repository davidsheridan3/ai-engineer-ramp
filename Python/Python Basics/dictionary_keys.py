# Keys need to be immutable (cannot change), therefore cannot be a list
# 99% of the time we use something descriptive, like a string
# Also, keys have to be unique.... if a key is repeated, previous value is overwritten

dictionary = {
    '123': [1,2,3],
    '123': 'hello'
}

print(dictionary['123']) # output = 'hello'