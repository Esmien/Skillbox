import random
def with_separator(func):
    """Рисует разделители"""
    def wrapper(*args, **kwargs):
        print('-' * 25)
        result = func(*args, **kwargs)
        print('-' * 25)
        return result
    return wrapper

class RockPaperScissor:
    def __init__(self):
        self.computer_choice = None
        self.user_choice = None

    def user(self):
        """Принимает выбор игрока"""
        while True:
            try:
                self.user_choice = int(input('Выберите действие:\n'
                                             '1. Камень\n'
                                             '2. Ножницы\n'
                                             '3. Бумага\n'))
            except ValueError:
                print('Ошибка! Нужно ввести число')
                continue
            if self.user_choice not in (1, 2, 3):
                print('Нет такого варианта, попробуйте ещё раз')
            else:
                break

    @with_separator
    def rock_paper_scissors(self):
        """Основная часть, логика игры"""
        while True:
            self.computer_choice = random.randint(1, 3)
            self.user()
            print_choice = {1: 'Камень',
                            2: 'Ножницы',
                            3: 'Бумага',
                            }
            result = (self.user_choice, self.computer_choice)
            combinations = [(1, 2), (2, 3), (3, 1)]
            print(f'Компьютер выбрал: {print_choice[self.computer_choice]}')
            if self.computer_choice == self.user_choice:
                print('Ничья!')
            elif result in combinations:
                print('Вы победили!')
            else:
                print('Вы проиграли')
            while True:
                retry = input('Сыграем еще? y/n ').lower()
                if retry == 'y':
                    break
                elif retry == 'n':
                    print('Спасибо за игру!')
                    return
                else:
                    print('Неправильный ввод, попробуйте ещё раз')

class GuessTheNumber:
    def __init__(self):
        self.start_number = None
        self.end_number = None
        self.num = None

    @with_separator
    def diapason(self):
        """Принимает диапазон, в котором будем угадывать число"""
        while True:
            try:
                self.start_number = int(input('Введите начало диапазона: '))
                self.end_number = int(input('Введите конец диапазона: '))
                if self.start_number >= self.end_number:
                    print('Ошибка! Конец диапазона должен быть больше начала.')
                    continue
                self.num = random.randint(self.start_number, self.end_number)
            except ValueError:
                print('Ошибка! Начало и конец диапазона должны быть целыми числами.')
                continue
            return

    def get_user_number(self):
        """Принимает угаданное число у пользователя"""
        while True:
            try:
                return int(input('Введите число: '))
            except ValueError:
                print('Ошибка! Нужно ввести целое число в указанном диапазоне.')

    def retry_game(self):
        """Предлагает сыграть ещё раз"""
        while True:
            retry = input('Сыграем ещё? y/n ').lower()
            if retry in ('y', 'n'):
                return retry
            print('Неправильный ввод!')

    @with_separator
    def guess_the_number(self):
        """Основная логика игры"""
        while True:
            self.diapason()
            count = 0
            while True:
                user_input = self.get_user_number()
                count += 1
                if user_input > self.num:
                    print('Загаданное число меньше твоего')
                elif user_input < self.num:
                    print('Загаданное число больше твоего')
                else:
                    print(f'Угадал! Тебе понадобилось {count} попыток')
                    break
            if self.retry_game() == 'n':
                print('\nСпасибо за игру!')
                return

def main_menu():
    while True:
        print('===== Игровая консоль =====')
        print('1. Камень, ножницы, бумага')
        print('2. Угадай число')
        print('3. Выход')
        try:
            choice = int(input('Выберите пункт меню: '))
        except ValueError:
            print('Ошибка! Требуется ввести число')
            continue
        if choice == 1:
            rock_paper_scissor = RockPaperScissor()
            rock_paper_scissor.rock_paper_scissors()
        elif choice == 2:
            guess_number = GuessTheNumber()
            guess_number.guess_the_number()
        elif choice == 3:
            print('До свидания!')
            break
        else:
            print('Такого пункта меню нет')

main_menu()