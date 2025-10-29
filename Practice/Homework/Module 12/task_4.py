def count_letters(text, number, letter):
    count_number = 0
    count_letter = 0
    for char in text:
        if char == letter:
            count_letter += 1
        if char == number:
            count_number += 1
    print(f'Количество цифр {number}: {count_number}')
    print(f'Количество букв {letter}: {count_letter}')

def main():
    text = input('Введите текст: ').lower()
    number = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ').lower()
    count_letters(text, number, letter)

main()