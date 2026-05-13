def word_counter(text):
    return "Total words: " + str(len(text.split()))

text = input("Enter a sentence, I'll count the words: ")
count = word_counter(text)
print(f"Total worlds: {count}")