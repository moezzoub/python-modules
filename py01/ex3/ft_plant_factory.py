class Plant:
    """A simple plant class to hold plant data."""
    def __init__(self, name, start_height, start_age):
        """Initialize plant with name, starting height, and starting age."""
        self.name = name
        self.start_height = start_height
        self.start_age = start_age

    def get_info(self):
        """Return a string representing the plant's information."""
        return f"{self.name} ({self.start_height}cm, {self.start_age} days)"


def main():
    print("=== Plant Factory Output ===")

    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    for i in range(5):
        name, height, age = plants_data[i]
        p = Plant(name, height, age)
        print(f"Created: {p.get_info()}")

    print()
    print("Total plants created:", 5)


if __name__ == "__main__":
    main()
