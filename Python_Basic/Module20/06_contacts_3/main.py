from utils import num_validator, with_separator

class PhoneBook:
    def __init__(self):
        self.phone_book = {}
    def add_contact(self):
        """
        Добавляет контакт в справочник с валидацией ввода
        """
        while True:
            contact_data = input('Введите имя и фамилию нового контакта (через пробел): ')
            if not contact_data:
                print('Ошибка! Пустой ввод')
                continue
            if len(contact_data.strip().split()) != 2:
                print('Неправильный ввод. Требуется ввести имя и фамилию через пробел')
                continue
            name, surname = contact_data.strip().title().split()
            if (name, surname) in self.phone_book:
                print('Такой человек уже есть в контактах')
                self.show_contacts()
                return
            break
        phone = num_validator('Введите номер телефона: ')
        self.phone_book[(name, surname)] = phone
        print('Запись успешно добавлена!')
        self.show_contacts()

    @with_separator
    def show_contacts(self):
        """
        Выводит на экран весь список контактов
        """
        print('Текущий словарь контактов:', self.phone_book)
    def find_contact(self, surname):
        """
        Ищет контакты по фамилии, собирает найденные контакты в список
        """
        found = []
        for person, phone in self.phone_book.items():
            name, sur = person
            if surname.lower() == sur.lower():
                found.append((person, phone))
        return found

def menu():
    print(f'{'Меню':=^25}')
    print('1. Добавить контакт')
    print('2. Найти контакт')
    print('3. Выход')
def main():
    phone_book = PhoneBook()
    while True:
        menu()
        choice = num_validator('Выберите действие(1-3): ', 1, 3)
        print()
        if choice == 1:
            phone_book.add_contact()
        elif choice == 2:
            surname = input('Введите фамилию для поиска: ').strip()
            print()
            contacts = phone_book.find_contact(surname)
            if contacts:
                print('Найдены контакты:')
                for contact_data, contact_phone in contacts:
                    print(*contact_data, '-', contact_phone)
                print()
            else:
                print('Контакты не найдены')
        elif choice == 3:
            print('До свидания')
            break

if __name__ == '__main__':
    main()