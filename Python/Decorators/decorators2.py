# A decorator supercharges our function
# A function that wraps another function and enhances it or changes it

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

# what if hello() actually takes a parameter

@my_decorator
def hello(greeting):
    print(greeting)

hello('hiiii') # results in an error, as wrapper function takes no positional arguments

