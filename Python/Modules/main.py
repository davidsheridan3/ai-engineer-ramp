# this 'modules.py' is a module. We want to separate modules for separate purposes.
import utility
import Shopping.shopping_cart as shopping_cart

print(utility.divide(10,2))
print(utility.multiply(10,2))
print(shopping_cart.buy('apple'))

# using utility module (utility.py) in my main file!

# now when I run this file, name of imported modules are outputted, due to print(__name__) in each

# the name __main__ is always outputted for the __name__ for file we run
print(__name__) # = __main__

class Student():
    pass

st1 = Student()
print(type(st1)) # <class '__main__.Student'>, '__main__' is the file it was created in


