numbers = int(input('Введите число: '))
count = 0
for num in range(1, numbers//2 + 1):
    num *= 2
    print(f'{num}^3 = {num ** 3}')
    count += 1
print(count)