while True:
    try:
        num = int(input("Введите число для рассчетов или 0 для выхода:"))
    except ValueError:
        print('Ошибка! Вы ввели не число, попробуйте ещё раз.')
        continue
    if num == 0:
        break
    num_count = 1
    while num_count <= num:
        print(f'{num_count} ** 3 = {num_count ** 3}')
        num_count += 1