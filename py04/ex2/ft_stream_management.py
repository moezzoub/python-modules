import sys


def main():
    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
        print("Input stream active .", end="")
        id = input("Enter archivist ID: ")
        print("Input stream active .", end="")
        st = input("Enter status report: ")
        print(f"\n[STANDARD] Archive status from {id}: {st}", file=sys.stdout)
        y = "[ALERT] System diagnostic: Communication channels verified"
        print(f"{y}", file=sys.stderr)
        print("[STANDARD] Data transmission complete")
        print("\nThree-channel communication test successful.")
    except KeyboardInterrupt:
        print("\nCommunication interrupted by user.", file=sys.stderr)


if __name__ == "__main__":
    main()
