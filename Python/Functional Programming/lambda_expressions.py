# lambda expressions

from functools import reduce

my_list = [1,2,3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(lambda item: item * 2, my_list))) # one and done, we can just delete the multiply by 2 function now
print(my_list)

# order for lambda expressions:
# lambda param: action(param)   call it, give it the param, then action we want to take on the param

# lets remove the filter function using lambda too:
print(list(filter(lambda item: item % 2 != 0, my_list)))
