def get_total_goods(goods: dict, store: dict) -> dict[str, tuple[int, int]]:
    """
    Подсчитывает количество и общую стоимость товаров на складе
    :param goods: таблица товаров вида {название: код}
    :param store: Входные данные в виде структуры данных вида {goods_code: [{goods_data}]}
    :return: Словарь из названия товара и кортежа с количеством и общей стоимостью
    """
    total_store = {}
    for name, code in goods.items():
        items = store[code]
        quantity = sum(item['quantity'] for item in items)
        total_amount = sum(item['price'] * item['quantity'] for item in items)
        total_store[name] = (quantity, total_amount)
    return total_store
def get_word_form(number: int, word_dict: dict) -> str:
    """
    Возвращает правильную форму сопутствующего слова в зависимости от числа
    :param number: Число для обработки
    :param word_dict: Словарь, по которому выбираем форму
    :return: Правильная форма сопутствующего слова
    """
    if 11 <= number % 100 <= 19:
        return word_dict[5]
    last_digit = number % 10
    if last_digit == 1:
        return word_dict[1]
    elif 2 <= last_digit <= 4:
        return word_dict[2]
    else:
        return word_dict[5]

def main():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }

    translate_rub = {1: 'рубль', 2: 'рубля', 5: 'рублей', }
    translate_count = {1: 'штука', 2: 'штуки', 5: 'штук', }
    result = get_total_goods(goods, store)
    for name, (total_items, total_amount) in result.items():
        tsl_rub = get_word_form(total_amount, translate_rub)
        tsl_count = get_word_form(total_items, translate_count)
        print(f'{name} — {total_items} {tsl_count}, стоимость {total_amount} {tsl_rub}')

if __name__ == '__main__':
    main()