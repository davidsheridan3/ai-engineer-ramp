# A decorator supercharges our function
# A function that wraps another function and enhances it or changes it

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("********")
        func(*args, **kwargs)
        print("********")
    return wrap_func

# what if hello() actually takes a parameter
# if we add more params to hello(), we need to add them to wrap_func(), this gets tedious!
# solution for this is '*args, **kwargs' for params in wrap func accepts all params and key:value params

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)

hello('hiiii')

