from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, block_power: int, health: int,
                 mana: int, spell_power: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.block_power = block_power
        self.health = health
        self.mana = mana
        self.spell_power = spell_power

    def play(self, game_state: dict) -> dict:
        """Simulate playing the card, returning a summary of the action."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite card deployed'
        }

    def attack(self, target) -> dict:
        """Simulate an attack on a target, returning combat details."""
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.attack_power,
            'combat_type': 'melee'
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Simulate casting a spell, consuming mana
                and applying effects to targets."""
        mana_used = 4
        if self.mana < mana_used:
            mana_used = self.mana
        self.mana -= mana_used
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [target.name for target in targets],
            'mana_used': mana_used
        }

    def defend(self, incoming_damage: int) -> dict:
        """Simulate defending against an attack,
                    calculating damage taken and blocked."""
        damage_blocked = min(self.block_power, incoming_damage)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        """Return the card's combat-related stats."""
        return {
            'attack_power': self.attack_power,
            'block_power': self.block_power,
            'health': self.health
        }

    def channel_mana(self, amount: int) -> dict:
        """Channel additional mana into the card, increasing its mana pool."""
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        """Return the card's magical attributes."""
        return {
            'mana': self.mana,
            'spell_power': self.spell_power
        }
