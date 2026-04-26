import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        if ":" in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, value = arg.split(":", 1)

        if name == "" or value == "":
            print(f"Error - invalid parameter '{arg}'")
            continue
        if name in inventory:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            quantity = int(value)
        except ValueError as e:
            print(
                f"Quantity error for '{name}': invalid literal for int() with base 10: '{value}'"
            )
            continue
        inventory[name] = quantity
    return inventory
def main()->None:
    print(f" Got inventory:{inventory}")
    items :list[str] = list(inventory.keys())
    print(f"item list:{items}")
    total: int = sum(inventory.keys())
    print(f"Item list: {items}")
    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item, quantity in inventory.items():
        percent : float =(quantity/total)*100
        print(f"Item {item} represents {round(percent, 1)}%")
    most_item:str 


