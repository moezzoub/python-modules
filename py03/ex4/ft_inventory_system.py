import sys


def parse_inventory(args) -> dict:
    inv = dict()
    i = 0
    while i < len(args):
        token = args[i]
        if ":" not in token:
            print("skipping invalid token (missing ':'):", token)
            i += 1
            continue
        parts = token.split(":")
        if len(parts) != 2:
            print("skipping invalid token (bad format):", token)
            i += 1
            continue
        name = parts[0].strip()
        qty_str = parts[1].strip()
        if name == "" or qty_str == "":
            print("skipping invalid token (empty name):", token)
            i += 1
            continue
        try:
            qty = int(qty_str)
        except ValueError:
            print("skipping invalid token (qty not an integer):", token)
            i += 1
            continue
        if qty < 0:
            print("skipping invalid token (qty negative):", token)
            i += 1
            continue
        current = inv.get(name, 0)
        inv.update({name: current + qty})
        i += 1
    return inv


def total_items(inv) -> int:
    total = 0
    for qty in inv.values():
        total += qty
    return total


def most_and_least(inv):
    most_name = None
    most_qty = None
    least_name = None
    least_qty = None

    for name, qty in inv.items():
        if most_qty is None or qty > most_qty:
            most_name = name
            most_qty = qty
        if least_qty is None or qty < least_qty:
            least_name = name
            least_qty = qty
    return most_name, most_qty, least_name, least_qty


def categorize(inv) -> dict:
    categories = dict()
    categories.update({"Moderate": dict()})
    categories.update({"Scarce": dict()})

    for name, qty in inv.items():
        if qty >= 5:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})
    return categories


def restock_list(inv) -> list:
    restock = []
    for name, qty in inv.items():
        if qty <= 1:
            restock.append(name)
    return restock


def print_report(inv):
    print("=== Inventory System Analysis ===")

    total = total_items(inv)
    unique_items = len(inv)

    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {unique_items}\n")

    print("=== Current Inventory ===")
    if total == 0:
        for name, qty in inv.items():
            print(name + ":", qty, "units (0.00%)")
    else:
        for name, qty in inv.items():
            percentage = (qty / total) * 100
            print(f"{name}: {qty} units ({percentage:.1f}%)")
    print()

    print("=== Inventory Statistics ===")
    if unique_items == 0:
        print("Most abundant: N/A")
        print("Least abundant: N/A")
    else:
        most_name, most_qty, least_name, least_qty = most_and_least(inv)
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")
    print()

    print("=== Item Categories ===")
    categories = categorize(inv)
    print("Moderate:", categories.get("Moderate", dict()))
    print("Scarce:", categories.get("Scarce", dict()))
    print()

    print("=== Management Suggestions ===")
    print("Restock needed:", restock_list(inv))
    print()

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", inv.keys())
    print("Dictionary values:", inv.values())
    print("Sample lookup 'sword' in inventory:", inv.get("sword", 0) > 0)


def main():
    args = sys.argv[1:]
    inv = parse_inventory(args)
    print_report(inv)


if __name__ == "__main__":
    main()
