letters = ['a', 'x', 'b', 'c', 'f', 'g', 'e']
letters.sort() # puts into order
letters.reverse() # flips the order
# print(letters[::-1]) # flips letters back again (into order)
# print(letters) # displays letters backwards

print(list(range(1,101))) # list() allows us to list out all components of the range stated

sentence = ' ' # space
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'David']) # joins space with each item in list, meaning we get a sentence as output
print(new_sentence)