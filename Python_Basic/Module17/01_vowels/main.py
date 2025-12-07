vowels = list('аеёиоуыэюя')
text = input('Введите текст: ').strip().lower()
chars = [char for char in text if char in vowels]
print(f'Список гласных букв: {chars}')
print(f'Длина списка: {len(chars)}')