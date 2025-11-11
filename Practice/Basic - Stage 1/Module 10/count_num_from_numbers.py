numbers = []
count = 0
while True:
    try:
        numeral = int(input('Введите число (для завершения введите 0): '))
        if numeral == 0:
            break
        numbers.append(abs(numeral))
    except ValueError:
        print('Я просил целое число!')
while True:
    try:
        number = int(input('Введите искомую цифру: '))
        if 0 <= number <= 9:
            break
        else:
            print('Лошара, цифра - это не число!')
    except ValueError:
        print('Введите корректную цифру!')
for num in numbers:
    while num > 0:
        if num % 10 == number:
            count += 1
        num //= 10
print(f'Цифра {number} встречается {count} раз(а)')