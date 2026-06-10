print(range(100)) # range(0, 100)

for number in range (0, 100):
    print(number) # prints 0 to 99 in console (line after line)

# There is also a 3rd parameter accepted in range() called step over

for _ in range(0, 10, 2):
    print(_) # 0, 2, 4, 6, 8

# printing lists from range()
for item in range(0, 10): # amount of times it's printed
    print(list(range(0, 6))) # what the lists actually contain