class Water:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Storm()
        return None

    def __str__(self):
        return 'Вода'

class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        return None

    def __str__(self):
        return 'Огонь'

class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        return None

    def __str__(self):
        return 'Воздух'

class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        return None

    def __str__(self):
        return 'Земля'

class Storm:
    def __str__(self):
        return 'Шторм'

class Steam:
    def __str__(self):
        return 'Пар'

class Dirt:
    def __str__(self):
        return 'Грязь'

class Lightning:
    def __add__(self, other):
        if isinstance(other, Ether):
            return Energy()
        return None
    def __str__(self):
        return 'Молния'

class Dust:
    def __str__(self):
        return 'Пыль'

class Lava:
    def __str__(self):
        return 'Лава'

class Ether:
    def __add__(self, other):
        if isinstance(other, Lightning):
            return Energy()
        return None
    def __str__(self):
        return 'Эфир'

class Energy:
    def __str__(self):
        return 'Энергия'
