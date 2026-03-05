def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")

    success = False

    try:
        with open("classified_data.txt", "r") as file:
            file_content = file.read()

        print("Vault connection established with failsafe protocols")
        print()
        print("SECURE EXTRACTION:")
        print(file_content, end="" if file_content.endswith("\n") else "\n")

        print()
        print("SECURE PRESERVATION:")

        with open("classified_data.txt", "a") as file:
            file.write("[CLASSIFIED] New security protocols archived\n")

        print("[CLASSIFIED] New security protocols archived")
        success = True

    except FileNotFoundError:
        print("Connection failed")

    except PermissionError:
        print("Connection failed")

    finally:
        print("Vault automatically sealed upon completion")
        print()
        if success:
            print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
