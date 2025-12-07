from typing import Iterator
from utils import num_validator

CHAT_FILE = 'chat.txt'
class User:
    """Хранит данные пользователя"""
    def __init__(self, name: str) -> None:
        if not name or len(name.strip()) < 2:
            raise ValueError('Имя пользователя должно быть длиннее 1 символа')
        self.name = name.strip().capitalize()

    def __str__(self) -> str:
        return self.name

class ChatStorage:
    """Работает с файлом чата"""
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def save_message(self, message: str) -> None:
        """Сохраняет сообщение в файл"""
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')

    def load_messages(self) -> Iterator[str]:
        """Создает генератор для чтения файла построчно"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            for line in f:
                yield line.strip()

class Interface:
    """Пользовательский интерфейс с бизнес-логикой"""
    def __init__(self, filename: str, user: User) -> None:
        self.storage = ChatStorage(filename)
        self.user = user

    def show_messages(self) -> None:
        """Показывает сообщения"""
        print(f'\n{"Переписка":-^25}')
        try:
            messages = self.storage.load_messages()

            is_empty = True
            for message in messages:
                print(message)
                is_empty = False

            if is_empty:
                print('История переписки пуста')

        except FileNotFoundError:
            print('Не найден файл с чатом')
        print('-' * 25)

    def send_message(self) -> None:
        """Отправляет сообщение"""
        while True:
            message = input(f'{self.user}, введите сообщение (для выхода введите exit): ')

            if not message:
                print('Вы не ввели сообщение')
                continue

            is_exit = message.lower() == 'exit'
            if is_exit:
                return

            self.storage.save_message(f'{self.user}: {message}')

    def user_menu(self) -> None:
        """Отображает персонализированное меню"""
        print(f'\nПривет, {self.user}')
        print('-' * 25)
        print('1. Посмотреть текущий текст чата')
        print('2. Отправить сообщение')
        print('3. Выйти')
        print('-' * 25)

def safe_create_user() -> User:
    """Безопасно создает пользователя"""
    while True:
        try:
            name = input('Введите имя: ')
            return User(name)
        except ValueError as e:
            print(e)

def main() -> None:
    user = safe_create_user()
    chat_interface = Interface(CHAT_FILE, user)

    while True:
        chat_interface.user_menu()
        user_choice = num_validator('Выберите действие: ', 1, 3)

        if user_choice == 1:
            chat_interface.show_messages()
        elif user_choice == 2:
            chat_interface.send_message()
        elif user_choice == 3:
            break

if __name__ == '__main__':
    main()