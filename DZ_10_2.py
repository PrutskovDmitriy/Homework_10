from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size
        Coat.expence_count += self.expence

    def __str__(self):
        return f'Пальто: {self.size} размера имеет расход ткани: {self.expence}, общий расход {Coat.expence_count:.02f} '

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(f'{exp:.02f}')


class Costume(Clothes):
    def __init__(self, height):
        self.height = height
        Costume.expence_count += self.expence

    def __str__(self):
        return f'Костюм: {self.height} роста имеет расход ткани {self.expence}, общий расход {Costume.expence_count:.02f}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(f'{exp:.01f}')


cloth_1 = Costume(182)
print(cloth_1)
cloth_2 = Coat(48)
print(cloth_2)
