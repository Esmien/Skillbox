text =  "Меняzzzzzzzzzzzzz зовут Аристарх"
max_len = 0
length_word = 0
for letter in text:
    length_word += 1
    if letter == ' ':
        max_len = length_word - 1 if length_word > max_len else max_len
        length_word = 0
    if length_word > max_len:
        max_len = length_word
print(f'Длина самого длинного слова: {max_len}')