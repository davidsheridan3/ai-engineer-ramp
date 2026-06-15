def sum(num1, num2):
    num1 + num2

sum(1, 2) # nothing happens as we have no print or return in our function
print(sum(1, 2)) # None

def addition(num1, num2):
    return num1 + num2 # return =  exit this function and return whatever this expression gives us

print(addition(1,2)) # 3

''' 
    Functions - rule of thumb:
    A function should do one thing really well.
    A function should return something.
'''

total = addition(10, 5) # 15
print(total)

print(addition(10,total)) # 25