def palindrome_check(text):
    """Проверяет, является ли входная строка палиндромом"""
    length = len(text) // 2
    first_half = [text[i] for i in range(length)]
    last_half = [text[i] for i in range(-1, -length-1, -1)]
    return first_half == last_half

word = input("Введите слово: ")
if palindrome_check(word):
    print(f'Слово "{word}" - палиндром.')
else:
    print(f'Слово "{word}" - не палиндром.')