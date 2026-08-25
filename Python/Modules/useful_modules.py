from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7,7,7,8,8]
print(Counter(li)) # prints how many times an item occurs: Counter({7: 4, 8: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})

# sentence = 'my name is david davidson'
# print(Counter(sentence))  # Counter({' ': 4, 'd': 4, 'a': 3, 'i': 3, 'm': 2, 'n': 2, 's': 2, 'v': 2, 'y': 1, 'e': 1, 'o': 1})
#
# dictionary = {'a':1, 'b':2, 'c':3}
# print(dictionary['a'])

dictionary = defaultdict(lambda: 6, {'a':1, 'b':2, 'c':3})
print(dictionary['c']) # 3
print(dictionary['d']) # 6, defaultdict means we can give a default value to non-existing keys