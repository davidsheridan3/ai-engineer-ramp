# iterable = any object that we are able to loop through
# everything that is a generator is iterable, but not everything that is iterable is a generator
# generator is a subset of an iterable

# instead of

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result

# instead of having to create list in memory, we just go 1 by 1, only holding 1 item in memory:

def generator_function(num):
    for i in range(num):
        yield i*2

# for item in generator_function(1000):
#     print(item)

g = generator_function(100);
next(g) # 0
next(g) # 2
print(next(g)) # = 4, yield keyword pauses the function

# yield pauses the function, and comes back to it when next() is called
# only keeps the most recent data in memory