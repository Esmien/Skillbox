INPUT_FILENAME = 'text.txt'
OUTPUT_FILENAME = 'analysis.txt'
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def get_dict(filename: str) -> dict[str, int]:
    """
    Создает из текста файла словарь с частотой каждой буквы английского алфавита без учета регистра
    :param filename: имя файла
    :return: несортированный словарь с частотами
    """
    total_letters_count = {}

    with open(filename, 'r') as f:
        for line in f: #в приведеном примре это не нужно, но если файл будет большой, то мы сэкономим RAM(прям сильно, очень)
            for char in line.lower():
                if char in ENGLISH_ALPHABET:
                    total_letters_count[char] = total_letters_count.get(char, 0) + 1
    return total_letters_count

def sort_dict(d: dict[str, int]) -> dict[str, float]:
    """
    Обрабатывает и сортирует валидный словарь по двум критериям:
    -доля вхождений по убыванию
    -алфавитный порядок по возрастанию
    :param d: валидный словарь для обработки
    :return: отсортированный словарь
    """
    total_letters = sum(d.values())

    letter_proportion = {
        letter: round(d[letter] / total_letters, 3)
        for letter in d}
    return dict(sorted(letter_proportion.items(), key=lambda item: (-item[1], item[0])))

def main():
    letter_proportion = sort_dict(get_dict(INPUT_FILENAME))

    with open(OUTPUT_FILENAME, 'w') as f:
        for letter, prop in letter_proportion.items():
            f.write(letter + '\t' + str(prop) + '\n')

if __name__ == '__main__':
    main()