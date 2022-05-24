import random
from tabnanny import check


class Puzzle:
    """Puzzle provides a random word and updates the users guesses and does a bunch of other things[I would replace this text in the future]
    
    Attributes:
    
    """

    def __init__(self):
        """Constructs a new instance of Puzzle with ...attribute.

        Args:
            ...
        """
        self._wordsList = ["water", "invert", "python", "pizza", "jumper"]
        self._current_word = ["w", "a", "t", "e", "r"]
        self._correct_guesses = ["t","r","w"]
        self._wrong_guesses = [""]
        self._guess_is_correct = True
        self._current_output = "_ _ _ _ _"


    def set_random_word(self):
         word = random.choice(self._wordsList)
         self._current_word = word.split("")


    def _letter_not_included(self, letter):
        value = False
        for each_letter in self._correct_guesses:
            if each_letter != letter:
                value = True
        return value

    def check_guess(self, guess):
        for letter in self._current_word:
            if (guess == letter) and (self._letter_not_included(guess)):
                self._correct_guesses.append(guess)
                self._guess_is_correct = True
            else:
                self._wrong_guesses.append(guess)
                self._guess_is_correct = False
        return self._guess_is_correct

    def set_current_word(self):
        word_list = []
        for letter in self._current_word:
            if letter in self._correct_guesses:
                word_list.append(letter)
            else: word_list.append("_")
        self._current_output = " ".join(word_list)


    def get_current_output(self):
        return self._current_output
            