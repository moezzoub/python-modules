# ex0/Card.py
from abc import ABC, abstractmethod
from typing import Any

class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """Execute the card effect and return a result dict."""
        raise NotImplementedError

    def get_card_info(self) -> dict:
        # type default: from class name (CreatureCard -> Creature)
        card_type = self.__class__.__name__.replace("Card", "")
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": card_type or self.__class__.__name__,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost