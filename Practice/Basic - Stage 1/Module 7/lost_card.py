N = int(input('Введите количество карточек: '))
sum_ids_of_cards = sum(card for card in range(1, N+1))
for card in range(1, N):
    exist_card = int(input('Введите номер оставшейся карточки: '))
    sum_ids_of_cards -= exist_card
print(f'Номер пропавшей карточки: {sum_ids_of_cards}')