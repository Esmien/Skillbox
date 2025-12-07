# Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2
#
# Последовательность: [1, 2, 1, 2, 2]
# Нужно приписать чисел: 3
# Сами числа: [1, 2, 1]
def num_validator(message):
    """Валидирует ввод. Нельзя ввести что-либо, кроме положительных чисел"""
    while True:
        try:
            num = int(input(message))
            if num < 1:
                print('Ошибка! Количество чисел в последовательности должно быть положительным')
                continue
            return num
        except ValueError:
            print(f'Ошибка! Требуется ввести число')
def is_simmetrical(sequence):
    """Проверяет на симметричность"""
    return sequence == sequence[::-1]
def simmetrical_seq(sequence):
    """Считает, какие числа и сколько нужно добавить к последовательности"""
    if len(sequence) == 0:
        print('Пустая последовательность')
        return
    if is_simmetrical(sequence):
        print(f'Последовательность: {sequence}')
        print('Последовательность симметричная, ничего не нужно дописывать')
        return
    for i in range(1, len(sequence) + 1):
        add_numbers = sequence[:i][::-1]
        new_sequence = sequence + add_numbers
        if is_simmetrical(new_sequence):
            print(f'Последовательность: {sequence}')
            print(f'Нужно приписать чисел: {len(add_numbers)}')
            print(f'Сами числа: {add_numbers}')
            return
def main():
    len_of_sequence = num_validator('Кол-во чисел: ')
    sequence = []
    for i in range(len_of_sequence):
        num = num_validator('Число: ')
        sequence.append(num)
    simmetrical_seq(sequence)

if __name__ == '__main__':
    main()