text = input("Hey user, enter a sentence and I'll return a word count!!!!")

def word_counter(text):
    return len(text.split())

print(word_counter(text))