INPUT_FILE = 'registrations.txt'
VALID_USERS = 'registrations_good.log'
INVALID_USERS = 'registrations_bad.log'

def check_name(name: str) -> bool:
    """Проверет валидность имени"""
    for char in name:
        if not char.isalpha():
            return False
    return True

def check_email(email: str) -> bool:
    """Проверяет валидность почты"""
    if '@' not in email or '.' not in email:
        return False
    return True

def check_age(age: str) -> bool:
    """Проверяет валидность возраста"""
    try:
        age = int(age)
        if 10 <= age <= 99:
            return True
    except ValueError:
        return False
    return False

def check_registrations(input_file: str) -> None:
    """Обрабатывает данные пользователей из файла при помощи вспомогательных функций,
       сортирует их на валидные и невалидные
    """
    with (open(input_file, 'r', encoding='utf-8') as f,
          open(VALID_USERS, 'w', encoding='utf-8') as f2,
          open(INVALID_USERS, 'w', encoding='utf-8') as f3):
        for line in f:
            user_data = line.split()
            try:
                if len(user_data) != 3:
                    raise IndexError('НЕ присутствуют все три поля')

                name, email, age = user_data
                if not check_name(name):
                    raise NameError('Имя содержит НЕ только буквы')
                if not check_email(email):
                    raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')
                if not check_age(age):
                    raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')

            except (IndexError, NameError, SyntaxError, ValueError) as e:
                res_line = f'{line.strip()}\t\t{e}\n'
                f3.write(res_line)
                continue
            f2.write(line)

def main():
    check_registrations(INPUT_FILE)

if __name__ == '__main__':
    main()