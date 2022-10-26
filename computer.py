from random import randint

from player import Player


class Computer(Player):
    """Computer participant of a game of Mastermind."""

    def __init__(self):
        """Inherits attributes form Player class."""
        super().__init__()

    def _pick_number(self, allowed_numbers):
        """Pick a random number from given list argument."""
        return randint(allowed_numbers[0], allowed_numbers[-1])

    def guess_code(self, code_crack_progress, allowed_numbers):
        """Computer tries to break the code created by the player."""  # TODO: Docstring
        guess = []
        for number in code_crack_progress:
            try:
                # Check if individual number in code is yet discovered.
                number = int(number)
            except:
                # Guess what the number is.
                number = randint(
                    allowed_numbers[0], allowed_numbers[-1]
                )  # TODO: Improve tactic
            guess.append(number)

        return guess


if __name__ == "__main__":
    c = Computer()
