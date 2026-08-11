#list, set, dictionary
# same as list_comprehensions.py, but just sets rather than lists

new_list = {char for char in 'hello'}
print(new_list) # exact same thing!!!!!

new_list2 = {num for num in range(100)}
print(new_list2)

new_list3 = {num ** 2 for num in new_list2}
print(new_list3)

new_list4 = {num for num in new_list3 if num % 2 == 0}
print(new_list4)

# quick way for us to generate sets (remember sets only allow unique items, duplicates removed

# now for dictionaries:

sample_dictionary = {
    'a': 1,
    'b': 2,
}

my_dict = {k:v * 2 for k, v in sample_dictionary.items()}

print(my_dict)

# another example, key = number in list, value = double number in list
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)
