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

# Tuples
my_new_tuple = (1,2,3,4,5,6,7,7,7)
x = my_new_tuple[1] # 2
y = my_new_tuple[2] # 3
print(x)
print(y)

# as with lists, we can still do:
a,b,c, *other = (1,2,3,4,5,6,7,7,7)
print(a) # 1
print(b) # 2
print(*other) # 4,5,6,7

print(my_new_tuple.count(7)) # 3 (counts frequency of stated item)
print(my_new_tuple.index(7)) # returns index of 7 (6), if multiple, returns first occurrence
print(len(my_new_tuple)) # returns amount of items (9)