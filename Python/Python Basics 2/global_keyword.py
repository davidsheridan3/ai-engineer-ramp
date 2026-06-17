# total = 0
#
# def count():
#     total += 1
#     return total
#
# print(count()) # cannot access local variable 'total' where it is not associated with a value

# So we can use the global keyword:

number = 0

def counter():
    global number # allows us to access a variable outside of local scope
    while number < 10:
        number += 1
    return number

print(counter())

# global keyword can start to get confusing though, so we can just do this:

def counter2(number):
    while number < 10:
        number += 1
    return number

print(counter2(number))