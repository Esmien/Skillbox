from typing import Any

def universal_script(data: Any) -> list[Any] | str:
    """
    Возвращает элементы с четными индексами в итерируемых объектах
    :param data: необработанные, сырые данные
    :return: либо список элементов, либо сообщение об ошибке
    """
    try:
        if isinstance(data, dict):
            data = data.values()
        return [elem for index, elem in enumerate(data) if index % 2 == 0]
    except TypeError:
        return 'Передан неитерируемый тип данных'