print('Начался восьмичасовой рабочий день.')
count = 1
call_from_wife = False #тут объявлена переменная-флаг
count_of_tasks = 0
while count <= 8:
    print(f'{count}-й час')
    try:
        tasks = int(input('Сколько задач решит Максим? '))
        if tasks < 0:
            print('Количество задач не может быть отрицательным')
            continue
        if not call_from_wife: #тут сделана проверка - если флаг "опущен", то задаем вопрос
            call_from_wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): ')) #тут меняем значение флага
    except ValueError:
        print('Ошибка! Введите числа')
        continue
    count += 1
    count_of_tasks += tasks
print(f'Рабочий день закончился. Всего выполнено задач: {count_of_tasks}')
if call_from_wife: #а тут проверяем, поднят или опущен флаг, затем уже принимаем решение - печатать или нет инфу про магазин
    print('Нужно зайти в магазин.')