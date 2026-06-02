li = [1,2,3,4,5]
li2 = ['a','b','c','d','e']
li3 = [1,2.2,'a',True,'b','c','d','e'] # lists can contain various data types

amazon_cart = [
    'laptop',
    'computer',
    'mouse',
    'remote',
    'keyboard'
]
print(amazon_cart[0]) # like strings can access specific indexes
print(amazon_cart[0::2]) # like strings, we can slice (by specifying indexes with first, last, step over)

# However, lists unlike strings, are actually mutable
amazon_cart[0] = 'vacuum'
print(amazon_cart)