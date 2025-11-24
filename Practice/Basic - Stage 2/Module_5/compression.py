def compression_string(text):
    if not text:
        return ''

    result = ''
    char = text[0]
    count = 1

    for i in range (1, len(text)):
        if text[i] == char:
            count += 1
        else:
            result += char + str(count)
            char = text[i]
            count = 1
    result += char + str(count)
    return result
input_str = input('Введите строку: ')
encoded = compression_string(input_str)
print(f'Закодированная строка: {encoded}')