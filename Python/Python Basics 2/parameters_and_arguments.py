# Parameters
def say_hello(name, age): # these parameters allow us to give the function arguments when we call it (as seen on line 7)
    print(f"Hello {name}, you are {age} years old")


# Arguments
say_hello("David",24)

# We can now create functions that do things based on what parameters we give it, and what arguments we call it with

# positional arguments (position matters)
say_hello("Tom",26)
say_hello("Jerry",39)
say_hello("William",19)
say_hello(24,"David") # prints backwards

# keyword arguments (allow us to not worry about the position)
say_hello(age=82,name="David")
say_hello(age=41,name="Jenny")

# Default Parameters (don't confuse with keyword arguments)
def say_goodbye(name='Tom', day='Tuesday'):
    print(f"Goodbye {name}. I will see you again next {day}!")

say_goodbye() # if no args are given, the default parameters are used : Goodbye Tom. I will see you again next Tuesday!
say_goodbye("Aaron","Sunday") # given args overwrite the default params