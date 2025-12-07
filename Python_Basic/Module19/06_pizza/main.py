from utils import num_validator

def get_order(count: int) -> dict[str, dict[str, int]]:
    """
    Принимает заказ у магазина
    :param count: Количество заказов
    :return: Словарь со всеми заказами, несортированный
    """
    num_word = ['Первый', 'Второй', 'Третий',
                'Четвертый', 'Пятый', 'Шестой',
                'Седьмой', 'Восьмой', 'Девятый', 'Десятый']
    orders = {}
    for i_order in range(count):
        while True:
            order = input(f'{num_word[i_order]} заказ: ')
            if not order.strip():
                print('Ошибка! Пустая строка.')
                continue
            if len(order.strip().split()) != 3:
                print('Ошибка! Ожидается 3 значения: Имя Пицца Количество')
                continue
            name, pizza, cnt_str = order.strip().split()
            if not cnt_str.isdigit() or int(cnt_str) < 1:
                print('Ошибка! Количество должно быть положительным числом.')
                continue
            cnt_pizza = int(cnt_str)
            if name not in orders:
                orders[name] = {}
            orders[name][pizza] = orders[name].get(pizza, 0) + cnt_pizza
            break
    return orders

def sort_orders(orders: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    """
    Сортирует заказы по алфавиту относительно пользователей и наполнения заказов
    :param orders: несортированный валидный словарь с заказами
    :return: отсортированный словарь
    """
    sorted_orders = {}

    for key, value in sorted(orders.items()):
        sorted_orders[key] = dict(sorted(value.items()))
    return sorted_orders

def main():
    count = num_validator('Введите количество заказов (1-10): ', 1, 10)
    result = sort_orders(get_order(count))
    for key, value in result.items():
        print(f'{key}: ')
        for pizza, cnt_pizza in value.items():
            print(f'\t\t{pizza}: {cnt_pizza}')

if __name__ == '__main__':
    main()