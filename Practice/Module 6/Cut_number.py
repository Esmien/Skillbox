while True:
    try:
        num = int(input("Введите натуральное число: "))
        temp = num
        digits = []
    except ValueError:
        print('Неправильный формат')
        continue
    if num <= 0:
        break
    else:
        while temp > 0:
            digits.append(temp % 10)
            temp = temp // 10
        digits.reverse()
        for digit in digits:
            print(f'{digit} ', end='')
        break
