text = input("Hey user, enter a sentence and I'll return a word count!!!!")
words = text.split()
count = len(words)

print(text)
print(words)
print("Total number of words: " + str(count))