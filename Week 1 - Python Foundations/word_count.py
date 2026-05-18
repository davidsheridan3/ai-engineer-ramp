def read_file(filepath):
    #Open and read the text file
    with open(filepath, "r") as file:
        return file.read()


def count_words(text):
    #Count total words
    return len(text.split())


def count_lines(text):
    #Count total lines
    return len(text.splitlines())


def count_characters(text):
    #Count total characters
    return len(text)


def get_word_counts(text):
    #Convert text to lowercase and split into words
    words = text.lower().split()

    #Store word frequencies
    word_counts = {}

    for word in words:
        #First time seeing the word
        if word not in word_counts:
            word_counts[word] = 1
        #Word already exists, increase count
        else:
            word_counts[word] += 1

    return word_counts


def get_top_words(word_counts):
    #Sort words by frequency (highest first)
    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    #Return top 5 most common words
    return sorted_words[:5]


def main():
    #Read file contents
    text = read_file("sample.txt")

    #Generate text statistics
    word_count = count_words(text)
    line_count = count_lines(text)
    char_count = count_characters(text)

    #Build word frequency dictionary
    word_counts = get_word_counts(text)

    #Get most common words
    top_words = get_top_words(word_counts)

    #Print results
    print(f"Total number of words: {word_count}")
    print(f"Total number of lines: {line_count}")
    print(f"Total number of characters: {char_count}")

    print("\nTop 5 most common words:")

    for word, count in top_words:
        print(f"{word}: {count}")


main()
