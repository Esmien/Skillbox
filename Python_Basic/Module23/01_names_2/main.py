LOG_FILE = 'errors.log'
INPUT_FILE = 'people.txt'

def save_log(err_msg: str) -> None:
    """Добавляет в файл логирования текст ошибки"""
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(err_msg + '\n')

def get_sym_count(filename: str) -> int:
    """
    Считает количество символов в файле. Пробрасывает ValueError, если длина строки меньше 3
    :param filename: имя файла
    :returns количество печатных символов в файле
    """
    line_count = 0
    total_sym_count = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            try:
                if len(line.strip()) < 3:
                    raise ValueError
            except ValueError:
                err_msg = f'Ошибка: менее трёх символов в строке {line_count}.'
                print(err_msg)
                save_log(err_msg)
            finally:
                total_sym_count += len(line.strip())

    return total_sym_count

def main():
    total_sym_count = get_sym_count(INPUT_FILE)
    print('Общее количество символов:', total_sym_count)

if __name__ == '__main__':
    main()