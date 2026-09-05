import sys

class InvalidParameterError(Exception):
    pass

def CheckItem(item: str, itens: dict) -> None:
    if item in itens:
        raise InvalidParameterError(f"Redundant item '{item}' - discarding")

def items_quantity(items: dict) -> None:
    most = None
    least = None
    name_most = None
    name_least = None

    for item in items:
        quantity = items[item]
        if most is None or quantity > most:
            most = quantity
            name_most = item
        if least is None or quantity < least:
            least = quantity
            name_least = item

    print(f"Item most abundant: {name_most} with quantity {most}")
    print(f"Item least abundant: {name_least} with quantity {least}")

    
if __name__ == "__main__":
    itens = {}

    for arg in sys.argv[1:]:
        try:
            if ":" not in arg:
                raise InvalidParameterError(f"Error - invalid parameter '{arg}'")
            
            name, qtd = arg.split(":")
            CheckItem(name, itens)
            itens[name] = int(qtd)
        except ValueError as error:
            print(f"Quantity error for '{name}': {error}")
        except InvalidParameterError as error:
            print(f"{error}")

    print(f"Got inventory: {itens}")

    print(f"Items list: {list(itens)}")

    total = sum(itens.values())
    print(f"Total quantity of {len(itens)} items: {total}")

    for item in itens:
        print(f"Item {item} representes {round(itens[item] * 100 / total, 1)}%")

    items_quantity(itens)

    itens.update({"Health Potion": 3})
    print(f"Updated inventory: {itens}")
