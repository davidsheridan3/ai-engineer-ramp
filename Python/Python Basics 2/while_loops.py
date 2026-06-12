# i = 0
# while i < 10:
#     print(i) # infinite loop

a = 0
while a < 10:
    print(a)
    a += 1 # this allows us to only loop through it 10 times
else:
    print("Finished!")

b = 0
while b < 10:
    print(b)
    b += 1
    break # the break statement means we exit the while loop => the else block never gets hits
else:
    print("Finished!")


# while loops vs. for loops: while loops are better for an unknown loop quantity, whereas for loops are better for a known amount e.g. for items in a list
# for while loops we need to have exit criteria to avoid infinite loops: e.g. a 'break' or an external variable

while True:
    response = input('say something: ')
    if response == 'bye':
        break # loop keeps running until the user inputs "bye"