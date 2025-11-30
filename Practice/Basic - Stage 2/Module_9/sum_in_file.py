import os


INPUT_FILENAME = os.path.abspath(os.path.join('.', 'numbers.txt'))
OUTPUT_FILENAME = os.path.abspath(os.path.join('.', 'result.txt'))

def sum_in_file(filename: str) -> int:
    """
    Считывает данные из файла и возвращает их сумму
    :param filename: имя файла
    :return: сумма данных
    """
    result = 0
    with open(filename, 'r') as f:
        for line in f:
            try:
                result += int(line)
            except ValueError:
                print('Ошибка при чтении данных(получено не число)')
    return result

def save_file(filename: str, data: int) -> None:
    """
    Записывает данные в файл
    :param filename: имя файла
    :param data: данные для записи(целые числа в контексте данной конкретной задачи)
    """
    with open(filename, 'w') as f:
        f.write(str(data))

def main():
    result = sum_in_file(INPUT_FILENAME)
    save_file(OUTPUT_FILENAME, result)

if __name__ == '__main__':
    main()