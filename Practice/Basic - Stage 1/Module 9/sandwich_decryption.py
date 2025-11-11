word = input('Введите зашифрованное слово: ')
odd_letters = ''
even_letters = ''
count = 1
for letter in word:
    if count % 2 != 0:
        odd_letters += letter
    else:
        even_letters = letter + even_letters
    count += 1
print('Расшифрованное слово: ', odd_letters + even_letters)