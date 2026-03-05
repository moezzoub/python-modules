import sys
import math


def parse_number(t):
    """Parse a string as an int or float."""
    t = t.strip()
    if "." in t:
        return float(t)

    return int(t)


def parse_coords(s):
    try:
        parts = [p.strip() for p in s.split(",")]
        if len(parts) != 3:
            raise ValueError('Expected exactly 3 values: "x,y,z"')

        return (
            parse_number(parts[0]),
            parse_number(parts[1]),
            parse_number(parts[2]),
        )

    except (ValueError, IndexError) as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def distance(a, b):
    """Calculate the Euclidean distance between 2 points a and b in 3Dspace."""
    x1, y1, z1 = a
    x2, y2, z2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    """Default points """
    origin = (0, 0, 0)
    pos = (10, 20, 5)

    """If the user provides two points as command-line
    arguments in the form "x,y,z", parse
    them and use them as origin and pos."""
    if len(sys.argv) >= 3:
        a = parse_coords(sys.argv[1])
        b = parse_coords(sys.argv[2])
        if a is None or b is None:
            sys.exit(1)
        origin = a
        pos = b

    print(f"Position created: {pos}")
    print(f"Distance between {origin} and {pos}: {distance(origin, pos):.2f}")

    """Demo parsing a valid coordinate string."""
    s = "3,4,0"
    print(f"\nParsing coordinates: {s}")
    parsed = parse_coords(s)
    """If parsing was successful,
    print the parsed position and the distance from the origin."""
    if parsed is not None:
        print(f"Parsed position: {parsed}")
        print(f"Distance between {origin} and "
              f"{parsed}: {distance(origin, parsed):.1f}")

    print("\nParsing invalid coordinates: \"abc,def,ghi\"")
    parse_coords("abc,def,ghi")

    """Demonstrate unpacking the coordinates
    from the pos tuple into individual variables x, y, z."""
    print("\nUnpacking demonstration:")
    x, y, z = parse_coords(s)
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
