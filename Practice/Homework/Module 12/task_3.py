def with_separator(func):
    def wrapper(*args, **kwargs):
        print('-' * 25)
        result = func(*args, **kwargs)
        print('-' * 25)
        return result
    return wrapper

def addition(num):
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result

def minimum(num):
    result = num
    while num > 0:
        if num % 10 < result:
            result = num % 10
        num = num // 10
    return result

def maximum(num):
    result = 0
    while num > 0:
        if num % 10 > result:
            result = num % 10
        num = num // 10
    return result

@with_separator
def menu():
    print('=== Калькулятор ===')
    print('1. Посчитать сумму цифр в числе')
    print('2. Найти максимальную цифру в числе')
    print('3. Найти минимальную цифру в числе')
    print('4. Выход')

def main():
    while True:
        menu()
        try:
            choice = int(input('Выберите действие(1-4):'))
            a = int(input('Введите число: '))
        except ValueError:
            print('Ошибка! Требуется ввести числа!')
            continue
        if choice == 1:
            print(f'Сумма равна: {addition(a)}\n')
        elif choice == 2:
            print(f'Максимальная цифра: {maximum(a)}\n')
        elif choice == 3:
            print(f'Минимальная цифра равна: {minimum(a)}\n')
        elif choice == 4:
            print('До свидания!')
            break
        else:
            print('Такого пункта меню нет, попробуйте еще раз')

main()