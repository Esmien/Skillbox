def get_min_income(incomes: dict) -> tuple[str, float]:
    """Находит фрукт с наименьшей выручкой, возвращает кортеж - фрукт, выручка"""
    min_fruit = min(incomes, key=incomes.get)
    return min_fruit, incomes[min_fruit]

def main():
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
    total = sum(incomes.values())
    min_fruit, min_value = get_min_income(incomes)

    print(f'Общий доход за год составил {total} рублей')
    print(f'Самый маленький доход у {min_fruit}. Он составляет {min_value} рублей')

    incomes.pop(min_fruit)

    print('Итоговый список фруктов:')
    for key, value in incomes.items():
        print(f'{key}\t -\t {value}')

if __name__ == '__main__':
    main()