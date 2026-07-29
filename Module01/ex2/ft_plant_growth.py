class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self):
        self.height += self.height * 0.03
        self.age += 1


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
