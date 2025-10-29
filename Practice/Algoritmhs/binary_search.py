#Тут есть алгоритм бинарного поиска, но помимо него ещё куча хуйни

import random
def menu():
    print('*' * 25)
    print('1. Игрок угадывает')
    print('2. Компьютер угадывает')
    print('3. Выход')
    print('*' * 25)
    print()
while True:
    menu()
    try:
        chase = int(input('Выберите пункт меню: '))
    except ValueError:
        print('Ошибка! Введите целое число!')
        continue
    if chase == 1:
        while True:
            try:
                start = int(input('Введите начало диапазона: '))
                end = int(input('Введите конец диапазона: '))
            except ValueError:
                print('Ошибка! Начало и конец диапазона должны быть целыми числами.')
                continue
            count = 0
            num = random.randint(start, end)
            while True:
                try:
                    user_input = int(input('Введите число: '))
                except ValueError:
                    print('Ошибка! Нужно ввести целое число в указанном диапазоне.')
                    continue
                if user_input == num:
                    count += 1
                    print('Угадал!')
                    print(f'Тебе понадобилось {count} попыток')
                    break
                elif user_input > num:
                    print('Загаданное число меньше твоего.')
                    count += 1
                else:
                    print('Загаданное число больше твоего')
                    count += 1
            break
    elif chase == 2:
        print('Сейчас мы с тобой зададим диапазон')
        print()
        try:
            minimum = int(input('Введи начало диапазона: '))
            maximum = int(input('Введи конец диапазона: '))
        except ValueError:
            print('Ошибка! Начало и конец диапазона должны быть целыми числами')
            continue
        n = (minimum+maximum) // 2
        print(f'Твоё число - {n}?')
        count = 0
        while True:
            count += 1
            try:
                answer = int(input('1 - меньше\n2 - больше\n3 - угадал\n'))
            except ValueError:
                print('Выбор должен быть целым числом!')
                continue
            if answer == 1 and maximum > minimum:
                maximum = n
                n = (minimum+maximum) // 2
                print(f'Твоё число - {n}?')
            elif answer == 2 and minimum < maximum:
                minimum = n
                n = (minimum+maximum) // 2
                print(f'Твоё число - {n}?')
            elif answer == 3:
                print(f'Я угадал за {count} попыток')
                break
            else:
                print('Меня не проведешь! Пожалуйста, отвечай честно!(1-3)')
    elif chase == 3:
        print('До свидания!')
        break
    else:
        print('Такого пункта меню нет!')