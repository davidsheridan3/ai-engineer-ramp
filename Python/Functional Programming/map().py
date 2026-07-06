# map, filter, zip, reduce

# def multiply_by2(li):
#     new_list =[]
#     for item in li:
#         new_list.append(item * 2)
#     return new_list


# the beauty of ,ap is all we need is:
def multiply_by2(item):
    return item * 2


print(list(map(multiply_by2,[1,2,3])))

my_list = [1,2,3]

def multiply_by3(item):
    return item * 3

print(list(map(multiply_by3,my_list))) # [3, 6, 9]
print(my_list) # still [3, 6, 9]

# here, map allows us to create a whole new list that doesn't modify my_list in outside world