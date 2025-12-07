import zipfile, os


FILENAME = 'voyna-i-mir.txt'

if not os.path.exists(FILENAME):
    zipfile.ZipFile('voina-i-mir.zip').extractall('.') # распаковываем архив

def get_sorted_letters_freq(filename: str) -> dict:
    """
    Считает частоту вхождений всех букв в тексте из файла
    :param filename: имя читаемого файла
    :return: отсортированный по убыванию словарь частоты букв
    """
    chars_counting = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for char in line:
                if char.isalpha():
                    chars_counting[char] = chars_counting.get(char, 0) + 1
    return dict(sorted(chars_counting.items(), key=lambda item: item[1], reverse=True))

def main():
    letters_frequency = get_sorted_letters_freq(FILENAME)
    for char, count in letters_frequency.items():
        print(f'{char}: {count}')

if __name__ == '__main__':
    main()

