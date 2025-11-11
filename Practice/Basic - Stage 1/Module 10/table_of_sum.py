num = int(input('Введите число: '))
for i in range(num):
    for j in range(0, -num, -1):
        print(i+j, end='\t')
    print()