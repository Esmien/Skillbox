text = input('Введите текст: ')
print('Ответ:', end=' ')
for index, char in enumerate(text):
    if char == '~':
        print(index, end=' ')