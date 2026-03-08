from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 card_id: str, rating: int, wins: int, losses: int):
        """Initialize a TournamentCard with combat and ranking attributes."""
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.wins = wins
        self.losses = losses

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed'
        }

    def attack(self, target) -> dict:
        """Simulate an attack on a target, returning combat details."""
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': self.cost * 2,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        """Simulate defending against an attack,
                     calculating damage taken and blocked."""
        blocked = min(self.cost, incoming_damage)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': True
        }

    def get_combat_stats(self) -> dict:
        """Return combat-related stats for the card."""
        return {
            'card_name': self.name,
            'attack_power': self.cost * 2,
            'defense_power': self.cost
        }

    def update_wins(self, wins: int) -> None:
        """Update the card's win count and adjust rating accordingly."""
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        """Update the card's loss count and adjust rating accordingly."""
        self.losses += losses
        self.rating -= 16 * losses

    def calculate_rating(self) -> int:
        """Calculate the card's rating based on wins and losses."""
        return self.rating

    def get_rank_info(self) -> dict:
        """Return ranking information for the card."""
        return {
            'card_name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        """Return a comprehensive dictionary of the card's
                        tournament-related stats."""
        return {
            'card_id': self.card_id,
            'card_name': self.name,
            'rarity': self.rarity,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
