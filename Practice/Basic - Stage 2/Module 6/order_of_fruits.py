def count_income(order: dict, incomes: dict) -> float:
    """
    Считает итоговую выручку по заказу
    :param order: простой словарь типа "товар - количество" {str: int}
    :param incomes: словарь типа "номенклатура - цена" {str: float}
    :return: итоговая сумма покупок float
    """
    return sum(order[item] * incomes.get(item, 0) for item in order)

def main():
    order = {
             'apple': 2,
             'banana': 3,
             'pear': 1,
             'watermelon': 10,
             'chocolate': 5
    }

    incomes = {
        'apple': 5600.20,
        'orange': 3500.45,
        'banana': 5000.00,
        'bergamot': 3700.56,
        'durian': 5987.23,
        'grapefruit': 300.40,
        'peach': 10000.50,
        'pear': 1020.00,
        'persimmon': 310.00,
    }
    result = count_income(order, incomes)
    print(result)

if __name__ == '__main__':
    main()