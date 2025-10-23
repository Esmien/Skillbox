import random
num = random.randint(1, 10)
count = 0
while True:
    try:
        answer = int(input('Введите число: '))
    except ValueError:
        print('Ошибка, нужно ввести число.')
        continue
    count += 1
    if answer < num:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif answer > num:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f'Вы угадали! Число попыток: {count}')
        break