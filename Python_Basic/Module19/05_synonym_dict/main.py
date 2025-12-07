from utils import num_validator
import json
from json import JSONDecodeError

def load_file(filename: str) -> dict:
    """
    Загружает словарь синонимов из json файла
    :param filename: имя файла
    :return: пустой словарь, если с файлом что-то не так, загруженный из файла словарь, если все ок
    """
    dictionary = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            dictionary = json.load(f)
    except FileNotFoundError:
        print('Словарь отсутствует, создаю новый')
    except JSONDecodeError:
        print('Словарь поврежден, создаю новый')
    return dictionary
def write_file(filename: str, dictionary: dict) -> str:
    """
    Сохраняет изменения в файл
    :param filename: Название файла, куда сохранять
    :param dictionary: словарь, с которым поработали
    :return: уведомление об успешном сохранении
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dictionary, f, ensure_ascii=False, indent=2)
    except IOError as e:
        return f'Ошибка сохранения файла: {e}'
    return 'Файл успешно сохранен'
def add_synonym(synonym_dict: dict, count: int):
    """
    Добавляет пару синонимов в словарь
    :param synonym_dict: словарь, с которым работаем
    :param count: количество пар
    :return: None
    """
    num_to_word = {
        1: 'Первая',
        2: 'Вторая',
        3: 'Третья',
        4: 'Четвертая',
        5: 'Пятая',
        6: 'Шестая',
        7: 'Седьмая',
        8: 'Восьмая',
        9: 'Девятая',
        10: 'Десятая',
    }
    format_err = 'Ошибка! Неверный формат. Используйте: слово — слово'
    empty_err = 'Ошибка! Слова не могут быть пустыми'
    exist_err = 'Ошибка! Такое слово уже есть в словаре'
    for i_word in range(1, count + 1):
        while True:
            words_pair = input(f'{num_to_word[i_word]} пара (слово - слово): ')
            if not words_pair.strip(): # проверка на пустую строку
                print(format_err)
                continue

            if ' — ' in words_pair: # проверка на разделитель
                words_pair = words_pair.split(' — ')
            elif ' - ' in words_pair:
                words_pair = words_pair.split(' - ')
            else:
                print(format_err)
                continue

            if len(words_pair) != 2: # проверка на количество слов
                print(format_err)
                continue

            word1, word2 = words_pair[0].strip().lower(), words_pair[1].strip().lower()

            if not word1 or not word2: # проверка на наличие отдельных слов
                print(empty_err)
                continue

            if word1 in synonym_dict or word2 in synonym_dict: # проверка на дубликаты
                print(exist_err)
                continue
            synonym_dict[word1] = word2 # добавление слов в обоих форматах - и как ключ, и как значение
            synonym_dict[word2] = word1
            print('Слово добавлено!')
            break

def get_synonym_dict(synonym_dict: dict, word: str) -> str:
    """
    Ищет синоним слова
    :param synonym_dict: рабочий словарь
    :param word: слово, к которому ищем синоним
    :return: искомое слово или уведомление об ошибке
    """
    if word in synonym_dict:
        return f'Синоним: {synonym_dict[word].capitalize()}'
    return 'Такого слова в словаре нет.'

def menu():
    print(f'{" Меню ":=^40}')
    print('1. Добавить пару')
    print('2. Найти синоним')
    print('3. Выход')
    print('=' * 40)

def main():
    filename = 'dictionary.json'
    synonym_pairs = load_file(filename)
    while True:
        menu()
        choice = num_validator('\nВыберите действие (1-3): ', 1, 3)
        if choice == 1:
            count = num_validator('\nВведите количество пар слов(1-10): ', 1, 10)
            add_synonym(synonym_pairs, count)
        elif choice == 2:
            word = input('\nВведите слово: ').lower()
            synonym = get_synonym_dict(synonym_pairs, word)
            print(synonym)
        elif choice == 3:
            print('\nДо свидания!')
            result = write_file(filename, synonym_pairs)
            print(result)
            break

if __name__ == '__main__':
    main()