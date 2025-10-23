minimum = 1
maximum = 1000
n = (minimum+maximum) // 2
print(f'Твоё число - {n}?')
count = 0
while True:
    count += 1
    answer = int(input('1 - меньше\n2 - больше\n3 - угадал\n'))
    if answer == 1:
        maximum = n
        n = (minimum+maximum) // 2
        print(f'Твоё число - {n}?')
    elif answer == 2:
        minimum = n
        n = (minimum+maximum) // 2
        print(f'Твоё число - {n}?')
    else:
        print(f'Я угадал за {count} попыток')
        break