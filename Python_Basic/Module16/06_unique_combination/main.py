def merge_sorted_lists(list_1, list_2):
    """Пошагово сравнивает элементы двух списков, проверяя,
    не является ли последний элемент итогового списка таким же, как добавляемый
    Это работает, потому что на входе два ОТСОРТИРОВАННЫХ списка,
    поэтому мы точно добавляем туда элемент, который больше последнего
    """
    result = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            if not result or result[-1] != list_1[i]:
                result.append(list_1[i])
            i += 1
        elif list_1[i] > list_2[j]:
            if not result or result[-1] != list_2[j]:
                result.append(list_2[j])
            j += 1
        else:
            if not result or result[-1] != list_1[i]:
                result.append(list_1[i])
                i += 1
                j += 1
    while i < len(list_1):
        if not result or result[-1] != list_1[i]:
            result.append(list_1[i])
            i += 1
    while j < len(list_2):
        if not result or result[-1] != list_2[j]:
            result.append(list_2[j])
            j += 1
    return result
# Пример использования:
list1 = [1, 3, 7, 9]
list2 = []
merged = merge_sorted_lists(list1, list2)
print(merged)