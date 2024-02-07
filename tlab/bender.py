from abc import ABC, abstractmethod


class Bender(ABC):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    @abstractmethod
    def bend(self):
        pass

    @abstractmethod
    def enhance_power(self, boost):
        pass

    @abstractmethod
    def special_ability(self):
        pass
