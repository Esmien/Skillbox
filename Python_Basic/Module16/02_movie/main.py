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

class MyFilmsCollection:
    def __init__(self):
        self.all_films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
                 'Леон', 'Богемская рапсодия', 'Город грехов',
                 'Мементо', 'Отступники', 'Деревня']
        self.films = []

    def is_film_exist(self, movie):
        """Проверяет, есть ли фильм в коллекции киносервиса"""
        return any(film.lower() == movie.lower() for film in self.all_films)

    def get_original_film_name(self, movie):
        """Делает нормализации названия, то есть:
        не важно, в каком регистре пользователь будет вводить название фильма,
        в списке всегда будут оригинальные"""
        for film in self.all_films:
            if film.lower() == movie.lower():
                return film
        return None

    def get_my_films(self):
        """Геттер списка фильмов пользователя"""
        return self.films

    def add_movie(self, movie):
        """Проверяет регистронезаввисимо, есть ли фильм у пользователя в списке и добавляет, если нет"""
        if any(film.lower() == movie.lower() for film in self.films):
            print('Этот фильм уже в вашей коллекции')
            return False
        else:
            self.films.append(movie)
            # print(f'Фильм "{movie}" добавлен в ваш список!')
            return True

    def show_films(self):
        """Выводит на экран список фильмов в коллекции"""
        print('Ваш список любимых фильмов:', end=' ')
        for film in self.films:
            print(f'{film}', end=', ' if film != self.films[-1] else '')

def main():
    my_films_manager = MyFilmsCollection()
    msg_count_of_films = 'Сколько фильмов хотите добавить? '
    count_of_films = num_validator(msg_count_of_films)
    for _ in range(count_of_films):
        movie = input('Название фильма: ').strip()
        if my_films_manager.is_film_exist(movie):
            movie = my_films_manager.get_original_film_name(movie)
            my_films_manager.add_movie(movie)
        else:
            print('К сожалению, выбранный вами фильм отсутствует в нашей коллекции')
    if my_films_manager.get_my_films():
        my_films_manager.show_films()
    else:
        print('Пусто')

if __name__ == '__main__':
    main()