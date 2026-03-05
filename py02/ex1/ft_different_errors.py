# ft_different_errors.py

def garden_operations(kind):
    if kind == "value":
        """ValueError"""
        int("abc")

    elif kind == "zero":
        """ZeroDivisionError"""
        number = 10
        print(number / 0)

    elif kind == "file":
        """ FileNotFoundError"""
        f = open("missing.txt", "r")
        f.close()

    elif kind == "key":
        """ KeyError"""
        plants = {"tomato": 3, "carrot": 5}
        print(plants["missing_plant"])

    else:
        print("unknown kind")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
