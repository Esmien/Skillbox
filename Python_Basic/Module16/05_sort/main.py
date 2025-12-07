def bubble_sorting(data):
    """Сортирует пузырьковым способом. Не стал копировать решение selection_sort из примера на уроке"""
    for i in range(len(data)):
        is_sorted = False #флаг для преждевременного завершения цикла в случае окончания сортировки
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                is_sorted = True
        if not is_sorted:
            break

data = [5, 4, 3, 2, 1]
bubble_sorting(data)
print(data)
