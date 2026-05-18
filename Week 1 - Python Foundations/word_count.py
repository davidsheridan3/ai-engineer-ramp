def count_words(text):
    return len(text.split())


def get_top_words(word_counts):
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:5]


try:
    with open("sample.txt", "r") as file:
        text = file.read()

    word_count = count_words(text)
    line_count = len(text.splitlines())
    char_count = len(text)

    words = text.lower().split()

    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    top_words = get_top_words(word_counts)

    print(f"Total number of words: {word_count}")
    print(f"Total number of lines: {line_count}")
    print(f"Total number of characters: {char_count}")

    print("\nTop 5 most common words:")

    for word, count in top_words:
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Error: File 'sample.txt' not found. Please check file path and try again.")