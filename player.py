class Player:
    """Human participant of a game of Mastermind."""

    def __init__(self):
        """Init with score attribute."""
        self.score = 0

    def create_code(self, code_length, available_numbers):
        """
        Method prompts player to pick numbers thats in the list given as an argument
        for the available_numbers equivalent to given integer argument for the
        code_length parameter.
        Takes in length of the code to produce as an integer and a list numbers to
        choose from as arguments.
        """
        code = []
        for i in range(code_length):
            code.append(self._pick_number(available_numbers))

        return code

    def guess_code(self, code_length, available_numbers):
        """
        Method prompts user to try to guess the code.
        Guessed numbers need to be in the list given as an argument for the
        available_numbers equivalent to given integer argument for the code_length
        parameter.
        Takes in length of the code to produce as an integer and a list numbers to
        choose from as arguments.
        """
        guess = []
        for i in range(code_length):
            guess.append(self._pick_number(available_numbers))

        return guess

    def _pick_number(self, available_numbers):
        """Pick a number from given list argument."""
        while True:
            number = int(input("> Pick a number: "))
            if number in available_numbers:
                return number
            else:
                print(f"{number} is not an option!\nPick one from {available_numbers}.")


if __name__ == "__main__":
    p = Player()
