def with_sets(array_1: list, array_2: list, array_3: list) -> tuple:
    """
    Находит пересечение и разность массивов с использованием множеств
    :param array_1: первый массив
    :param array_2: второй массив
    :param array_3: третий массив
    :return: кортеж из пересечения и разности массивов
    """
    arr1 = set(array_1)
    arr2 = set(array_2)
    arr3 = set(array_3)
    result_1 = arr1.intersection(arr2, arr3)
    result_2 = arr1.difference(arr2, arr3)
    return result_1, result_2

def without_sets(array_1: list, array_2: list, array_3: list) -> tuple:
    """
    Находит пересечение и разность массивов без использования множеств
    :param array_1: первый массив
    :param array_2: второй массив
    :param array_3: третий массив
    :return: кортеж из пересечения и разности массивов
    """
    result_1 = []
    result_2 = []
    for num in array_1:
        if num in array_2 and num in array_3 and num not in result_1:
            result_1.append(num)
        if num not in array_2 and num not in array_3 and num not in result_2:
            result_2.append(num)
    return result_1, result_2
def main():
    array_1 = [1, 2, 3, 4]
    array_2 = [2, 4]
    array_3 = [2, 3]
    set_result_1, set_result_2 = with_sets(array_1, array_2, array_3)
    result_1, result_2 = without_sets(array_1, array_2, array_3)
    print(f"{'Задача 1:':^25}")
    print('Решение без множеств:', *result_1)
    print('Решение с множествами:', *sorted(set_result_1))
    print(f"\n{'Задача 2:': ^25}")
    print('Решение без множеств:', *result_2)
    print('Решение с множествами:', *sorted(set_result_2))


if __name__ == '__main__':
    main()