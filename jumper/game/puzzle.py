from operator import concat, truediv
import random
# from tabnanny import check


class Puzzle:
    """Puzzle provides a random word from a list of words, 
    and processes a guess by checking:
    * if the guess exists in the current word
    * if the guess has been guessed before
    
    Attributes:
    wordList(list): A list of words which would be selected randomly
    current_word: A randomly selected word from the wordList in from of a list. 
    i.e if randomly selected word is "water",
    current_word is ["w", "a", "t", "e", "r"]
    correct_guesses(list) : A list of correct guesses
    wrong_guesses(list) : A list of incorrect guesses
    guess_is_correct(boolean): check if a guess is correct or not
    current_output(string): a string that produces a visual update of 
    correctly guessed letters with blank spaces for letters that haven't been guessed yet.
    output_list:  A list version of the current output.
    
    """

    def __init__(self):
        """Constructs a new instance of Puzzle.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        self._wordsList = ["water", "invert", "python", "pizza", "jumper", "fighter", "painter","kicker","panda","stranger","creator","finisher"]
        self._current_word = []
        self._correct_guesses = []
        self._wrong_guesses = []
        self._guess_is_correct = True
        self._current_output = "_ _ _ _ _"
        self._output_list = []


    def set_random_word(self):
        """Assigns current_word to a random word form word list.

        Args:
            self (Puzzle): an instance of Puzzle.
        """

        word = random.choice(self._wordsList)
        self._current_word = list(word)


    def _letter_not_included(self, letter):
        """Checks if a letter is not included in correct guesses list.

        Args:
            self (Puzzle): an instance of Puzzle.
            letter (String): a letter.
        """
        return not(letter in self._correct_guesses)
           

    def check_guess(self, guess):
        """Checks if guess is included in correct word.

        Args:
            self (Puzzle): an instance of Puzzle.
            guess (String): users guess.
        """
        for letter in self._current_word:
            if (guess == letter) and (self._letter_not_included(guess)):
                self._correct_guesses.append(guess)
            else:
                self._wrong_guesses.append(guess)

        self._guess_is_correct = (guess in self._correct_guesses)
        return self._guess_is_correct

    def set_current_word(self):
        """Construct current word that includes correctly guessed letter and blanks"

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        word_list = []
        for letter in self._current_word:
            if letter in self._correct_guesses:
                word_list.append(letter)
            else: word_list.append("_")
        self._current_output = " ".join(word_list)
        self._output_list = word_list


    def get_current_output(self):
        """Returns current output.

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return f"            {self._current_output}"

    def word_is_guessed(self):
        """Checks if word has been completely guessed

        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._output_list == self._current_word
            
    def already_guessed(self, guess):
        """Checks if letter has been guessed. 

        Args:
            self (Puzzle): an instance of Puzzle.
            guess (String): users guess.
        """   
        guess_list = concat(self._correct_guesses, self._wrong_guesses)
        return guess in guess_list
