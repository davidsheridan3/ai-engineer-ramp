# map, filer, zip, reduce

my_list = [1,2,3]
your_list = [10,20,30]

def only_odd(item):
    return item % 2 != 0

# we can use zip() to "zip" 2 lists or iterables together
# I created your_list to demo this


print(list(zip(my_list,your_list))) # [(1, 10), (2, 20), (3, 30)]

# items get zipped together into a tuple

# to use zip() on 3 iterables:
their_list = (60,70,80) # notice, we even used a tuple instead of a list (as long as it's an iterable!)

print(list(zip(my_list, your_list, their_list))) # [(1, 10, 60), (2, 20, 70), (3, 30, 80)]



