import string
import re


def process_word(word):
    """
    Функция для обработки слова: удаляет знаки препинания и приводит к нижнему регистру.
    Если слово - четырехзначное число, то добавляет кавычки.
    """
    if re.match(r'^\d{4}$', word):
        word = f'"{word}": "'
    return word


def process_line(line, end_sign='",'):
    """
    Функция для обработки строки: добавляет знак в конце и обрабатывает каждое слово.
    """
    line = line.strip() + end_sign
    words = line.split(' ', 1)
    processed_words = [process_word(word) for word in words]
    processed_line = ''.join(processed_words)
    return processed_line


def process_file(file_path, end_sign='", '):
    """
    Функция для обработки всего файла и сохранения изменений обратно в файл.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = [process_line(line, end_sign) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_lines)


file_path = 'codes.py'
process_file(file_path, end_sign='", ')
