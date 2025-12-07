from utils import num_validator

def show_nums(num: int) -> None:
    """
    Печатает числа от 1 до num используя рекурсию
    :param num: верхняя граница печати
    :return: функция ничего не возвращает
    """
    if num >= 1:
        show_nums(num - 1)
        print(num)


def main():
    num = num_validator('Введите натуральное число: ', 1)
    show_nums(num)

if __name__ == '__main__':
    main()