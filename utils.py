def num_validator(message: str, min_value = float('-inf'), max_value = float('inf')) -> int:
    """Валидирует ввод. Нельзя ввести что-либо, кроме целых чисел в указанном диапазоне"""
    while True:
        try:
            num = int(input(message))
            if not (min_value <= num <= max_value):
                print(f'Ошибка! Нужно ввести целое число({min_value} - {max_value})')
                continue
            return num
        except ValueError:
            print(f'Ошибка! Требуется ввести число({min_value} - {max_value})')