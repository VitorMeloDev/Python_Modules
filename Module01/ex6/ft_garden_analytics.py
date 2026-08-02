class PlantStatistics:
    def __init__(self):
        self._count_grow = 0
        self._count_age = 0
        self._count_show = 0

    def increment_grow(self):
        self._count_grow += 1

    def increment_age(self):
        self._count_age += 1

    def increment_show(self):
        self._count_show += 1

    def show(self):
        print(
            f"Stats: {self._count_grow} "
            f"grow,{self._count_age} age, {self._count_show} show"
        )


class Plant:
    def __init__(self, name, height, age):
        self._stats = PlantStatistics()
        self.name = name
        self._age = age
        if age < 0:
            self._age = 0
        self._height = height
        if height < 0:
            self._height = 0.0

    def show(self):
        self._stats.increment_show()
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self):
        self._stats.increment_grow()
        self.set_height(self._height + self._height * 0.03)

    def age(self):
        self._stats.increment_age()
        self.set_age(self._age + 1)

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = value
        print(f"Height updated: {self.get_height():.1f}cm")

    def get_height(self):
        return self._height

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = value
        print(f"Age updated: {self.get_age()} days")

    def get_age(self):
        return self._age

    @staticmethod
    def check_year_old(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self):
        self.blooming = True
        print(f"[asking the {self.name} to bloom]")

    def show(self):
        super().show()
        print(
            f"Color: {self.color}, "
            f"Blooming: {'Yes' if self.blooming else 'No'}"
        )


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds += 42
        print(f"{self.name} has produced {self.seeds} seeds")

    def show(self):
        super().show()
        print(f"Seeds produced: {self.seeds}")


class Tree(Plant):
    class TreeStatistics(PlantStatistics):
        def __init__(self):
            super().__init__()
            self._count_shade = 0

        def increment_shade(self):
            self._count_shade += 1

        def show(self):
            super().show()
            print(f" {self._count_shade} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.TreeStatistics()

    def produce_shade(self):
        self._stats.increment_shade()
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide"
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.show()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")

    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)

    oak.show()
    display_statistics(oak)

    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")

    sunflower.show()

    print("[make sunflower grow, age and bloom]")

    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()

    display_statistics(sunflower)

    print("\n=== Anonymous ===")
    unknown = Plant.anonymous()

    unknown.show()
    display_statistics(unknown)
