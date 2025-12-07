import os

def num_validator(message: str, min_value = float('-inf'), max_value = float('inf')) -> int:
    """Валидирует ввод. Нельзя ввести что-либо, кроме целых чисел в указанном диапазоне"""
    while True:
        try:
            num = int(input(message))
            if not (min_value <= num <= max_value):
                print(f'Ошибка! Нужно ввести целое число({min_value} - {max_value})')
                continue
            return num
        except ValueError:
            print(f'Ошибка! Требуется ввести число({min_value} - {max_value})')

def with_separator(func):
    def wrapper(*args, **kwargs):
        print('-' * 25)
        result = func(*args, **kwargs)
        print('-' * 25)
        return result
    return wrapper

def dir_validator(path: str) -> list[str] | None:
    """
    Проверяет наличие и доступ к искомой директории
    :param path: абсолютный путь до директории
    :return: список содержимого директории
    """
    try:
        if not os.listdir(path):
            print(f'Директория {path} пуста')
            return []
        return os.listdir(path)
    except NotADirectoryError:
        print(f'{path} не является директорией')
        return None
    except PermissionError:
        print(f'Нет доступа к директории: {path}')
        return None
    except FileNotFoundError:
        print(f'Директория {path} не найдена')
        return None