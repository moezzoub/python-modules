
class Plant:
    """Base class for all plant types."""
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show_base(self):
        """Print the base information of the plant."""
        print(f"{self.name} ({self.__class__.__name__}): {
            self.height}cm, {self.age} days", end="")


class Flower(Plant):
    """Flower subclass of Plant."""
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def show(self):
        """Print the flower's information."""
        self.show_base()
        print(f", {self.color} color")

    def bloom(self):
        """Simulate the flower blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Tree subclass of Plant."""
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        """Print the tree's information."""
        self.show_base()
        print(f", {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        """Simulate the tree providing shade."""
        shade = self.trunk_diameter + 28
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Vegetable subclass of Plant."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        """Initialize a vegetable with harvest season and nutritional value."""
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        """Print the vegetable's information."""
        self.show_base()
        print(f", {self.harvest_season} harvest")

    def nutrition(self):
        """Display the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    print()

    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 450, 1500, 40),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 30, 70, "spring", "beta-carotene"),
    ]

    for i in range(1):
        flowers[i].show()
        flowers[i].bloom()
        print()

    for i in range(1):
        trees[i].show()
        trees[i].produce_shade()
        print()

    for i in range(1):
        vegetables[i].show()
        vegetables[i].nutrition()
        print()


if __name__ == "__main__":
    main()
