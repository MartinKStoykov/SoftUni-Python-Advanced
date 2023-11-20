from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    WEIGHT_GAIN = 0

    def __init__(self, name: str, weight: float, food_eaten: int= 0):
        self.name= name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def edible_food(self):
        pass

    def feed(self, food: Food):
        if food.__class__ not in self.edible_food():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_GAIN * food.quantity
        self.food_eaten += food.quantity

class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int= 0,):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int= 0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"