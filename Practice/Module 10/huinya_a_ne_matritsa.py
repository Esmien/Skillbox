size = int(input('Введите размер "матрицы": '))
for i in range(1, size + 1):
    for j in range(1, size + 1):
        if j % 3 == 0:
            print(j, end='\t')
        else:
            print(i, end='\t')
    print()