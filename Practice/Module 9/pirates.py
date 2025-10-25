count = 0
for _ in range(10):
    text = input('Введите слово: ')
    if text.lower() == 'карамба':
        count += 1
print(f'\nНа борт попало {count} пиратов!')