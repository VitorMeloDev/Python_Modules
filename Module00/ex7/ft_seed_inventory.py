def ft_seed_inventory(seed_type: str, quantity: int, unit: str)-> None:
    match unit:
        case "packets":
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
        case "grams":
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
        case "area":
            print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
