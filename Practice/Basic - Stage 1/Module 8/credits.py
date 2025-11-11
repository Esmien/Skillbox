persons = int(input('Введите количество должников: '))
total_credit = 0
for person in range(0, persons, 5):
    print(f'Должник с номером {person}')
    credit = int(input('Сколько должны? '))
    total_credit += credit
print()
print(f'Общая сумма долгов: {total_credit}')