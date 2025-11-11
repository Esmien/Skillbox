is_true = True
while is_true:
    try:
        height = int(input('Введите высоту пирамидки: '))
    except ValueError:
        print('Ошибка! Высота должна быть натуральным числом!')
        continue
    for row in range(1, height + 1):
        for col in range(height - row):
            print(" ", end="")
        for col in range(2 * row - 1):
            print("#", end="")
        print()
    print()
    while True:
        chase = input('Построить ещё одну? y/n ').lower()
        if chase == 'y':
            break
        elif chase == 'n':
            is_true = False
            print('До свидания!')
            break
        else:
            print('Неправильный ввод, попробуйте ещё раз')