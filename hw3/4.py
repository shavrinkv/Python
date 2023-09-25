class Apple:

    states = {'Цветение': 1, 'Зеленое': 2, 'Красное': 3}

    def __init__(self, index):
        self._index = index
        self._state = self.states['Цветение']

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return True if self._state == 3 else False


class AppleTree:
    def __init__(self, num):
        self.apples = [Apple(index) for index in range(1, num+1)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print('яблоки созрели!')
            self._plant.give_away_all()
        else:
            print('еще не дозрели')


tree = AppleTree(5)
gardener = Gardener('Лев', tree)

gardener.work()
gardener.work()

gardener.harvest()

