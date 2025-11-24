from typing import Any

def create_dict(data: Any, template: dict | None = None) -> dict | None:
    """
    Создает словарь по шаблону
    :param data: данные для проверки на соответствие требуемым типам
    :param template: словарь по шаблону
    :return: обработанные данные
    """
    if isinstance(data, dict):
        return data
    elif isinstance(data, (int, float, str)):
        return {data: data}
    else:
        return None

def data_preparation(old_list: list[Any]) -> list[dict]:
    """
    Создает список с обработанными данными
    :param old_list: исходные данные для обработки
    :return: список с обработанными данными
    """
    new_list = []
    for item in old_list:
        new_item = create_dict(item)
        if new_item:
            new_list.append(new_item)
    return new_list

def main():
    data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]
    handled_data = data_preparation(data)
    print(handled_data)

if __name__ == '__main__':
    main()