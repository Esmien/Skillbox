def positive(num):
    if num > 0:
        print('Положительное')
def negative(num):
    if num < 0:
        print('Отрицательное')
def test():
    num = None
    while True:
        try:
            num = int(input('Введите число: '))
        except ValueError:
            print('Ошибка! Требуется число')
            continue
        if num == 0:
            print('А про ноль в условии забыли указать?')
            continue
        break
    if num > 0:
        positive(num)
    else:
        negative(num)
test()