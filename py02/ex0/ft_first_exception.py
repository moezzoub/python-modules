def check_temperature(temp_str):
    try:
        temperature = int(temp_str)
    except ValueError:
        raise ValueError("Invalid temperature value")
    if temperature < 0:
        raise ValueError(f"Error: {temperature}°C"
                         " is too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"Error: {temperature}"
                         "°C is too hot for plants (max 40°C)")
    else:
        return temperature


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-5"]
    for test in tests:
        print()
        print(f"Testing temperature: {test}")
        try:
            result = check_temperature(test)
            print(f"Temperature {result}°C is suitable for plants.")
        except ValueError as e:
            print(e)
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
