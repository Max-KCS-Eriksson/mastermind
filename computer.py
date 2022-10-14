from random import randint

from player import Player


class Computer(Player):
    """Computer participant of a game of Mastermind."""

    def __init__(self):
        """Inherits attributes form Player class."""
        super().__init__()

    def _pick_number(self, available_numbers):
        """Pick a random number from given list argument."""
        return randint(available_numbers[0], available_numbers[-1])


if __name__ == "__main__":
    c = Computer()
