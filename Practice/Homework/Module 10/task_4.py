def prime_number(number):
    if number < 2:
        return False
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
    return True
while True:

    try:
        total_nums = int(input('Введите количество чисел: '))
    except ValueError:
        print('Ошибка! Количество должно быть натуральным числом.')
        continue
    if total_nums <= 0:
        print('Количество должно быть натуральным числом.')
        continue
    else:
        count = 0
        for _ in range(total_nums):
            try:
                num = int(input('Введите число: '))
            except ValueError:
                print('Ошибка! Требуется ввести число')
                continue
            if prime_number(num):
                count += 1
        print(f'Количество простых чисел в последовательности: {count}')
    break