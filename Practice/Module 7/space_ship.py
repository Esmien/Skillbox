count = 0
for _ in range(10):
    try:
        num = int(input('Введите номер человека: '))
    except ValueError:
        print('Ошибка! Номер должен быть числомю')
        continue
    if num > 0 and num % 2 == 0:
        count += 1
print(f'Количество корректных номеров (чётных и положительных): {count}')