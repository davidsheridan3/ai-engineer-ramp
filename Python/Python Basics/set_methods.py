my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

# .difference
print(my_set.difference(your_set)) # find what items 'my_set' has, that 'your_set' doesn't

# .discard
# my_set.discard(5) # removes if it exists
# print(my_set) # no 5

# .difference_update()
# my_set.difference_update(your_set)
# print(my_set) # {1, 2, 3}

# .intersection()
print(my_set.intersection(your_set)) # {4, 5} (intersection)

# .isdisjoint()
print(my_set.isdisjoint(your_set)) # False, as they have 4 + 5 in common
# = True, if they have no overlap

# .union()
print(my_set.union(your_set)) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} (united, removes duplicates)

# .issubset()
print(my_set.issubset(your_set)) # False, only true if it is actually a subset

# .isssuperset()
print(my_set.issuperset(your_set)) # False, only true if it is actually a superset

# True outputs for .issubset() & .isssuperset()

set_one = {1,2,3,4,5}
set_two = {1,2,3,4,5,6,7}

print(set_one.issubset(set_two)) # True
print(set_two.issuperset(set_one)) # True 
