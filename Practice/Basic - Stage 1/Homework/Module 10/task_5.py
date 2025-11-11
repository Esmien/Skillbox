def sum_of_digits(num):
    summ = 0
    while num > 0:
        summ += num % 10
        num = num // 10
    return summ

while True: #это надо для того, чтобы программа продолжила работать после сработавших исключений
    maximum = 0
    target_num = 0
    try:
        total_nums = int(input('Введите количество чисел: '))
    except ValueError:
        print('Ошибка! Количество должно быть натуральным числом.')
        continue
    if total_nums <= 0:
        print('Количество должно быть натуральным числом.')
        continue

    for _ in range(total_nums):
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Ошибка! Требовалось ввести натуральное число.')
            continue
        if sum_of_digits(num) > maximum:
            maximum = sum_of_digits(num)
            target_num = num
    print(f'Число {target_num} имеет максимальную сумму цифр: {maximum}')
    break