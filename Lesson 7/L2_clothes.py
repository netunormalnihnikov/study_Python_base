from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_mat(self):
        pass


class CalcMaterials(Clothes):
    def __init__(self, mat_1, mat_2):
        self.mat_1 = mat_1
        self.mat_2 = mat_2

    @property
    def calc_mat(self):
        return self.mat_1 + self.mat_2


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def calc_mat(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def calc_mat(self):
        return round((self.height * 2 + 0.3) / 100, 2)


coat = Coat(32).calc_mat
suit = Suit(180).calc_mat
calc = CalcMaterials(coat, suit).calc_mat

print(f"Для пошива пальто потребуется {coat} м. ткани.\n"
      f"Для пошива костюма потребуется {suit} м. ткани.\n"
      f"Всего потребуется {calc} м. ткани.")
