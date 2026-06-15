def addition(args):
    return sum(args)

# addition(1,2,3,4,5) # TypeError: addition() takes 1 positional argument but 5 were given

def super_function(*args):
    return sum(args)

print(super_function(1,2,3,4,5)) # 15, '*' allows us to accept any amount of arguments

def kwarg_function(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(kwarg_function(1,2,3,4,5, num1=50, num2=50)) # 115

# '*' lets us enter as many arguments as we want, '**' lets us enter as many keyword arguments as we want
# Parameter order rule: params, *args, default params, **kwargs:

def profile(name, *args, age=24, **kwargs): #usually we would just use 1 or 2 at a time...
    print(name, args, age, **kwargs)


