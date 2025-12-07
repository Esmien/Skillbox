def get_modified_data(data: dict) -> list[tuple]:
    """
    Модифицирует данные из словаря путем объединения кортежей
    :param data: исходный словарь
    :return: список с модифицированным представлением исходных данных
    """
    return [key + value for key, value in data.items()]

def main():
    players = {
        ("Ivan", "Volkin"): (10, 5, 13),
        ("Bob", "Robbin"): (7, 5, 14),
        ("Rob", "Bobbin"): (12, 8, 2)
    }
    print(get_modified_data(players))

if __name__ == '__main__':
    main()