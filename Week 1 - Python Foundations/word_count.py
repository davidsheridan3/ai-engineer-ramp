def word_counter(file_content):
    return len(file_content.split())

try:
    with open("sample.txt", "r") as file:
        file_content = file.read()
    print(f"Total number of words in 'sample.txt' is: {word_counter(file_content)}")

except FileNotFoundError:
    print("Error: File 'sample.txt' not found. Please check file path and try again.")

line_count = len(file_content.splitlines())
print(f"Total number of lines in 'sample.txt' is: {line_count}")

char_count = len(file_content)
print(f"Total number of characters in 'sample.txt' is: {char_count}")

word_list = file_content.lower().split()
print(word_list)



