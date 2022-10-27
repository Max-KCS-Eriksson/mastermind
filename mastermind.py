import subprocess

from player import Player
from computer import Computer

CLEAR_CLI = "clear"


class Mastermind:
    """Game of Mastermind."""

    def __init__(self):
        """
        Init with attributes: player, computer, code_length, allowed_numbers,
        turn and max_turns.
        The value for turn is an integer that increments by 1 for each turn, starting
        from 1, until its equal t the value of max_turns.
        The value for round is an integer that increments by 1 for each complete game
        round, starting from 1, until its equal t the value of max_rounds.
        The value for code_length determines how long the code given by the code
        creator can be.
        The value for numbers is a list of numbers to choose from when making a code
        for the opponent to break.
        """
        # Static attributes.
        self.player = Player()
        self.computer = Computer()

        # Setting attributes.
        self.max_rounds = 4
        self.max_turns = 12
        self.code_length = 4
        self.allowed_numbers = [1, 2, 3, 4, 5, 6]

        # Dynamic attributes.
        self.round = 1
        self.turn = 1

    def run_game(self):
        """Main loop of the game."""
        subprocess.run(CLEAR_CLI)

        rules_info = f"Choose {self.code_length} numbers from: {self.allowed_numbers}"

        while True:
            print(f"### ROUND {self.round} ###")
            # Determine who will create a code for their opponent to break.
            # Roles are switched each turn.

            # Player tries to break the computers code.
            if self.round % 2 == 0:

                # Create list of single whitespace characters to represent uncracked code.
                guess_feedback = [" " for i in range(self.code_length)]
                wrong_index_for_number = None

                # Computer creates a code.
                code = self.computer.create_code(self.code_length, self.allowed_numbers)
                code_cracked = False
                while not code_cracked:
                    # Check that the are more turns to be played.
                    # Plus one to allow for the last turn to be played.
                    if self.turn == self.max_turns + 1:
                        break
                    print(f"\n--- TURN  {self.turn} ---")

                    # Player try to crack the code.
                    print("\nTry to crack the computers code.\n")
                    print(rules_info)
                    guess = self.player.guess_code(
                        self.code_length, self.allowed_numbers
                    )

                    subprocess.run(CLEAR_CLI)
                    # Give feedback about the guess.
                    guess_feedback, wrong_index_for_number = self._get_guess_feedback(
                        code, guess, guess_feedback, wrong_index_for_number
                    )
                    print("Your guess:")
                    print(guess)
                    print("Correctly guessed values:")
                    print(guess_feedback)

                    # Check if the code is cracked.
                    if guess == code:
                        code_cracked = True

                    self.turn += 1

                if code_cracked:
                    self.round += 1
                    self.player.score += 1
                    print("\nCongratulations, you cracked the code!\n")

                    # Reset turn.
                    self.turn = 0

            # Computer tries to break the players code.
            else:

                # Create list of single whitespace characters to represent uncracked code.
                guess_feedback = [" " for i in range(self.code_length)]
                # Used fot he computer to evaluate what number to place where in the guess.
                wrong_index_for_number = None

                # Player creates a code.
                print("\nCreate a code for the computer to crack.\n")
                print(rules_info)
                code = self.player.create_code(self.code_length, self.allowed_numbers)
                code_cracked = False
                while not code_cracked:
                    # Check that the are more turns to be played.
                    # Plus one to allow for the last turn to be played.
                    if self.turn == self.max_turns + 1:
                        break
                    print(f"\n--- TURN  {self.turn} ---")

                    # Computer try to crack the code.
                    self.computer.update_code_breaking_tactic(
                        guess_feedback, self.allowed_numbers
                    )
                    guess = self.computer.guess_code(
                        self.code_length,
                        guess_feedback,
                        wrong_index_for_number,
                        self.allowed_numbers,
                    )  # TODO

                    # subprocess.run(CLEAR_CLI)
                    # Give feedback about the guess.
                    guess_feedback, wrong_index_for_number = self._get_guess_feedback(
                        code, guess, guess_feedback, wrong_index_for_number
                    )
                    print(
                        "*DEBUG*\tMisplaced numbers:", wrong_index_for_number
                    )  # TODO: Remove after debugging.
                    print("Player's code:")
                    print(code)
                    print("Computer's guess:")
                    print(guess)
                    print("Correctly guessed values:")
                    print(guess_feedback)

                    # Check if the code is cracked.
                    if guess == code:
                        code_cracked = True

                    self.turn += 1

                if code_cracked:
                    self.round += 1
                    self.computer.score += 1
                    print("\nThe computer has cracked your code!\n")

                    # Reset turn.
                    self.turn = 0

            print("\nWould you like to switch roles and play another round?")
            another_round = input("(y/n) : ").lower()
            if another_round == "y":
                subprocess.run(CLEAR_CLI)
                continue
            elif another_round == "n":
                print("\nThank you for playing =)\n")
                break

    def _get_guess_feedback(
        self, code, guess, code_crack_progress, wrong_index_for_number=None
    ):
        """
        Gives feedback about the codebreaker's guess.
        Tells if a value in given list argument for the guess parameter is in its the
        same place as in given list argument for the code parameter or if the value is
        in the code but in an other place.
        Takes in a list argument for the code_crack_progress parameter and return it
        with changes index values to indicate where correctly guessed values have
        been places.
        """
        if wrong_index_for_number is None:
            wrong_index_for_number = {}

        for i, number in enumerate(guess):
            # Check if each value of the guess is in the right place.
            if guess[i] == code[i]:
                code_crack_progress[i] = code[i]
            # Check if each guess value is in the code, but in the wrong place.
            elif number in code:
                print(f"The value {number} is in the code, but not in the index {i}.")
                # Add wrongly guessed index to set value of guessed number key.
                wrong_index_for_number.setdefault(number, set())
                wrong_index_for_number[number].add(i)

        return code_crack_progress, wrong_index_for_number


if __name__ == "__main__":
    mm = Mastermind()
    mm.run_game()
