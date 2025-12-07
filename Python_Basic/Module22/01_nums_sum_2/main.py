import os


INPUT_FILE_PATH = os.path.abspath(os.path.join('.', 'numbers.txt'))
OUTPUT_FILE_PATH = os.path.abspath(os.path.join('.', 'answer.txt'))

def get_sum_of_nums(file_path: str) -> tuple[int, int]:
    """
    Считает сумму чисел в файле и количество ошибок
    :param file_path: имя файла
    :return: кортеж из суммы чисел и количества ошибок
    """
    result = 0
    count_of_errors = 0
    with open(file_path, 'r') as f:
        for line in f:
            for elem in line.split():
                try:
                    result += int(elem)
                except ValueError:
                    print(f'Ошибка: {elem} не является числом')
                    count_of_errors += 1
    return result, count_of_errors

def write_answer(file_path: str, result: int, count_of_errors: int) -> None:
    """
    Записывает сумму чисел в файл, печатает в консоль количество ошибок
    :param file_path: имя файла
    :param result: сумма чисел
    :param count_of_errors: количество ошибок
    """
    with open(file_path, 'w') as f:
        f.write(str(result))
    print('Ошибок чтения:', count_of_errors)

def main():
    result, count_of_errors = get_sum_of_nums(INPUT_FILE_PATH)
    write_answer(OUTPUT_FILE_PATH, result, count_of_errors)

if __name__ == '__main__':
    main()