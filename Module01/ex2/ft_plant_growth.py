class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.height * 0.03

    def age(self) -> None:
        self._age += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Growth ===")
    plant.show()
    growth = plant.height
    for i in range(1, 8):
        plant.grow()
        plant.show()
    growth = plant.height - growth
    print(f"Growth this week: {growth:.1f}cm")
