from utils import num_validator


class Child:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.calm = False
        self.hungry = True

    def calm_down(self) -> None:
        """Ребенок успокаивается"""
        self.calm = True
        print(f'Ребенок {self.name} успокоился')

    def eat(self) -> None:
        """Ребенок ест"""
        self.hungry = False
        print(f'Ребенок {self.name} поел')

    def __str__(self) -> str:
        return f'{self.name}. {self.age} лет, {"голоден/-на" if self.hungry else "сыт/-а"}, {"спокоен/-на" if self.calm else "возбужден/-на"}'

class Parents:
    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        self.children: list[Child] = []

    def add_child(self, child: Child) -> None:
        """Добавляет ребенка в список детей"""
        if self.age - child.age < 16:
            raise ValueError('Ребенок слишком взрослый, чтобы быть вашим')
        self.children.append(child)
        print(f'Ребенок {child.name} добавлен в список детей')

    def calm_child(self, child: Child) -> None:
        """Успокаивает ребенка"""
        print(f'{self.name} успокаивает {child.name}...')
        child.calm_down()

    def feed(self, child: Child) -> None:
        """Кормит ребенка"""
        print(f'{self.name} кормит {child.name}...')
        child.eat()

    def get_children(self) -> list[Child]:
        return self.children

    def __str__(self) -> str:
        kids_info = '\n  '.join([str(kid) for kid in self.children])
        return (f'Родитель {self.name}, {self.age} лет.\n'
                f'Дети:\n  {kids_info if self.children else "Детей нет"}')

def main() -> None:
    parent_name = input('Введите ваше имя: ')
    parent_age = num_validator('Введите ваш возраст: ', 18, 100)
    parent = Parents(parent_name, parent_age)

    while True:
        children = parent.get_children()
        if not children:
            print('У вас нет детей')
        else:
            for index, child in enumerate(children, start=1):
                print(f'{index}. {child}')

        print('\nМеню:')
        print('1. Добавить ребенка')
        print('2. Успокоить ребенка')
        print('3. Кормить ребенка')
        print('4. Выйти')
        choice = num_validator('Выберите действие: ', 1, 4)

        if choice == 1:
            child_name = input('Введите имя ребенка: ')
            child_age = num_validator('Введите возраст ребенка: ', 0)
            child = Child(child_name, child_age)
            try:
                parent.add_child(child)
            except ValueError as e:
                print(e)
                continue
        elif choice == 2:
            if not parent.children:
                print('У вас нет детей')
                continue
            child = parent.children[num_validator('Выберите ребенка: ', 1, len(parent.children)) - 1]
            parent.calm_child(child)
        elif choice == 3:
            if not parent.children:
                print('У вас нет детей')
                continue
            child = parent.children[num_validator('Выберите ребенка: ', 1, len(parent.children)) - 1]
            parent.feed(child)
        elif choice == 4:
            print('До свидания')
            break

if __name__ == '__main__':
    main()
