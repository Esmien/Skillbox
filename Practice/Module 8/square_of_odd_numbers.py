numbers = int(input('Введите число: '))
for num in range(1, numbers+1, 2):
    print(f'{num}^2 = {num ** 2}')