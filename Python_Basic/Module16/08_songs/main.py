def num_validator(message):
    """Валидирует ввод. Нельзя ввести что-либо, кроме чисел от 1 до 9 в данном конкретном случае"""
    while True:
        try:
            num = int(input(message))
            if not (0 < num <= 9):
                print('Ошибка! Нужно ввести положительное число(1-9)')
                continue
        except ValueError:
            print('Ошибка! Требуется ввести число(1-9)')
            continue
        return num

def time_of_play(song, songs_list):
    """Ищет время проигрывания искомой песни, также участвует в проверке на включение в список"""
    for song_name, time in songs_list:
        if song_name.lower() == song.lower():
            return time
    return None

def main():
    violator_songs = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83]
    ]
    count_songs = num_validator('Сколько песен выбрать? ')
    total_time = 0
    for i in range(1, count_songs+1):
        song = input(f'Название {i}-й песни: ').strip()
        time = time_of_play(song, violator_songs)
        if time: #проверка на включение в список песен
            total_time += time
        else:
            print('Такой песни нет в списке')
    print(f'Общее время звучания песен: {round(total_time, 2)} минуты.')

if __name__ == '__main__':
    main()
