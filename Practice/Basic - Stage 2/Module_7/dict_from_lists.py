import random

russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
lst_1 = [random.choice(russian_alphabet) for _ in range(10)]
lst_2 = [random.choice(russian_alphabet) for _ in range(10)]
dict_1 = {index: char for index, char in enumerate(lst_1)}
dict_2 = {index: char for index, char in enumerate(lst_2)}

print('Первый список:', lst_1)
print('Второй список:', lst_2)
print()
print('Первый словарь:', dict_1)
print('Второй словарь:', dict_2)