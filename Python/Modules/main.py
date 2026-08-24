# this 'modules.py' is a module. We want to separate modules for separate purposes.
import utility
import Shopping.shopping_cart as shopping_cart

print(utility.divide(10,2))
print(utility.multiply(10,2))
print(shopping_cart.buy('apple'))

# using utility module (utility.py) in my main file!
