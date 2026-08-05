class GardenError(Exception):
	def __init__(self, message: str = "Unknown plant error"):
		self.message = message
		super().__init__(self.message)


class PlantError(GardenError):
	pass


class WaterError(GardenError):
	pass


def water_plant(plant_name: str) -> None:
	if plant_name == plant_name.capitalize():
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name: {plant_name}")


def test_watering_system(*args: str) -> None:
    print("Opening watering system")
    try:
        for plant in args:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system("Tomato", "Lettuce", "Carrots")
    print()
    print("Testing invalid plants...")
    test_watering_system("Tomato", "lettuce", "carrots")
    print()
    print("Cleanup always happens, even with errors!")
