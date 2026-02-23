from abc import ABC, abstractmethod


class HouseBuilder(ABC):

    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def get_house(self):
        pass



class ConcreteHouseBuilder(HouseBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    def build_foundation(self):
        self._house.add("Foundation")

    def build_walls(self):
        self._house.add("Walls")

    def build_roof(self):
        self._house.add("Roof")

    def get_house(self):
        house = self._house
        self.reset()
        return house


class House:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("House parts:", ", ".join(self.parts))



class Director:

    def __init__(self, builder: HouseBuilder):
        self._builder = builder

    def build_minimal_house(self):
        self._builder.build_foundation()

    def build_full_house(self):
        self._builder.build_foundation()
        self._builder.build_walls()
        self._builder.build_roof()


if __name__ == "__main__":
    builder = ConcreteHouseBuilder()
    director = Director(builder)

    print("Minimal house:")
    director.build_minimal_house()
    house1 = builder.get_house()
    house1.show()

    print("\nFull house:")
    director.build_full_house()
    house2 = builder.get_house()
    house2.show()

    print("\nCustom house:")
    builder.build_foundation()
    builder.build_walls()
    custom_house = builder.get_house()
    custom_house.show()