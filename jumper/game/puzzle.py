from operator import concat, truediv
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
        self._wordsList = ["water", "invert", "python", "pizza", "jumper", "fighter", "painter","kicker","panda","stranger","creator","finisher"]
        self._current_word = []
        self._correct_guesses = []
        self._wrong_guesses = []
        self._guess_is_correct = True
        self._current_output = "_ _ _ _ _"
        self._output_list = []


    def set_random_word(self):
         word = random.choice(self._wordsList)
         self._current_word = list(word)


    def _letter_not_included(self, letter):
        return not(letter in self._correct_guesses)
           

    def check_guess(self, guess):
        for letter in self._current_word:
            if (guess == letter) and (self._letter_not_included(guess)):
                self._correct_guesses.append(guess)
            else:
                self._wrong_guesses.append(guess)

        self._guess_is_correct = (guess in self._correct_guesses)
        return self._guess_is_correct

    def set_current_word(self):
        word_list = []
        for letter in self._current_word:
            if letter in self._correct_guesses:
                word_list.append(letter)
            else: word_list.append("_")
        self._current_output = " ".join(word_list)
        self._output_list = word_list


    def get_current_output(self):
        return f"            {self._current_output}"

    def word_is_guessed(self):
        return self._output_list == self._current_word
            
    def already_guessed(self, guess):   
        guess_list = concat(self._correct_guesses, self._wrong_guesses)
        return guess in guess_list
