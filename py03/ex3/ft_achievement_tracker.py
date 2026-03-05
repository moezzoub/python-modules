if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all_unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements : {len(all_unique)}\n")

    intersection = alice.intersection(bob).intersection(charlie)
    print(f"Common to all player: {intersection}")

    all_shared = (alice.intersection(bob)) \
        .union(alice.intersection(charlie)) \
        .union(bob.intersection(charlie))
    rare = all_unique.difference(all_shared)
    print(f"Rare achievements (1 player): {rare}\n")

    intersection_alice_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {intersection_alice_bob}")
    alice_unique = alice.union(bob).difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.union(alice).difference(alice)
    print(f"Bob unique: {bob_unique}")
