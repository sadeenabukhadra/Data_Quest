import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, value = arg.split(":", 1)

        if name == "" or value == "":
            print(f"Error - invalid parameter '{arg}'")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(value)
        except ValueError:
            print(f"Quantity error for '{name}': invalid literal for int() with base 10: '{value}'")
            continue

        inventory[name] = quantity

    return inventory


def main() -> None:
    args = sys.argv[1:]
    inventory = parse_inventory(args)

    print(f"Got inventory: {inventory}")

    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    if total > 0:
        for item, quantity in inventory.items():
            percent = (quantity / total) * 100
            print(f"Item {item} represents {round(percent, 1)}%")
    if len(inventory) > 0:
        most_item = max(inventory.items(), key=lambda x: x[1])
        least_item = min(inventory.items(), key=lambda x: x[1])
        print(f"Item most abundant: {most_item[0]} with quantity {most_item[1]}")
        print(f"Item least abundant: {least_item[0]} with quantity {least_item[1]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main()