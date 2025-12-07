# Изначально не задалось с неймингом - код выглядел громоздким из-за snake_case, плюс неточности перевода
# Затем я загуглил правильные именования переменных в быстрой сортировке
# Затем разбил одну функцию на две отдельные, с разной логикой

import random

def partition(nums_list: list[int]) -> tuple[list[int], list[int], list[int]]:
    """
    Разбивает исходный список на 3 списка:
    список с элементами меньше опорного, равными опорному и большими опорного
    :param nums_list: исходный список
    :return: 3 списка less, equal, greater
    """
    pivot = nums_list[-1]
    less = [num for num in nums_list if num < pivot]
    greater = [num for num in nums_list if num > pivot]
    equal = [num for num in nums_list if num == pivot]
    return less, equal, greater

def quick_sort(nums_list: list[int]) -> list[int]:
    """
    Рекурсивно сортирует список по возрастанию
    :param nums_list: исходный список
    :return: отсортированный список
    """
    if len(nums_list) <= 1:
        return nums_list
    less, equal, greater = partition(nums_list)
    return quick_sort(less) + equal + quick_sort(greater)

def main():
    nums_list = [random.randint(1, 100) for _ in range(10)]
    print(f'Исходный список: {nums_list}')
    print(f'Отсортированный список: {quick_sort(nums_list)}')

if __name__ == '__main__':
    main()