for item in 'Zero to Mastery ': # 'Zero to Mastery ' is iterable = can be looped over
    print(item)

# also works for lists
for number in [1,2,3,4,5]:
    print(number)

# also ranges too!
for number in range(1,11):
    print(number)

# also sets
for number in {1,2,3,4,5}:
    print(number)

# also tuples
for number in (1,2,3,4,5):
    print(number)
print('hello world') # only prints once due to indentation

# we can also nest for loops!
for item in [1,2,3,4,5]:
    for x in ('a', 'b', 'c'):
        print(item, x) # 1 a, 1 b, 1 c, 2 a, 2 b (and so on)
