import re


def process_word(word):
    if re.match(r'^\d{4}$', word):
        word = f'"{word}": '
    return word


def create_dictionary(file_path):
    word_count = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = process_word(word)
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    return word_count


file_path = 'your_text_file.txt'
dictionary = create_dictionary(file_path)
