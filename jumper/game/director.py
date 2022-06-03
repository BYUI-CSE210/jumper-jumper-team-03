from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.puzzle import Puzzle

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        parachute: For updating the parachute based on the player's guess.
        puzzle: For getting random word from list and updating output based on player's guess.
        current_guess:  Holds the current output from the puzzle class.
        player_guess:  Holds the letter currently guessed by the player.
        puzzle_results(boolean): Whether or not the player_guess exists in the current word. 
        level(int): The parachute level [4-0]
        guessed_before(boolean): Whether or not the player_guess has been guessed before.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._puzzle = Puzzle()
        self._current_guess = ""
        self._player_guess = ""
        self._puzzle_results = True
        self._level = 4
        self._guessed_before = False

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """

        # SET RANDOM WORD [PUZZLE]
        self._puzzle.set_random_word()
        self._current_guess = self._puzzle.get_current_output()
        
        # DISPLAY DEFAULT GUESS OUTPT [BLANKS]
        self._terminal_service.write_text(self._puzzle.get_current_output())

        # DISPLAY DEFAULT PARACHUTE [4]
        self._terminal_service.write_text(self._parachute.get_parachute())

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """
        Gets player guess from the terminal and stores in a variable

        Args:
            self (Director): An instance of Director.
        """
        
        # GET PLAYERS GUESS AND STORE IT IN A VARIABLE
        self._player_guess = self._terminal_service.read_text("guess a letter [a -z]: ")
        if self._puzzle.already_guessed(self._player_guess):
            self._terminal_service.write_text("you already guessed that")

    def _do_updates(self):
        """
        Checks if player's guess is correct using the Puzzle class,
        reduces parachute by a step if guess is wrong,
        and updates visual parachute.

        Args:
            self (Director): An instance of Director.
        """
        # RUN GUESS IN PUZZLE
        self._puzzle_results = self._puzzle.check_guess(self._player_guess)
        
        self._puzzle.set_current_word()

        # GET CURRENT WORDS VALUE AND STORE IN VARIABLE
        self._current_guess = self._puzzle.get_current_output()
        
        # VALIDATES WITH PARACHUTE THEN GETS CURRENT PARACHUTE
        if self._puzzle_results:
            self._parachute.get_parachute()
        else:
            self._level -= 1
            self._parachute.parachute_remaining(self._level)
        

    def _do_outputs(self):
        """
        Displays value of current word,
        displays current parachute lavel,
        and ends loop if the game is over.
        Args:
            self (Director): An instance of Director.
        """
        # DISPLAY CURRENT WORDS VALUE
        self._terminal_service.write_text(self._current_guess)

        # DISPLAY PARCHUTE
        self._terminal_service.write_text(self._parachute.get_parachute())

        # GAME OVER CHECK
        if (self._level == 0) or (self._puzzle.word_is_guessed()):
            self._is_playing = False
