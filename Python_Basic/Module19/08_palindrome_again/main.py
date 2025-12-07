def check_palindrome(word: str) -> bool:
    """
    Проверяет, можно ли из строки сделать палиндром путем перестановки символов.
    Палиндром возможен, если не более одного символа встречается нечетное число раз
    (этот символ будет в центре палиндрома).
    :param word: Проверяемая строка
    :return: Результат проверки
    """
    chars_dict = {}
    for char in word:
        chars_dict[char] = chars_dict.get(char, 0) + 1
    odd_count = sum(1 for count in chars_dict.values() if count % 2 != 0) # считаем количество символов с нечетными вхождениями
    return odd_count <= 1

def main():
    word = input('Введите строку: ').lower()
    if check_palindrome(word):
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')

if __name__ == '__main__':
    main()