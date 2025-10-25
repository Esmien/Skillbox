timer = int(input('Введите время разогрева(с): '))
print(f'Время разогрева - {timer} сек.')
print()
is_ready = False
for second in range(timer, 1, -1):
    print(f'Осталось {second} секунд')
    is_ready = int(input('Введите 1, если еда готова, или 0, чтобы продолжить: 0 '))
    if is_ready:
        print(f'Ваша еда готова, можете забрать! Таймер был прерван на {second} секундах.')
        break
else:
    print()
    print('Ваша еда готова. Осторожно, горячo!')