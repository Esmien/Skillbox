class Student:
    def __init__(self, name: str, surname: str, group: int, grades: list[int]) -> None:
        self.surname = surname
        self.name = name
        self.group = group
        self.grades = grades

    def get_grades(self) -> list[int]:
        """Возвращает список оценок"""
        return self.grades

    def get_avg_grade(self) -> float:
        """Возвращает среднюю оценку"""
        return sum(self.get_grades()) / len(self.get_grades())

    def __str__(self) -> str:
        """Возвращает строку с данными студента"""
        return f'{self.surname} {self.name},\tгруппа {self.group},\tсредний балл:\t{self.get_avg_grade()}'

def main():
    students = [
        Student('Иван', 'Иванов', 1, [5, 4, 3, 2, 5]),
        Student('Петр', 'Петров', 2, [4, 3, 2, 5, 4]),
        Student('Сидор', 'Сидоров', 3, [3, 2, 5, 4, 3]),
        Student('Анна', 'Аннова', 1, [5, 4, 3, 2, 5]),
        Student('Мария', 'Марнова', 2, [4, 3, 2, 5, 4]),
        Student('Олег', 'Олегов', 3, [3, 2, 5, 4, 3]),
        Student('Елена', 'Еленова', 1, [5, 4, 3, 2, 5]),
        Student('Александр', 'Александров', 2, [4, 3, 2, 5, 4]),
        Student('Дарья', 'Дарьянова', 3, [3, 2, 5, 4, 3]),
        Student('Евгений', 'Евгеньев', 1, [5, 4, 3, 2, 5]),
    ]
    sorted_students_list = sorted(students, key=lambda s: s.get_avg_grade())
    for student in sorted_students_list:
        print(student)

if __name__ == '__main__':
    main()
