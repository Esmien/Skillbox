def summa_n(num):
    return int(num * (1 + num) / 2)
while True:
    try:
        num = int(input('Введите число: '))
    except ValueError:
        print('Ошибка! Нужно ввести натуральное число')
        continue
    if num <= 0:
        print('Число должно быть положительным')
        continue
    print(f'Сумма чисел от 1 до {num} равна {summa_n(num)}')
    break