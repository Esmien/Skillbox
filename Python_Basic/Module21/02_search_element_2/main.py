from utils import num_validator

def get_key_and_depth() -> tuple[str, int | None]:
    """
    Запрашивает у пользователя глубину поиска
    Нужна исключительно для валидации ввода отдельно от основного кода
    :return: искомый ключ и глубина поиска
    """

    key = input('Введите искомый ключ: ')
    while True:
        choice = input('Хотите ввести максимальную глубину? Y/N: ').strip().lower()
        if choice == 'y':
            depth = num_validator('Введите максимальную глубину: ', 1)
            return key, depth
        elif choice == 'n':
            return key, None
        else:
            print('Неправильный ввод! Введите "y" или "n"')

def search_key(data: dict, key: str, depth: int | None = None) -> object | None:
    """
    Ищет во вложенном словаре значение по ключу по всем уровням
    :param data: входной словарь
    :param key: ключ, который ищем
    :param depth: максимальная глубина вложенности словаря
    :return: значение искомого ключа в словаре или None, если ключ не найден
    """
    if depth is not None:
        if depth < 1:
            return None
        depth -= 1
    if key in data:
        return data[key]
    for sub_data in data.values():
        if isinstance(sub_data, dict):
            result = search_key(sub_data, key, depth)
            if result is not None:
                return result
    return None

def main():
    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    key, depth = get_key_and_depth()
    result = search_key(site, key, depth)

    if result is not None:
        print(f'Значение ключа: {result}')
    else:
        print('Ключ не найден')

if __name__ == '__main__':
    main()