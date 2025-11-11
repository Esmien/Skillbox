height = int(input('Введите размер лесенки: '))
for row in range (1, height+1):
    for col in range(0, row):
        print(row, end='\t')
    print()