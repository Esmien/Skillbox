def choice_validator():
   while True:
        num = input('Команды:'
                    '\n1. Добавить'
                    '\n2. Вставить'
                    '\n3. Удалить'
                    '\n4. Выход\n')
        try:
            num = int(num)
            if num in range(1, 5):
                return num
            else:
                print('Нет такого пункта меню, попробуйте еще раз(1-4) ')
        except ValueError:
            print('Ошибка! Нужно ввести число')
class MyFilmsCollection:
    def __init__(self):
        self.all_films = [
            'Крепкий орешек', 'Назад в будущее', 'Таксист',
            'Леон', 'Богемская рапсодия', 'Город грехов',
            'Мементо', 'Отступники', 'Деревня',
            'Проклятый остров', 'Начало', 'Матрица'
        ]
        self.films = []
    def is_film_exist(self, movie):
        return any(film.lower() == movie.lower() for film in self.all_films)
    def get_original_film_name(self, movie):
        for film in self.all_films:
            if film.lower() == movie.lower():
                return film
        return None
    def get_my_films(self):
        return self.films
    def add_movie(self, movie):
        if any(film.lower() == movie.lower() for film in self.films):
            print('Этот фильм уже в вашей коллекции')
            return False
        else:
            self.films.append(movie)
            print(f'Фильм "{movie}" добавлен в ваш список!')
            return True
    def remove_film(self, movie):
        for film in self.films:
            if film.lower() == movie.lower():
                self.films.remove(film)
                print(f'Фильм "{film}" удалён из вашего списка!')
                return
        print(f'Фильм "{movie}" не найден в вашей коллекции!')
    def insert_film(self, movie, position):
        if any(film.lower() == movie.lower() for film in self.films):
            print('Этот фильм уже в вашей коллекции')
            return False
        else:
            self.films.insert(position - 1, movie)
            print(f'Фильм "{movie}" вставлен в ваш список на позицию {position}!')
            return True
    def show_films(self):
        for i, film in enumerate(self.films, 1):
            print(f'{i}. {film}')
def main():
    my_films_manager = MyFilmsCollection()
    while True:
        print('Ваш текущий топ фильмов:')
        if my_films_manager.get_my_films():
            my_films_manager.show_films()
        else:
            print('Пусто')
        movie = input('\nНазвание фильма: ').strip()
        if my_films_manager.is_film_exist(movie):
            movie = my_films_manager.get_original_film_name(movie)
            choice = choice_validator()

            if choice == 1:
                my_films_manager.add_movie(movie)
            elif choice == 2:
                while True:
                    try:
                        position = int(input(f'Введите позицию, на которую хотите вставить ваш фильм(1-{len(my_films_manager.get_my_films()) + 1}): '))
                        if position < 1 or position > len(my_films_manager.get_my_films()) + 1:
                            print('К сожалению, невозможно вставить фильм на выбранную позицию, так как она вне допустимого диапазона. Попробуйте ещё раз')
                            continue
                    except ValueError:
                        print('Ошибка! Позиция должна быть числом! попробуйте ещё раз')
                        continue
                    if not my_films_manager.insert_film(movie, position):
                        break
                    break
            elif choice == 3:
                my_films_manager.remove_film(movie)
            elif choice == 4:
                print('До свидания!')
                break
        else:
            print('К сожалению, выбранный вами фильм отсутствует в нашей коллекции')

if __name__ == '__main__':
    main()