begin = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
sum_of_nums = 0
count = 0
print('Числа из отрезка, которые делятся на 3:')
for num in range(begin, end + 1):
    if num % 3 == 0:
        sum_of_nums += num
        print(num)
        count += 1
print(f'Среднее арифметическое этих чисел: {sum_of_nums / count}')