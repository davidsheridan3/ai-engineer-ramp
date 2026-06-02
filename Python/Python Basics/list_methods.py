basket = ['apple', 'banana', 'orange']

# adding
basket.append('watermelon')
print(basket)
# can also use extend for this:
basket.extend(['mango', 'pineapple'])
print(basket)

# inserting
basket.insert(0, 'mango')
print(basket)

# removing
basket.pop() # pops off whatever is at the end of the list
basket.pop(0) # removes item at index 0
print(basket)
# we can also use remove for this:
basket.remove('banana') # give it the specific value
print(basket)
# also to empty list completely
basket.clear()
print(basket)