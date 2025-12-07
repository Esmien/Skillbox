def my_sum(*args: int | float | list | tuple | set | frozenset) -> int:
    """
    Считает сумму любого количества переданных аргументов,
    раскрывая вложенные структуры
    :param args: списки, списки списков, числа, множества чисел, в любой комбинации
    :return: итоговая сумма
    """
    total = 0
    for item in args:
        if isinstance(item, (list, tuple, set, frozenset)):
            total += my_sum(*item)
        elif isinstance(item, int, float):
            total += item
    return total