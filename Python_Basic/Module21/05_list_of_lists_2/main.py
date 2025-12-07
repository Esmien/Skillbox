def unpack_list(data: list) -> list:
    """
    Разворачивает вложенные списки в один общий список
    :param data: структура вложенных списков
    :return: развернутый список
    """
    result = []
    for item in data:
        if not isinstance(item, list):
            result.append(item)
        else:
            result.extend(unpack_list(item))
    return result

def main():
    nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
                 [[11, 12, 13], [14, 15], [16, 17, 18]]]

    print('Ответ:', unpack_list(nice_list))

if __name__ == '__main__':
    main()