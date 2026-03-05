def handle_crisis(file_name, mode_file):
    print(f"{mode_file}:Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as file:
            data = file.read().strip()
        print(f"SUCCESS: Archive recovered - ''{data}''")
        print("STATUS: Normal operations resumed")
        return

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        return
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        return


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    handle_crisis("lost_archive.txt", "CRISIS ALERT")
    print()
    handle_crisis("classified_vault.txt", "CRISIS ALERT")
    print()
    handle_crisis("standard_archive.txt", "ROUTINE ACCESS")
    print()
    print("All crisis scenarios handled successfully. Archives secure.")
