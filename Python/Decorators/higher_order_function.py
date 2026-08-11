# Higher Order Function
# A function that accepts, inside its parameters, another function

def greet(func):
    func()

# Or a function that returns another function

def greet2():
    def func():
        return "hello"
    return func

# Higher Order Function = any that accepts a function as a parameter or returns a function