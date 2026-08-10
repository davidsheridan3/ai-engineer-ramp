#list, set, dictionary


my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# faster way of doing this?

new_list = [char for char in 'hello']
print(new_list) # exact same thing!!!!!

new_list2 = [num for num in range(100)]
print(new_list2)

new_list3 = [num ** 2 for num in new_list2]
print(new_list3)

new_list4 = [num for num in new_list3 if num % 2 == 0]
print(new_list4)