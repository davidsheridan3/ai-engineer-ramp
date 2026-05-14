with open("sample.txt", "r") as file:
    file_content = file.read()

print(file_content)

def word_counter(file_content):
    return len(file_content.split())




