class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age
        if age < 0:
            self._age = 0
        self._height = height
        if height < 0:
            self._height = 0.0
        print(f"Created: {self.name}: {self._height:.1f}cm, {self._age} days old")

    def __str__(self):
        return f"{self.name}: {self._height:.1f}cm, {self._age} days old"

    def grow(self):
        self.set_height(self._height + self._height * 0.03)
        self.set_age(self._age + 1)

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = value
        print(f"Height updated: {self.get_height()}cm")

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

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-15)
    rose.set_age(-2)
    print()
    print(f"Current state: {rose}")