from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(card.get_card_info())

    mana = 6
    print(f"\nPlaying {card.name} with {mana} mana available:")
    print("Playable:", card.is_playable(mana))
    print("Play result:", card.play({}))

    print(f"\n{card.name} attacks Goblin Warrior:")
    print("Attack result:", card.attack_target("Goblin Warrior"))

    mana = 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print("Playable:", card.is_playable(mana))
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
