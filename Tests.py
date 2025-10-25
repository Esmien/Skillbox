# educational_grant = 10000
# expenses = 12000
parents_money = 0
for month in range(1, 11):
    lost_money = expenses - educational_grant
    print(f'{month} месяц: траты {expenses} рублей, не хватает {lost_money} рублей.')
    expenses += int(expenses*0.03)
    parents_money += lost_money
print(f'Сумма денег, которую необходимо получить у родителей: {parents_money} рублей.')
