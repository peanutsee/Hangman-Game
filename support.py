class Hangman:
    def __init__(self, word_to_guess):
        # Word to guess
        self.word_to_guess = word_to_guess

        # Guessing slate
        self.guessing_slate = ['_' if i != " " else " " for i in self.word_to_guess]

        # Word dict
        def _word_to_guess(word):
            """
            This function extracts letters from the word to guess.
            Letters are mapped to a dictionary.
            :param word: Word to guess
            :return: Dictionary of letters in the word to guess
            """
            word_dict = {}
            for index, letter in enumerate(word):
                if letter == ' ':
                    continue
                else:
                    if letter in word_dict.keys():
                        word_dict[letter].append(index)
                    else:
                        word_dict.update({letter: [index]})
            return word_dict

        self.word_dict = _word_to_guess(self.word_to_guess)

        # Hangman
        self.hangman = [
            "|---------------\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|_______________",
            "|---------------\n"
            "|       |\n"
            "|\n"
            "|\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (\n"
            "|\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_\n"
            "|\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|       |\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|       |\n"
            "|\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|       |\n"
            "|      /\n"
            "|_______________",

            "|---------------\n"
            "|       |\n"
            "|      (_)\n"
            "|      /|\\\n"
            "|       |\n"
            "|      / \\\n"
            "|_______________"
        ]

        # Error count
        self.error_counter = 0

    def display_guessing_slate(self):
        """
        This function displays the current guessing slate.
        :return: None
        """
        print(''.join(self.guessing_slate))

    def display_hangman(self):
        """
        This function displays the current hangman state.
        :return: None
        """
        print(self.hangman[self.error_counter])

    def letter_validator(self, letter):
        """
        This function valiates the user's letter input.
        :param letter: User's guess
        :return: Respective functions
        """
        if letter in self.word_dict.keys():
            for index in self.word_dict[letter]:
                self.guessing_slate = self.guessing_slate[:index] + [letter] + self.guessing_slate[index + 1:]
            return self.display_guessing_slate()
        else:
            self.error_counter += 1
            return self.display_hangman()
