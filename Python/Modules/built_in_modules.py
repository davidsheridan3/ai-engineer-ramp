import random

# help(random) # documentation for random module
# print(dir(random)) # prints all methods available in module

print(random.random()) # random number between 0 - 1

print(random.randint(1, 10)) # random integer between 1 - 10 (inclusive)

print(random.choice([1, 2, 3, 4, 5])) # random choice from list given

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) # re-arranges order of items in list (randomly)