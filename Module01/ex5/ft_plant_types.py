class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age
        if age < 0:
            self._age = 0
        self._height = height
        if height < 0:
            self._height = 0.0

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self):
        self.set_height(self._height + self._height * 0.03)

    def age(self):
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


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
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


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    # Flower
    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    rose.bloom()
    rose.show()

    # Tree
    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    oak.produce_shade()

    # Vegetable
    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
