width, length = 15, 20
x, y = width // 2, length // 2
while True:
    print(f'[Программа]: Марсоход находится на позиции {x}, {y}')
    move_key = input('[Оператор]: ')
    if move_key == 'W' and y < length:
        y += 1
    elif move_key == 'S' and y > 0:
        y -= 1
    elif move_key == 'D' and x < width:
        x += 1
    elif move_key == 'A' and x > 0:
        x -= 1
    elif move_key == 'Q':
        print('\nВсего доброго! ')
        break
    else:
        print('Невозможно выполнить команду!')