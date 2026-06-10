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