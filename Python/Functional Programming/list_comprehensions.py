#list, set, dictionary


my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# faster way of doing this?

new_list = [char for char in 'hello']
print(new_list) # exact same thing!!!!!