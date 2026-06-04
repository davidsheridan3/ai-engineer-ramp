# Sets = unordered collections of unique objects

my_set = {1,2,3,4,5}
print(my_set)

test_set = {1,2,3,4,5,5}
print(test_set) # doesn't return second 5, as sets only allows or unique items

test_set.add(6) # gets added
test_set.add(2) # doesn't get added (as exists already)
print(test_set)

# Converting a list to a set (removing duplicated values):
my_list = [1,2,3,4,5,5,6,6]
print(set(my_list)) # use set() function

new_set = {1,2,3,4,5,5,6,7}
# print(new_set[0]) # sets don't support indexing so = error
# to check if something exists:
print(1 in new_set) # True
print(list(new_set)) # converts to list
newer_set = new_set.copy() # copies set and stores as a new one

