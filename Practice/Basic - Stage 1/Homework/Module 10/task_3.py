def borders(width, height):
    """Принимает ширину и высоту, рисует прямоугольник"""
    for row in range(height):
        for col in range(width):
            if col == 0 or col == width - 1:
                print('|', end='')
            elif row == 0 or row == height - 1:
                print('-', end='')
            else:
                print(' ', end='')
        print()
is_true = True #флаг для выхода из программы
while True:
    try:
        user_input_width = int(input('Введите ширину(целое положительное число): '))
        user_input_height = int(input('Введите высоту(целое положительное число): '))
    except ValueError:
        print('Ошибка! Высота и ширина должны быть положительными целыми числами!')
        continue
    if user_input_width <=0 or user_input_height <= 0:
        print('Я же просил положительное! Попробуте ещё раз')
        continue

    borders(user_input_width, user_input_height) #вызов функции для отрисовки

    while True:
        chase = input('Попробуем ещё?(y/n)').lower()
        if chase == 'y':
            print()
            break
        elif chase == 'n':
            print('До свидания!')
            is_true = False
            break
        else:
            print('Неверный ввод')
            continue
    if not is_true:
        break