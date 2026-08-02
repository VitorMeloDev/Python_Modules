def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type_cap = seed_type.capitalize()
    match unit:
        case "packets":
            print(f"{seed_type_cap} seeds: {quantity} {unit} available")
        case "grams":
            print(f"{seed_type_cap} seeds: {quantity} {unit} total")
        case "area":
            print(f"{seed_type_cap} seeds: covers {quantity} square meters")
        case _:
            print("Unknown unit type")
