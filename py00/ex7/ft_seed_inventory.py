def ft_seed_inventory(a: str, b: int, c: str) -> None:
    if c == "packets":
        print(f"{a.capitalize()} seeds: {b} {c} available")
    elif c == "grams":
        print(f"{a.capitalize()} seeds: {b} {c} total")
    elif c == "area":
        print(f"{a.capitalize()} seeds: overs {b} square meters")
    else:
        print("Unknown unit type")
