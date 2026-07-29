class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old")

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self):
        self.height += self.height * 0.03
        self.age += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
