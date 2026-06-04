# Unlike lists, tuples are immutable (makes code safer + more predictable, but less flexible
my_tuple = (1,2,3,4,5,6,7)
# my_tuple[1] = 5 # error, as tuple doesn't support object assignment
print(my_tuple[1]) # can still access it through an index though, like a list
print(5 in my_tuple) # True

# if you don't need the values to change often, tuples are a good choice (over lists)
# Due to their immutability, they can be used as keys in dictionaries (unlike lists):
user = {
    ('name','age','gender'): ['John','24','male'],
    'greet': 'hello',
    'reply': 'hey, how are things?'
}

print(user[('name','age','gender')]) # it works!