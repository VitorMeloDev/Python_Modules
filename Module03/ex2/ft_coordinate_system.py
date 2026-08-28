import math

def get_player_pos() -> tuple:
    try: 
        x = float(input("Enter x coordinate: "))
        y = float(input("Enter y coordinate: "))
        z = float(input("Enter z coordinate: "))
        return (x, y, z)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_player_pos()


def calculate_distance(coord1: tuple, coord2: tuple) -> float:
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2 + (coord2[2] - coord1[2]) ** 2)

if __name__ == "__main__":
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coordinate = get_player_pos()

    print(f"Got a first tuple: {coordinate}")
    print(f"It includes: X={coordinate[0]}, Y={coordinate[1]}, Z={coordinate[2]}")
    print(f"Distance from origin: {calculate_distance((0, 0, 0), coordinate):.4f}")

    print()

    print("Get a second set of coordinates")
    coordinate2 = get_player_pos()

    distance = calculate_distance(coordinate, coordinate2)
    print(f"Distance between the two coordinates: {distance:.4f}")