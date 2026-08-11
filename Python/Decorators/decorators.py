# A decorator supercharges our function
# A function that wraps another function and enhances it or changes it

def my_decorator(func):
    def wrap_func():
        print("********")
        func()
        print("********")
    return wrap_func

@my_decorator
def hello():
    print("hellooooooooo")

hello()

# we've just super boosted our hello function with stars! (without touching the hello function)

def bye():
    print("byebyebyebye")
bye() # nothing changes, but to super boost we do below:

@my_decorator
def bye2():
    print("byebyebyebye")
bye2() # superboosted!!!!!!, stars

# it is the same as hello2 = my_decorator(hello)
# hello2()