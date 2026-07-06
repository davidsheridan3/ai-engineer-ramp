def multiply_by2(li):
    new_list =[]
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1,2,3,4,5,6,7,8,9,10]))

'''
always gives me the same output for the same input
doesn't produce any side affects, doesn't touch anything un the outside world
nothing in the outside world matter to this function
this is a pure function (less buggy)
'''


new_list = []
def multiply_by2(li):
    for item in li:
        new_list.append(item * 2)
    return new_list

'''
this gives the same output, but interacts with and produces side affects in the outside world
this new list could be modified by another developer in the outside world and it could make out function give errors (side affect)
this is not a pure function (more buggy)
'''

# Pure functions = a guideline, not an absolute. It is impossible to have no interactions with the outside world with functions.