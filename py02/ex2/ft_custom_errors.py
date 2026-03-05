class GardenerError(Exception):
    """Base class for all gardener-related errors."""
    pass


class Planterror(GardenerError):
    """Raised when there is an error in the gardening plan."""
    pass


class WaterError(GardenerError):
    """Raised when there is an issue with watering the plants."""
    pass


def check_gardening_plan():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise Planterror("The tomato plant is wilting!")
    except Planterror as pe:
        print(f"Caught an error: {pe}")
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as wa:
        print(f"Caught WaterError: {wa}")
    print()
    print("Testing catching all garden errors...")
    try:
        raise Planterror("The tomato plant is wilting!")
    except GardenerError as ga:
        print(f"Caught a garden error: {ga}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenerError as ga:
        print(f"Caught a garden error: {ga}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    check_gardening_plan()
