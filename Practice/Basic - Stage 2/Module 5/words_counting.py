words = [input('Введите слово: ')
         for _ in range(int(input('Сколько слов? ')))]
text = input('Введите текст: ')
words_count = {word: text.count(word) for word in words}
for key, value in words_count.items():
    print(f'{key}: {value}')