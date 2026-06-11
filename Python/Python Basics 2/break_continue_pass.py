my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
    break # exits loop after first iteration

for item in my_list:
    print(item)
    continue # sends the interpreter back to the top of the loop

for item in my_list:
    continue
    print(item) # never gets ran due to continue

# 'pass' essentially does nothing, just sends interpreter to the next line
