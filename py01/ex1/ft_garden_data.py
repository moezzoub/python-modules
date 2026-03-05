

class Plant:
    """A simple plant class to hold plant data."""
    def __init__(self, name, height, age):
        """Initialize plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)

    plants = [p1, p2, p3]

    print("=== Garden Plant Registry ===")
    for i in range(len(plants)):
        plant = plants[i]
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
