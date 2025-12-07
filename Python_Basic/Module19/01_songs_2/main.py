from utils import num_validator

def get_time_of_playback(playlist: dict, songs: list) -> float:
    """
    Считает, сколько времени потребуется на прослушивание выбранных песен
    :param playlist: Плейлист в виде словаря {'title': playback_time}
    :param songs: Выбранные пользователем песни в виде списка [titles]
    :return: Итоговое время воспроизведения
    """
    return sum(playlist[song] for song in songs)
def choice_songs(playlist: dict, size: int) -> list[str]:
    """
    Принимает ввод от пользователя и создает список песен
    :param playlist: Плейлист песен в виде словаря {'title': playback_time}
    :param size: Количество песен в плейлисте, для валидатора ввода, тип int
    :return: Список выбранных пользователем песен
    """
    result = []
    words_presentation = {
          1: 'первой',
          2: 'второй',
          3: 'третьей',
          4: 'четвертой',
          5: 'пятой',
          6: 'шестой',
          7: 'седьмой',
          8: 'восьмой',
          9: 'девятой',
    }
    count = num_validator('Сколько песен выбрать? ', 1, size)
    for i in range(1, count + 1):
        while True:
            song = input(f'Название {words_presentation.get(i, f'{i}-й')} песни: ')
            if song in playlist:
                result.append(song)
                break
            else:
                print(f'Ошибка: песня "{song}" не найдена. Попробуйте снова.')
    return result
def show_playlist(playlist: dict) -> None:
    print(f"{'Список песен':=^40}")
    for key, value in playlist.items():
        print(f'{key} - {value}')
    print(f"{'=' * 40}")
def main():
    violator_songs = {
        'World in My Eyes': 4.86,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.9,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.20,
        'Policy of Truth': 4.76,
        'Blue Dress': 4.29,
        'Clean': 5.83
    }
    size = len(violator_songs)
    show_playlist(violator_songs)
    result = get_time_of_playback(violator_songs, choice_songs(violator_songs, size))
    print(f'Общее время звучания песен: {result} минуты')
if __name__ == '__main__':
    main()