boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
is_solution = False
if not (boys > (2 * girls) or girls > (2 * boys)):
    is_solution = True
if is_solution:
    if girls >= boys:
        k = girls - boys
        result = ('GBG' * k) +('GB' * (boys - k))
    else:
        k = boys - girls
        result = ('BGB' * k) + ('BG' * (girls - k))
    print(result)
else:
    print('Решений нет')