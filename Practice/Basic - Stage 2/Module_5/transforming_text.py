text = input('Введите строку: ')
count_up = len([char for char in text if char.isupper()])
count_low = len([char for char in text if char.islower()])
if count_up > count_low:
    result = text.upper()
else:
    result = text.lower()
print(result)