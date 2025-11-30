import os

def get_sum(data: list) -> int:
    total = 0
    for line in data:
        try:
            total += int(line.split()[-1])
        except ValueError:
            print('Ошибка в записи данных')
    return total

def get_difference(data: list) -> int:
    difference = 0
    for line in data:
        try:
            difference -= int(line.split()[-1])
        except ValueError:
            print('Ошибка в записи данных')
    return difference

def get_multiplication(data: list) -> int:
    multiplication = 1
    for line in data:
        try:
            multiplication *= int(line.split()[-1])
        except ValueError:
            print('Ошибка в записи данных')
    return multiplication

def main():
    filename_1 = os.path.abspath(os.path.join('.', 'task', 'group_1.txt'))
    filename_2 = os.path.abspath(os.path.join('.', 'task', 'Additional_info', 'group_2.txt'))
    with open(filename_1, 'r', encoding='utf-8') as f1, open(filename_2, 'r', encoding='utf-8') as f2:
        file_1 = f1.readlines()
        file_2 = f2.readlines()

    total = get_sum(file_1)
    difference = get_difference(file_1)
    multiplication = get_multiplication(file_2)

    print(total)
    print(difference)
    print(multiplication)

if __name__ == '__main__':
    main()
