from random import randint

from player import Player


class Computer(Player):
    """Computer participant of a game of Mastermind."""

    def __init__(self):
        """
        Inherits attributes form Player class and inits attributes unique to this class.

        The flag attribute first_stage_tactic used to determine what tactic to used when
        trying to break the opponents code.
        The previous_max_guessed_number attribute is used to keep track of what the
        highest number is that the class instance has guessed when trying to break the
        opponents code. This aids in deciding on what number to guess next.
        """
        super().__init__()

        # Attributes used when computer crack code.
        self.first_stage_tactic = True
        self.previous_max_guessed_number = None

    def _pick_number(self, allowed_numbers):
        """Pick a random number from given list argument."""
        return randint(allowed_numbers[0], allowed_numbers[-1])

    def guess_code(
        self,
        code_length,
        code_crack_progress,
        wrong_index_for_number,
        allowed_numbers,
        numbers_not_in_code,
    ):
        """Computer tries to break the code created by the player.
        Explain stages of tactic.

        In the first stage, the computer places two pair of numbers next to each other
        to maximize potential intel from feedback.
        In the second stage, the computer picks numbers for each index of the code based
        on previously given feedback. This is done by restricting the possible numbers
        for all indices of the code to be cracked.
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
            for code_index, number in enumerate(code_crack_progress):
                try:
                    # Check if individual number in code is already placed correctly.
                    number = int(number)
                except ValueError:
                    # Place numbers that have been misplaced somewhere else.
                    for key in wrong_index_for_number.keys():

                        if code_index not in wrong_index_for_number[key]:
                            # if code_index not in wrong_index_for_number[key]:
                            # Number has not been attempted to be placed here.
                            number = key

                            break

                    else:
                        # No misplaced numbers to try for index in opponent's code.
                        number = self.previous_max_guessed_number

                # Check if previous feedback has reviled that number is not in code.
                if number in numbers_not_in_code:
                    # To not guess same wrong number every turn.
                    number += 1

                guess.append(number)

        return guess

    def update_code_breaking_tactic(self, code_crack_progress, allowed_numbers):
        """
        Checks if any numbers have been placed correctly, and if so changes the value of
        the flag attribute first_stage_tactic to False.
        """
        if self.first_stage_tactic:
            # Check if no numbers have been guessed in right place.
            for number in allowed_numbers:
                if number in code_crack_progress:
                    # Move on from first stage of tactic.
                    self.first_stage_tactic = False
                    break


if __name__ == "__main__":
    c = Computer()
