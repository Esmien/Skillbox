# Кол-во человек: 5
# Какое число в считалке? 7
# Значит, выбывает каждый 7-й человек
#
# Текущий круг людей: [1, 2, 3, 4, 5]
# Начало счёта с номера 1
# Выбывает человек под номером 2
#
# Текущий круг людей: [1, 3, 4, 5]
# Начало счёта с номера 3
# Выбывает человек под номером 5
#
# Текущий круг людей: [1, 3, 4]
# Начало счёта с номера 1
# Выбывает человек под номером 1
#
# Текущий круг людей: [3, 4]
# Начало счёта с номера 3
# Выбывает человек под номером 3
#
# Остался человек под номером 4
def num_validator(message):
    """Валидирует ввод. Нельзя ввести что-либо, кроме положительных чисел"""
    while True:
        try:
            num = int(input(message))
            if num < 1:
                print('Ошибка! Количество детей должно быть положительным')
                continue
            return num
        except ValueError:
            print(f'Ошибка! Требуется ввести число')
def exclusion(num, count_children):
    """Считает и удаляет 'проигравшего ребёнка' """
    idx = 0
    children = list(range(1, count_children + 1))
    print(f'Текущий круг людей: {children}')
    while len(children) > 1:
        print(f'Начало счёта с номера {children[idx]}')
        idx = (idx + num- 1) % len(children)
        excluded = children[idx]
        print(f'Выбывает человек под номером {excluded}')
        print()
        children.remove(excluded)
        idx %= len(children)
        if len(children) > 1:
            print(f'Текущий круг людей: {children}')
        else:
            print(f'Остался человек под номером {children[0]}')

def main():
    count_of_children = num_validator('Кол-во человек: ')
    rhyme_cnt = num_validator('Какое число в считалке? ')
    print(f'Значит, выбывает каждый {rhyme_cnt}-й человек')
    print()
    exclusion(rhyme_cnt, count_of_children)

if __name__ == '__main__':
    main()