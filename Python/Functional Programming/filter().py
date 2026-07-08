# map, filer, zip, reduce

my_list = [1,2,3]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd,my_list)))
print(my_list)

# filter creates a new list for us, doesn't modify the existing list
