with open("sample.txt", "r") as file:
    file_content = file.read()

def word_counter(file_content):
    return len(file_content.split())

print(f"Total number of words in 'sample.txt' is: {word_counter(file_content)}")


