basket = ['apple', 'banana', 'orange']

# adding
# basket.append('watermelon')
# print(basket)
# can also use extend for this:
# basket.extend(['mango', 'pineapple'])
# print(basket)

# inserting
# basket.insert(0, 'mango')
# print(basket)

# removing
# basket.pop() # pops off whatever is at the end of the list
# basket.pop(0) # removes item at index 0
# print(basket)
# we can also use remove for this:
# basket.remove('banana') # give it the specific value
# print(basket)
# also to empty list completely
# basket.clear()
# print(basket)

# print(basket.index('banana')) # prints index of banana
# print(basket.index('orange', 0, 1)) # starts at index 0, stops at 1, error due to orange being at 2
#
# print('apple' in basket) # = True
# print('cherry' in basket) # = False

numbers = [1, 2, 3, 4, 5, 8, 7, 6, 9, 11, 10]
# numbers.sort() # sorts the numbers in order, can do the same for letters
# print(numbers)

# apart from sort() as a method, we also have a sorted function, which doesn't modify the basket, but creates a new one
print(sorted(numbers))
print(numbers) # two different lists

basket.reverse() # reverses the order of the items in the basket
print(basket)


