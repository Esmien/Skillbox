from utils import num_validator

def add_contact(phone_book):
    print('Текущие контакты на телефоне:')
    if not phone_book:
        print('<Пусто>')
    else:
        for key, value in phone_book.items():
            print(f'{key} - {value}')
    while True:
        name = input('Введите имя (для выхода введите exit): ').strip()
        if not name:
            print('Имя не может быть пустым')
            continue
        if name.lower() == 'exit':
            print('До свидания!')
            return True
        if name in phone_book:
            while True:
                choice = input(f'Контакт {name} уже существует, перезаписать? (y/n): ').strip().lower()
                if choice in  ('y', 'n'):
                    break
                else:
                    print('Неправильный ввод!')
            if choice == 'n':
                continue
        phone_number = num_validator('Введите номер телефона: ', 89000000000, 89999999999)
        phone_book[name] = phone_number
        return False

def main():
    phone_book = {}
    while True:
        if add_contact(phone_book):
            break
        while True:
            is_exit = input('Завершить? (y/n): ').strip().lower()
            if is_exit == 'y':
                is_exit = True
                break
            elif is_exit == 'n':
                is_exit = False
                break
            else:
                print('Неправильный ввод')
        if is_exit:
            break
if __name__ == '__main__':
    main()