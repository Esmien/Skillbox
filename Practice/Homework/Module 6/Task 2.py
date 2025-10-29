def count_of_letters(num):
    if num:
        result = 0
    else:
        result = 1
    while num > 0:
        result +=1
        num //=10
    return result
while True:
    try:
        number = int(input('Введите число: '))
        if number < 0:
            print('Сожалею, но программа работает только с положительными числами.')
            continue
        else:
            print(f'Кол-во цифр в числе: {count_of_letters(number)}')
            break
    except ValueError:
        print('Ошибка! Требуется число!')