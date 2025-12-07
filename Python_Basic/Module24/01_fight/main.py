import random


class Warrior:
    def __init__(self, name = 'Воин') -> None:
        self._health = 100
        self.damage = 20
        self.name = name

    def make_hit(self, target: Warrior) -> None:
        target.get_damage(self.damage)

    def get_damage(self, damage) -> None:
        self._health -= damage

    def get_warrior_health(self) -> int:
        return self._health

    def __str__(self) -> str:
        return f'{self.name}'

class BattleGround:
    def __init__(self, warriors: list[Warrior]) -> None:
        self.warriors = warriors
        self.is_game_over = False

    def check_game_over(self) -> bool:
        """Проверяет, есть ли мертвые воины и меняет флаг, если кто-то умер"""
        if not all(warrior.get_warrior_health() > 0 for warrior in self.warriors):
            self.is_game_over = True
        return self.is_game_over

    def get_alive_warrior(self) -> Warrior | None:
        """Находит выжившего воина"""
        # return next(warrior for warrior in self.warriors if warrior.get_warrior_health() > 0)
        # вариант выше мне нравится больше, но тот, что оставил - нагляднее
        for warrior in self.warriors:
            if warrior.get_warrior_health() > 0:
                return warrior
        return None

    def make_turn(self) -> None:
        """Логика боя. Ударил-получил урон"""
        random.shuffle(self.warriors)
        attacker, defender = self.warriors
        attacker.make_hit(defender)
        defender_health = defender.get_warrior_health()
        print(f'Атакует {attacker}. Состояние здоровья {defender}: {defender_health}')

    def play(self) -> None:
        """Запуск игры"""
        while not self.check_game_over():
            self.make_turn()
        winner = self.get_alive_warrior()
        print(f'Победу одержал {winner}')

def main() -> None:
    knight = Warrior('Рыцарь')
    demon = Warrior('Демон')
    warriors = [knight, demon]
    battleground = BattleGround(warriors)
    battleground.play()

if __name__ == '__main__':
    main()