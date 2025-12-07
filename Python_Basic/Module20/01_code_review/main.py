def get_id_and_age(students: dict) -> list[tuple[int, int]]:
    """
    Получает из словаря id и возраст студента
    :param students: словарь с перечнем студентов
    :return: список со всеми id и возрастом студентов
    """
    return [(student_id, data['age']) for student_id, data in students.items()]

def get_interests_and_len_surnames(students: dict) -> tuple[set[str], int]:
    """
    Получает список уникальных интересов студентов из словаря и считает общую длину фамилий
    :param students: словарь с перечнем студентов
    :return: перечень всех уникальных интересов всех студентов и общая длина фамилий
    """
    interests = set()
    len_surnames = 0
    for _, data in students.items():
        interests.update(data['interests'])
        len_surnames += len(data['surname'])
    return interests, len_surnames

def main():
    students = {
        1: {
            'name': 'Bob',
            'surname': 'Vazovski',
            'age': 23,
            'interests': ['biology, swimming'] # здесь изначально опечатка! Эти два хобби - один интерес
        },
        2: {
            'name': 'Rob',
            'surname': 'Stepanov',
            'age': 24,
            'interests': ['math', 'computer games', 'running']
        },
        3: {
            'name': 'Alexander',
            'surname': 'Krug',
            'age': 22,
            'interests': ['languages', 'health food']
        }
    }
    pairs = get_id_and_age(students)
    interests, length_surnames = get_interests_and_len_surnames(students)
    print('Список пар "ID студента — возраст":', end=' ')
    print(*pairs, sep=', ')  # Решил написать с распаковкой, так красивее вывод
    print('Полный список интересов всех студентов:', end=' ')
    print(*interests, sep=', ')
    print('Общая длина всех фамилий студентов:', length_surnames)

if __name__ == '__main__':
    main()