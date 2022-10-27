from random import randint

from player import Player


class Computer(Player):
    """Computer participant of a game of Mastermind."""

    def __init__(self):
        """Inherits attributes form Player class."""
        super().__init__()

        # Attributes used when computer crack code.
        self.first_stage_tactic = True
        self.previous_max_guessed_number = None

    def _pick_number(self, allowed_numbers):
        """Pick a random number from given list argument."""
        return randint(allowed_numbers[0], allowed_numbers[-1])

    def guess_code(
        self, code_length, code_crack_progress, wrong_index_for_number, allowed_numbers
    ):
        """Computer tries to break the code created by the player.
        Explain stages of tactic.
        """  # TODO: Docstring
        guess = []
        if self.first_stage_tactic:

            # First stage of tactic.
            if self.previous_max_guessed_number is None:
                guess_pair_number = 1
            else:
                guess_pair_number = self.previous_max_guessed_number
            for i in range(0, code_length, 2):
                # Append pair of numbers.
                guess.append(guess_pair_number)
                guess.append(guess_pair_number)

                guess_pair_number += 1
            self.previous_max_guessed_number = guess_pair_number

        else:
            # Second stage tactic.
            print(
                "*DEBUG*\t Entering second stage tactic."
            )  # TODO: Remove after debug.

            for code_index, number in enumerate(code_crack_progress):
                try:
                    # Check if individual number in code is already placed correctly.
                    number = int(number)
                except ValueError:
                    # Place numbers that have been misplaced somewhere else.
                    for key in wrong_index_for_number.keys():

                        if code_index not in wrong_index_for_number[key]:
                            # Number has not been attempted to be placed here.
                            print("*DEBUG*\tN in cracked code:", number)  # TODO: Remove
                            print("*DEBUG*\tcode_index:", code_index)  # TODO: Remove
                            print("*DEBUG*\tnumber:", key)  # TODO: Remove
                            print(
                                "*DEBUG*\ttried indices:", wrong_index_for_number[key]
                            )  # TODO: Remove
                            print()

                            number = key
                            print(
                                "*DEBUG*\tguessed number:",
                                number,
                                "for code index:",
                                code_index,
                                "\n",
                            )  # TODO: Remove

                        elif code_index in wrong_index_for_number[key]:
                            # No misplaced numbers to try for index in opponent's code.
                            number = self.previous_max_guessed_number

                            print(
                                "*DEBUG*\tguessed number:",
                                number,
                                "for code index:",
                                code_index,
                                "\n",
                            )  # TODO: Remove

                guess.append(number)

            # Update highest number guessed.
            self.previous_max_guessed_number += 1

            print(
                "*DEBUG* previous_max_guessed_number:",
                self.previous_max_guessed_number,
            )  # TODO: remove

        return guess

    def update_code_breaking_tactic(self, code_crack_progress, allowed_numbers):
        """"""  # TODO: Docstring
        if self.first_stage_tactic:
            # Check if no numbers have been guessed in right place.
            for number in allowed_numbers:
                if number in code_crack_progress:
                    # Move on from first stage of tactic.
                    self.first_stage_tactic = False
                    break


if __name__ == "__main__":
    c = Computer()
