# lambda expressions

from functools import reduce

my_list = [1,2,3]


def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(list(map(lambda item: item * 2, my_list))) # one and done, we can just delete the multiply by 2 function now
print(my_list)