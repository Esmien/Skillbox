while True:
    try:
        deposit = int(input('Вклад в банке: '))
        rate = int(input('Проценты: '))
        total = int(input('Порог вклада: '))
        if (deposit or rate or total) < 0:
            print('Введенные данные не могут быть отрицательными, попробуйте ещё раз.')
            continue
    except ValueError:
        print('Ошибка! Введите числа!')
        continue
    count = 0
    dep = deposit
    while dep < total:
        dep = int(deposit + deposit * rate / 100)
        print(f'{count+1} год. {deposit} + {rate}% = {dep}')
        deposit = dep
        count += 1
    print(f'Кол-во лет для достижения порога: {count}')
    break