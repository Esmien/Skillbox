from typing import Any
def is_prime(number: int) -> bool:
    """ Проверяет число на 'простоту' """
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
    else:
        return False
    return True

def crypto(data: Any) -> list[Any] | str:
    """
    Создает список элементов итерируемого объекта, у которых индекс - простое число
    :param data: любой итерируемый объект
    :return: список с отфильтрованными элементами или сообщение об ошибке
    """
    try:
        return [element
                for index, element in enumerate(data.values()
                                                if isinstance(data, dict) # для словаря будем выводить значения, а не ключи
                                                else data) if is_prime(index)]
    except Exception as e:
        return f'Ошибка! Передан неверный тип данных: {e}'

def main():
    data = {0: 5, 1: 7, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7: 13, 8: 14}
    print(crypto(data))

if __name__ == "__main__":
    main()