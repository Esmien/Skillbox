total_hours = int(input('Введите время эксперимента в часах: '))
cells = 1
print(f'Общее время наблюдения: {total_hours}')
print()
for hour in range(1, total_hours // 3 + 1):
    cells *= 2
    print(f'Прошло времени: {hour * 3} часа.')
    print(f'Количество клеток: {cells}')
    print(f'Осталось времени: {total_hours - hour * 3} часа/-ов')
    print()
print('Наблюдение окончено')