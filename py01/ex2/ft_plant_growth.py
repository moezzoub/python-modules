class Plant:
    """A simple plant class to hold plant data and simulate growth."""
    def __init__(self, name, height, age):
        """Initialize plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Print the plant's current information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        """Simulate the plant growing by 1 cm."""
        self.height = self.height + 1

    def age_one_day(self) -> None:
        """Simulate the plant aging by one day."""
        self.age = self.age + 1


if __name__ == "__main__":
    p = Plant("Rose", 25, 30)
    start = 1
    end = 7
    print(f"=== Day {start} ===")
    p.get_info()
    start_height = p.height

    for start in range(end - 1):
        p.grow()
        p.age_one_day()
    end_height = p.height
    growth = end_height - start_height
    print(F"=== Day {end} ===")
    p.get_info()
    print(f"Growth this week: +{growth}cm")
