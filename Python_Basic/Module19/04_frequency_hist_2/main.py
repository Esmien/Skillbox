def get_dictionary(text: str) -> dict[str, int]:
    """
    Считает частоту каждого символа в строке
    :param text: входная строка
    :return: словарь символов с частотами
    """
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def invert_dict(dictionary: dict[str, int]) -> dict[int, list[str]]:
    """
    Собирает буквы с одинаковой частотой в список и использует его в качестве значения ключа с частотой
    :param dictionary: словарь типа {char: freq}
    :return: Словарь, в котором ключи - частота, а значения - список символов с этой частотой
    """
    inverted = {}
    for char, freq in dictionary.items():
        if freq not in inverted:
            inverted[freq] = []
        inverted[freq].append(char)
    return inverted
def main():
    text = input('Введите текст: ').capitalize() #использую исключительно потому что в условии в примере "З" заглавная при выводе
    dictionary = get_dictionary(text)
    char_freq = invert_dict(dictionary)
    print('Оригинальный словарь частот:')
    for char, freq in dictionary.items():
        print(f'{char} : {freq}')
    print('\nИнвертированный словарь частот:')
    for freq, chars in char_freq.items():
        print(f'{freq} : {chars}')

if __name__ == '__main__':
    main()