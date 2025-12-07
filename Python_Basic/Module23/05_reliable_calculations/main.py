def get_sage_sqrt(num: float) -> float | str:
    try:
        if not isinstance(num, (float, int)):
            raise TypeError('Ошибка! Требуется число!')
        if num < 0:
            raise ValueError('Ошибка! Ожидается неотрицательное число!')
        return round(num ** 0.5, 4)
    except ValueError as e:
        return e.args[0]
    except TypeError as e:
        return e.args[0]
    except Exception as e:
        return e.args[0]

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")