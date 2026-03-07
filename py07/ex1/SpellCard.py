from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        """Initialize a SpellCard with its effect type."""
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """Cast the spell and apply its effect."""
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        """Resolve the spell's effect on the given targets."""
        return {
            'card': self.name,
            'effect_type': self.effect_type,
            'targets': targets
        }
