# A decorator supercharges our function
# A function that wraps another function and enhances it or changes it

def my_decorator(func):
    def wrap_func(greeting):
        print("********")
        func(greeting)
        print("********")
    return wrap_func

# what if hello() actually takes a parameter

@my_decorator
def hello(greeting):
    print(greeting)

hello('hiiii') # now output = hiiii, as added parameter to wrap_func

