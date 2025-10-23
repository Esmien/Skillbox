numbers = int(input('Введите число: '))
count = 0
for num in range(1, numbers, 2):
    print(f'{num}^2 = {num ** 2}')
    count += 1
print(count)
