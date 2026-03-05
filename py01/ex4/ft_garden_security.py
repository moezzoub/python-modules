# ft_garden_security.py

class SecurePlant:
    """A plant with security checks on its attributes."""
    def __init__(self, name) -> None:
        self.__name = name
        self.__height_cm = 0
        self.__age_days = 0

    def get_height(self) -> int:
        """Return the height of the plant in centimeters."""
        return self.__height_cm

    def get_age(self) -> int:
        """Return the age of the plant in days."""
        return self.__age_days

    def set_height(self, h) -> None:
        """Set the height of the plant, rejecting negative values."""
        if h < 0:
            print(f"Invalid operation attempted: height {h}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height_cm = h
        print(f"Height updated: {h}cm [OK]")

    def set_age(self, a) -> None:
        """Set the age of the plant, rejecting negative values."""
        if a < 0:
            print(f"Invalid operation attempted: age {a} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age_days = a
        print(f"Age updated: {a} days [OK]")

    def get_info(self) -> str:
        """Return a string representing the plant's information."""
        return (
            f"{self.__name} ({self.__height_cm}cm, "
            f"{self.__age_days} days)"
        )


if __name__ == "__main__":

    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    print("Plant created: Rose")

    plant.set_height(25)
    plant.set_age(30)

    print("")
    plant.set_height(-5)
    print("")
    print("Current plant:", plant.get_info())
