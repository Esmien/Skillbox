def get_actual_list(video_cards):
    actual_list = [video_card for video_card in video_cards if video_card is not max(video_cards)]
    return actual_list
def num_validator(message):
    while True:
        try:
            num = int(input(message))
            if num < 0:
                print('Ошибка! Нужно ввести положительное число')
                continue
        except ValueError:
            print('Ошибка! Требуется ввести число')
            continue
        return num
def main():
    video_cards = []
    msg_about_count = 'Количество видеокарт: '
    count_of_cards = num_validator(msg_about_count)
    for count in range(1, count_of_cards+1):
        msg_about_card = f'{count} Видеокарта: '
        video_cards.append(num_validator(msg_about_card))
    print(f'Старый список видеокарт: {video_cards}')
    print(f'Новый список видеокарт: {get_actual_list(video_cards)}')

if __name__ == '__main__':
    main()