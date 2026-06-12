# Check for duplicates in the list

letters = ['a','b','c','d','e','f','a','d']

duplicates = []

for letter in letters:
    if letters.count(letter) > 1:
        if letter not in duplicates: # ensure duplicates are only printed once
            duplicates.append(letter)

print(duplicates)