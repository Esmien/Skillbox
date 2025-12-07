import random
from utils import num_validator


class Refrigerator:
    def __init__(self) -> None:
        self._food = 50

    def add_food(self, amount: int) -> None:
        self._food += amount

    def remove_food(self, amount: int) -> None:
        self._food -= amount

    def get_food(self) -> int:
        return self._food

    def __str__(self) -> str:
        return f'{self._food}'

class Box:
    def __init__(self) -> None:
        self._money = 0

    def add_money(self, amount: int) -> None:
        self._money += amount

    def spend_money(self, amount: int) -> None:
        self._money -= amount

    def get_money(self) -> int:
        return self._money

    def __str__(self) -> str:
        return f'{self._money}'

class Home:
    def __init__(self) -> None:
        self.box = Box()
        self.refrigerator = Refrigerator()

    def __str__(self) -> str:
        return f'Денег: {self.box}\nЕды: {self.refrigerator}'

class Human:
    def __init__(self, name, home: Home) -> None:
        self.home = home
        self.name = name
        self.satiety = 50

        self.got_money_at_work = random.randint(5, 10)
        self.got_food_from_grocery = random.randint(5, 10)
        self.got_satiety_for_eat = random.randint(5, 10)
        self.lost_satiety_at_work = random.randint(5, 10)
        self.lost_satiety_at_play = random.randint(5, 10)
        self.lost_food_for_eat = random.randint(5, 10)
        self.lost_money_at_grocery = random.randint(5, 10)

    def is_alive(self) -> bool:
        """Проверяет, жив ли человек"""
        return self.satiety > 0

    def increase_satiety(self, amount: int) -> None:
        """Увеличивает сытость"""
        self.satiety += amount

    def decrease_satiety(self, amount: int) -> None:
        """Уменьшает сытость"""
        self.satiety -= amount

    def eat(self) -> None:
        """Ест. Если еды мало, то ест все, что есть. Насыщается пропорционально съеденному"""
        my_food = self.home.refrigerator.get_food()
        got_satiety = self.got_satiety_for_eat

        if my_food == 0:
            print('Нет еды')
            return

        amount_to_eat = self.lost_food_for_eat

        if my_food < self.lost_food_for_eat:
            amount_to_eat = my_food
            got_satiety = int(my_food / self.lost_food_for_eat * self.got_satiety_for_eat)
        self.home.refrigerator.remove_food(amount_to_eat)
        self.increase_satiety(got_satiety)

    def work(self) -> None:
        """Работает"""
        self.decrease_satiety(self.lost_satiety_at_work)
        self.home.box.add_money(self.got_money_at_work)

    def play(self) -> None:
        """Играет"""
        self.decrease_satiety(self.lost_satiety_at_play)

    def go_to_grocery(self) -> None:
        """Идёт в магазин, если денег не хватает, но они есть, покупает продуктов пропорционально финансам"""
        money_for_grocery = self.home.box.get_money()
        got_food = self.got_food_from_grocery

        if money_for_grocery == 0:
            print('Нет денег')
            return

        amount_to_spend = self.lost_money_at_grocery

        if money_for_grocery < self.lost_money_at_grocery:
            amount_to_spend = money_for_grocery
            got_food = int(money_for_grocery / self.lost_money_at_grocery * self.got_food_from_grocery)
        self.home.box.spend_money(amount_to_spend)
        self.home.refrigerator.add_food(got_food)

    def live_one_day(self) -> None:
        """Живет один день по алгоритму"""
        if not self.is_alive():
            return
        cube = random.randint(1, 6)

        if self.satiety < 20:
            if self.home.refrigerator.get_food() > 0:
                self.eat()
            elif self.home.box.get_money() > 0:
                self.go_to_grocery()
            else:
                self.work()

        elif self.home.refrigerator.get_food() < 10:
            if self.home.box.get_money() >= self.lost_money_at_grocery:
                self.go_to_grocery()
            else:
                self.work()

        elif self.home.box.get_money() < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

    def __str__(self) -> str:
        return f'{self.name}. {self.satiety} сытости'

def add_people(people: list, home: Home) -> None:
    """Вспомогательная функция для добавления людей"""
    count_of_people = num_validator('Сколько людей будет проживать в доме?', 1)

    for i in range(1, count_of_people + 1):
        name = input(f'Введите имя {i} человека: ')
        people.append(Human(name, home))

def main() -> None:
    people = []
    home = Home()
    add_people(people, home)
    is_all_alive = True

    for day in range(365):
        if is_all_alive:
            for human in people:
                human.live_one_day()
                print(f'День {day + 1}')
                print(home)
                print(human)
                print()
                if not human.is_alive():
                    print(f'{human} умер на {day} дне')
                    is_all_alive = False
        else:
            break
    else:
        print('Все выжили! Можно сходиться!')

if __name__ == '__main__':
    main()