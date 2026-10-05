class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_garden_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    test_plant_error()
    print()
    print("Testing WaterError...")
    test_water_error()
    print()
    print("Testing catching all garden errors...")
    test_garden_error()
    print()
    print("All custom error types work correctly!")
