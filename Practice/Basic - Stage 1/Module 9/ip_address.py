num = int(input('Введите число: '))
step = int(input('Введите шаг '))
last_block = 0
for _ in range(3):
    print(num, end='.')
    last_block += num
    num += step
print(last_block)