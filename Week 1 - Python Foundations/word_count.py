def word_counter(text):
    return len(text.split())

text = input("Enter a sentence, I'll count the words: ")
count = word_counter(text)
print(f"Total worlds: {count}")


with open("sample.txt", "r") as file:
    file_content = file.read()

print(file_content)