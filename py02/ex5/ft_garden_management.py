class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant) -> None:
        if plant is None or plant == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as we:
            print(f"Error: {we}")
            return
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant, water_l, sunlight_h) -> None:
        if plant is None or plant == "":
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        if water_l < 1:
            raise WaterError(f"Error checking {plant}: "
                             f"Water level {water_l} is too low (min 1)")
        if water_l > 10:
            raise WaterError(f"Error checking {plant}: "
                             f"Water level {water_l} is too high (max 10)")
        if sunlight_h < 2:
            raise PlantError(f"Error checking {plant}: "
                             f"Sunlight hours {sunlight_h} is too low (min 2)")
        if sunlight_h > 12:
            raise PlantError(f"Error checking {plant}: "
                             f"Sunlight hours {sunlight_h} "
                             f"is too high (max 12)")
        print(f"{plant}: healthy (water: {water_l}, sun: {sunlight_h})")

    def check_water(self) -> None:
        raise WaterError("Not enough water in tank")


def test_garden_management():
    print("=== Garden Management System ===")
    print()

    manager = GardenManager()
    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    try:
        manager.add_plant("")
    except PlantError as va:
        print(va)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    try:
        manager.check_plant_health("lettuce", 15, 8)
    except GardenError as vu:
        print(vu)

    print("\nTesting error recovery...")
    try:
        manager.check_water()
    except GardenError as vaa:
        print(f"Caught GardenError: {vaa}")
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
