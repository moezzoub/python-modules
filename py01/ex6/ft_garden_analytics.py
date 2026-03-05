class Plant:
    """Base class representing a generic plant with a name and height."""

    def __init__(self, name, height_cm):
        self.name = name
        self.height_cm = height_cm
        self.kind = "regular"

    def grow(self, cm) -> int:
        self.height_cm += cm
        return cm

    def describe(self) -> str:
        """Return a string representing the plant's name and height."""
        return f"- {self.name}: {self.height_cm}cm"


class FloweringPlant(Plant):
    """A specialized plant that also features flower colors."""

    def __init__(self, name, height_cm, flower_color, is_blooming):
        """Initialize a flowering plant with stats and flower settings."""
        super().__init__(name, height_cm)
        self.flower_color = flower_color
        self.is_blooming = is_blooming
        self.kind = "flowering"

    def describe(self) -> str:
        """Return a string showing the plant's stats and flower color."""
        bloom_txt = "blooming" if self.is_blooming else "not blooming"
        return (
            f"- {self.name}: {self.height_cm}cm, "
            f"{self.flower_color} flowers ({bloom_txt})"
        )


class PrizeFlower(FloweringPlant):
    """A flowering plant that has won prizes."""

    def __init__(
        self,
        name,
        height_cm,
        flower_color,
        is_blooming,
        prize_points,
    ):
        super().__init__(name, height_cm, flower_color, is_blooming)
        self.prize_points = prize_points
        self.kind = "prize"

    def describe(self) -> str:
        """Return a string showing the plant's stats and prize points."""
        base = super().describe()
        return f"{base}, Prize points: {self.prize_points}"


def my_len(item) -> int:
    """Manually calculate and return the number of items in an iterable."""
    count = 0
    for _ in item:
        count += 1
    return count


class Garden:
    """A garden that holds multiple plants."""

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.plants_added = 0
        self.total_growth_cm = 0

    def add_plant(self, plant):
        """Add a plant to the garden and update statistics."""
        self.plants.append(plant)
        self.plants_added += 1


class GardenManager:
    class GardenStats:
        """Statistics and analytics for a garden."""

        def count_types(self, garden):
            """Return count of each plant kind in the garden."""
            regular = 0
            flowering = 0
            prize = 0

            for p in garden.plants:
                if p.kind == "regular":
                    regular += 1
                elif p.kind == "flowering":
                    flowering += 1
                elif p.kind == "prize":
                    prize += 1

            return regular, flowering, prize

        def garden_score(self, garden):
            """Return a score representing the garden's overall value."""
            total_height = 0
            total_prize = 0

            for p in garden.plants:
                total_height += p.height_cm
                if isinstance(p, PrizeFlower):
                    total_prize += p.prize_points

            plants_count = my_len(garden.plants)
            return total_height + (10 * plants_count) + total_prize

    def __init__(self):
        """Manage multiple gardens and provide analytics."""
        self.gardens = {}
        self.stats = GardenManager.GardenStats()

    def add_garden(self, owner):
        """Add a new garden for the owner if it doesn't exist."""
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)

    def add_plant(self, owner, plant):
        """Add a plant to the specified owner's garden."""
        self.add_garden(owner)
        self.gardens[owner].add_plant(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def help_garden_grow(self, owner, cm):
        """Grow all plants in the owner's garden by a given amount."""
        if owner not in self.gardens:
            return 0

        garden = self.gardens[owner]
        print(f"\n{owner} is helping all plants grow...")

        total = 0
        for plant in garden.plants:
            grew = plant.grow(cm)
            total += grew
            print(f"{plant.name} grew {grew}cm")

        garden.total_growth_cm += total
        return total

    def print_garden_report(self, owner):
        """Print a detailed report of the specified owner's garden."""
        if owner not in self.gardens:
            return

        garden = self.gardens[owner]
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in garden.plants:
            print(plant.describe())

        regular, flowering, prize = self.stats.count_types(garden)
        print(
            f"\nPlants added: {garden.plants_added}, "
            f"Total growth: {garden.total_growth_cm}cm"
        )
        print(
            f"Plant types: {regular} regular, {flowering} flowering, "
            f"{prize} prize flowers"
        )

    @classmethod
    def create_garden_network(cls):
        """Return a manager with some predefined gardens."""
        mgr = cls()
        mgr.add_garden("Alice")
        mgr.add_garden("Bob")
        return mgr

    @staticmethod
    def validate_height(height_cm):
        """Validate that height is within a reasonable range."""
        return 0 <= height_cm <= 500


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()

    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", FloweringPlant("Rose", 25, "red", True))

    sunflower = PrizeFlower(
        "Sunflower",
        50,
        "yellow",
        True,
        10,
    )
    manager.add_plant("Alice", sunflower)
    manager.help_garden_grow("Alice", 1)
    manager.print_garden_report("Alice")
    manager.add_plant("Bob", Plant("Pine", 82))

    print("\nHeight validation test:", GardenManager.validate_height(120))

    alice_score = manager.stats.garden_score(manager.gardens["Alice"])
    bob_score = manager.stats.garden_score(manager.gardens["Bob"])
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    total_gardens = my_len(manager.gardens)
    print(f"Total gardens managed: {total_gardens}")
