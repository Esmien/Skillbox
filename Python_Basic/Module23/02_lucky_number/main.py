import random
from utils import num_validator


OUTPUT_FILE = 'out_file.txt'

def get_random_exception():
    """Выбирает исключение из набора исключений и с вероятностью 1к13 выбрасывает его"""
    unlucky_exceptions = (ValueError, TypeError, IndexError)
    if random.randint(1, 13) == 1:
        exception = random.choice(unlucky_exceptions)
        try:
            raise exception
        except exception:
            print(f'Вас постигла неудача!')
        return True
    return False

def add_num_to_file(filename: str, num_to_add: int) -> None:
    """Добавляет число в файл"""
    with open(filename, 'a') as f:
        f.write(str(num_to_add)+'\n')

def main():
    num = 0

    while num < 777:
        num_to_add = num_validator('Введите число: ', 0)

        if get_random_exception():
            break

        num += num_to_add
        add_num_to_file(OUTPUT_FILE, num_to_add)
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')

if __name__ == '__main__':
    main()